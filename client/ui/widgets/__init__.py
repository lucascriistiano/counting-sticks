# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets


class RegisterWidget(QtWidgets.QWidget):

    def __init__(self, parent, counting_sticks):
        super(RegisterWidget, self).__init__(parent)

        self.counting_sticks = counting_sticks

        self.parent = parent
        self.parent.setObjectName("RegisterWindow")
        self.parent.setWindowTitle("Register - Counting Sticks")
        self.parent.resize(300, 400)
        self.parent.setAutoFillBackground(False)
        self.parent.setStyleSheet("")

        self.central_widget = parent.central_widget
        self.central_widget.setObjectName("centralWidget")

        self.vertical_layout = QtWidgets.QVBoxLayout(self)
        self.vertical_layout.setContentsMargins(11, 11, 11, 11)
        self.vertical_layout.setSpacing(6)
        self.vertical_layout.setObjectName("vertical_layout")

        font = QtGui.QFont()
        font.setFamily("Al Nile")
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)

        self.label_logo = QtWidgets.QLabel(self)
        self.label_logo.setText("Counting Sticks")
        self.label_logo.setFont(font)
        self.label_logo.setAlignment(QtCore.Qt.AlignCenter)
        self.label_logo.setWordWrap(False)
        self.label_logo.setObjectName("label_logo")
        self.vertical_layout.addWidget(self.label_logo)

        self.label_username = QtWidgets.QLabel(self)
        self.label_username.setText("Username")
        self.label_username.setObjectName("label_username")
        self.vertical_layout.addWidget(self.label_username)

        self.line_edit_username = QtWidgets.QLineEdit(self)
        self.line_edit_username.setInputMask("")
        self.line_edit_username.setText("")
        self.line_edit_username.setObjectName("line_edit_username")
        self.vertical_layout.addWidget(self.line_edit_username)

        self.label_email = QtWidgets.QLabel(self)
        self.label_email.setText("Email")
        self.label_email.setObjectName("label_email")
        self.vertical_layout.addWidget(self.label_email)

        self.line_edit_email = QtWidgets.QLineEdit(self)
        self.line_edit_email.setInputMask("")
        self.line_edit_email.setText("")
        self.line_edit_email.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.line_edit_email.setObjectName("line_edit_email")
        self.vertical_layout.addWidget(self.line_edit_email)

        self.label_password = QtWidgets.QLabel(self)
        self.label_password.setText("Password")
        self.label_password.setObjectName("label_password")
        self.vertical_layout.addWidget(self.label_password)

        self.line_edit_password = QtWidgets.QLineEdit(self)
        self.line_edit_password.setInputMask("")
        self.line_edit_password.setText("")
        self.line_edit_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.line_edit_password.setObjectName("line_edit_password")
        self.vertical_layout.addWidget(self.line_edit_password)

        self.label_confirm_password = QtWidgets.QLabel(self)
        self.label_confirm_password.setText("Confirm Password")
        self.label_confirm_password.setObjectName("label_confirm_password")
        self.vertical_layout.addWidget(self.label_confirm_password)

        self.line_edit_confirm_password = QtWidgets.QLineEdit(self)
        self.line_edit_confirm_password.setInputMask("")
        self.line_edit_confirm_password.setText("")
        self.line_edit_confirm_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.line_edit_confirm_password.setObjectName("line_edit_confirm_password")
        self.vertical_layout.addWidget(self.line_edit_confirm_password)

        self.push_button_register = QtWidgets.QPushButton(self)
        self.push_button_register.setText("Register")
        self.push_button_register.setObjectName("push_button_register")
        self.vertical_layout.addWidget(self.push_button_register)

        palette = QtGui.QPalette()
        palette.setColor(QtGui.QPalette.Foreground, QtCore.Qt.red)

        self.label_error_message = QtWidgets.QLabel(self)
        self.label_error_message.setObjectName("label_error_message")
        self.label_error_message.setPalette(palette)
        self.label_error_message.setAlignment(QtCore.Qt.AlignCenter)
        self.vertical_layout.addWidget(self.label_error_message)

        spacer_item = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Ignored)
        self.vertical_layout.addItem(spacer_item)

        self.push_button_back = QtWidgets.QPushButton(self)
        self.push_button_back.setText("Back")
        self.push_button_back.setObjectName("push_button_back")
        self.vertical_layout.addWidget(self.push_button_back)

        # self.parent.setCentralWidget(self.central_widget)

        # self.menu_bar = QtWidgets.QMenuBar(self.parent)
        # self.menu_bar.setGeometry(QtCore.QRect(0, 0, 300, 22))
        # self.menu_bar.setObjectName("menu_bar")
        # self.parent.setMenuBar(self.menu_bar)

        # self.status_bar = QtWidgets.QStatusBar(self.parent)
        # self.status_bar.setObjectName("status_bar")
        # self.parent.setStatusBar(self.status_bar)

        self.connect_buttons()

    def connect_buttons(self):
        self.push_button_register.clicked.connect(self.register)
        self.push_button_back.clicked.connect(self.close)

    def register(self):
        username = self.line_edit_username.text()
        email = self.line_edit_email.text()
        password = self.line_edit_password.text()
        password_confirm = self.line_edit_confirm_password.text()

        if password == password_confirm:
            self.counting_sticks.register(username, email, password)

            self.fill_user_login()
            self.close()
        else:
            self.label_error_message.setText('Entered passwords must be equal.')

    def fill_user_login(self):
        username = self.line_edit_username.text()
        password = self.line_edit_password.text()

        self.parent.login_widget.line_edit_username.setText(username)
        self.parent.login_widget.line_edit_password.setText(password)

    def close(self):
        self.central_widget.removeWidget(self)


