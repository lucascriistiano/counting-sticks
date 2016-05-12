# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'register.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_RegisterWindow(object):
    def setupUi(self, RegisterWindow):
        RegisterWindow.setObjectName("RegisterWindow")
        RegisterWindow.resize(300, 400)
        RegisterWindow.setAutoFillBackground(False)
        RegisterWindow.setStyleSheet("")
        self.centralWidget = QtWidgets.QWidget(RegisterWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralWidget)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_logo = QtWidgets.QLabel(self.centralWidget)
        font = QtGui.QFont()
        font.setFamily("Al Nile")
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.label_logo.setFont(font)
        self.label_logo.setAlignment(QtCore.Qt.AlignCenter)
        self.label_logo.setWordWrap(False)
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
        self.label_email = QtWidgets.QLabel(self.centralWidget)
        self.label_email.setObjectName("label_email")
        self.verticalLayout.addWidget(self.label_email)
        self.lineEdit_email = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit_email.setInputMask("")
        self.lineEdit_email.setText("")
        self.lineEdit_email.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_email.setObjectName("lineEdit_email")
        self.verticalLayout.addWidget(self.lineEdit_email)
        self.label_password = QtWidgets.QLabel(self.centralWidget)
        self.label_password.setObjectName("label_password")
        self.verticalLayout.addWidget(self.label_password)
        self.lineEdit_password = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit_password.setInputMask("")
        self.lineEdit_password.setText("")
        self.lineEdit_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.verticalLayout.addWidget(self.lineEdit_password)
        self.label_confirm_password = QtWidgets.QLabel(self.centralWidget)
        self.label_confirm_password.setObjectName("label_confirm_password")
        self.verticalLayout.addWidget(self.label_confirm_password)
        self.lineEdit_confirm_password = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit_confirm_password.setInputMask("")
        self.lineEdit_confirm_password.setText("")
        self.lineEdit_confirm_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_confirm_password.setObjectName("lineEdit_confirm_password")
        self.verticalLayout.addWidget(self.lineEdit_confirm_password)
        self.pushButton_register = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_register.setObjectName("pushButton_register")
        self.verticalLayout.addWidget(self.pushButton_register)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Ignored)
        self.verticalLayout.addItem(spacerItem)
        self.pushButton_back = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_back.setObjectName("pushButton_back")
        self.verticalLayout.addWidget(self.pushButton_back)
        RegisterWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(RegisterWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 300, 22))
        self.menuBar.setObjectName("menuBar")
        RegisterWindow.setMenuBar(self.menuBar)
        self.statusBar = QtWidgets.QStatusBar(RegisterWindow)
        self.statusBar.setObjectName("statusBar")
        RegisterWindow.setStatusBar(self.statusBar)

        self.retranslateUi(RegisterWindow)
        QtCore.QMetaObject.connectSlotsByName(RegisterWindow)

    def retranslateUi(self, RegisterWindow):
        _translate = QtCore.QCoreApplication.translate
        RegisterWindow.setWindowTitle(_translate("RegisterWindow", "Register - Counting Sticks"))
        self.label_logo.setText(_translate("RegisterWindow", "Counting Sticks"))
        self.label_username.setText(_translate("RegisterWindow", "Username"))
        self.label_email.setText(_translate("RegisterWindow", "Email"))
        self.label_password.setText(_translate("RegisterWindow", "Password"))
        self.label_confirm_password.setText(_translate("RegisterWindow", "Confirm Password"))
        self.pushButton_register.setText(_translate("RegisterWindow", "Register"))
        self.pushButton_back.setText(_translate("RegisterWindow", "Back"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    RegisterWindow = QtWidgets.QMainWindow()
    ui = Ui_RegisterWindow()
    ui.setupUi(RegisterWindow)
    RegisterWindow.show()
    sys.exit(app.exec_())

