# -*- coding: utf-8 -*-
import pymongo
import bson


class CountingSticks(object):

    def __init__(self):
        pass

    def register(self, username, email, password):
        mongo_client = pymongo.MongoClient()
        db = mongo_client.countingsticks
        new_user = {'username': username, 'email': email, 'password': password}
        db.user.insert_one(new_user)
        mongo_client.close()

    def login(self, username, password):
        mongo_client = pymongo.MongoClient()
        db = mongo_client.countingsticks
        found_user = db.user.find_one({'username': username, 'password': password})
        mongo_client.close()

        return found_user is not None

    def list_rooms_ids(self):
        mongo_client = pymongo.MongoClient()
        db = mongo_client.countingsticks

        rooms = []  # change to get only id
        for room in db.room.find({}):
            rooms.append(str(room['_id']))

        mongo_client.close()
        return rooms

    def room_state(self, room_id):
        mongo_client = pymongo.MongoClient()
        db = mongo_client.countingsticks
        room = db.room.find_one({'_id': bson.objectid.ObjectId(room_id.strip())})
        mongo_client.close()
        return room

    def create_room(self, name, min_players, max_players):
        mongo_client = pymongo.MongoClient()
        db = mongo_client.countingsticks
        new_room = {'name': name, 'min_players': min_players, 'max_players': max_players,
                    'current_players': [], 'playing': False}
        result = db.room.insert_one(new_room)
        mongo_client.close()

        return result.inserted_id

    def close_room(self, room_id, username):
        # check if the user who is closing is who created
        # check if a game isn't running
        pass

    def send_message(self, room_id, message):
        # print message and add in message list
        print(message)

    def join_room(self):
        # join room
        pass

    def start_game(self, room_id):
        # start a new game in the room
        pass

    def confirm_presence(self, username):
        # confirm that client is still present on room
        pass


class Game(object):

    def __init__(self, room_id):
        self.room_id = room_id
        self.players = []


