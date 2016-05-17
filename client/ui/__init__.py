# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
import ui.widgets as widgets


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, counting_sticks, parent=None, update_time=1000):
        super(MainWindow, self).__init__(parent)

        self.counting_sticks = counting_sticks

        self.central_widget = QtWidgets.QStackedWidget()
        self.setCentralWidget(self.central_widget)

        self.login_widget = widgets.LoginWidget(self, self.counting_sticks)
        self.central_widget.addWidget(self.login_widget)

        self.setWindowIcon(QtGui.QIcon('img/fire_matchstick.png'))

        self.update_time = update_time
        self.timer_ui_update = QtCore.QTimer()

    def start_update_timer(self):
        self.timer_ui_update.start(self.update_time)

    def stop_update_timer(self):
        self.timer_ui_update.stop()

    def reconnect_update_timer(self, new_handler, old_handler=None):
        while True:
            try:
                if old_handler is not None:
                    self.timer_ui_update.timeout.disconnect(old_handler)
                else:
                    self.timer_ui_update.timeout.disconnect()
            except TypeError:
                break
        if new_handler is not None:
            self.timer_ui_update.timeout.connect(new_handler)

    def center_on_screen(self):
        resolution = QtWidgets.QDesktopWidget().screenGeometry()
        self.move((resolution.width() / 2) - (self.frameSize().width() / 2),
                  (resolution.height() / 2) - (self.frameSize().height() / 2))
