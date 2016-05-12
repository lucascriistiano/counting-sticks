# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, counting_sticks, parent=None):
        super(MainWindow, self).__init__(parent)

        self.counting_sticks = counting_sticks

        self.central_widget = QtWidgets.QStackedWidget()
        self.setCentralWidget(self.central_widget)

        self.login_widget = LoginWidget(self, self.counting_sticks)
        self.login_widget.pushButton_register.clicked.connect(self.register)
        self.central_widget.addWidget(self.login_widget)

    def register(self):
        register_widget = RegisterWidget(self, self.counting_sticks)
        self.central_widget.addWidget(register_widget)
        self.central_widget.setCurrentWidget(register_widget)


class LoginWidget(QtWidgets.QWidget):

    def __init__(self, parent, counting_sticks):
        super(LoginWidget, self).__init__(parent)

        self.counting_sticks = counting_sticks

        self.parent = parent
        self.parent.setObjectName("LoginWindow")
        self.parent.resize(300, 400)
        self.parent.setAutoFillBackground(False)
        self.parent.setStyleSheet("")

        self.central_widget = parent.central_widget
        self.central_widget.setObjectName("centralWidget")

        self.vertical_layout = QtWidgets.QVBoxLayout(self)
        self.vertical_layout.setContentsMargins(11, 11, 11, 11)
        self.vertical_layout.setSpacing(6)
        self.vertical_layout.setObjectName("verticalLayout")

        font = QtGui.QFont()
        font.setFamily("Al Nile")
        font.setPointSize(40)
        font.setBold(True)
        font.setWeight(75)

        self.label_logo = QtWidgets.QLabel(self)
        self.label_logo.setFont(font)
        self.label_logo.setAlignment(QtCore.Qt.AlignCenter)
        self.label_logo.setWordWrap(True)
        self.label_logo.setObjectName("label_logo")
        self.vertical_layout.addWidget(self.label_logo)

        self.label_username = QtWidgets.QLabel(self)
        self.label_username.setObjectName("label_username")
        self.vertical_layout.addWidget(self.label_username)

        self.lineEdit_username = QtWidgets.QLineEdit(self)
        self.lineEdit_username.setInputMask("")
        self.lineEdit_username.setText("")
        self.lineEdit_username.setObjectName("lineEdit_username")
        self.vertical_layout.addWidget(self.lineEdit_username)

        self.label_password = QtWidgets.QLabel(self)
        self.label_password.setObjectName("label_password")
        self.vertical_layout.addWidget(self.label_password)

        self.lineEdit_password = QtWidgets.QLineEdit(self)
        self.lineEdit_password.setInputMask("")
        self.lineEdit_password.setText("")
        self.lineEdit_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.vertical_layout.addWidget(self.lineEdit_password)

        self.pushButton_login = QtWidgets.QPushButton(self)
        self.pushButton_login.setObjectName("pushButton_login")
        self.vertical_layout.addWidget(self.pushButton_login)

        spacer_item = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.vertical_layout.addItem(spacer_item)

        self.pushButton_register = QtWidgets.QPushButton(self)
        self.pushButton_register.setObjectName("pushButton_register")
        self.vertical_layout.addWidget(self.pushButton_register)

        spacer_item_2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.vertical_layout.addItem(spacer_item_2)

        # parent.setCentralWidget(self.centralWidget)
        # self.menuBar = QtWidgets.QMenuBar(LoginWindow)
        # self.menuBar.setGeometry(QtCore.QRect(0, 0, 300, 22))
        # self.menuBar.setObjectName("menuBar")
        # LoginWindow.setMenuBar(self.menuBar)
        # self.statusBar = QtWidgets.QStatusBar(LoginWindow)
        # self.statusBar.setObjectName("statusBar")
        # LoginWindow.setStatusBar(self.statusBar)

        self.retranslate_ui(parent)
        # QtCore.QMetaObject.connectSlotsByName(LoginWindow)

        self.connect_buttons()

    def retranslate_ui(self, LoginWindow):
        _translate = QtCore.QCoreApplication.translate
        LoginWindow.setWindowTitle(_translate("LoginWindow", "Login - Counting Sticks"))
        self.label_logo.setText(_translate("LoginWindow", "Counting Sticks"))
        self.label_username.setText(_translate("LoginWindow", "Username"))
        self.label_password.setText(_translate("LoginWindow", "Password"))
        self.pushButton_login.setText(_translate("LoginWindow", "Login"))
        self.pushButton_register.setText(_translate("LoginWindow", "Register"))

    def login(self):
        username = self.lineEdit_username.text()
        password = self.lineEdit_password.text()

        logged = self.counting_sticks.login(username, password)

        if logged:
            print('Logged')
        else:
            print('Not logged')

    def connect_buttons(self):
        self.pushButton_login.clicked.connect(self.login)


