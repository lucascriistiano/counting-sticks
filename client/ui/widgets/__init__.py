# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
from os.path import dirname, join, abspath
from ui.widgets import room
import ui.dialogs as dialogs
import qtawesome
import json

class LoginWidget(QtWidgets.QWidget):

    def __init__(self, main_window, counting_sticks):
        super(LoginWidget, self).__init__(main_window)

        self.counting_sticks = counting_sticks

        self.main_window = main_window
        self.main_window.setWindowTitle("Login - Counting Sticks")
        self.main_window.resize(300, 400)
        self.main_window.setAutoFillBackground(False)
        self.main_window.setStyleSheet("")
        self.main_window.center_on_screen()

        self.setStyleSheet("QLabel{color: white;}")

        self.setFixedSize(300, 400)
        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(self.backgroundRole(), QtGui.QColor("#2e8ece"))
        self.setPalette(palette)

        self.vertical_layout = QtWidgets.QVBoxLayout(self)
        self.vertical_layout.setContentsMargins(11, 11, 11, 11)
        self.vertical_layout.setSpacing(6)
        self.vertical_layout.setObjectName("vertical_layout")

        parent_folder_path = dirname(dirname(abspath(__file__)))
        pixmap_logo = QtGui.QPixmap(join(parent_folder_path, "img", "logo.png")).scaledToHeight(130)

        self.label_logo = QtWidgets.QLabel(self)
        self.label_logo.setPixmap(pixmap_logo)
        self.label_logo.setAlignment(QtCore.Qt.AlignCenter)
        self.label_logo.setWordWrap(True)
        self.label_logo.setObjectName("label_logo")
        self.vertical_layout.addWidget(self.label_logo)

        self.label_username = QtWidgets.QLabel("Username", self)
        self.label_username.setObjectName("label_username")
        self.vertical_layout.addWidget(self.label_username)

        self.line_edit_username = QtWidgets.QLineEdit(self)
        self.line_edit_username.setInputMask("")
        self.line_edit_username.setText("")
        self.line_edit_username.setObjectName("line_edit_username")
        self.vertical_layout.addWidget(self.line_edit_username)

        self.label_password = QtWidgets.QLabel("Password", self)
        self.label_password.setObjectName("label_password")
        self.vertical_layout.addWidget(self.label_password)

        self.line_edit_password = QtWidgets.QLineEdit(self)
        self.line_edit_password.setInputMask("")
        self.line_edit_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.line_edit_password.setObjectName("line_edit_password")
        self.vertical_layout.addWidget(self.line_edit_password)

        fa_login_icon = qtawesome.icon('fa.sign-in')
        self.push_button_login = QtWidgets.QPushButton(fa_login_icon, "Login", self)
        self.push_button_login.setObjectName("push_button_login")
        self.push_button_login.setDefault(True)
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

        fa_register_icon = qtawesome.icon('fa.plus')
        self.push_button_register = QtWidgets.QPushButton(fa_register_icon, "Register", self)
        self.push_button_register.setObjectName("push_button_register")
        self.vertical_layout.addWidget(self.push_button_register)

        spacer_item_2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.vertical_layout.addItem(spacer_item_2)

        self.connect_buttons()

    def connect_buttons(self):
        self.line_edit_username.returnPressed.connect(self.login)
        self.line_edit_password.returnPressed.connect(self.login)
        self.push_button_login.clicked.connect(self.login)
        self.push_button_register.clicked.connect(self.show_register_widget)

    def login(self):
        username = self.line_edit_username.text()
        password = self.line_edit_password.text()

        valid_login = self.counting_sticks.login(username, password)
        if valid_login:
            self.show_room_list_widget(username)
        else:
            self.label_error_message.setText('Invalid username/password.')

    def show_register_widget(self):
        register_widget = RegisterWidget(self.main_window, self.counting_sticks)
        self.main_window.central_widget.addWidget(register_widget)
        self.main_window.central_widget.setCurrentWidget(register_widget)

    def show_room_list_widget(self, username):
        room_list_widget = RoomListWidget(self.main_window, self.counting_sticks, username)
        self.main_window.central_widget.addWidget(room_list_widget)
        self.main_window.central_widget.setCurrentWidget(room_list_widget)


