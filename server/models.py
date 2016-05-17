from mongoengine import *


class User(Document):
    username = StringField()
    email = StringField()
    password = StringField()


class Message(EmbeddedDocument):
    datetime = DateTimeField()
    username = StringField()
    message = StringField()


class Room(Document):
    created_by = StringField()
    name = StringField()
    min_players = IntField()
    max_players = IntField()
    current_players = ListField(StringField(), default=list)
    playing = BooleanField()
    messages = ListField(EmbeddedDocumentField(Message))

# class Game(Document):
#     pass