from PyQt5.QtGui import QColor, QTextCharFormat, QFont, QSyntaxHighlighter
from PyQt5.QtCore import QRegularExpression as QRegExp


def getformat(color, style=""):
    """Return a QTextCharFormat with the given attributes.
    """

    _color = QColor()
    _color.setNamedColor(color)

    _format = QTextCharFormat()
    _format.setForeground(_color)

    if 'bold' in style:
        _format.setFontWeight(QFont.Bold)
    if 'italic' in style:
        _format.setFontItalic(True)

    return _format


STYLES = {
    'keyword': getformat('blue'),
    'operator': getformat('red'),
    'brace': getformat('darkGray'),
    'defclass': getformat('black', 'bold'),
    'defvar': getformat('lightbrown'),
    'string': getformat('magenta'),
    'string2': getformat('darkMagenta'),
    'comment': getformat('darkGreen', 'italic'),
    'self': getformat('black', 'italic'),
    'numbers': getformat('brown'),
}


class PythonHighlighter(QSyntaxHighlighter):

    KEYWORDS = ['False', 'def', 'if', 'raise', 'None',
                'del', 'import', 'return',
                'True', 'elif', 'in', 'try',
                'and', 'else', 'is', 'while', 'as',
                'except', 'lambda', 'with', 'assert', 'finally',
                'nonlocal', 'yield', 'break', 'for', 'not',
                'class', 'from', 'or', 'continue', 'global', 'pass']

    OPERATORS = [
        '=',
        # Comparison
        '==', '!=', '<', '<=', '>', '>=',
        # Arithmetic
        '\+', '-', '\*', '/', '//', '\%', '\*\*',
        # In-place
        '\+=', '-=', '\*=', '/=', '\%=',
        # Bitwise
        '\^', '\|', '\&', '\~', '>>', '<<',
    ]

    BRACES = ['\{', '\}', '\(', '\)', '\[', '\]']

    def __init__(self, document):

        QSyntaxHighlighter.__init__(self, document)

        rules = []

        # These are the defaults rules
        rules += [(r'\b%s\b' % kw, 0, STYLES["keyword"])
                  for kw in PythonHighlighter.KEYWORDS]
        rules += [(r'%s' % o, 0, STYLES["operator"])
                  for o in PythonHighlighter.OPERATORS]
        rules += [(r'%s' % b, 0, STYLES["brace"])
                  for b in PythonHighlighter.BRACES]

        # All other rules
        rules += [
            # 'self'
            (r'\bself\b', 0, STYLES['self']),

            # Double-quoted string, possibly containing escape sequences
            (r'"[^"\\]*(\\.[^"\\]*)*"', 0, STYLES['string']),
            # Single-quoted string, possibly containing escape sequences
            (r"'[^'\\]*(\\.[^'\\]*)*'", 0, STYLES['string']),


            # 'def' followed by an identifier
            (r'\bdef\b\s*(\w+)', 1, STYLES['defclass']),
            # 'class' followed by an identifier
            (r'\bclass\b\s*(\w+)', 1, STYLES['defclass']),

            # From '#' until a newline
            (r'#[^\n]*', 0, STYLES['comment']),

            # Numeric literals
            (r'\b[+-]?[0-9]+[lL]?\b', 0, STYLES['numbers']),
            (r'\b[+-]?0[xX][0-9A-Fa-f]+[lL]?\b', 0, STYLES['numbers']),
            (r'\b[+-]?[0-9]+(?:\.[0-9]+)?(?:[eE][+-]?[0-9]+)?\b',
             0, STYLES['numbers']),
        ]

        self.rules = [(QRegExp(pat), index, fmt)
                      for (pat, index, fmt) in rules]

        self.multiline_end = QRegExp(r'"""')
        self.multiline_start = QRegExp(r'"""')

    def highlightBlock(self, text):
        """Apply highlight"""

        # expression is a QRegularExpression
        # Nth is the index of the matched thing
        for expression, nth, fmt in self.rules:
            matchIter = expression.globalMatch(text)
            while matchIter.hasNext():
                match = matchIter.next()
                self.setFormat(match.capturedStart(nth),
                               match.capturedLength(nth), fmt)

        self.setCurrentBlockState(0)

        startIndex = 0
        if (self.previousBlockState() != 1):
            startIndex = self.multiline_start.match(text).capturedStart()

        while (startIndex >= 0):
            # print(dir(self.multiline_end))
            match = self.multiline_end.match(text, startIndex)
            endIndex = match.capturedStart()
            commentLength = 0
            if (endIndex == -1):
                self.setCurrentBlockState(1)
                commentLength = text.length() - startIndex
            else:
                commentLength = endIndex - startIndex + match.capturedLength()
            self.setFormat(startIndex, commentLength, STYLES["string2"])
            startIndex = self.multiline_start.match(
                text, startIndex + commentLength).capturedStart()