class RegisterWidget(QtWidgets.QWidget):

    def __init__(self, main_window, counting_sticks):
        super(RegisterWidget, self).__init__(main_window)

        self.counting_sticks = counting_sticks

        self.main_window = main_window
        self.main_window.setWindowTitle("Register - Counting Sticks")
        self.main_window.resize(300, 400)
        self.main_window.setAutoFillBackground(False)
        self.main_window.center_on_screen()

        self.setStyleSheet("QLabel{color: white;}")

        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(self.backgroundRole(), QtGui.QColor("#2e8ece"))
        self.setPalette(palette)

        self.vertical_layout = QtWidgets.QVBoxLayout(self)
        self.vertical_layout.setContentsMargins(11, 11, 11, 11)
        self.vertical_layout.setSpacing(6)
        self.vertical_layout.setObjectName("vertical_layout")

        parent_folder_path = dirname(dirname(abspath(__file__)))
        pixmap_logo = QtGui.QPixmap(join(parent_folder_path, "img", "logo.png")).scaledToHeight(130)

        self.label_logo = QtWidgets.QLabel(self)
        self.label_logo.setPixmap(pixmap_logo)
        self.label_logo.setAlignment(QtCore.Qt.AlignCenter)
        self.label_logo.setWordWrap(False)
        self.label_logo.setObjectName("label_logo")
        self.vertical_layout.addWidget(self.label_logo)

        self.label_username = QtWidgets.QLabel("Username", self)
        self.label_username.setObjectName("label_username")
        self.vertical_layout.addWidget(self.label_username)

        self.line_edit_username = QtWidgets.QLineEdit(self)
        self.line_edit_username.setInputMask("")
        self.line_edit_username.setObjectName("line_edit_username")
        self.vertical_layout.addWidget(self.line_edit_username)

        self.label_email = QtWidgets.QLabel("Email", self)
        self.label_email.setObjectName("label_email")
        self.vertical_layout.addWidget(self.label_email)

        self.line_edit_email = QtWidgets.QLineEdit(self)
        self.line_edit_email.setInputMask("")
        self.line_edit_email.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.line_edit_email.setObjectName("line_edit_email")
        self.vertical_layout.addWidget(self.line_edit_email)

        self.label_password = QtWidgets.QLabel("Password", self)
        self.label_password.setObjectName("label_password")
        self.vertical_layout.addWidget(self.label_password)

        self.line_edit_password = QtWidgets.QLineEdit(self)
        self.line_edit_password.setInputMask("")
        self.line_edit_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.line_edit_password.setObjectName("line_edit_password")
        self.vertical_layout.addWidget(self.line_edit_password)

        self.label_confirm_password = QtWidgets.QLabel("Confirm Password", self)
        self.label_confirm_password.setObjectName("label_confirm_password")
        self.vertical_layout.addWidget(self.label_confirm_password)

        self.line_edit_confirm_password = QtWidgets.QLineEdit(self)
        self.line_edit_confirm_password.setInputMask("")
        self.line_edit_confirm_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.line_edit_confirm_password.setObjectName("line_edit_confirm_password")
        self.vertical_layout.addWidget(self.line_edit_confirm_password)

        fa_register_icon = qtawesome.icon('fa.plus')
        self.push_button_register = QtWidgets.QPushButton(fa_register_icon, "Register", self)
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

        fa_back_icon = qtawesome.icon('fa.long-arrow-left')
        self.push_button_back = QtWidgets.QPushButton(fa_back_icon, "Back", self)
        self.push_button_back.setObjectName("push_button_back")
        self.vertical_layout.addWidget(self.push_button_back)

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

        self.main_window.login_widget.line_edit_username.setText(username)
        self.main_window.login_widget.line_edit_password.setText(password)

    def close(self):
        self.main_window.central_widget.removeWidget(self)


