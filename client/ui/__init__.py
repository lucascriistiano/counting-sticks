# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
import ui.widgets as widgets


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, counting_sticks, parent=None):
        super(MainWindow, self).__init__(parent)

        self.counting_sticks = counting_sticks

        self.central_widget = QtWidgets.QStackedWidget()
        self.setCentralWidget(self.central_widget)

        self.login_widget = widgets.LoginWidget(self, self.counting_sticks)
        self.login_widget.push_button_register.clicked.connect(self.register)
        self.central_widget.addWidget(self.login_widget)

        self.setWindowIcon(QtGui.QIcon('img/fire_matchstick.png'))

    def register(self):
        register_widget = widgets.RegisterWidget(self, self.counting_sticks)
        self.central_widget.addWidget(register_widget)
        self.central_widget.setCurrentWidget(register_widget)
