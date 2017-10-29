# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets


class Ui_Form():
    
    def setupUi(self, Form):
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.buffLabelInfos = QtWidgets.QLabel(Form)
        self.buffLabelInfos.setObjectName("buffLabelInfos")
        self.gridLayout.addWidget(self.buffLabelInfos, 2, 0, 1, 1)
        self.buffTEntry = QtWidgets.QTextEdit(Form)
        self.buffTEntry.setObjectName("buffTEntry")
        self.gridLayout.addWidget(self.buffTEntry, 1, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.buffLabelInfos.setText(_translate("Form", "TextLabel"))
