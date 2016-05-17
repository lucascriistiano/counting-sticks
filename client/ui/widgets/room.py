# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
from os.path import abspath, dirname, join
import qtawesome
import json


class RoomWidget(QtWidgets.QWidget):

    def __init__(self, main_window, counting_sticks, room_id, room_name, username, update_time=500, confirm_time=5000):
        super(RoomWidget, self).__init__(main_window)

        self.counting_sticks = counting_sticks
        self.room_id = room_id
        self.username = username

        self.widget_players_dict = {}
        self.my_sticks = []
        self.selected_sticks = []
        self.hidden_sticks = []
        self.current_state = 0
        self.waiting_other_users_action = False
        self.waiting_on_state = 0

        self.main_window = main_window
        self.main_window.setWindowTitle("Room " + room_name + " - Counting Sticks")
        self.main_window.resize(1024, 600)
        self.main_window.setMinimumSize(QtCore.QSize(1024, 600))
        self.main_window.setMaximumSize(QtCore.QSize(1024, 600))
        self.main_window.center_on_screen()

        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(self.backgroundRole(), QtGui.QColor("#27ae60"))
        self.setPalette(palette)

        self.horizontal_layout_widget_content = QtWidgets.QHBoxLayout(self)
        self.horizontal_layout_widget_content.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontal_layout_widget_content.setObjectName("horizontal_layout_widget_content")

        self.widget_container_game = QtWidgets.QWidget(self)
        self.widget_container_game.setStyleSheet("#widget_container_game{background-color: #27ae60;}")  # border: 2px solid red;
        self.widget_container_game.setObjectName("widget_container_game")

        self.vertical_layout_widget_container_game = QtWidgets.QVBoxLayout(self.widget_container_game)
        self.vertical_layout_widget_container_game.setContentsMargins(0, 0, 0, 0)
        self.vertical_layout_widget_container_game.setObjectName("vertical_layout_widget_container_game")

        # ------------------------ Players List --------------------------------------
        self.widget_players_list = QtWidgets.QWidget(self.widget_container_game)
        self.widget_players_list.setMaximumSize(QtCore.QSize(16777215, 180))
        self.widget_players_list.setObjectName("widget_players_list")

        self.horizontal_layout_player_list = QtWidgets.QHBoxLayout(self.widget_players_list)
        self.horizontal_layout_player_list.setContentsMargins(5, 5, 5, 5)
        self.horizontal_layout_player_list.setObjectName("horizontal_layout_player_list")

        self.vertical_layout_widget_container_game.addWidget(self.widget_players_list)
        # ----------------------------------------------------------------------------

        # ------------------------ Message label --------------------------------------
        font_label_message = QtGui.QFont()
        font_label_message.setPointSize(30)
        font_label_message.setBold(True)
        font_label_message.setWeight(65)

        self.label_message = QtWidgets.QLabel(self.widget_container_game)
        self.label_message.setMaximumHeight(40)
        self.label_message.setMinimumHeight(40)
        # self.label_message.setText("It's your turn!")
        self.label_message.setFont(font_label_message)
        self.label_message.setStyleSheet("color: white;")
        self.label_message.setAlignment(QtCore.Qt.AlignCenter)
        self.label_message.setObjectName("label_message")
        self.vertical_layout_widget_container_game.addWidget(self.label_message)
        # ----------------------------------------------------------------------------

        # -!-!-!-!-!-!-!-!-!-!-!- Game elements container !-!-!-!-!-!-!-!-!-!-!-!-!-!-
        self.widget_game = QtWidgets.QWidget(self.widget_container_game)
        self.widget_game.setObjectName("widget_game")

        # ---------------------------- Guess widget ----------------------------------
        self.widget_guess = QtWidgets.QWidget(self.widget_game)
        self.widget_guess.setGeometry(QtCore.QRect(20, 0, 150, 120))
        self.widget_guess.setMaximumSize(QtCore.QSize(150, 120))
        self.widget_guess.setObjectName("widget_guess")
        self.widget_guess.setVisible(False)

        self.vertical_layout_widget_guess = QtWidgets.QVBoxLayout(self.widget_guess)
        self.vertical_layout_widget_guess.setContentsMargins(0, 0, 0, 0)
        self.vertical_layout_widget_guess.setObjectName("vertical_layout_widget_guess")

        font_label_guess_title = QtGui.QFont()
        font_label_guess_title.setPointSize(25)
        font_label_guess_title.setWeight(70)

        self.label_guess_title = QtWidgets.QLabel(self.widget_container_game)
        self.label_guess_title.setText("What's your guess?")
        self.label_guess_title.setFont(font_label_guess_title)
        self.label_guess_title.setStyleSheet("color: white;")
        self.label_guess_title.setAlignment(QtCore.Qt.AlignCenter)
        self.label_guess_title.setWordWrap(True)
        self.label_guess_title.setObjectName("label_guess_title")

        font_line_edit_guess = QtGui.QFont()
        font_line_edit_guess.setPointSize(25)
        font_line_edit_guess.setWeight(70)

        self.line_edit_guess = QtWidgets.QLineEdit(self)
        self.line_edit_guess.setFixedHeight(40)
        self.line_edit_guess.setAlignment(QtCore.Qt.AlignCenter)
        self.line_edit_guess.setPlaceholderText("Guess")
        self.line_edit_guess.setFont(font_line_edit_guess)
        self.line_edit_guess.setObjectName("line_edit_guess")
        self.line_edit_guess.setMaxLength(2)

        self.vertical_layout_widget_guess.addWidget(self.label_guess_title)
        self.vertical_layout_widget_guess.addWidget(self.line_edit_guess)
        # ---------------------------------------------------------------------------

        # ------------------------- Player sticks -----------------------------------
        self.widget_my_sticks = QtWidgets.QWidget(self.widget_game)
        self.widget_my_sticks.setGeometry(QtCore.QRect(15, 160, 150, 150))
        self.widget_my_sticks.setMaximumSize(QtCore.QSize(150, 150))
        self.widget_my_sticks.setStyleSheet("QLabel{color: #f1c40f;}, QLabel:hover{color:  #f39c12;}")
        self.widget_my_sticks.setObjectName("widget_my_sticks")
        self.widget_my_sticks.setVisible(False)

        self.horizontal_layout_my_sticks = QtWidgets.QHBoxLayout(self.widget_my_sticks)
        self.horizontal_layout_my_sticks.setContentsMargins(0, 0, 0, 0)
        self.horizontal_layout_my_sticks.setObjectName("horizontal_layout_my_sticks")

        self.font_big_stick = QtGui.QFont()
        self.font_big_stick.setPointSize(150)
        self.font_big_stick.setBold(True)
        self.font_big_stick.setWeight(75)

        # ------------------------ Add player sticks ----------------------------
        for i in range(3):                                                      #
            label_my_stick = QtWidgets.QLabel(self.widget_my_sticks)            #
            label_my_stick.setText("|")                                         #
            label_my_stick.setFont(self.font_big_stick)                         #
            label_my_stick.setStyleSheet(":hover {color:  #f39c12;}")           #
            label_my_stick.setAlignment(QtCore.Qt.AlignCenter)                  #
            label_my_stick.setObjectName("label_stick")                         #
            self.horizontal_layout_my_sticks.addWidget(label_my_stick)          #
                                                                                #
            label_my_stick.mousePressEvent = self.add_stick                     #
            self.my_sticks.append(label_my_stick)                               #
        # -----------------------------------------------------------------------
        # -------------------------------------------------------------------------------

        # ------------------------------- Player hand -----------------------------------
        self.widget_player_hand = QtWidgets.QWidget(self.widget_game)
        self.widget_player_hand.setGeometry(QtCore.QRect(230, 10, 300, 300))
        self.widget_player_hand.setMaximumSize(QtCore.QSize(300, 300))
        self.widget_player_hand.setStyleSheet("background-color: #2ecc71; border-radius: 15px;")
        self.widget_player_hand.setObjectName("widget_player_hand")
        self.widget_player_hand.setVisible(False)

        self.horizontal_layout_player_hand = QtWidgets.QHBoxLayout(self.widget_player_hand)
        self.horizontal_layout_player_hand.setContentsMargins(0, 0, 0, 0)
        self.horizontal_layout_player_hand.setObjectName("horizontal_layout_11")

        font_chosen_hand = QtGui.QFont()
        font_chosen_hand.setPointSize(100)
        font_chosen_hand.setBold(True)
        font_chosen_hand.setWeight(75)

        parent_folder_path = dirname(dirname(abspath(__file__)))
        self.pixmap_hand_closed = QtGui.QPixmap(join(parent_folder_path, "img", "hand_closed.png"))
        self.pixmap_hand_open = QtGui.QPixmap(join(parent_folder_path, "img", "hand_open.png"))

        self.label_hand = QtWidgets.QLabel(self.widget_player_hand)
        self.label_hand.setPixmap(self.pixmap_hand_open)
        self.label_hand.setFont(font_chosen_hand)
        self.label_hand.setStyleSheet("color: white;")
        self.label_hand.setAlignment(QtCore.Qt.AlignCenter)
        self.label_hand.setObjectName("label_hand")
        self.horizontal_layout_player_hand.addWidget(self.label_hand)
        # -------------------------------------------------------------------------------

        # ----------------------------- Chosen sticks -----------------------------------
        self.widget_chosen_sticks = QtWidgets.QWidget(self.widget_game)
        self.widget_chosen_sticks.setGeometry(QtCore.QRect(350, 160, 110, 110))
        self.widget_chosen_sticks.setMaximumSize(QtCore.QSize(150, 150))
        self.widget_chosen_sticks.setStyleSheet("QLabel{color: #f1c40f;}, "
                                                "QLabel:hover{color:  #f39c12;}")
        self.widget_chosen_sticks.setObjectName("widget_chosen_sticks")
        self.widget_chosen_sticks.setVisible(False)

        self.horizontal_layout_chosen_sticks = QtWidgets.QHBoxLayout(self.widget_chosen_sticks)
        self.horizontal_layout_chosen_sticks.setContentsMargins(0, 0, 0, 0)
        self.horizontal_layout_chosen_sticks.setObjectName("horizontal_layout_chosen_sticks")
        # -------------------------------------------------------------------------------

        # -------------------------------- Button Go! -----------------------------------
        self.widget_button_go = QtWidgets.QWidget(self.widget_game)
        self.widget_button_go.setGeometry(QtCore.QRect(180, 50, 100, 100))
        self.widget_button_go.setMaximumSize(QtCore.QSize(200, 200))
        self.widget_button_go.setStyleSheet("QWidget{background-color: #3498db; border-radius: 50%;} "
                                            "QWidget:hover{background-color: #2e8ece; border-radius: 50%;}")
        self.widget_button_go.setObjectName("widget_button_go")
        self.widget_button_go.setVisible(False)

        self.horizontal_layout_button_go = QtWidgets.QHBoxLayout(self.widget_button_go)
        self.horizontal_layout_button_go.setContentsMargins(0, 0, 0, 0)
        self.horizontal_layout_button_go.setObjectName("horizontal_layout_button_go")

        font_label_go = QtGui.QFont()
        font_label_go.setPointSize(35)
        font_label_go.setBold(True)
        font_label_go.setWeight(75)

        self.label_button_go = QtWidgets.QLabel(self.widget_button_go)
        self.label_button_go.setText("Go!")
        self.label_button_go.setFont(font_label_go)
        self.label_button_go.setStyleSheet("color: white;")
        self.label_button_go.setAlignment(QtCore.Qt.AlignCenter)
        self.label_button_go.setObjectName("label_button_go")
        self.horizontal_layout_button_go.addWidget(self.label_button_go)
        # -------------------------------------------------------------------------------

        # ---------------------------- Time widget --------------------------------------
        self.widget_time = QtWidgets.QWidget(self.widget_game)
        self.widget_time.setGeometry(QtCore.QRect(540, 30, 200, 120))
        self.widget_time.setMaximumSize(QtCore.QSize(200, 120))
        self.widget_time.setStyleSheet("color: white;")
        self.widget_time.setObjectName("widget_time")
        self.widget_time.setVisible(False)

        self.vertical_layout_widget_time = QtWidgets.QVBoxLayout(self.widget_time)
        self.vertical_layout_widget_time.setContentsMargins(0, 0, 0, 0)
        self.vertical_layout_widget_time.setObjectName("vertical_layout_widget_time")

        font_label_time_title = QtGui.QFont()
        font_label_time_title.setPointSize(25)
        font_label_time_title.setWeight(70)

        self.label_time_title = QtWidgets.QLabel(self.widget_container_game)
        self.label_time_title.setText("Time")
        self.label_time_title.setFont(font_label_time_title)
        self.label_time_title.setStyleSheet("color: white;")
        self.label_time_title.setAlignment(QtCore.Qt.AlignCenter)
        self.label_time_title.setObjectName("label_time_title")

        font_label_time_value = QtGui.QFont()
        font_label_time_value.setPointSize(70)
        font_label_time_value.setBold(True)
        font_label_time_value.setWeight(70)

        self.label_time_value = QtWidgets.QLabel(self.widget_container_game)
        self.label_time_value.setText("-")
        self.label_time_value.setFont(font_label_time_value)
        self.label_time_value.setStyleSheet("color: white;")
        self.label_time_value.setAlignment(QtCore.Qt.AlignCenter)
        self.label_time_value.setObjectName("label_time_value")

        self.vertical_layout_widget_time.addWidget(self.label_time_title)
        self.vertical_layout_widget_time.addWidget(self.label_time_value)
        # ----------------------------------------------------------------------------

        font_label_new_game_exit = QtGui.QFont()
        font_label_new_game_exit.setPointSize(30)
        font_label_new_game_exit.setWeight(60)

        # ----------------------------- Button New Game ------------------------------
        self.widget_button_new_game = QtWidgets.QWidget(self.widget_game)
        self.widget_button_new_game.setGeometry(QtCore.QRect(540, 170, 200, 60))
        self.widget_button_new_game.setMaximumSize(QtCore.QSize(200, 65))
        self.widget_button_new_game.setStyleSheet("QWidget{background-color: #e67e22; border-radius: 10px;} "
                                                  "QWidget:hover{background-color: #d35400; border-radius: 10px;}")
        self.widget_button_new_game.setObjectName("widget_button_new_game")

        self.horizontal_layout_button_new_game = QtWidgets.QHBoxLayout(self.widget_button_new_game)
        self.horizontal_layout_button_new_game.setContentsMargins(0, 0, 0, 0)
        self.horizontal_layout_button_new_game.setObjectName("horizontal_layout_button_new_game")

        self.label_button_new_game = QtWidgets.QLabel(self.widget_button_new_game)
        self.label_button_new_game.setText("New Game")
        self.label_button_new_game.setFont(font_label_new_game_exit)
        self.label_button_new_game.setStyleSheet("color: white;")
        self.label_button_new_game.setAlignment(QtCore.Qt.AlignCenter)
        self.label_button_new_game.setObjectName("label_button_new_game")
        self.horizontal_layout_button_new_game.addWidget(self.label_button_new_game)
        # ----------------------------------------------------------------------------

        # -------------------------------- Button Exit -------------------------------
        self.widget_button_exit = QtWidgets.QWidget(self.widget_game)
        self.widget_button_exit.setGeometry(QtCore.QRect(540, 240, 200, 60))
        self.widget_button_exit.setMaximumSize(QtCore.QSize(200, 65))
        self.widget_button_exit.setStyleSheet("QWidget{background-color: #e74c3c; border-radius: 10px;} "
                                              "QWidget:hover{background-color: #c0392b; border-radius: 10px;}")
        self.widget_button_exit.setObjectName("widget_button_exit")

        self.horizontal_layout_button_exit = QtWidgets.QHBoxLayout(self.widget_button_exit)
        self.horizontal_layout_button_exit.setContentsMargins(0, 0, 0, 0)
        self.horizontal_layout_button_exit.setObjectName("horizontal_layout_button_exit")

        self.label_button_exit = QtWidgets.QLabel(self.widget_button_exit)
        self.label_button_exit.setText("Exit")
        self.label_button_exit.setFont(font_label_new_game_exit)
        self.label_button_exit.setStyleSheet("color: white;")
        self.label_button_exit.setAlignment(QtCore.Qt.AlignCenter)
        self.label_button_exit.setObjectName("label_button_exit")
        self.horizontal_layout_button_exit.addWidget(self.label_button_exit)
        # ----------------------------------------------------------------------------

        self.widget_guess.raise_()
        self.widget_my_sticks.raise_()
        self.widget_player_hand.raise_()
        self.widget_button_go.raise_()
        self.widget_time.raise_()
        self.widget_button_new_game.raise_()
        self.widget_button_exit.raise_()
        self.widget_chosen_sticks.raise_()

        self.vertical_layout_widget_container_game.addWidget(self.widget_game)
        self.horizontal_layout_widget_content.addWidget(self.widget_container_game)
        # -!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-

        # -!-!-!-!-!-!-!-!-!-!- Messenger elements container !-!-!-!-!-!-!-!-!-!-!-!-!-
        self.widget_messenger = QtWidgets.QWidget(self)
        self.widget_messenger.setMaximumSize(QtCore.QSize(220, 16777215))
        self.widget_messenger.setStyleSheet("#widget_messenger{background-color: #2ecc71; border-radius: 10px;}")
        self.widget_messenger.setObjectName("widget_messenger")

        self.vertical_layout = QtWidgets.QVBoxLayout(self.widget_messenger)
        self.vertical_layout.setContentsMargins(0, 0, 0, 0)
        self.vertical_layout.setObjectName("vertical_layout")

        # ----------------------------- Label Username -------------------------------
        font_label_username = QtGui.QFont()
        font_label_username.setPointSize(25)
        font_label_username.setWeight(50)

        self.widget_username = QtWidgets.QWidget(self.widget_messenger)
        self.widget_username.setStyleSheet("QWidget{background-color: #95a5a6; border-radius: 10px;}")
        self.widget_username.setObjectName("widget_username")

        self.horizontal_layout_widget_username = QtWidgets.QHBoxLayout(self.widget_username)
        self.horizontal_layout_widget_username.setContentsMargins(0, 0, 0, 0)
        self.horizontal_layout_widget_username.setObjectName("horizontal_layout_widget_username")

        self.label_username = QtWidgets.QLabel(self.widget_username)
        self.label_username.setText(self.username)
        self.label_username.setFont(font_label_username)
        self.label_username.setStyleSheet("color: white;")
        self.label_username.setAlignment(QtCore.Qt.AlignCenter)
        self.label_username.setObjectName("label_username")
        self.horizontal_layout_widget_username.addWidget(self.label_username)

        self.vertical_layout.addWidget(self.widget_username)
        # ----------------------------------------------------------------------------

        # ----------------------- Message list widget ---------------------------------
        self.list_widget_messages = QtWidgets.QListWidget(self.widget_messenger)
        self.list_widget_messages.setWordWrap(True)
        self.list_widget_messages.setLineWidth(10)
        self.list_widget_messages.setAutoScroll(True)
        self.list_widget_messages.setFocusPolicy(QtCore.Qt.NoFocus)
        self.list_widget_messages.setStyleSheet("background-color: white;")
        self.list_widget_messages.setObjectName("list_widget_messages")
        self.vertical_layout.addWidget(self.list_widget_messages)
        # -----------------------------------------------------------------------------

        # -------------------------- Edit text widget ---------------------------------
        self.plain_text_edit_message = QtWidgets.QPlainTextEdit(self.widget_messenger)
        self.plain_text_edit_message.setPlaceholderText("Type your message")
        self.plain_text_edit_message.setMaximumSize(QtCore.QSize(16777215, 80))
        self.plain_text_edit_message.setStyleSheet("background-color:white;")
        self.plain_text_edit_message.setObjectName("plain_text_edit_message")
        self.vertical_layout.addWidget(self.plain_text_edit_message)
        # -----------------------------------------------------------------------------

        # ---------------------------- Button message ---------------------------------
        font_button_send_message = QtGui.QFont()
        font_button_send_message.setPointSize(15)

        fa_send_message_icon = qtawesome.icon('fa.comment-o')
        self.push_button_send_message = QtWidgets.QPushButton(fa_send_message_icon, "Send Message",
                                                              self.widget_messenger)
        self.push_button_send_message.setFont(font_button_send_message)
        self.push_button_send_message.setStyleSheet("")
        self.push_button_send_message.setObjectName("push_button_send_message")
        self.vertical_layout.addWidget(self.push_button_send_message)
        # -----------------------------------------------------------------------------

        self.horizontal_layout_widget_content.addWidget(self.widget_messenger)

        # -!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-

        self.connect_buttons()

        self.timer_confirm_presence = QtCore.QTimer()
        self.timer_confirm_presence.timeout.connect(self.confirm_presence)
        self.timer_confirm_presence.start(confirm_time)

        self.main_window.reconnect_update_timer(self.update_game_state)
        self.main_window.start_update_timer()

    def connect_buttons(self):
        self.label_button_go.mousePressEvent = self.go_button_action
        self.label_button_new_game.mousePressEvent = self.new_game_button_action
        self.label_button_exit.mousePressEvent = self.exit_button_action
        self.push_button_send_message.clicked.connect(self.send_message)

    def update_game_state(self):
        room_info_raw_json = self.counting_sticks.get_room_info(self.room_id)
        room_info = json.loads(room_info_raw_json)

        if 'current_players' not in room_info:
            room_info['current_players'] = []

        current_players = room_info['current_players']

        # Remove current user info from list
        if self.username in current_players:
            current_players.remove(self.username)

        self.check_created_player_info_widgets(current_players)

        if room_info['playing']:
            game_state = self.counting_sticks.get_game_state(self.room_id)
            user_player_info = game_state['players_info'].pop(self.username)

            self.current_state = game_state['current_state']

            # Fill game info for each player
            for username in game_state['players_info']:
                player_info = game_state['players_info'][username]
                if username in self.widget_players_dict:
                    widget_player = self.widget_players_dict[username]
                    widget_player.update_info(player_info['username'], player_info['current_sticks'],
                                              player_info['last_guesses'], player_info['current_guess'])

            if self.current_state == 0:  # choose sticks
                self.label_message.setText('Select your sticks')

                # Check number of sticks and hide sticks excess
                if len(self.my_sticks) > user_player_info['current_sticks']:
                    sticks_to_remove = len(self.my_sticks) - user_player_info['current_sticks']
                    for i in range(sticks_to_remove):
                        self.hide_stick()

                # Set pixmap to hand
                self.label_hand.setPixmap(self.pixmap_hand_open)

                # Clear indicator of current player making guess
                for username in self.widget_players_dict:
                    widget_player = self.widget_players_dict[username]
                    palette = widget_player.palette()
                    palette.setColor(self.backgroundRole(), QtGui.QColor("#2ecc71"))
                    widget_player.setPalette(palette)

                # Make components visible
                self.widget_guess.setVisible(False)
                self.widget_my_sticks.setVisible(True)
                self.widget_button_go.setVisible(True)
                self.widget_player_hand.setVisible(True)
                self.widget_chosen_sticks.setVisible(True)
                self.widget_time.setVisible(True)
                self.widget_button_new_game.setVisible(False)

                # change items when is waiting for users action
                if self.waiting_other_users_action and self.waiting_on_state == self.current_state:
                    self.widget_my_sticks.setVisible(False)
                    self.widget_button_go.setVisible(False)
                    self.widget_chosen_sticks.setVisible(False)
                    self.widget_time.setVisible(False)

                    # Set pixmap to hand close
                    self.label_hand.setPixmap(self.pixmap_hand_closed)

            elif self.current_state == 1:  # guess sticks number
                self.move_selected_sticks_to_my_sticks()

                # Set pixmap to hand
                self.label_hand.setPixmap(self.pixmap_hand_closed)

                if game_state['current_player'] == self.username:
                    self.label_message.setText('It\'s your time to guess!')
                else:
                    self.label_message.setText('Waiting guesses')

                # Indicate current player making guess
                for username in self.widget_players_dict:
                    widget_player = self.widget_players_dict[username]
                    palette = widget_player.palette()

                    if game_state['current_player'] == username:
                        palette.setColor(self.backgroundRole(), QtGui.QColor("#e67e22"))
                    else:
                        palette.setColor(self.backgroundRole(), QtGui.QColor("#2ecc71"))

                    widget_player.setPalette(palette)

                # Make components visible
                if game_state['current_player'] == self.username:
                    self.widget_guess.setVisible(True)
                    self.widget_button_go.setVisible(True)
                else:
                    self.widget_guess.setVisible(False)
                    self.widget_button_go.setVisible(False)

                self.widget_my_sticks.setVisible(False)
                self.widget_player_hand.setVisible(True)
                self.widget_chosen_sticks.setVisible(False)
                self.widget_time.setVisible(True)
                self.widget_button_new_game.setVisible(False)

                # change items when is waiting for users action
                if self.waiting_other_users_action and self.waiting_on_state == self.current_state:
                    self.widget_guess.setVisible(False)
                    self.widget_button_go.setVisible(False)
                    self.widget_time.setVisible(False)

            else:  # game finished
                self.move_selected_sticks_to_my_sticks()
                self.show_hidden_sticks()

                # Make components visible
                self.widget_guess.setVisible(False)
                self.widget_my_sticks.setVisible(False)
                self.widget_button_go.setVisible(False)
                self.widget_player_hand.setVisible(False)
                self.widget_chosen_sticks.setVisible(False)
                self.widget_time.setVisible(False)
                self.widget_button_new_game.setVisible(True)

                print('Game finished')

        else:
            # Make components visible
            self.widget_guess.setVisible(False)
            self.widget_my_sticks.setVisible(False)
            self.widget_button_go.setVisible(False)
            self.widget_player_hand.setVisible(False)
            self.widget_chosen_sticks.setVisible(False)
            self.widget_time.setVisible(False)
            self.widget_button_new_game.setVisible(True)

    def check_created_player_info_widgets(self, current_players):
        # Add new users widgets
        for username in current_players:
            if username not in self.widget_players_dict:
                self.add_new_player_info_widget(username)

        # Remove players that exited
        for username in list(self.widget_players_dict):
            if username not in current_players:
                self.remove_player_info_widget(username)

    def add_new_player_info_widget(self, username):
        widget_player = PlayerInfoWidget(self.widget_players_list, username)
        widget_player.setObjectName("widget_player" + username)
        self.horizontal_layout_player_list.addWidget(widget_player)
        self.widget_players_dict[username] = widget_player

    def remove_player_info_widget(self, username):
        widget_player = self.widget_players_dict.pop(username)
        self.horizontal_layout_player_list.removeWidget(widget_player)
        widget_player.deleteLater()

    def go_button_action(self, event):
        if self.current_state == 0:
            self.send_selected_sticks()
        elif self.current_state == 1:
            self.send_guess()

    def send_selected_sticks(self):
        self.counting_sticks.send_chosen_sticks(self.room_id, self.username, len(self.selected_sticks))

        # check if sticks number was accepted
        self.waiting_other_users_action = True
        self.waiting_on_state = self.current_state

    def send_guess(self):
        str_guess = self.line_edit_guess.text()
        if str_guess != '':
            guess_sticks_number = int(str_guess)
            self.counting_sticks.send_guess(self.room_id, self.username, guess_sticks_number)

            # check if sticks number was accepted
            self.waiting_other_users_action = True
            self.waiting_on_state = self.current_state

            self.line_edit_guess.clear()
        else:
            self.label_message.setText('Enter your guess first')

    def confirm_presence(self):
        self.counting_sticks.confirm_presence(self.room_id, self.username)

    def new_game_button_action(self, event):
        response = self.counting_sticks.create_new_game(self.room_id)
        if not response['success']:
            self.label_message.setText(response['error_message'])

    def exit_button_action(self, event):
        print('Leave room')

    def hide_stick(self):
        stick = self.my_sticks.pop(0)
        self.horizontal_layout_my_sticks.removeWidget(stick)

        stick.setParent(None)
        stick.mousePressEvent = None
        self.hidden_sticks.append(stick)

    def show_hidden_sticks(self):
        # Remove stick from hidden sticks
        hidden_sticks_number = len(self.hidden_sticks)
        for i in range(hidden_sticks_number):
            # Get stick and move to available sticks
            hidden_stick = self.hidden_sticks.pop(0)
            hidden_stick.setParent(self.widget_my_sticks)
            hidden_stick.mousePressEvent = self.add_stick
            self.horizontal_layout_my_sticks.addWidget(hidden_stick)
            self.my_sticks.append(hidden_stick)

    def move_selected_sticks_to_my_sticks(self):
        selected_sticks_number = len(self.selected_sticks)
        for i in range(selected_sticks_number):
            self.remove_stick(None)

    def add_stick(self, event):
        if len(self.my_sticks) > 0:
            # Remove stick from available sticks
            clicked_label_my_stick = self.my_sticks.pop(0)
            self.horizontal_layout_my_sticks.removeWidget(clicked_label_my_stick)

            # Move stick to selected sticks
            clicked_label_my_stick.setParent(self.widget_chosen_sticks)
            clicked_label_my_stick.mousePressEvent = self.remove_stick
            self.horizontal_layout_chosen_sticks.addWidget(clicked_label_my_stick)
            self.selected_sticks.append(clicked_label_my_stick)

    def remove_stick(self, event):
        if len(self.selected_sticks) > 0:
            # Remove stick from selected sticks
            clicked_label_chosen_stick = self.selected_sticks.pop(0)
            self.horizontal_layout_chosen_sticks.removeWidget(clicked_label_chosen_stick)

            # Move stick to available sticks
            clicked_label_chosen_stick.setParent(self.widget_my_sticks)
            clicked_label_chosen_stick.mousePressEvent = self.add_stick
            self.horizontal_layout_my_sticks.addWidget(clicked_label_chosen_stick)
            self.my_sticks.append(clicked_label_chosen_stick)

    def send_message(self):
        message = self.plain_text_edit_message.toPlainText()

        if message != "":
            self.counting_sticks.send_message(self.room_id, self.username, message)
            self.plain_text_edit_message.clear()

            self.list_widget_messages.addItem(self.username + ': ' + message)
            print('Message sent! Update messages later')
            
            
