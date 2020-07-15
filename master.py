# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'master.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets
from rhcontrol import RHcontrol
from rhControlGUI import Ui_RHcontrolGUI
from optical.spectrometerGUI import Ui_spectrometerGUI
from optical.spectrometer import Spectrometer
import matplotlib
matplotlib.use('Qt5Agg')

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(291, 228)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        #rh control push button
        self.rhControlpushButton = QtWidgets.QPushButton(self.centralwidget)
        self.rhControlpushButton.setGeometry(QtCore.QRect(50, 20, 181, 61))
        self.rhControlpushButton.setObjectName("rhControlpushButton")
        self.rhControlpushButton.clicked.connect(self.openRHcontrol)
        
        #spectrometer push button
        self.spectrometerPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.spectrometerPushButton.setGeometry(QtCore.QRect(50, 90, 181, 61))
        self.spectrometerPushButton.setObjectName("spectrometerPushButton")
        self.spectrometerPushButton.clicked.connect(self.openSpectrometer)
        
        #main window
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 291, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Master Control"))
        self.rhControlpushButton.setText(_translate("MainWindow", "RH Control"))
        self.spectrometerPushButton.setText(_translate("MainWindow", "Spectrometer Control"))

    def initRHcontrol(self):
        self.rhcontrol = RHcontrol()

    def openRHcontrol(self):
        #show the RH control window
        rhWindow.show()
        
    def initSpectrometer(self):
        self.spectrometer = Spectrometer()
        
    def openSpectrometer(self):
        spectrometerWindow.show()



if __name__ == "__main__":
    #create main window
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    uiMain = Ui_MainWindow()
    uiMain.setupUi(MainWindow)
    MainWindow.show()
    
    #create window for RH control (don't show it yet)
    uiMain.initRHcontrol()
    rhWindow = QtWidgets.QMainWindow()
    uiRH = Ui_RHcontrolGUI()
    #give RH control window the rhcontrol object
    uiRH.setupUi(rhWindow,uiMain.rhcontrol)
    #give RH control object the window
    uiMain.rhcontrol.assignWindow(uiRH)
    
    #creae window for spectrometer control (doesn't show it yet)
    uiMain.initSpectrometer()
    spectrometerWindow = QtWidgets.QMainWindow()
    uiSpec = Ui_spectrometerGUI()
    #give spectrometer gui the spectrometer object
    uiSpec.setupUi(spectrometerWindow,uiMain.spectrometer)
    #give spectrometer object the window
    uiMain.spectrometer.assignWindow(uiSpec)
    
    #for exit
    sys.exit(app.exec_())

