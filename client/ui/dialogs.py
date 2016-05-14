# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets


class NewRoomDialog(QtWidgets.QDialog):

    def __init__(self, parent, counting_sticks):
        super(NewRoomDialog, self).__init__(parent)

        self.counting_sticks = counting_sticks

        self.setWindowTitle("New Room - Counting Sticks")
        self.setObjectName("NewRoomWindow")
        self.resize(300, 300)
        self.setAutoFillBackground(False)
        self.setStyleSheet("")
        self.resize(300, 300)

        font = QtGui.QFont()
        font.setFamily("Baskerville")
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)

        self.label_logo = QtWidgets.QLabel(self)
        self.label_logo.setText("New Room")
        self.label_logo.setGeometry(QtCore.QRect(40, 20, 221, 31))
        self.label_logo.setFont(font)
        self.label_logo.setAlignment(QtCore.Qt.AlignCenter)
        self.label_logo.setWordWrap(False)
        self.label_logo.setObjectName("label_logo")

        self.label_room_name = QtWidgets.QLabel(self)
        self.label_room_name.setText("Room Name")
        self.label_room_name.setGeometry(QtCore.QRect(44, 70, 81, 20))
        self.label_room_name.setObjectName("label_room_name")

        self.line_edit_room_name = QtWidgets.QLineEdit(self)
        self.line_edit_room_name.setGeometry(QtCore.QRect(40, 93, 220, 20))
        self.line_edit_room_name.setInputMask("")
        self.line_edit_room_name.setText("")
        self.line_edit_room_name.setObjectName("line_edit_room_name")

        self.label_min_players = QtWidgets.QLabel(self)
        self.label_min_players.setText("Min Players")
        self.label_min_players.setGeometry(QtCore.QRect(46, 122, 81, 20))
        self.label_min_players.setObjectName("label_min_players")

        self.spin_box_min_players = QtWidgets.QSpinBox(self)
        self.spin_box_min_players.setGeometry(QtCore.QRect(41, 144, 91, 24))
        self.spin_box_min_players.setMinimum(4)
        self.spin_box_min_players.setMaximum(6)
        self.spin_box_min_players.setObjectName("spin_box_min_players")

        self.label_max_players = QtWidgets.QLabel(self)
        self.label_max_players.setText("Max Players")
        self.label_max_players.setGeometry(QtCore.QRect(167, 123, 81, 20))
        self.label_max_players.setObjectName("label_max_players")

        self.spin_box_max_players = QtWidgets.QSpinBox(self)
        self.spin_box_max_players.setGeometry(QtCore.QRect(162, 144, 91, 24))
        self.spin_box_max_players.setMinimum(4)
        self.spin_box_max_players.setMaximum(6)
        self.spin_box_max_players.setObjectName("spin_box_max_players")

        self.push_button_create_room = QtWidgets.QPushButton(self)
        self.push_button_create_room.setText("Create Room")
        self.push_button_create_room.setGeometry(QtCore.QRect(40, 191, 220, 40))
        self.push_button_create_room.setObjectName("push_button_create_room")

        self.connect_buttons()

    def connect_buttons(self):
        self.push_button_create_room.clicked.connect(self.create_room)

    def create_room(self):
        if not self.has_empty_fields():
            room_name = self.line_edit_room_name.text()
            min_players = self.spin_box_min_players.value()
            max_players = self.spin_box_max_players.value()

            self.counting_sticks.create_room(room_name, min_players, max_players)
            self.close()
        else:
            print("All fields must be filled")  # Set in a label

    def has_empty_fields(self):
        return self.line_edit_room_name.text() == "" or self.spin_box_min_players.text() == "" \
               or self.spin_box_max_players.text() == ""
