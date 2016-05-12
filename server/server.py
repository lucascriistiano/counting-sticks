

class CountingSticks(object):

    def __init__(self):
        self.users = {}

    def register(self, username, email, password):
        print(username, email, password)
        self.users[username] = {'username': username, 'email': email, 'password': password }
        print("Registered")

        print('Current users: ', self.users)

    def login(self, username, password):
        if username in self.users:
            found_user = self.users[username]
            return found_user['password'] == password