class RoomListWidget(QtWidgets.QWidget):

    def __init__(self, main_window, counting_sticks, username):
        super(RoomListWidget, self).__init__(main_window)

        self.counting_sticks = counting_sticks
        self.username = username

        self.main_window = main_window
        self.main_window.setWindowTitle("Room List - Counting Sticks")
        self.main_window.resize(640, 350)
        # self.main_window.setAutoFillBackground(False)
        self.main_window.center_on_screen()

        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(self.backgroundRole(), QtGui.QColor("#27ae60"))
        self.setPalette(palette)

        self.vertical_layout = QtWidgets.QVBoxLayout(self)
        self.vertical_layout.setObjectName("vertical_layout")

        font = QtGui.QFont()
        font.setFamily("Al Nile")
        font.setPointSize(20)
        font.setWeight(75)

        self.label_title = QtWidgets.QLabel("Counting Sticks - Room List", self)
        self.label_title.setFont(font)
        self.label_title.setAlignment(QtCore.Qt.AlignCenter)
        self.label_title.setObjectName("label_title")

        self.vertical_layout.addWidget(self.label_title)

        self.scroll_area = QtWidgets.QScrollArea(self.main_window.central_widget)
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setObjectName("scroll_area")

        self.scroll_area_widget_contents = QtWidgets.QWidget()
        # self.scroll_area_widget_contents.setGeometry(QtCore.QRect(0, 0, 670, 280))
        self.scroll_area_widget_contents.setObjectName("scroll_area_widget_contents")

        self.horizontal_layout = QtWidgets.QHBoxLayout(self.scroll_area_widget_contents)
        self.horizontal_layout.setContentsMargins(0, 0, 0, 0)
        self.horizontal_layout.setObjectName("horizontal_layout")

        self.room_widget_dict = {}

        self.scroll_area.setWidget(self.scroll_area_widget_contents)
        self.vertical_layout.addWidget(self.scroll_area)

        fa_create_room_icon = qtawesome.icon('fa.plus')
        self.push_button_create_room = QtWidgets.QPushButton(fa_create_room_icon, "Create New Room", self)
        self.push_button_create_room.setObjectName("push_button_create_room")
        self.vertical_layout.addWidget(self.push_button_create_room)

        fa_logout_icon = qtawesome.icon('fa.sign-out')
        self.push_button_logout = QtWidgets.QPushButton(fa_logout_icon, "Logout", self)
        self.push_button_logout.setObjectName("push_button_logout")
        self.vertical_layout.addWidget(self.push_button_logout)

        self.status_bar = QtWidgets.QStatusBar(self.main_window)
        self.status_bar.setObjectName("status_bar")
        self.main_window.setStatusBar(self.status_bar)

        self.connect_buttons()

        self.main_window.reconnect_update_timer(self.update_room_list)
        self.main_window.start_update_timer()

    def connect_buttons(self):
        self.push_button_create_room.clicked.connect(self.show_new_room_dialog)
        self.push_button_logout.clicked.connect(self.logout)

    def show_new_room_dialog(self):
        new_room_dialog = dialogs.NewRoomDialog(self, self.counting_sticks, self.username)
        new_room_dialog.exec_()

    def logout(self):
        print('Will do logout')

    def update_room_list(self):
        rooms_info_list_raw_json = self.counting_sticks.list_rooms_info()
        rooms_info_list = json.loads(rooms_info_list_raw_json)

        # Add new rooms and update existing and new rooms
        for room_info in rooms_info_list:
            room_id = room_info['_id']['$oid']

            # Add a new room info widget
            if room_id not in self.room_widget_dict:
                self.add_new_info_widget(room_id)

            # Update widget room info
            room_info_widget = self.room_widget_dict[room_id]
            room_info_widget.update_room_info(room_info)

        # Remove closed rooms
        room_id_list = self.counting_sticks.list_rooms_ids()
        for room_id in list(self.room_widget_dict):
            if room_id not in room_id_list:
                self.remove_room_info_widget(room_id)

    def add_new_info_widget(self, room_id):
        room_widget = RoomInfoWidget(self, self.main_window, self.counting_sticks, room_id, self.username)
        room_widget.setObjectName("room_widget_" + room_id)
        self.horizontal_layout.addWidget(room_widget)
        self.room_widget_dict[room_id] = room_widget

    def remove_room_info_widget(self, room_id):
        room_info_widget = self.room_widget_dict.pop(room_id)
        self.horizontal_layout.removeWidget(room_info_widget)
        room_info_widget.deleteLater()


