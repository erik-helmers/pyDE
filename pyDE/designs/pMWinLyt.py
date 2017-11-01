# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pMWindowLayout.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_pMWindowLayout(object):
    def setupUi(self, pMWindowLayout):
        pMWindowLayout.setObjectName("pMWindowLayout")
        pMWindowLayout.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(pMWindowLayout)
        self.centralwidget.setObjectName("centralwidget")
        self.mainLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.mainLayout.setContentsMargins(0, 0, 0, 0)
        self.mainLayout.setSpacing(0)
        self.mainLayout.setObjectName("mainLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.gridLayout.setObjectName("gridLayout")
        self.mainLayout.addLayout(self.gridLayout)
        self.minibuferEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.minibuferEdit.setObjectName("minibuferEdit")
        self.mainLayout.addWidget(self.minibuferEdit)
        pMWindowLayout.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(pMWindowLayout)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 29))
        self.menubar.setObjectName("menubar")
        pMWindowLayout.setMenuBar(self.menubar)

        self.retranslateUi(pMWindowLayout)
        QtCore.QMetaObject.connectSlotsByName(pMWindowLayout)

    def retranslateUi(self, pMWindowLayout):
        _translate = QtCore.QCoreApplication.translate
        pMWindowLayout.setWindowTitle(_translate("pMWindowLayout", "MainWindow"))

