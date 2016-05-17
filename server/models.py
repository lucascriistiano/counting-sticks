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

    def get_new_messages(self, last_message_datetime):
        if last_message_datetime is None:
            return self.messages
        else:
            return [message for message in self.messages if message.datetime > last_message_datetime]
