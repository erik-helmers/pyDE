from PyQt5.QtWidgets import QTextEdit


class PTextEntry(QTextEdit):

    def __init__(self, mbuffer, parent=None):

        # initialize QTextEdit
        super().__init__(parent)
