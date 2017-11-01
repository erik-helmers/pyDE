""" Main window related:
        - is always top window
"""
import sys

# TODO(1000): CHANGE THIS
from ..designs.Ui_MainWin import Ui_pMWindowLayout
from .FileBuffer import FileBuffer
from PyQt5.QtWidgets import QMainWindow, QGridLayout, QApplication, QLabel
#from PyQt5.QtCore import QApplication


class pyDEMWin(QMainWindow, Ui_pMWindowLayout):

    DEFAULT_BUFFER = None

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.load_buffer(self.get_default_buffer(), (0, 0, 2, 1))
        self.load_buffer(self.get_default_buffer(), (0, 1))
        self.load_buffer(self.get_default_buffer(), (1, 1))

        self.show()

    def get_default_buffer(self):
        filebuffer = FileBuffer.new("<temp>", pyDEMWin.DEFAULT_BUFFER)
        # print(filebuffer.qdocument)
        return filebuffer.getFileBufferWidget(self)

    def load_buffer(self, mbuffer, pos):
        self.buffersLayout.addWidget(mbuffer, *pos)
