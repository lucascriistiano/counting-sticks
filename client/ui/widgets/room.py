# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
from os.path import abspath, dirname, join


class RoomWidget(QtWidgets.QWidget):

    def __init__(self, main_window, counting_sticks, room_id, update_time=500):
        super(RoomWidget, self).__init__(main_window)

        self.counting_sticks = counting_sticks
        self.room_id = room_id

        self.main_window = main_window
        self.main_window.setWindowTitle("Room " + room_id + " - Counting Sticks")
        self.main_window.resize(1024, 600)
        self.main_window.setMinimumSize(QtCore.QSize(1024, 600))
        self.main_window.setMaximumSize(QtCore.QSize(1024, 600))
        # self.main_window.setAutoFillBackground(False)

        self.setObjectName("room_widget")
        self.setStyleSheet("#room_widget{background-color: #27ae60;}")

        self.horizontal_layout_3 = QtWidgets.QHBoxLayout(self)
        self.horizontal_layout_3.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontal_layout_3.setObjectName("horizontal_layout_3")

        self.widget_container_game = QtWidgets.QWidget(self)
        self.widget_container_game.setStyleSheet("#widget_container_game{background-color: #27ae60;}")
        self.widget_container_game.setObjectName("widget_container_game")

        self.vertical_layout_4 = QtWidgets.QVBoxLayout(self.widget_container_game)
        self.vertical_layout_4.setContentsMargins(0, 0, 0, 0)
        self.vertical_layout_4.setObjectName("vertical_layout_4")

        self.widget_players_list = QtWidgets.QWidget(self.widget_container_game)
        self.widget_players_list.setMaximumSize(QtCore.QSize(16777215, 180))
        self.widget_players_list.setStyleSheet("")
        self.widget_players_list.setObjectName("widget_players_list")

        self.horizontal_layout_2 = QtWidgets.QHBoxLayout(self.widget_players_list)
        self.horizontal_layout_2.setContentsMargins(5, 5, 5, 5)
        self.horizontal_layout_2.setObjectName("horizontal_layout_2")

        self.widget_player = QtWidgets.QWidget(self.widget_players_list)
        self.widget_player.setMaximumSize(QtCore.QSize(125, 200))
        self.widget_player.setStyleSheet("background-color: #2ecc71; border-radius: 15px;")
        self.widget_player.setObjectName("widget_player")

        self.vertical_layout_3 = QtWidgets.QVBoxLayout(self.widget_player)
        self.vertical_layout_3.setContentsMargins(0, 0, 0, 0)
        self.vertical_layout_3.setObjectName("vertical_layout_3")

        font = QtGui.QFont()
        font.setPointSize(14)

        self.label_username = QtWidgets.QLabel(self.widget_player)
        self.label_username.setText("lucascriistiano")
        self.label_username.setMaximumSize(QtCore.QSize(16777215, 40))
        self.label_username.setFont(font)
        self.label_username.setStyleSheet("color: white;")
        self.label_username.setAlignment(QtCore.Qt.AlignCenter)
        self.label_username.setWordWrap(True)
        self.label_username.setObjectName("label_username")
        self.vertical_layout_3.addWidget(self.label_username)

        font = QtGui.QFont()
        font.setPointSize(40)
        font.setBold(True)
        font.setWeight(75)

        self.label_sticks = QtWidgets.QLabel(self.widget_player)
        self.label_sticks.setText("|||")
        self.label_sticks.setFont(font)
        self.label_sticks.setStyleSheet("color: #f1c40f;")
        self.label_sticks.setAlignment(QtCore.Qt.AlignCenter)
        self.label_sticks.setObjectName("label_sticks")
        self.vertical_layout_3.addWidget(self.label_sticks)

        font = QtGui.QFont()
        font.setPointSize(16)

        self.label_last_plays = QtWidgets.QLabel(self.widget_player)
        self.label_last_plays.setText("2 - 0 - 1")
        self.label_last_plays.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_last_plays.setFont(font)
        self.label_last_plays.setStyleSheet("color: white;")
        self.label_last_plays.setAlignment(QtCore.Qt.AlignCenter)
        self.label_last_plays.setWordWrap(True)
        self.label_last_plays.setObjectName("label_last_plays")
        self.vertical_layout_3.addWidget(self.label_last_plays)

        font = QtGui.QFont()
        font.setPointSize(29)

        self.label_current_guess = QtWidgets.QLabel(self.widget_player)
        self.label_current_guess.setText("10")
        self.label_current_guess.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_current_guess.setFont(font)
        self.label_current_guess.setStyleSheet("color: white;")
        self.label_current_guess.setAlignment(QtCore.Qt.AlignCenter)
        self.label_current_guess.setWordWrap(True)
        self.label_current_guess.setObjectName("label_current_guess")
        self.vertical_layout_3.addWidget(self.label_current_guess)

        self.horizontal_layout_2.addWidget(self.widget_player)
        self.vertical_layout_4.addWidget(self.widget_players_list)

        self.widget_game = QtWidgets.QWidget(self.widget_container_game)
        self.widget_game.setStyleSheet("")
        self.widget_game.setObjectName("widget_game")

        self.widget_my_sticks = QtWidgets.QWidget(self.widget_game)
        self.widget_my_sticks.setGeometry(QtCore.QRect(10, 160, 180, 180))
        self.widget_my_sticks.setMaximumSize(QtCore.QSize(180, 180))
        self.widget_my_sticks.setStyleSheet("QLabel{color: #f1c40f;}, QLabel:hover{color:  #f39c12;}")
        self.widget_my_sticks.setObjectName("widget_my_sticks")

        self.horizontal_layout_my_sticks = QtWidgets.QHBoxLayout(self.widget_my_sticks)
        self.horizontal_layout_my_sticks.setContentsMargins(0, 0, 0, 0)
        self.horizontal_layout_my_sticks.setObjectName("horizontal_layout_my_sticks")

        # Add player sticks
        self.font_big_stick = QtGui.QFont()
        self.font_big_stick.setPointSize(150)
        self.font_big_stick.setBold(True)
        self.font_big_stick.setWeight(75)

        self.my_sticks = []
        for i in range(0, 3):
            label_my_stick = QtWidgets.QLabel(self.widget_my_sticks)
            label_my_stick.setText("|")
            label_my_stick.setFont(self.font_big_stick)
            label_my_stick.setStyleSheet(":hover {color:  #f39c12;}")
            label_my_stick.setAlignment(QtCore.Qt.AlignCenter)
            label_my_stick.setObjectName("label_stick")
            self.horizontal_layout_my_sticks.addWidget(label_my_stick)

            label_my_stick.mousePressEvent = self.add_stick
            self.my_sticks.append(label_my_stick)

        self.selected_sticks = []

        self.widget_play = QtWidgets.QWidget(self.widget_game)
        self.widget_play.setGeometry(QtCore.QRect(580, 230, 100, 100))
        self.widget_play.setMaximumSize(QtCore.QSize(200, 200))
        self.widget_play.setStyleSheet("QWidget{background-color: #3498db; border-radius: 50%;} "
                                       "QWidget:hover{background-color: #2e8ece; border-radius: 50%;}")
        self.widget_play.setObjectName("widget_play")

        self.horizontal_layout_10 = QtWidgets.QHBoxLayout(self.widget_play)
        self.horizontal_layout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontal_layout_10.setObjectName("horizontal_layout_10")

        font_label_go = QtGui.QFont()
        font_label_go.setPointSize(35)
        font_label_go.setBold(True)
        font_label_go.setWeight(75)

        self.label_button_go = QtWidgets.QLabel(self.widget_play)
        self.label_button_go.setText("Go!")
        self.label_button_go.setFont(font_label_go)
        self.label_button_go.setStyleSheet("color: white;")
        self.label_button_go.setAlignment(QtCore.Qt.AlignCenter)
        self.label_button_go.setObjectName("label_button_go")
        self.horizontal_layout_10.addWidget(self.label_button_go)

        self.widget_player_hand = QtWidgets.QWidget(self.widget_game)
        self.widget_player_hand.setGeometry(QtCore.QRect(230, 40, 300, 300))
        self.widget_player_hand.setMaximumSize(QtCore.QSize(300, 300))
        self.widget_player_hand.setStyleSheet("background-color: #2ecc71; border-radius: 15px;")
        self.widget_player_hand.setObjectName("widget_player_hand")

        self.horizontal_layout_11 = QtWidgets.QHBoxLayout(self.widget_player_hand)
        self.horizontal_layout_11.setContentsMargins(0, 0, 0, 0)
        self.horizontal_layout_11.setObjectName("horizontal_layout_11")

        font_chosen_hand = QtGui.QFont()
        font_chosen_hand.setPointSize(100)
        font_chosen_hand.setBold(True)
        font_chosen_hand.setWeight(75)

        parent_folder_path = dirname(dirname(abspath(__file__)))
        pixmap_hand = QtGui.QPixmap(join(parent_folder_path, "img", "hand_cursor_xxl.png"))
        # pixmap_hand = QtGui.QPixmap(join(parent_folder_path, "img", "hand_white.png"))

        self.label_hand = QtWidgets.QLabel(self.widget_player_hand)
        # self.label_hand.setText("H")
        self.label_hand.setPixmap(pixmap_hand)
        self.label_hand.setFont(font_chosen_hand)
        self.label_hand.setStyleSheet("color: white;")
        self.label_hand.setAlignment(QtCore.Qt.AlignCenter)
        self.label_hand.setObjectName("label_hand")
        self.horizontal_layout_11.addWidget(self.label_hand)

        self.widget_chosen_sticks = QtWidgets.QWidget(self.widget_game)
        self.widget_chosen_sticks.setGeometry(QtCore.QRect(350, 180, 110, 110))
        self.widget_chosen_sticks.setMaximumSize(QtCore.QSize(150, 150))
        self.widget_chosen_sticks.setStyleSheet("QLabel{color: #f1c40f;}, "
                                                "QLabel:hover{color:  #f39c12;}")  # to user test border: 1px solid red;
        self.widget_chosen_sticks.setObjectName("widget_chosen_sticks")

        self.horizontal_layout_chosen_sticks = QtWidgets.QHBoxLayout(self.widget_chosen_sticks)
        self.horizontal_layout_chosen_sticks.setContentsMargins(0, 0, 0, 0)
        self.horizontal_layout_chosen_sticks.setObjectName("horizontal_layout_chosen_sticks")

        self.widget_my_sticks.raise_()
        self.widget_play.raise_()
        self.widget_player_hand.raise_()
        self.widget_chosen_sticks.raise_()

        self.vertical_layout_4.addWidget(self.widget_game)
        self.horizontal_layout_3.addWidget(self.widget_container_game)

        self.widget_messenger = QtWidgets.QWidget(self)
        self.widget_messenger.setMaximumSize(QtCore.QSize(220, 16777215))
        self.widget_messenger.setStyleSheet("#widget_messenger{background-color: #2ecc71; border-radius: 10px;}")
        self.widget_messenger.setObjectName("widget_messenger")

        self.vertical_layout = QtWidgets.QVBoxLayout(self.widget_messenger)
        self.vertical_layout.setContentsMargins(0, 0, 0, 0)
        self.vertical_layout.setObjectName("vertical_layout")

        self.list_widget_messages = QtWidgets.QListWidget(self.widget_messenger)
        self.list_widget_messages.setFocusPolicy(QtCore.Qt.NoFocus)
        self.list_widget_messages.setStyleSheet("background-color: white;")
        self.list_widget_messages.setObjectName("list_widget_messages")
        self.vertical_layout.addWidget(self.list_widget_messages)

        self.plain_text_edit_message = QtWidgets.QPlainTextEdit(self.widget_messenger)
        self.plain_text_edit_message.setPlaceholderText("Type your message")
        self.plain_text_edit_message.setMaximumSize(QtCore.QSize(16777215, 80))
        self.plain_text_edit_message.setStyleSheet("background-color:white;")
        self.plain_text_edit_message.setObjectName("plain_text_edit_message")
        self.vertical_layout.addWidget(self.plain_text_edit_message)

        font_button_send_message = QtGui.QFont()
        font_button_send_message.setPointSize(15)

        self.push_button_send_message = QtWidgets.QPushButton(self.widget_messenger)
        self.push_button_send_message.setText("Send Message")
        self.push_button_send_message.setFont(font_button_send_message)
        self.push_button_send_message.setStyleSheet("")
        self.push_button_send_message.setObjectName("push_button_send_message")
        self.vertical_layout.addWidget(self.push_button_send_message)

        self.horizontal_layout_3.addWidget(self.widget_messenger)

        self.connect_buttons()

    def connect_buttons(self):
        self.label_button_go.mousePressEvent = self.go_button_action

    def go_button_action(self, event):
        print('Selected sticks: ' + str(len(self.selected_sticks)))

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
