import sys
from .MFile import MFile
from .WFileBuffer import WFileBuffer
from PyQt5.QtGui import QTextDocument
from .pWidgets.python_highlight_rules import PythonHighlighter

"""FileBuffer class:
gestion of files :
    - try to load files
    - stock them
    - if already loaded don't load again
"""


class FileBuffer:

    """ FileBuffer class :
Since a file is described by a name and a path,
And we don't want to load to load multiple times
the same file, we use the name and path as a base
description (hash <- bad name), and keep track of
the loaded files with a loaded_buffers dict.
"""
    # TODO !! Bad idea because if x=y then hash(x)=hash(y)
    # else hash(x) may be equal to hash(y)
    # Use (name, path) attribute

    loaded_buffers = {}
    code = 14938430480394834948

    def __init__(self, code, name, path=None):
        """ Don't use this method to create file buffer
        use the static method new instead.

        The code is a temporary security feature, which
        check that the function has been called from new"""
        if code != FileBuffer.code:
            raise ValueError("Should use new staticmethod" +
                             " instead of default constructor")
        self.file = MFile(name, path)
        self.qdocument = QTextDocument(self.file.getContent())
        self.highlighter = PythonHighlighter(self.qdocument)

    def getFileBufferWidget(self, parent):
        return WFileBuffer(self, parent)

    @staticmethod
    def getHashFrom(name, path):
        "create 'hash' from name and path"
        return (name, path)

    @staticmethod
    def new(name, path=None):
        thisHash = (name, path)
        try:
            return FileBuffer.loaded_buffers[thisHash]
        except KeyError:
            newFileBuff = FileBuffer(FileBuffer.code, name, path)
            FileBuffer.loaded_buffers[thisHash] = newFileBuff
            return newFileBuff
