# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
from os.path import abspath, dirname, join
import qtawesome


class RoomWidget(QtWidgets.QWidget):

    def __init__(self, main_window, counting_sticks, room_id, username, update_time=500):
        super(RoomWidget, self).__init__(main_window)

        self.counting_sticks = counting_sticks
        self.room_id = room_id
        self.username = username

        self.dict_widget_players = {}
        self.my_sticks = []
        self.selected_sticks = []

        self.main_window = main_window
        self.main_window.setWindowTitle("Room " + room_id + " - Counting Sticks")
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
        self.widget_container_game.setStyleSheet("#widget_container_game{background-color: #27ae60;}")
        # self.widget_container_game.setStyleSheet("border: 2px solid red;")  # change --------------------------------------
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

        # ----------------------------- Widgets Players -----------------------------------------#
        for username in ['lucascriistiano', 'ana_maria', 'joao_batista', 'cczinha', 'marcelo']:  #
            widget_player = PlayerInfoWidget(self.widget_players_list, username)                 #
            self.horizontal_layout_player_list.addWidget(widget_player)                          #
        # ---------------------------------------------------------------------------------------#

        self.vertical_layout_widget_container_game.addWidget(self.widget_players_list)
        # ----------------------------------------------------------------------------

        # ------------------------ Message label --------------------------------------
        font_label_message = QtGui.QFont()
        font_label_message.setPointSize(35)
        font_label_message.setBold(True)
        font_label_message.setWeight(70)

        self.label_message = QtWidgets.QLabel(self.widget_container_game)
        self.label_message.setMaximumHeight(40)
        self.label_message.setMinimumHeight(40)
        self.label_message.setText("It's your turn!")
        self.label_message.setFont(font_label_message)
        self.label_message.setStyleSheet("color: white;")
        self.label_message.setAlignment(QtCore.Qt.AlignCenter)
        self.label_message.setObjectName("label_message")
        self.vertical_layout_widget_container_game.addWidget(self.label_message)
        # ----------------------------------------------------------------------------

        # --------------- Game Elements container ------------------------------------
        self.widget_game = QtWidgets.QWidget(self.widget_container_game)
        # self.widget_game.setStyleSheet("border: 2px solid red;")  # change -----------------------------------------------
        self.widget_game.setObjectName("widget_game")

        # ---------------------------- Guess widget --------------------------------------
        self.widget_guess = QtWidgets.QWidget(self.widget_game)
        self.widget_guess.setGeometry(QtCore.QRect(20, 0, 150, 120))
        self.widget_guess.setMaximumSize(QtCore.QSize(150, 120))
        self.widget_guess.setObjectName("widget_guess")

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
        # ----------------------------------------------------------------------------

        # ------------------------- Player sticks ------------------------------------
        self.widget_my_sticks = QtWidgets.QWidget(self.widget_game)
        self.widget_my_sticks.setGeometry(QtCore.QRect(15, 160, 150, 150))
        self.widget_my_sticks.setMaximumSize(QtCore.QSize(150, 150))
        self.widget_my_sticks.setStyleSheet("QLabel{color: #f1c40f;}, QLabel:hover{color:  #f39c12;}")
        self.widget_my_sticks.setObjectName("widget_my_sticks")

        self.horizontal_layout_my_sticks = QtWidgets.QHBoxLayout(self.widget_my_sticks)
        self.horizontal_layout_my_sticks.setContentsMargins(0, 0, 0, 0)
        self.horizontal_layout_my_sticks.setObjectName("horizontal_layout_my_sticks")

        self.font_big_stick = QtGui.QFont()
        self.font_big_stick.setPointSize(150)
        self.font_big_stick.setBold(True)
        self.font_big_stick.setWeight(75)

        # ------------------------ Add player sticks ------------------------------------
        for i in range(3):                                                              #
            label_my_stick = QtWidgets.QLabel(self.widget_my_sticks)                    #
            label_my_stick.setText("|")                                                 #
            label_my_stick.setFont(self.font_big_stick)                                 #
            label_my_stick.setStyleSheet(":hover {color:  #f39c12;}")                   #
            label_my_stick.setAlignment(QtCore.Qt.AlignCenter)                          #
            label_my_stick.setObjectName("label_stick")                                 #
            self.horizontal_layout_my_sticks.addWidget(label_my_stick)                  #
                                                                                        #
            label_my_stick.mousePressEvent = self.add_stick                             #
            self.my_sticks.append(label_my_stick)                                       #
        # -------------------------------------------------------------------------------
        # -------------------------------------------------------------------------------

        # ------------------------------- Player hand -----------------------------------
        self.widget_player_hand = QtWidgets.QWidget(self.widget_game)
        self.widget_player_hand.setGeometry(QtCore.QRect(230, 10, 300, 300))
        self.widget_player_hand.setMaximumSize(QtCore.QSize(300, 300))
        self.widget_player_hand.setStyleSheet("background-color: #2ecc71; border-radius: 15px;")
        self.widget_player_hand.setObjectName("widget_player_hand")

        self.horizontal_layout_player_hand = QtWidgets.QHBoxLayout(self.widget_player_hand)
        self.horizontal_layout_player_hand.setContentsMargins(0, 0, 0, 0)
        self.horizontal_layout_player_hand.setObjectName("horizontal_layout_11")

        font_chosen_hand = QtGui.QFont()
        font_chosen_hand.setPointSize(100)
        font_chosen_hand.setBold(True)
        font_chosen_hand.setWeight(75)

        parent_folder_path = dirname(dirname(abspath(__file__)))
        pixmap_hand = QtGui.QPixmap(join(parent_folder_path, "img", "hand_cursor_xxl.png"))

        self.label_hand = QtWidgets.QLabel(self.widget_player_hand)
        self.label_hand.setPixmap(pixmap_hand)
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
                                                "QLabel:hover{color:  #f39c12;}")  # to user test border: 1px solid red;
        self.widget_chosen_sticks.setObjectName("widget_chosen_sticks")

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

        self.vertical_layout_widget_time = QtWidgets.QVBoxLayout(self.widget_time)
        self.vertical_layout_widget_time.setContentsMargins(0, 0, 0, 0)
        self.vertical_layout_widget_time.setObjectName("vertical_layout_widget_time")

        font_label_time_title = QtGui.QFont()
        font_label_time_title.setPointSize(25)
        # font_label_time_title.setBold(True)
        font_label_time_title.setWeight(70)

        self.label_time_title = QtWidgets.QLabel(self.widget_container_game)
        # self.label_time_title.setMaximumHeight(40)
        # self.label_time_title.setMinimumHeight(40)
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
        # self.label_time_value.setMaximumHeight(40)
        # self.label_time_value.setMinimumHeight(40)
        self.label_time_value.setText("30")
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

        # -------------------------------- Button New Game ------------------------------
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
        # ------------------------------------------------------------------------------

        # -------------------------------- Button Exit ---------------------------------
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
        # -----------------------------------------------------------------------------

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
        # ----------------------------------------------------------------------------------

        # --------------- Messenger elements container -------------------------------------
        self.widget_messenger = QtWidgets.QWidget(self)
        self.widget_messenger.setMaximumSize(QtCore.QSize(220, 16777215))
        self.widget_messenger.setStyleSheet("#widget_messenger{background-color: #2ecc71; border-radius: 10px;}")
        self.widget_messenger.setObjectName("widget_messenger")

        self.vertical_layout = QtWidgets.QVBoxLayout(self.widget_messenger)
        self.vertical_layout.setContentsMargins(0, 0, 0, 0)
        self.vertical_layout.setObjectName("vertical_layout")

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
        # ----------------------------------------------------------------------------------

        self.connect_buttons()

    def connect_buttons(self):
        self.label_button_go.mousePressEvent = self.go_button_action
        self.label_button_new_game.mousePressEvent = self.new_game_button_action
        self.label_button_exit.mousePressEvent = self.exit_button_action
        self.push_button_send_message.clicked.connect(self.send_message)

    def closeEvent(self, event):
        # event.accept()  # let the window close
        print('Wants to close')
        event.ignore()

    def go_button_action(self, event):
        print('Selected sticks: ' + str(len(self.selected_sticks)))

    def new_game_button_action(self, event):
        print('New game')

    def exit_button_action(self, event):
        print('Leave room')

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
