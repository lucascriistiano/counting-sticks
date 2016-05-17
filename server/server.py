# -*- coding: utf-8 -*-
from datetime import datetime
import mongoengine
import threading
import models
import timer
import game


class CountingSticks(object):

    def __init__(self):
        print(str(datetime.now()), 'Starting CountingSticks object')

        print(str(datetime.now()), 'Connecting to database')
        mongoengine.connect('counting_sticks')

        print(str(datetime.now()), 'Setting up object')
        self.lock = threading.Lock()
        self.current_games = {}

        self.exclusion_verification_time = 20  # in seconds
        self.confirm_presence_timer_dict = {}

        print(str(datetime.now()), 'Deleting existing rooms')
        models.Room.objects.delete()  # clean rooms on startup

        print(str(datetime.now()), 'Creating test room')
        self.create_room('lucas', 'Test Room', 2, 3)

    def register(self, username, email, password):
        new_user = models.User(username=username, email=email, password=password)
        new_user.save()

    def login(self, username, password):
        found_user = models.User.objects(username=username, password=password).first()
        return found_user is not None

    def list_rooms_ids(self):
        rooms_ids = []
        for room in models.Room.objects():
            rooms_ids.append(str(room.id))

        return rooms_ids

    def list_rooms_info(self):
        return models.Room.objects.to_json()

    def get_room_info(self, room_id):
        return models.Room.objects.with_id(room_id).to_json()

    def create_room(self, username, name, min_players, max_players):
        new_room = models.Room(created_by=username, name=name, min_players=min_players, max_players=max_players,
                               current_players=[], playing=False, messages=[])
        new_room.save()

        str_new_room_id = str(new_room.id)
        self.confirm_presence_timer_dict[str_new_room_id] = {}
        return str_new_room_id

    def close_room(self, room_id, username):
        # check if the user who is closing is who created
        # check if a game isn't running

        self.lock.acquire()
        try:
            room = models.Room.objects.with_id(room_id)
            if room.created_by == username and len(room.current_players) == 0:
                models.Room.objects.with_id(room_id).delete()
                return True
            else:
                return False

        finally:
            self.lock.release()

    def join_room(self, room_id, username):
        self.lock.acquire()
        try:
            room = models.Room.objects.with_id(room_id)
            if not room.playing:
                if len(room.current_players) < room.max_players:
                    if username not in room.current_players:
                        room.current_players.append(username)
                        room.save()

                    confirm_presence_timer = timer.ConfirmPresenceTimerThread(self.exclusion_verification_time, self,
                                                                              room_id, username)
                    self.confirm_presence_timer_dict[room_id][username] = confirm_presence_timer
                    self.confirm_presence_timer_dict[room_id][username].start()
                    return True
                else:
                    print(str(datetime.now()), 'Impossible to join room: Room is full')
            else:
                print(str(datetime.now()), 'Impossible to join room: A game is in execution')
                return False
        finally:
            self.lock.release()

    def confirm_presence(self, room_id, username):
        print(str(datetime.now()), 'Confirm presence of', username, 'in room', room_id)
        self.confirm_presence_timer_dict[room_id][username].reset()

    def disconnect_player(self, room_id, username):
        print(str(datetime.now()), 'Disconnected', username, 'of room', room_id)

        # Remove player from room info on DB
        room = models.Room.objects.with_id(room_id)
        room.current_players.remove(username)
        room.save()

        # Remove player from game list

    def send_message(self, room_id, username, message):
        room = models.Room.objects.with_id(room_id)
        message = models.Message(datetime=datetime.now(), username=username, message=message)
        room.messages.append(message)
        room.save()

    def create_new_game(self, room_id):
        self.lock.acquire()
        try:
            new_game_created = False
            error_message = ''

            if room_id not in self.current_games:
                room = models.Room.objects.with_id(room_id)
                if len(room.current_players) >= room.min_players:
                    room.playing = True
                    room.save()

                    new_game = game.Game(list(room.current_players))
                    self.current_games[room_id] = new_game
                    new_game_created = True
                else:
                    print(str(datetime.now()), 'Impossible to create game: There are not enough players')
                    error_message = 'There aren\'t enough players'
            else:
                print(str(datetime.now()), 'Impossible to create game: A game for this room is already started')
                error_message = 'A game for this room is already started'

            response = {'success': new_game_created, 'error_message': error_message}
            return response
        finally:
            self.lock.release()

    def get_game_state(self, room_id):
        current_game = self.current_games[room_id]
        game_state_dict = {'current_state': current_game.current_state, 'current_player': current_game.current_player,
                           'players_info': current_game.players_info}
        return game_state_dict

    def send_chosen_sticks(self, room_id, username, sticks_number):
        print(str(datetime.now()), 'User', username, 'sent', str(sticks_number), 'sticks')
        current_game = self.current_games[room_id]
        current_game.choose_sticks(username, sticks_number)

    def send_guess(self, room_id, username, sticks_number):
        print(str(datetime.now()), 'User', username, 'sent', str(sticks_number), 'in your guess')
        current_game = self.current_games[room_id]
        current_game.guess(username, sticks_number)

    def get_messages(self, room_id, last_message_datetime=None):
        str_last_message_datetime = last_message_datetime

        message_datetime = None
        if last_message_datetime is not None:
            message_datetime = datetime.strptime(str_last_message_datetime, "%Y-%m-%d %H:%M:%S.%f")

        room_messages = models.Room.objects.with_id(room_id).get_new_messages(message_datetime)

        result_messages = []
        for found_message in room_messages:
            message = {'datetime': str(found_message.datetime), 'username': found_message.username,
                       'message': found_message.message}
            result_messages.append(message)

        return result_messages
