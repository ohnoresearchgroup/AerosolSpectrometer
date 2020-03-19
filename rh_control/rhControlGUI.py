# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rhControlGUI.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets
from acquisitionRH import AcquisitionRH


class Ui_rhControlMainWindow(object):
    def setupUi(self, rhControlMainWindow):
        #main
        rhControlMainWindow.setObjectName("rhControlMainWindow")
        rhControlMainWindow.resize(359, 294)
        self.centralwidget = QtWidgets.QWidget(rhControlMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        #start push button
        self.startPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.startPushButton.setGeometry(QtCore.QRect(210, 40, 113, 32))
        self.startPushButton.setObjectName("startPushButton")
        self.startPushButton.clicked.connect(self.startFunc)
        
        #stop push button
        self.stopPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.stopPushButton.setGeometry(QtCore.QRect(210, 70, 113, 32))
        self.stopPushButton.setObjectName("stopPushButton")
        self.stopPushButton.clicked.connect(self.stopFunc)
        
        #rh display
        self.rhDisplay = QtWidgets.QLCDNumber(self.centralwidget)
        self.rhDisplay.setGeometry(QtCore.QRect(20, 40, 141, 61))
        self.rhDisplay.setObjectName("rhDisplay")
        
        
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 20, 60, 16))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(240, 20, 60, 16))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(170, 110, 60, 16))
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(50, 160, 60, 16))
        self.label_4.setObjectName("label_4")
        
        #interval edit
        self.intervalEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.intervalEdit.setGeometry(QtCore.QRect(240, 110, 81, 21))
        self.intervalEdit.setObjectName("intervalEdit")
        self.intervalEdit.insertPlainText('1')
        
        #set point edit
        self.setPointEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.setPointEdit.setGeometry(QtCore.QRect(30, 180, 101, 41))
        self.setPointEdit.setObjectName("setPointEdit")
        
        #set point check
        self.setPointcheckBox = QtWidgets.QCheckBox(self.centralwidget)
        self.setPointcheckBox.setGeometry(QtCore.QRect(160, 190, 87, 20))
        self.setPointcheckBox.setObjectName("setPointcheckBox")
        
        #main
        rhControlMainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(rhControlMainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 359, 22))
        self.menubar.setObjectName("menubar")
        rhControlMainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(rhControlMainWindow)
        self.statusbar.setObjectName("statusbar")
        rhControlMainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(rhControlMainWindow)
        QtCore.QMetaObject.connectSlotsByName(rhControlMainWindow)

    def retranslateUi(self, rhControlMainWindow):
        _translate = QtCore.QCoreApplication.translate
        rhControlMainWindow.setWindowTitle(_translate("rhControlMainWindow", "MainWindow"))
        self.startPushButton.setText(_translate("rhControlMainWindow", "Start"))
        self.stopPushButton.setText(_translate("rhControlMainWindow", "Stop"))
        self.label.setText(_translate("rhControlMainWindow", "RH"))
        self.label_2.setText(_translate("rhControlMainWindow", "Log"))
        self.label_3.setText(_translate("rhControlMainWindow", "Interval"))
        self.label_4.setText(_translate("rhControlMainWindow", "Set Point"))
        self.setPointcheckBox.setText(_translate("rhControlMainWindow", "CheckBox"))
        
    def updateLCD(self,number):
        self.rhDisplay.display(number)
        
    def startFunc(self):
        interval = float(self.intervalEdit.toPlainText())
        self.acq = AcquisitionRH(interval,self)
        self.acq.start()
        
    def stopFunc(self):
        self.acq.stop()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    rhControlMainWindow = QtWidgets.QMainWindow()
    ui = Ui_rhControlMainWindow()
    ui.setupUi(rhControlMainWindow)
    rhControlMainWindow.show()
    sys.exit(app.exec_())

