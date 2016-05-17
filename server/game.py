# -*- coding: utf-8 -*-
import threading


class Game(object):

    def __init__(self, players):
        self.rounds = 0

        self.current_state = 0  # 0 - Choose sticks, 1 - Guess, 2 - Finished

        self.players_info = {}
        for username in players:
            self.players_info[username] = {'username': username, 'current_sticks': 3,
                                           'last_guesses': [], 'current_guess': None}

        self.players_order = list(players)
        self.pending_players_action = list(self.players_order)

        self.selected_sticks = {}
        self.round_results = {}
        self.game_results = []
        self.winners = []

        self.lock = threading.RLock()

    def choose_sticks(self, username, sticks_number):
        self.lock.acquire()
        try:
            if self.current_state == 0:  # choose sticks mode

                if username in self.pending_players_action:
                    self.selected_sticks[username] = sticks_number
                    self.pending_players_action.remove(username)

                if not self.pending_players_action:
                    print('Everybody chose sticks number')
                    self.go_to_next_state()

        finally:
            self.lock.release()

    def guess(self, username, sticks_number):
        self.lock.acquire()
        try:
            if self.current_state == 1:  # make guess mode

                if self.has_pending_players():
                    if username in self.pending_players_action:  # players who didn't make guess yet
                        if username == self.current_player:
                            if username in self.players_info:
                                # Check sticks guess limit value
                                # Avoid repeated guesses

                                # save guess and pass to next player
                                self.players_info[username]['current_guess'] = sticks_number
                                self.remove_current_player_of_round()

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
            if self.current_state == 0:  # Choose Sticks State
                self.current_state = 1

            elif self.current_state == 1:  # Guess State
                self.process_results()

                if self.is_game_finished():
                    self.current_state = 2  # Game Finished

                    print('Game is finished')
                    print('Winners')
                    print(self.winners)
                    print('Results')
                    print(self.game_results)
                else:
                    self.rounds += 1
                    self.round_results = {}
                    self.current_state = 0

                    for username in self.players_info:
                        current_guess = self.players_info[username]['current_guess']

                        last_guesses_number = len(self.players_info[username]['last_guesses'])
                        if last_guesses_number == 3:
                            self.players_info[username]['last_guesses'].pop(0)

                        self.players_info[username]['last_guesses'].append(current_guess)
                        self.players_info[username]['current_guess'] = None

                self.define_next_round_players_order()

            self.pending_players_action = list(self.players_order)
        finally:
            self.lock.release()

    def define_next_round_players_order(self):
        last_round_first_player = self.players_order.pop(0)
        self.players_order.append(last_round_first_player)

    def remove_current_player_of_round(self):
        self.pending_players_action.pop(0)

    @property
    def current_player(self):
        return self.pending_players_action[0]

    def has_pending_players(self):
        return len(self.pending_players_action) > 0

    def is_game_finished(self):
        players_with_sticks = 0
        for username in self.players_info:
            current_sticks = self.players_info[username]['current_sticks']
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
        for username in self.players_info:
            current_guess = self.players_info[username]['current_guess']
            if current_guess == total_selected_sticks:
                round_has_winner = True
                self.round_results['winner'] = username
                self.round_results['total_sticks'] = total_selected_sticks

                # remove a stick of winner
                self.players_info[username]['current_sticks'] -= 1

                if self.players_info[username]['current_sticks'] == 0:
                    # remove player from order list to play
                    self.winners.append(username)

                print(username, ' hit the total of sticks!')
                break

        if round_has_winner:
            self.game_results.append(self.round_results)
