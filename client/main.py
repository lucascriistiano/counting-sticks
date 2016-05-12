from PyQt5 import QtWidgets

import sys
import Pyro4
import ui


def main():
    counting_sticks = Pyro4.Proxy("PYRONAME:countingsticks")  # use name server object lookup uri shortcut

    app = QtWidgets.QApplication(sys.argv)
    window = ui.MainWindow(counting_sticks)
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()