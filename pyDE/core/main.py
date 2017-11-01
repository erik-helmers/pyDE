from .MMainWin import pyDEMWin
from PyQt5.QtWidgets import QApplication
import sys


def main():
    app = QApplication(sys.argv)
    print(sys.argv)
    pyDEMWin.DEFAULT_BUFFER = sys.argv[1]
    mainw = pyDEMWin()
    sys.exit(app.exec_())
