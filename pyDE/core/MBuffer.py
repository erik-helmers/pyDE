""" Buffers related classes"""

import sys
from .MFile import MFile
from PyQt5.QtWidgets import (QApplication, QGridLayout, QLabel,
                             QPlainTextEdit,
                             QWidget)

print("The use of this module is deprecated !!!")

# TODO: improve buffer (file gestion) maybe use tempfile.spooftempfile ?


class MBuffer():

    loaded_buffers = {}

    def __init__(self, name, file):
        pass

    def getLabelInfos(self) -> str:
        return self.name

    def getMenuList(self) -> list:
        pass

    def write(self, s):
        self.file.write(s)

# TODO: custom Text edit for syntax coloring


class QBufferWidget(QWidget):

    """Graphic related only"""

    def __init__(self, parent, mbuffer, *args, **kwargs):

        super().__init__(parent, **kwargs)

        self.mbuffer = mbuffer
        self.initUI()

    def initUI(self):

        # Graphic setup

        # Layout settings
        gridLayout = QGridLayout(self)
        self.setLayout(gridLayout)
        gridLayout.setContentsMargins(0, 0, 0, 0)
        gridLayout.setSpacing(0)

        # Info label
        self.buffLabelInfos = QLabel(self)
        self.buffLabelInfos.setText(self.mbuffer.getLabelInfos())

        # Entry :
        # Todo: Replace by custom text edit for syntax coloration purpose
        gridLayout.addWidget(self.buffLabelInfos, 2, 0)
        self.buffTEntry = QPlainTextEdit(self)

        gridLayout.addWidget(self.buffTEntry, 1, 0)


if __name__ == "__main__":

    app = QApplication(sys.argv)
    ex = QBufferWidget(None)
    print("hello")
    sys.exit(app.exec_())