class RoomInfoWidget(QtWidgets.QWidget):

    def __init__(self, parent, main_window, counting_sticks, room_id, username):
        super(RoomInfoWidget, self).__init__(parent)

        self.counting_sticks = counting_sticks
        self.room_id = room_id
        self.username = username
        self.room_name = ''  # get on update event

        self.parent = parent
        self.main_window = main_window

        # self.setAutoFillBackground(True)

        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        size_policy.setHorizontalStretch(200)
        size_policy.setVerticalStretch(200)
        size_policy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(size_policy)

        self.setMinimumSize(QtCore.QSize(200, 250))
        self.setMaximumSize(QtCore.QSize(200, 250))
        self.setObjectName("room_widget")

        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(self.backgroundRole(), QtGui.QColor("#2ecc71"))
        self.setPalette(palette)

        self.vertical_layout_2 = QtWidgets.QVBoxLayout(self)
        self.vertical_layout_2.setContentsMargins(0, 0, 0, 0)
        self.vertical_layout_2.setObjectName("vertical_layout_2")

        spacer_item = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.vertical_layout_2.addItem(spacer_item)

        palette = QtGui.QPalette()
        palette.setColor(QtGui.QPalette.Foreground, QtCore.Qt.white)

        font = QtGui.QFont()
        font.setPointSize(20)

        self.label_room_name = QtWidgets.QLabel(self)
        self.label_room_name.setFont(font)
        self.label_room_name.setAlignment(QtCore.Qt.AlignCenter)
        self.label_room_name.setObjectName("label_room_name")
        self.label_room_name.setPalette(palette)
        self.vertical_layout_2.addWidget(self.label_room_name)

        font = QtGui.QFont()
        font.setPointSize(35)

        self.label_current_players = QtWidgets.QLabel(self)
        self.label_current_players.setFont(font)
        self.label_current_players.setAlignment(QtCore.Qt.AlignCenter)
        self.label_current_players.setObjectName("label_current_players")
        self.label_current_players.setPalette(palette)
        self.vertical_layout_2.addWidget(self.label_current_players)

        font = QtGui.QFont()
        font.setPointSize(15)

        self.label_game_status = QtWidgets.QLabel(self)
        self.label_game_status.setFont(font)
        self.label_game_status.setAlignment(QtCore.Qt.AlignCenter)
        self.label_game_status.setObjectName("label_game_status")
        self.label_game_status.setPalette(palette)
        self.vertical_layout_2.addWidget(self.label_game_status)

        spacer_item_1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.vertical_layout_2.addItem(spacer_item_1)

        fa_play_icon = qtawesome.icon('fa.gamepad')
        self.push_button_play = QtWidgets.QPushButton(fa_play_icon, "Play", self)
        self.push_button_play.setObjectName("push_button_play")
        self.vertical_layout_2.addWidget(self.push_button_play)

        fa_close_room_icon = qtawesome.icon('fa.times')
        self.push_button_close_room = QtWidgets.QPushButton(fa_close_room_icon, "Close", self)
        self.push_button_close_room.setObjectName("push_button_close_room")
        self.vertical_layout_2.addWidget(self.push_button_close_room)

        self.connect_buttons()

    def connect_buttons(self):
        self.push_button_play.clicked.connect(self.play)
        self.push_button_close_room.clicked.connect(self.close_room)

    def play(self):
        joined_room = self.counting_sticks.join_room(self.room_id, self.username)
        if joined_room:
            room_widget = room.RoomWidget(self.main_window, self.counting_sticks,
                                          self.room_id, self.room_name, self.username)
            self.main_window.central_widget.addWidget(room_widget)
            self.main_window.central_widget.setCurrentWidget(room_widget)
        else:
            QtWidgets.QMessageBox.information(self, "Operation Failed", "It wasn't possible to join the room. "
                                                                        "Maybe it's full now. Try again later. :(")

    def close_room(self):
        closed_room = self.counting_sticks.close_room(self.room_id, self.username)
        if not closed_room:
            QtWidgets.QMessageBox.information(self, "Operation Failed", "It wasn't possible to close the room. "
                                                                        "Check if it's empty first.")

    def update_room_info(self, room_info):
        if room_info is not None:
            self.room_name = room_info['name']
            self.label_room_name.setText(self.room_name)

            if 'current_players' in room_info:
                current_players_number = len(room_info['current_players'])
            else:
                current_players_number = 0

            min_players = room_info['min_players']
            max_players = room_info['max_players']
            self.label_current_players.setText(str(min_players) + '/' + str(current_players_number) + '/' +
                                               str(max_players))

            playing = room_info['playing']
            self.label_game_status.setText('Playing' if playing else 'Waiting')

            accepting_players = not playing and current_players_number < max_players
            self.push_button_play.setEnabled(accepting_players)

            is_room_creator = room_info['created_by'] == self.username
            self.push_button_close_room.setEnabled(is_room_creator)
        else:
            self.push_button_play.setEnabled(False)
