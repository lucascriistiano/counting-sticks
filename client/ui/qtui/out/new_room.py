# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'new_room.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_NewRoomWindow(object):
    def setupUi(self, NewRoomWindow):
        NewRoomWindow.setObjectName("NewRoomWindow")
        NewRoomWindow.resize(300, 300)
        NewRoomWindow.setAutoFillBackground(False)
        NewRoomWindow.setStyleSheet("")
        self.centralWidget = QtWidgets.QWidget(NewRoomWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.lineEdit_room_name = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit_room_name.setGeometry(QtCore.QRect(40, 93, 220, 20))
        self.lineEdit_room_name.setInputMask("")
        self.lineEdit_room_name.setText("")
        self.lineEdit_room_name.setObjectName("lineEdit_room_name")
        self.label_room_name = QtWidgets.QLabel(self.centralWidget)
        self.label_room_name.setGeometry(QtCore.QRect(44, 70, 81, 20))
        self.label_room_name.setObjectName("label_room_name")
        self.label_min_players = QtWidgets.QLabel(self.centralWidget)
        self.label_min_players.setGeometry(QtCore.QRect(46, 122, 81, 20))
        self.label_min_players.setObjectName("label_min_players")
        self.pushButton_create_room = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_create_room.setGeometry(QtCore.QRect(40, 191, 220, 40))
        self.pushButton_create_room.setObjectName("pushButton_create_room")
        self.label_logo = QtWidgets.QLabel(self.centralWidget)
        self.label_logo.setGeometry(QtCore.QRect(40, 20, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Baskerville")
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.label_logo.setFont(font)
        self.label_logo.setAlignment(QtCore.Qt.AlignCenter)
        self.label_logo.setWordWrap(False)
        self.label_logo.setObjectName("label_logo")
        self.label_max_players = QtWidgets.QLabel(self.centralWidget)
        self.label_max_players.setGeometry(QtCore.QRect(167, 123, 81, 20))
        self.label_max_players.setObjectName("label_max_players")
        self.spinBox_min_players = QtWidgets.QSpinBox(self.centralWidget)
        self.spinBox_min_players.setGeometry(QtCore.QRect(41, 144, 91, 24))
        self.spinBox_min_players.setMinimum(4)
        self.spinBox_min_players.setMaximum(6)
        self.spinBox_min_players.setObjectName("spinBox_min_players")
        self.spinBox_max_players = QtWidgets.QSpinBox(self.centralWidget)
        self.spinBox_max_players.setGeometry(QtCore.QRect(162, 144, 91, 24))
        self.spinBox_max_players.setMinimum(4)
        self.spinBox_max_players.setMaximum(6)
        self.spinBox_max_players.setObjectName("spinBox_max_players")
        NewRoomWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(NewRoomWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 300, 22))
        self.menuBar.setObjectName("menuBar")
        NewRoomWindow.setMenuBar(self.menuBar)
        self.statusBar = QtWidgets.QStatusBar(NewRoomWindow)
        self.statusBar.setObjectName("statusBar")
        NewRoomWindow.setStatusBar(self.statusBar)

        self.retranslateUi(NewRoomWindow)
        QtCore.QMetaObject.connectSlotsByName(NewRoomWindow)

    def retranslateUi(self, NewRoomWindow):
        _translate = QtCore.QCoreApplication.translate
        NewRoomWindow.setWindowTitle(_translate("NewRoomWindow", "New Room - Counting Sticks"))
        self.label_room_name.setText(_translate("NewRoomWindow", "Room Name"))
        self.label_min_players.setText(_translate("NewRoomWindow", "Min Players"))
        self.pushButton_create_room.setText(_translate("NewRoomWindow", "Create Room"))
        self.label_logo.setText(_translate("NewRoomWindow", "New Room"))
        self.label_max_players.setText(_translate("NewRoomWindow", "Max Players"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    NewRoomWindow = QtWidgets.QMainWindow()
    ui = Ui_NewRoomWindow()
    ui.setupUi(NewRoomWindow)
    NewRoomWindow.show()
    sys.exit(app.exec_())

