import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QLCDNumber, QSlider, 
    QVBoxLayout, QApplication)


import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QGridLayout, QLabel


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        lcd = QLCDNumber(self)
        sld = QSlider(Qt.Horizontal, self)

        vbox = QVBoxLayout()
        vbox.addWidget(lcd)
        vbox.addWidget(sld)

        self.setLayout(vbox)
        sld.valueChanged.connect(lcd.display)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Signal and slot')
        self.show()

class Example2(QWidget):
    
    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):      

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Event handler')
        self.show()


    def keyPressEvent(self, e):

        if e.key() == Qt.Key_Escape:
            self.close()

class Example3(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):      
        
        grid = QGridLayout()
        grid.setSpacing(10)
        
        x = 0
        y = 0
        
        self.text = "x: {0},  y: {1}".format(x, y)
        
        self.label = QLabel(self.text, self)
        grid.addWidget(self.label, 0, 0, Qt.AlignTop)
        
        self.setMouseTracking(True)
        
        self.setLayout(grid)
        
        self.setGeometry(300, 300, 350, 200)
        self.setWindowTitle('Event object')
        self.show()
        
        
    def mouseMoveEvent(self, e):
        
        x = e.x()
        y = e.y()
        
        text = "x: {0},  y: {1}".format(x, y)
        self.label.setText(text)


import sys
from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication

class Example4(QMainWindow):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):      

        btn1 = QPushButton("Button 1", self)
        btn1.move(30, 50)

        btn2 = QPushButton("Button 2", self)
        btn2.move(150, 50)
      
        btn1.clicked.connect(self.buttonClicked)            
        btn2.clicked.connect(self.buttonClicked)
        
        self.statusBar()
        
        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Event sender')
        self.show()
        
        
    def buttonClicked(self):
      
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' was pressed')

import sys
from PyQt5.QtCore import pyqtSignal, QObject
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox


class Communicate(QObject):
    
    closeApp = pyqtSignal() 
    

class Example5(QMainWindow):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):      

        self.c = Communicate()
        self.c.closeApp.connect(self.close)       
        
        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Emit signal')
        self.show()
        
        
    def mousePressEvent(self, event):
        
        self.c.closeApp.emit()
        
    def closeEvent(self, event):

        reply = QMessageBox.question(self, 'MyMessage',
                                     "Vraiment quitter fdp ?",
                                     QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example5()
    sys.exit(app.exec_())
