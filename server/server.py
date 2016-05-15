# -*- coding: utf-8 -*-
import pymongo
import bson
from datetime import datetime
import threading


class CountingSticks(object):

    def __init__(self):
        self.lock = threading.Lock()

    def register(self, username, email, password):
        mongo_client = pymongo.MongoClient()
        user_collection = mongo_client.countingsticks.user
        new_user = {'username': username, 'email': email, 'password': password}
        user_collection.insert_one(new_user)
        mongo_client.close()

    def login(self, username, password):
        mongo_client = pymongo.MongoClient()
        user_collection = mongo_client.countingsticks.user
        found_user = user_collection.find_one({'username': username, 'password': password})
        mongo_client.close()

        return found_user is not None

    def list_rooms_ids(self):
        mongo_client = pymongo.MongoClient()
        room_collection = mongo_client.countingsticks.room

        rooms = []  # change to get only id
        for room in room_collection.find({}):
            rooms.append(str(room['_id']))

        mongo_client.close()
        return rooms

    def room_state(self, room_id):
        mongo_client = pymongo.MongoClient()
        room_collection = mongo_client.countingsticks.room
        room = room_collection.find_one({'_id': bson.objectid.ObjectId(room_id.strip())})
        mongo_client.close()
        return room

    def create_room(self, name, min_players, max_players):
        mongo_client = pymongo.MongoClient()
        room_collection = mongo_client.countingsticks.room
        new_room = {'name': name, 'min_players': min_players, 'max_players': max_players,
                    'current_players': [], 'playing': False, 'messages': []}
        result = room_collection.insert_one(new_room)
        mongo_client.close()

        return result.inserted_id

    def close_room(self, room_id, username):
        # check if the user who is closing is who created
        # check if a game isn't running
        pass

    def send_message(self, room_id, username, message):
        mongo_client = pymongo.MongoClient()
        room_collection = mongo_client.countingsticks.room
        room = room_collection.find_one({'_id': bson.objectid.ObjectId(room_id.strip())})

        message_dict = {'datetime': datetime.now(), 'username': username, 'message': message}
        room['messages'].append(message_dict)
        room_collection.save(room)

        mongo_client.close()

    def join_room(self, room_id, username):
        self.lock.acquire()
        try:
            mongo_client = pymongo.MongoClient()
            room_collection = mongo_client.countingsticks.room
            room = room_collection.find_one({'_id': bson.objectid.ObjectId(room_id.strip())})

            current_players = room['current_players']
            if len(current_players) < room['max_players']:
                if username not in current_players:
                    room['current_players'].append(username)
                    room_collection.save(room)
                    mongo_client.close()
                return True
            else:
                return False
        finally:
            self.lock.release()
            print('Released')

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


