""" Buffers related classes"""

import sys

from PyQt5.QtWidgets import (QApplication, QGridLayout, QLabel, QPlainTextEdit,
                             QWidget)


# TODO: improve buffer (file gestion) maybe use tempfile.spooftempfile ?
class MBuffer():
    def __init__(self, name, file, active=False, **kwargs):

        self.name = name
        self.file = file
        self.active = active
        self.kwargs = kwargs

    def getLabelInfos(self) -> str:
        return self.name

    def getMenuList(self) -> list:
        pass


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
