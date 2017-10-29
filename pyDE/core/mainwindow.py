""" Main window related:
        - is always top window
"""
import sys

# TODO(1000): CHANGE THIS
from MBuffer import MBuffer, QBufferWidget

from PyQt5.QtWidgets import QMainWindow, QGridLayout, QApplication, QLabel
#from PyQt5.QtCore import QApplication


class pyDEMWin(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        # Layout setup
        mainLayout = QGridLayout(self)
        mainLayout.setObjectName("MainWindowLayout")
        self.setLayout(mainLayout)

        # TODO: custom GridLayout for easy split ?
        # TODO: use splitter
        self.buffersLayout = QGridLayout(self)
        self.buffersLayout.setObjectName("BuffersLayout")

        alabel = QLabel()
        self.buffersLayout.addWidget(alabel, 0, 0)
        # self.buffersLayout.addWidget(
        #     QBufferWidget(MBuffer("dummy", None)), 0, 0)

        mainLayout.addLayout(self.buffersLayout, 0, 0)

        self.statusBar().showMessage('Ready')

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle("PyDE")
        self.show()


class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.statusBar().showMessage('Ready')

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Statusbar')
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = pyDEMWin()
    sys.exit(app.exec_())
