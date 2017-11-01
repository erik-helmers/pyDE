""" The file class for PyDE which supports :
        - hard disk file editing
        - temporary file which switch between
          memory and hard disk writting.
"""


class MFile:

    def __init__(self, name=None, path=None):

        self.name = name
        self.path = path
        self.baseFile = None

        if path is not None:
            self.baseFile = MFile.loadRealFile(path)

    @staticmethod
    def loadRealFile(path):
        try:
            file = open(path, "r")
            return file.read()
        except FileNotFoundError:
            return None

    def getHash(self):
        return hash(self.name) + hash(self.path)

    def getContent(self):
        if self.baseFile is None:
            return ""
        return self.baseFile