class PlayerInfoWidget(QtWidgets.QWidget):
    
    def __init__(self, parent, username):
        super(PlayerInfoWidget, self).__init__(parent)

        self.setMaximumSize(QtCore.QSize(125, 200))
        # self.setStyleSheet("background-color: #2ecc71; border-radius: 15px;")
        # self.setObjectName("widget_player")

        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(self.backgroundRole(), QtGui.QColor("#2ecc71"))
        self.setPalette(palette)

        self.vertical_layout_widget_player = QtWidgets.QVBoxLayout(self)
        self.vertical_layout_widget_player.setContentsMargins(0, 0, 0, 0)
        self.vertical_layout_widget_player.setObjectName("vertical_layout_widget_player")

        font = QtGui.QFont()
        font.setPointSize(14)

        self.label_username = QtWidgets.QLabel(self)
        self.label_username.setText(username)
        self.label_username.setMaximumSize(QtCore.QSize(16777215, 40))
        self.label_username.setFont(font)
        self.label_username.setStyleSheet("color: white;")
        self.label_username.setAlignment(QtCore.Qt.AlignCenter)
        self.label_username.setWordWrap(True)
        self.label_username.setObjectName("label_username")
        self.vertical_layout_widget_player.addWidget(self.label_username)

        font = QtGui.QFont()
        font.setPointSize(40)
        font.setBold(True)
        font.setWeight(75)

        self.label_sticks = QtWidgets.QLabel(self)
        self.label_sticks.setText("")
        self.label_sticks.setFont(font)
        self.label_sticks.setStyleSheet("color: #f1c40f;")
        self.label_sticks.setAlignment(QtCore.Qt.AlignCenter)
        self.label_sticks.setObjectName("label_sticks")
        self.vertical_layout_widget_player.addWidget(self.label_sticks)

        font = QtGui.QFont()
        font.setPointSize(16)

        self.label_last_guesses = QtWidgets.QLabel(self)
        self.label_last_guesses.setText("")
        self.label_last_guesses.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_last_guesses.setFont(font)
        self.label_last_guesses.setStyleSheet("color: white;")
        self.label_last_guesses.setAlignment(QtCore.Qt.AlignCenter)
        self.label_last_guesses.setWordWrap(True)
        self.label_last_guesses.setObjectName("label_last_guesses")
        self.vertical_layout_widget_player.addWidget(self.label_last_guesses)

        font = QtGui.QFont()
        font.setPointSize(29)

        self.label_current_guess = QtWidgets.QLabel(self)
        self.label_current_guess.setText("")
        self.label_current_guess.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_current_guess.setFont(font)
        self.label_current_guess.setStyleSheet("color: white;")
        self.label_current_guess.setAlignment(QtCore.Qt.AlignCenter)
        self.label_current_guess.setWordWrap(True)
        self.label_current_guess.setObjectName("label_current_guess")
        self.vertical_layout_widget_player.addWidget(self.label_current_guess)

    def update_info(self, username, current_sticks, last_guesses, current_guess):
        self.label_username.setText(username)

        str_label_sticks = ''.join('|' for x in range(current_sticks))
        self.label_sticks.setText(str_label_sticks)

        if len(last_guesses) > 0:
            str_last_guesses = '-'.join(str(x) for x in last_guesses)
            self.label_last_guesses.setText(str_last_guesses)
        else:
            self.label_last_guesses.setText('?')

        self.label_current_guess.setText('-' if current_guess is None else str(current_guess))
