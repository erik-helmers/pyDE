""" Highlighter class. """

from .python_highlight_rules import Rules

from PyQt5.QtGui import (
    QSyntaxHighlighter, QTextCharFormat, QRegExpValidator, QFont, QColor)


class qHighlighter(QSyntaxHighlighter):

    def __init__(self, parent):
        super().__init__(parent)

        rules = self.getRule()
        print(rules)

    def getRule(self):
        return Rules