class LoginWidget(QtWidgets.QWidget):

    def __init__(self, parent, counting_sticks):
        super(LoginWidget, self).__init__(parent)

        self.counting_sticks = counting_sticks

        self.parent = parent
        self.parent.setWindowTitle("Login - Counting Sticks")
        self.parent.setObjectName("LoginWindow")
        self.parent.resize(300, 400)
        self.parent.setAutoFillBackground(False)
        self.parent.setStyleSheet("")

        self.setFixedSize(300, 400)

        self.central_widget = parent.central_widget
        self.central_widget.setObjectName("centralWidget")

        self.vertical_layout = QtWidgets.QVBoxLayout(self)
        self.vertical_layout.setContentsMargins(11, 11, 11, 11)
        self.vertical_layout.setSpacing(6)
        self.vertical_layout.setObjectName("vertical_layout")

        font = QtGui.QFont()
        font.setFamily("Al Nile")
        font.setPointSize(40)
        font.setBold(True)
        font.setWeight(75)

        self.label_logo = QtWidgets.QLabel(self)
        self.label_logo.setText("Counting Sticks")
        self.label_logo.setFont(font)
        self.label_logo.setAlignment(QtCore.Qt.AlignCenter)
        self.label_logo.setWordWrap(True)
        self.label_logo.setObjectName("label_logo")
        self.vertical_layout.addWidget(self.label_logo)

        self.label_username = QtWidgets.QLabel(self)
        self.label_username.setText("Username")
        self.label_username.setObjectName("label_username")
        self.vertical_layout.addWidget(self.label_username)

        self.line_edit_username = QtWidgets.QLineEdit(self)
        self.line_edit_username.setInputMask("")
        self.line_edit_username.setText("")
        self.line_edit_username.setObjectName("line_edit_username")
        self.vertical_layout.addWidget(self.line_edit_username)

        self.label_password = QtWidgets.QLabel(self)
        self.label_password.setText("Password")
        self.label_password.setObjectName("label_password")
        self.vertical_layout.addWidget(self.label_password)

        self.line_edit_password = QtWidgets.QLineEdit(self)
        self.line_edit_password.setInputMask("")
        self.line_edit_password.setText("")
        self.line_edit_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.line_edit_password.setObjectName("line_edit_password")
        self.vertical_layout.addWidget(self.line_edit_password)

        self.push_button_login = QtWidgets.QPushButton(self)
        self.push_button_login.setText("Login")
        self.push_button_login.setObjectName("push_button_login")
        self.vertical_layout.addWidget(self.push_button_login)

        palette = QtGui.QPalette()
        palette.setColor(QtGui.QPalette.Foreground, QtCore.Qt.red)

        self.label_error_message = QtWidgets.QLabel(self)
        self.label_error_message.setObjectName("label_error_message")
        self.label_error_message.setPalette(palette)
        self.label_error_message.setAlignment(QtCore.Qt.AlignCenter)
        self.vertical_layout.addWidget(self.label_error_message)

        spacer_item = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.vertical_layout.addItem(spacer_item)

        self.push_button_register = QtWidgets.QPushButton(self)
        self.push_button_register.setText("Register")
        self.push_button_register.setObjectName("push_button_register")
        self.vertical_layout.addWidget(self.push_button_register)

        spacer_item_2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.vertical_layout.addItem(spacer_item_2)

        # self.parent.setCentralWidget(self.central_widget)

        # self.menu_bar = QtWidgets.QMenuBar(self.parent)
        # self.menu_bar.setGeometry(QtCore.QRect(0, 0, 300, 22))
        # self.menu_bar.setObjectName("menu_bar")
        # self.parent.setMenuBar(self.menu_bar)

        # self.status_bar = QtWidgets.QStatusBar(self.parent)
        # self.status_bar.setObjectName("status_bar")
        # self.parent.setStatusBar(self.status_bar)

        self.connect_buttons()

    def connect_buttons(self):
        self.push_button_login.clicked.connect(self.login)

    def login(self):
        username = self.line_edit_username.text()
        password = self.line_edit_password.text()

        valid_login = self.counting_sticks.login(username, password)
        if valid_login:
            self.show_room_list_widget()
        else:
            self.label_error_message.setText('Invalid username/password.')

    def show_room_list_widget(self):
        room_list_widget = RoomListWidget(self.parent, self.counting_sticks)
        self.central_widget.addWidget(room_list_widget)
        self.central_widget.setCurrentWidget(room_list_widget)


