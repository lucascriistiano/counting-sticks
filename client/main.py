from PyQt5 import QtWidgets
import sys
import Pyro4
import Pyro4.util
import ui

sys.excepthook = Pyro4.util.excepthook

def main():
    counting_sticks = Pyro4.Proxy("PYRONAME:counting_sticks")  # use name server object lookup uri shortcut

    app = QtWidgets.QApplication(sys.argv)
    window = ui.MainWindow(counting_sticks)
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()