class RegisterWidget(QtWidgets.QWidget):

    def __init__(self, parent, counting_sticks):
        super(RegisterWidget, self).__init__(parent)

        self.counting_sticks = counting_sticks

        self.parent = parent
        self.parent.setObjectName("RegisterWindow")
        self.parent.resize(300, 400)
        self.parent.setAutoFillBackground(False)
        self.parent.setStyleSheet("")

        self.central_widget = parent.central_widget
        self.central_widget.setObjectName("centralWidget")

        self.verticalLayout = QtWidgets.QVBoxLayout(self)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")

        font = QtGui.QFont()
        font.setFamily("Al Nile")
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)

        self.label_logo = QtWidgets.QLabel(self)
        self.label_logo.setFont(font)
        self.label_logo.setAlignment(QtCore.Qt.AlignCenter)
        self.label_logo.setWordWrap(False)
        self.label_logo.setObjectName("label_logo")
        self.verticalLayout.addWidget(self.label_logo)

        self.label_username = QtWidgets.QLabel(self)
        self.label_username.setObjectName("label_username")
        self.verticalLayout.addWidget(self.label_username)

        self.lineEdit_username = QtWidgets.QLineEdit(self)
        self.lineEdit_username.setInputMask("")
        self.lineEdit_username.setText("")
        self.lineEdit_username.setObjectName("lineEdit_username")
        self.verticalLayout.addWidget(self.lineEdit_username)

        self.label_email = QtWidgets.QLabel(self)
        self.label_email.setObjectName("label_email")
        self.verticalLayout.addWidget(self.label_email)

        self.lineEdit_email = QtWidgets.QLineEdit(self)
        self.lineEdit_email.setInputMask("")
        self.lineEdit_email.setText("")
        self.lineEdit_email.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_email.setObjectName("lineEdit_email")
        self.verticalLayout.addWidget(self.lineEdit_email)

        self.label_password = QtWidgets.QLabel(self)
        self.label_password.setObjectName("label_password")
        self.verticalLayout.addWidget(self.label_password)

        self.lineEdit_password = QtWidgets.QLineEdit(self)
        self.lineEdit_password.setInputMask("")
        self.lineEdit_password.setText("")
        self.lineEdit_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.verticalLayout.addWidget(self.lineEdit_password)

        self.label_confirm_password = QtWidgets.QLabel(self)
        self.label_confirm_password.setObjectName("label_confirm_password")
        self.verticalLayout.addWidget(self.label_confirm_password)

        self.lineEdit_confirm_password = QtWidgets.QLineEdit(self)
        self.lineEdit_confirm_password.setInputMask("")
        self.lineEdit_confirm_password.setText("")
        self.lineEdit_confirm_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_confirm_password.setObjectName("lineEdit_confirm_password")
        self.verticalLayout.addWidget(self.lineEdit_confirm_password)

        self.pushButton_register = QtWidgets.QPushButton(self)
        self.pushButton_register.setObjectName("pushButton_register")
        self.verticalLayout.addWidget(self.pushButton_register)

        spacer_item = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Ignored)
        self.verticalLayout.addItem(spacer_item)

        self.pushButton_back = QtWidgets.QPushButton(self)
        self.pushButton_back.setObjectName("pushButton_back")
        self.verticalLayout.addWidget(self.pushButton_back)

        # parent.setCentralWidget(self.centralWidget)
        # self.menuBar = QtWidgets.QMenuBar(RegisterWindow)
        # self.menuBar.setGeometry(QtCore.QRect(0, 0, 300, 22))
        # self.menuBar.setObjectName("menuBar")
        # RegisterWindow.setMenuBar(self.menuBar)

        # self.statusBar = QtWidgets.QStatusBar(RegisterWindow)
        # self.statusBar.setObjectName("statusBar")
        # RegisterWindow.setStatusBar(self.statusBar)

        self.retranslate_ui(parent)
        # QtCore.QMetaObject.connectSlotsByName(RegisterWindow)

        self.connect_buttons()

    def retranslate_ui(self, RegisterWindow):
        _translate = QtCore.QCoreApplication.translate
        RegisterWindow.setWindowTitle(_translate("RegisterWindow", "Register - Counting Sticks"))
        self.label_logo.setText(_translate("RegisterWindow", "Counting Sticks"))
        self.label_username.setText(_translate("RegisterWindow", "Username"))
        self.label_email.setText(_translate("RegisterWindow", "Email"))
        self.label_password.setText(_translate("RegisterWindow", "Password"))
        self.label_confirm_password.setText(_translate("RegisterWindow", "Confirm Password"))
        self.pushButton_register.setText(_translate("RegisterWindow", "Register"))
        self.pushButton_back.setText(_translate("RegisterWindow", "Back"))

    def register(self):
        username = self.lineEdit_username.text()
        email = self.lineEdit_email.text()
        password = self.lineEdit_password.text()
        password_confirm = self.lineEdit_confirm_password.text()

        self.counting_sticks.register(username, email, password)

        self.fill_user_login()
        self.close()

    def fill_user_login(self):
        username = self.lineEdit_username.text()
        password = self.lineEdit_password.text()

        self.parent.login_widget.lineEdit_username.setText(username)
        self.parent.login_widget.lineEdit_password.setText(password)

    def close(self):
        self.central_widget.removeWidget(self)

    def connect_buttons(self):
        self.pushButton_register.clicked.connect(self.register)
        self.pushButton_back.clicked.connect(self.close)

#
# if __name__ == '__main__':
#
#
#     # app = QtWidgets.QApplication(sys.argv)
#
#     # ui = LoginWindow()
#     # ui.setupUi(LoginWindow)
#     # LoginWindow.show()
#     # sys.exit(app.exec_())
