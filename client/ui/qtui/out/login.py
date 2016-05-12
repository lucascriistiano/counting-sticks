# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_LoginWindow(object):
    def setupUi(self, LoginWindow):
        LoginWindow.setObjectName("LoginWindow")
        LoginWindow.resize(300, 400)
        LoginWindow.setAutoFillBackground(False)
        LoginWindow.setStyleSheet("")
        self.centralWidget = QtWidgets.QWidget(LoginWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralWidget)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_logo = QtWidgets.QLabel(self.centralWidget)
        font = QtGui.QFont()
        font.setFamily("Al Nile")
        font.setPointSize(40)
        font.setBold(True)
        font.setWeight(75)
        self.label_logo.setFont(font)
        self.label_logo.setAlignment(QtCore.Qt.AlignCenter)
        self.label_logo.setWordWrap(True)
        self.label_logo.setObjectName("label_logo")
        self.verticalLayout.addWidget(self.label_logo)
        self.label_username = QtWidgets.QLabel(self.centralWidget)
        self.label_username.setObjectName("label_username")
        self.verticalLayout.addWidget(self.label_username)
        self.lineEdit_username = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit_username.setInputMask("")
        self.lineEdit_username.setText("")
        self.lineEdit_username.setObjectName("lineEdit_username")
        self.verticalLayout.addWidget(self.lineEdit_username)
        self.label_password = QtWidgets.QLabel(self.centralWidget)
        self.label_password.setObjectName("label_password")
        self.verticalLayout.addWidget(self.label_password)
        self.lineEdit_password = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit_password.setInputMask("")
        self.lineEdit_password.setText("")
        self.lineEdit_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.verticalLayout.addWidget(self.lineEdit_password)
        self.pushButton_login = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_login.setObjectName("pushButton_login")
        self.verticalLayout.addWidget(self.pushButton_login)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.pushButton_register = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_register.setObjectName("pushButton_register")
        self.verticalLayout.addWidget(self.pushButton_register)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        LoginWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(LoginWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 300, 22))
        self.menuBar.setObjectName("menuBar")
        LoginWindow.setMenuBar(self.menuBar)
        self.statusBar = QtWidgets.QStatusBar(LoginWindow)
        self.statusBar.setObjectName("statusBar")
        LoginWindow.setStatusBar(self.statusBar)

        self.retranslateUi(LoginWindow)
        QtCore.QMetaObject.connectSlotsByName(LoginWindow)

    def retranslateUi(self, LoginWindow):
        _translate = QtCore.QCoreApplication.translate
        LoginWindow.setWindowTitle(_translate("LoginWindow", "Login - Counting Sticks"))
        self.label_logo.setText(_translate("LoginWindow", "Counting Sticks"))
        self.label_username.setText(_translate("LoginWindow", "Username"))
        self.label_password.setText(_translate("LoginWindow", "Password"))
        self.pushButton_login.setText(_translate("LoginWindow", "Login"))
        self.pushButton_register.setText(_translate("LoginWindow", "Register"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LoginWindow = QtWidgets.QMainWindow()
    ui = Ui_LoginWindow()
    ui.setupUi(LoginWindow)
    LoginWindow.show()
    sys.exit(app.exec_())

