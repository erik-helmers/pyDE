from PyQt5.QtWidgets import QLabel, QWidget, QGridLayout, QTextEdit


class WFileBuffer(QWidget):

    """Graphic related only of WFileBuffer"""

    # TODO: support shell like behavior (partial readonly) (nocustom?)
    # TODO: use behavior defined by buffer

    def __init__(self, mbuffer, parent, *args, **kwargs):

        super().__init__(parent, **kwargs)

        self.mbuffer = mbuffer
        self.initUI()

        self.wEntry.setDocument(self.mbuffer.qdocument)
        self.setInfoLabText()

    def initUI(self):

        # Graphic setup Only

        # Layout settings
        gridLayout = QGridLayout(self)
        self.setLayout(gridLayout)
        gridLayout.setContentsMargins(0, 0, 0, 0)
        gridLayout.setSpacing(0)

        # Info label
        self.wInfosLab = QLabel(self)

        # Entry :
        # Todo: Replace by custom text edit for syntax coloration purpose
        gridLayout.addWidget(self.wInfosLab, 2, 0)
        self.wEntry = QTextEdit(self)
        gridLayout.addWidget(self.wEntry, 1, 0)

    def setInfoLabText(self):

        # TODO: signal call with self as arg

        self.wInfosLab.setText(self.mbuffer.file.name)