class RoomListWidget(QtWidgets.QWidget):

    def __init__(self, parent, counting_sticks):
        super(RoomListWidget, self).__init__(parent)

        self.counting_sticks = counting_sticks

        self.parent = parent
        self.parent.setWindowTitle("Room List - Counting Sticks")
        self.parent.setObjectName("RoomListWindow")
        self.parent.resize(700, 350)
        self.parent.setAutoFillBackground(False)
        self.parent.setStyleSheet("QWidget#room_widget {border: 1px solid #C0C0C0; background-color: #FFFF99;}")

        self.central_widget = parent.central_widget
        self.central_widget.setObjectName("centralWidget")

        self.vertical_layout = QtWidgets.QVBoxLayout(self)
        self.vertical_layout.setObjectName("vertical_layout")

        self.scroll_area = QtWidgets.QScrollArea(self.central_widget)
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setObjectName("scroll_area")

        self.scroll_area_widget_contents = QtWidgets.QWidget()
        self.scroll_area_widget_contents.setGeometry(QtCore.QRect(0, 0, 674, 281))
        self.scroll_area_widget_contents.setObjectName("scroll_area_widget_contents")

        self.horizontal_layout = QtWidgets.QHBoxLayout(self.scroll_area_widget_contents)
        self.horizontal_layout.setContentsMargins(0, 0, 0, 0)
        self.horizontal_layout.setObjectName("horizontal_layout")

        self.room_widget_dict = {}
        room_id_list = self.counting_sticks.list_rooms_ids()
        for room_id in room_id_list:
            if room_id not in self.room_widget_dict:
                room_widget = RoomInfoWidget(self, self.counting_sticks, room_id)
                room_widget.setObjectName("room_widget_" + room_id)
                self.horizontal_layout.addWidget(room_widget)

                self.room_widget_dict[room_id] = room_widget

        self.scroll_area.setWidget(self.scroll_area_widget_contents)
        self.vertical_layout.addWidget(self.scroll_area)

        self.push_button_create_room = QtWidgets.QPushButton(self)
        self.push_button_create_room.setText("Create New Room")
        self.push_button_create_room.setObjectName("push_button_create_room")
        self.vertical_layout.addWidget(self.push_button_create_room)

        self.push_button_logout = QtWidgets.QPushButton(self)
        self.push_button_logout.setText("Logout")
        self.push_button_logout.setObjectName("push_button_logout")
        self.vertical_layout.addWidget(self.push_button_logout)

        # self.parent.setCentralWidget(self.central_widget)

        self.status_bar = QtWidgets.QStatusBar(self.parent)
        self.status_bar.setObjectName("status_bar")
        self.parent.setStatusBar(self.status_bar)

        self.connect_buttons()

    def connect_buttons(self):
        self.push_button_create_room.clicked.connect(self.show_new_room_dialog)
        self.push_button_logout.clicked.connect(self.logout)

    def show_new_room_dialog(self):
        new_room_dialog = NewRoomDialog(self, self.counting_sticks)
        new_room_dialog.exec_()

    def logout(self):
        print('Will do logout')


