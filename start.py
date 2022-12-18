# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'master.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets
from aerosol.rhcontrol import RHcontrol
from aerosol.rhControlGUI import Ui_RHcontrolGUI
from aerosol.aerosolcontrol import AerosolControl
from aerosol.aerosolControlGUI import Ui_aerosolControlGUI
from optical.spectrometerGUI import Ui_spectrometerGUI
from optical.spectrometer import Spectrometer
import matplotlib
matplotlib.use('Qt5Agg')

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(284, 293)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        #rh control pushbutton
        self.rhControlpushButton = QtWidgets.QPushButton(self.centralwidget)
        self.rhControlpushButton.setGeometry(QtCore.QRect(50, 20, 181, 61))
        self.rhControlpushButton.setObjectName("rhControlpushButton")
        self.rhControlpushButton.clicked.connect(self.openRHcontrol)
        
        #spectrometer control pushbutton
        self.spectrometerPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.spectrometerPushButton.setGeometry(QtCore.QRect(50, 90, 181, 61))
        self.spectrometerPushButton.setObjectName("spectrometerPushButton")
        self.spectrometerPushButton.clicked.connect(self.openSpectrometer)
        
        #aerosol pushbutton
        self.AerosolpushButton = QtWidgets.QPushButton(self.centralwidget)
        self.AerosolpushButton.setGeometry(QtCore.QRect(50, 160, 181, 61))
        self.AerosolpushButton.setObjectName("AerosolpushButton")
        self.AerosolpushButton.clicked.connect(self.openAerosol)
        
        #main window
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 284, 22))
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
        self.AerosolpushButton.setText(_translate("MainWindow", "Aerosol Control"))
        
    def initRHcontrol(self):
        #called in beginning to setup window
        self.rhcontrol = RHcontrol()

    def openRHcontrol(self):
        #show RH control window when button pressed
        rhWindow.show()
        
    def initSpectrometer(self):
        #called in beginning to setup window
        self.spectrometer = Spectrometer()
        
    def openSpectrometer(self):
        #show spectrometer window when button pressed
        spectrometerWindow.show()
        
    def initAerosol(self):
        #called in beginning to setup window
        self.aerosol = AerosolControl()
        
    def openAerosol(self):
        #show aerosol window when button pressed
        aerosolWindow.show()


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
    
    #create window for spectrometer control (doesn't show it yet)
    uiMain.initSpectrometer()
    spectrometerWindow = QtWidgets.QMainWindow()
    uiSpec = Ui_spectrometerGUI()
    #give spectrometer gui the spectrometer object
    uiSpec.setupUi(spectrometerWindow,uiMain.spectrometer)
    #give spectrometer object the window
    uiMain.spectrometer.assignWindow(uiSpec)
    
    #create window for aerosol control (doesn't show it yet)
    uiMain.initAerosol()
    aerosolWindow = QtWidgets.QMainWindow()
    uiAer = Ui_aerosolControlGUI()
    #give aerosol gui the aerosol object
    uiAer.setupUi(aerosolWindow,uiMain.aerosol)
    
    #for exit
    sys.exit(app.exec_())

