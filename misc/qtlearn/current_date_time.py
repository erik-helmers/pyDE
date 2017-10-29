#!/usr/bin/env python3

from PyQt5.QtCore import QDate, QTime, QDateTime, Qt


print("==========================ETC DATE=================")
now = QDate.currentDate()
print(now.toString(Qt.ISODate))
print(now.toString(Qt.DefaultLocaleLongDate))

datetime = QDateTime.currentDateTime()
print(datetime.toString())

time = QTime.currentTime()
print(time.toString(Qt.DefaultLocaleLongDate))

print("==========================UTC=====================")

now = QDateTime.currentDateTime()

print("Local datetime : ", now.toString(Qt.ISODate))
print("Universal datetime: ", now.toUTC().toString(Qt.ISODate))

print("The offset from UTC is: {} seconds".format(now.offsetFromUtc()))
