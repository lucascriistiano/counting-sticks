# -*- coding: utf-8 -*-
import threading


class GameState(object):

    def __init__(self, players):
        self.current_state = 0  # 0 - Choose sticks, 1 - Guess, 2 - Finished
        self.current_player = ''

        self.players_info = {}
        for username in players:
            self.players_info[username] = {'username': username, 'current_sticks': 3,
                                           'last_guesses': [], 'current_guess': None}


class Game(object):

    def __init__(self, room_id, players):
        self.room_id = room_id

        self.rounds = 0
        self.pending_players_to_start = set(players)

        self.players_order = list(players)
        self.pending_players_action = list(self.players_order)

        self.game_state = GameState(players)
        self.game_state.current_player = self.current_player()

        self.selected_sticks = {}
        self.round_results = {}
        self.game_results = []

        self.winners = []

        self.lock = threading.RLock()

    def choose_sticks(self, username, sticks_number):
        self.lock.acquire()
        try:
            if self.game_state.current_state == 0:  # choose sticks mode

                if username in self.pending_players_action:
                    self.selected_sticks[username] = sticks_number
                    self.pending_players_action.remove(username)
                    print(username, ' chose ', self.selected_sticks[username], ' sticks')

                if not self.pending_players_action:
                    print('Everybody chose sticks number')
                    self.go_to_next_state()

        finally:
            self.lock.release()

    def guess(self, username, sticks_number):
        self.lock.acquire()
        try:
            if self.game_state.current_state == 1:  # make guess mode
                if self.has_pending_players():
                    if username in self.pending_players_action:  # players who didn't make guess yet
                        if username == self.current_player():
                            if username in self.game_state.players_info:
                                # Check sticks guess limit value
                                # Avoid repeated guesses

                                # save guess and pass to next player
                                self.game_state.players_info[username]['current_guess'] = sticks_number
                                self.next_player()
                                print('Guess ', username, ': ', sticks_number)

                                if not self.has_pending_players():
                                    print('Everybody made guess')
                                    self.go_to_next_state()
                            else:
                                print(username, ' is not in the players info dict')
                        else:
                            print(username, ' is not the current player')
                    else:
                        print(username, ' had already made your guess')

        finally:
            self.lock.release()

    def go_to_next_state(self):
        self.lock.acquire()
        try:
            if self.game_state.current_state == 0:  # Choose Sticks State
                if self.rounds != 0:
                    self.set_next_round_players_order()

                self.game_state.current_state = 1

            elif self.game_state.current_state == 1:  # Guess State
                self.process_results()
                if self.is_game_finished():
                    self.game_state.current_state = 2
                else:
                    self.rounds += 1
                    self.round_results = {}
                    self.game_state.current_state = 0

                    for username in self.game_state.players_info:
                        current_guess = self.game_state.players_info[username]['current_guess']

                        if len(self.game_state.players_info[username]['last_guesses']) == 3:
                            self.game_state.players_info[username]['last_guesses'].pop(0)
                        self.game_state.players_info[username]['last_guesses'].append(current_guess)

                        self.game_state.players_info[username]['current_guess'] = None

            elif self.game_state.current_state == 2:  # Game Finished
                print('Game is finished')

            self.pending_players_action = list(self.players_order)
        finally:
            self.lock.release()

    def current_state(self):
        return self.game_state

    def remove_player(self, username):
        self.players_order.remove(username)

    def set_next_round_players_order(self):
        last_round_first_player = self.players_order.pop(0)
        self.pending_players_to_start.remove(last_round_first_player)
        self.players_order.append(last_round_first_player)

    def next_player(self):
        self.pending_players_action.pop(0)

        if self.has_pending_players():
            self.game_state.current_player = self.current_player()

    def current_player(self):
        return self.pending_players_action[0]

    def has_pending_players(self):
        return len(self.pending_players_action) > 0

    def is_game_finished(self):
        players_with_sticks = 0
        for username in self.game_state.players_info:
            current_sticks = self.game_state.players_info[username]['current_sticks']
            if current_sticks > 0:
                players_with_sticks += 1

            if players_with_sticks > 1:
                return False

        return True

    def process_results(self):
        total_selected_sticks = 0
        for username in self.selected_sticks:
            total_selected_sticks += self.selected_sticks[username]

        round_has_winner = False
        for username in self.game_state.players_info:
            current_guess = self.game_state.players_info[username]['current_guess']
            if current_guess == total_selected_sticks:
                round_has_winner = True
                self.round_results['winner'] = username
                self.round_results['total_sticks'] = total_selected_sticks

                # remove a stick of winner
                self.game_state.players_info[username]['current_sticks'] -= 1

                if self.game_state.players_info[username]['current_sticks'] == 0:
                    # remove player from order list to play
                    self.winners.append(username)

                print(username, ' hit the total of sticks!')
                break

        if round_has_winner:
            self.game_results.append(self.game_results)
