# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\1_university\Anul III\1_Sem1\BD\BD-Tema\newStudio.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3 as sl

class Ui_StudioWindow(object):

    def discard(self):
        self.nameEdit.clear()
        self.dateEdit.clear()


    def add(self,current_win):
        # TODO
        con = sl.connect('TEMA.DB')
        cursor = con.cursor()

        cursor.execute("SELECT studio_id  FROM Studio")

        results = cursor.fetchall()
        max = results[0][0]
        print(max)
        for r in results:
            if (max < r[0]):
                max = r[0]
        print(max)
        max = max + 1
        sql = 'INSERT INTO Studio (studio_id,studio_name,date_founded) values( ?, ?,?)'
        data = [
            (max, self.nameEdit.text(), self.dateEdit.text())
        ]
        with con:
            con.executemany(sql, data)
        current_win.close()

    def setupUi(self, StudioWindow):
        # STUDIO WINDOW
        StudioWindow.setObjectName("StudioWindow")
        StudioWindow.resize(805, 700)
        StudioWindow.setMinimumSize(QtCore.QSize(805, 700))
        StudioWindow.setMaximumSize(QtCore.QSize(805, 700))
        StudioWindow.setStyleSheet("background-color: rgb(151, 232, 255);")
        self.centralwidget = QtWidgets.QWidget(StudioWindow)
        self.centralwidget.setObjectName("centralwidget")



        #DICARD BUTTON
        self.discardButton = QtWidgets.QPushButton(self.centralwidget)
        self.discardButton.setGeometry(QtCore.QRect(30, 610, 171, 61))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI Semilight")
        font.setPointSize(15)
        self.discardButton.setFont(font)
        self.discardButton.setStyleSheet("QPushButton{\n"
"    background: pink;\n"
"    border: 2px solid rgb(151, 232, 255);\n"
"    border-radius: 20px;\n"
"    color: black;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color:rgb(206, 164, 196);\n"
"    border: 2px solid rgb(206, 164, 196);\n"
"}")
        self.discardButton.setObjectName("discardButton")
        self.discardButton.clicked.connect(self.discard)

        # NAME LABEL
        self.namelabel = QtWidgets.QLabel(self.centralwidget)
        self.namelabel.setGeometry(QtCore.QRect(70, 290, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI Semilight")
        font.setPointSize(12)
        self.namelabel.setFont(font)
        self.namelabel.setObjectName("namelabel")

        # NAME EDIT
        self.nameEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.nameEdit.setGeometry(QtCore.QRect(260, 280, 451, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.nameEdit.setFont(font)
        self.nameEdit.setStyleSheet("QLineEdit{\n"
"    background: pink;\n"
"    border: 2px solid rgb(151, 232, 255);\n"
"    border-radius: 20px;\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"    border: 2px solid rgb(111, 165, 171);\n"
"}\n"
"")
        self.nameEdit.setText("")
        self.nameEdit.setObjectName("lineEdit")

        # DATE LABEL
        self.dateLabel = QtWidgets.QLabel(self.centralwidget)
        self.dateLabel.setGeometry(QtCore.QRect(70, 330, 101, 51))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI Semilight")
        font.setPointSize(12)
        self.dateLabel.setFont(font)
        self.dateLabel.setObjectName("dateLabel")

        #DATE EDIT
        '''
        self.dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit.setGeometry(QtCore.QRect(420, 340, 110, 22))
        self.dateEdit.setStyleSheet("QDateEdit{\n"
"    background: pink;\n"
"    border: 2px solid rgb(151, 232, 255);\n"
"    border-radius: 20px;\n"
"    color: black;\n"
"    \n"
"    selection-color:pink;\n"
"\n"
"}\n"
"")
        self.dateEdit.setObjectName("dateEdit")
        '''
        #DATE EDIT
        self.dateEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.dateEdit.setGeometry(QtCore.QRect(420, 340, 110, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.dateEdit.setFont(font)
        self.dateEdit.setStyleSheet("QLineEdit{\n"
                                    "    background: pink;\n"
                                    "    border: 2px solid rgb(151, 232, 255);\n"
                                    "    border-radius: 20px;\n"
                                    "}\n"
                                    "\n"
                                    "QLineEdit:focus{\n"
                                    "    border: 2px solid rgb(111, 165, 171);\n"
                                    "}\n"
                                    "")
        self.dateEdit.setText("")
        self.dateEdit.setObjectName("dateEdit")
        # ADD BUTTON
        self.addButton = QtWidgets.QPushButton(self.centralwidget)
        self.addButton.setGeometry(QtCore.QRect(620, 610, 171, 61))
        self.addButton.clicked.connect(lambda: self.add(StudioWindow))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI Semilight")
        font.setPointSize(15)
        self.addButton.setFont(font)
        self.addButton.setStyleSheet("QPushButton{\n"
"    background: pink;\n"
"    border: 2px solid rgb(151, 232, 255);\n"
"    border-radius: 20px;\n"
"    color: black;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color:rgb(206, 164, 196);\n"
"    border: 2px solid rgb(206, 164, 196);\n"
"}")
        self.addButton.setObjectName("addButton")


        StudioWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(StudioWindow)
        self.statusbar.setObjectName("statusbar")
        StudioWindow.setStatusBar(self.statusbar)

        self.retranslateUi(StudioWindow)
        QtCore.QMetaObject.connectSlotsByName(StudioWindow)

    def retranslateUi(self, StudioWindow):
        _translate = QtCore.QCoreApplication.translate
        StudioWindow.setWindowTitle(_translate("StudioWindow", "StudioWindow"))
        self.discardButton.setText(_translate("StudioWindow", "Discard"))
        self.namelabel.setText(_translate("StudioWindow", "Name"))
        self.dateLabel.setText(_translate("StudioWindow", "Established"))
        self.addButton.setText(_translate("StudioWindow", "Add"))