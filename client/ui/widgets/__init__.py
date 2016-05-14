# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
import ui.dialogs as dialogs
from ui.widgets import room


class RegisterWidget(QtWidgets.QWidget):

    def __init__(self, main_window, counting_sticks):
        super(RegisterWidget, self).__init__(main_window)

        self.counting_sticks = counting_sticks

        self.main_window = main_window
        self.main_window.setWindowTitle("Register - Counting Sticks")
        self.main_window.resize(300, 400)
        self.main_window.setAutoFillBackground(False)

        self.setStyleSheet("QLabel{color: white;}")

        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(self.backgroundRole(), QtGui.QColor("#2e8ece"))
        self.setPalette(palette)

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


class LoginWidget(QtWidgets.QWidget):

    def __init__(self, main_window, counting_sticks):
        super(LoginWidget, self).__init__(main_window)

        self.counting_sticks = counting_sticks

        self.main_window = main_window
        self.main_window.setWindowTitle("Login - Counting Sticks")
        self.main_window.resize(300, 400)
        self.main_window.setAutoFillBackground(False)
        self.main_window.setStyleSheet("")

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
        room_list_widget = RoomListWidget(self.main_window, self.counting_sticks)
        self.main_window.central_widget.addWidget(room_list_widget)
        self.main_window.central_widget.setCurrentWidget(room_list_widget)


class RoomListWidget(QtWidgets.QWidget):

    def __init__(self, main_window, counting_sticks, update_time=1000):
        super(RoomListWidget, self).__init__(main_window)

        self.counting_sticks = counting_sticks

        self.main_window = main_window
        self.main_window.setWindowTitle("Room List - Counting Sticks")
        self.main_window.resize(640, 350)
        self.main_window.setAutoFillBackground(False)

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

        self.label_title = QtWidgets.QLabel(self)
        self.label_title.setText("Counting Sticks - Room List")
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

        # self.update_room_list()

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

        # self.main_window.setCentralWidget(self.main_window.central_widget)

        self.status_bar = QtWidgets.QStatusBar(self.main_window)
        self.status_bar.setObjectName("status_bar")
        self.main_window.setStatusBar(self.status_bar)

        self.connect_buttons()

        self.update_room_list()

        self.timer_room_list_update = QtCore.QTimer()
        self.timer_room_list_update.timeout.connect(self.update_room_list)
        self.timer_room_list_update.start(update_time)

    def connect_buttons(self):
        self.push_button_create_room.clicked.connect(self.show_new_room_dialog)
        self.push_button_logout.clicked.connect(self.logout)

    def show_new_room_dialog(self):
        new_room_dialog = dialogs.NewRoomDialog(self, self.counting_sticks)
        new_room_dialog.exec_()

    def logout(self):
        print('Will do logout')

    def update_room_list(self):
        room_id_list = self.counting_sticks.list_rooms_ids()

        for room_id in room_id_list:
            if room_id not in self.room_widget_dict:
                room_widget = RoomInfoWidget(self, self.main_window, self.counting_sticks, room_id)
                room_widget.setObjectName("room_widget_" + room_id)
                self.horizontal_layout.addWidget(room_widget)

                self.room_widget_dict[room_id] = room_widget

        # remove closed rooms
        # remove closed rooms
        # remove closed rooms
        # remove closed rooms
        # remove closed rooms
        # remove closed rooms
        # remove closed rooms
        # remove closed rooms
        # remove closed rooms
        # remove closed rooms
        # remove closed rooms
        # remove closed rooms
        # remove closed rooms
        # remove closed rooms
        # remove closed rooms
        # remove closed rooms
        # remove closed rooms
        # remove closed rooms
        # remove closed rooms
        # remove closed rooms
        # remove closed rooms
        # remove closed rooms
        # remove closed rooms
        # remove closed rooms


class RoomInfoWidget(QtWidgets.QWidget):

    def __init__(self, parent, main_window, counting_sticks, room_id, update_time=1000):
        super(RoomInfoWidget, self).__init__(parent)

        self.counting_sticks = counting_sticks
        self.room_id = room_id

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

        self.timer_info_update = QtCore.QTimer()
        self.timer_info_update.timeout.connect(self.update_room_info)
        self.timer_info_update.start(update_time)

    def connect_buttons(self):
        self.push_button_play.clicked.connect(self.play)
        self.push_button_watch.clicked.connect(self.watch)

    def play(self):
        print('# To implement: test if can enter') # test if can enter
        can_play = True  # change

        if can_play:
            print('# To implement: add in players list')  # test if can enter

            entered_on_room = True  # change
            if entered_on_room:
                room_widget = room.RoomWidget(self.main_window, self.counting_sticks, self.room_id)
                self.main_window.central_widget.addWidget(room_widget)
                self.main_window.central_widget.setCurrentWidget(room_widget)
            else:
                QtWidgets.QMessageBox(self, "It wasn't possible to join the room. Maybe it's full now. "
                                            "Try again later. :(")
        else:
            QtWidgets.QMessageBox(self, "Sorry. You can't join this room.")

    def watch(self):
        print('# To implement: watch')  # implement watch

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