class RoomInfoWidget(QtWidgets.QWidget):

    def __init__(self, parent, counting_sticks, room_id):
        super(RoomInfoWidget, self).__init__(parent)

        self.counting_sticks = counting_sticks
        self.room_id = room_id

        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        size_policy.setHorizontalStretch(200)
        size_policy.setVerticalStretch(200)
        size_policy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())

        self.setSizePolicy(size_policy)
        self.setMinimumSize(QtCore.QSize(200, 250))
        self.setMaximumSize(QtCore.QSize(200, 250))
        self.setStyleSheet("")
        self.setObjectName("room_widget")

        self.vertical_layout_2 = QtWidgets.QVBoxLayout(self)
        self.vertical_layout_2.setContentsMargins(0, 0, 0, 0)
        self.vertical_layout_2.setObjectName("vertical_layout_2")

        spacer_item = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.vertical_layout_2.addItem(spacer_item)

        font = QtGui.QFont()
        font.setPointSize(20)

        self.label_room_name = QtWidgets.QLabel(self)
        self.label_room_name.setFont(font)
        self.label_room_name.setAlignment(QtCore.Qt.AlignCenter)
        self.label_room_name.setObjectName("label_room_name")
        self.vertical_layout_2.addWidget(self.label_room_name)

        font = QtGui.QFont()
        font.setPointSize(35)

        self.label_current_players = QtWidgets.QLabel(self)
        self.label_current_players.setFont(font)
        self.label_current_players.setAlignment(QtCore.Qt.AlignCenter)
        self.label_current_players.setObjectName("label_current_players")
        self.vertical_layout_2.addWidget(self.label_current_players)

        font = QtGui.QFont()
        font.setPointSize(15)

        self.label_game_status = QtWidgets.QLabel(self)
        self.label_game_status.setFont(font)
        self.label_game_status.setAlignment(QtCore.Qt.AlignCenter)
        self.label_game_status.setObjectName("label_game_status")
        self.vertical_layout_2.addWidget(self.label_game_status)

        spacer_item_1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.vertical_layout_2.addItem(spacer_item_1)

        self.push_button_play = QtWidgets.QPushButton(self)
        self.push_button_play.setText("Play")
        self.push_button_play.setObjectName("push_button_play")
        self.vertical_layout_2.addWidget(self.push_button_play)

        self.push_button_watch = QtWidgets.QPushButton(self)
        self.push_button_watch.setText("Watch")
        self.push_button_watch.setObjectName("push_button_watch")
        self.vertical_layout_2.addWidget(self.push_button_watch)

        self.connect_buttons()

        self.update_room_info()

    def connect_buttons(self):
        self.push_button_play.clicked.connect(self.play)
        self.push_button_watch.clicked.connect(self.watch)

    def play(self):
        print('Play')

    def watch(self):
        print('Watch')

    def update_room_info(self):
        room_state_info = self.counting_sticks.room_state(self.room_id)
        self.label_room_name.setText(room_state_info['name'])

        current_players = room_state_info['current_players']

        min_players = room_state_info['min_players']
        current_players_number = len(current_players)
        max_players = room_state_info['max_players']
        self.label_current_players.setText(str(min_players) + '/' + str(current_players_number) \
                                           + '/' + str(max_players))

        playing = room_state_info['playing']
        self.label_game_status.setText('Playing' if playing else 'Waiting')

        accepting_players = not playing and current_players_number < max_players
        self.push_button_play.setEnabled(accepting_players)


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
