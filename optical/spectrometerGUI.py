# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'spectrometerGUI.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject, pyqtSignal

class Ui_spectrometerGUI(object):
    def setupUi(self, spectrometerGUI,spectrometer):
        #give window spectrometer object
        self.spectrometer = spectrometer
        #main window
        spectrometerGUI.setObjectName("spectrometerGUI")
        spectrometerGUI.resize(678, 307)
        self.centralwidget = QtWidgets.QWidget(spectrometerGUI)
        self.centralwidget.setObjectName("centralwidget")
        
        #connect monochromator push button
        self.connectMonochromatorPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.connectMonochromatorPushButton.setGeometry(QtCore.QRect(10, 40, 191, 61))
        self.connectMonochromatorPushButton.setObjectName("connectMonochromatorPushButton")
        
        #connect photon counter push button
        self.connectPhotonCounterPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.connectPhotonCounterPushButton.setGeometry(QtCore.QRect(10, 100, 191, 61))
        self.connectPhotonCounterPushButton.setObjectName("connectPhotonCounterPushButton")
        
        #connect laser ard
        self.connectLaserArdPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.connectLaserArdPushButton.setGeometry(QtCore.QRect(10, 190, 191, 61))
        self.connectLaserArdPushButton.setObjectName("connectLaserArdPushButton")
        
        #laser checkbox
        self.laserCheckBox = QtWidgets.QCheckBox(self.centralwidget)
        self.laserCheckBox.setGeometry(QtCore.QRect(220, 210, 121, 21))
        self.laserCheckBox.setObjectName("laserCheckBox")
                 
        #monochromator lcd number
        self.monochromatorLcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.monochromatorLcdNumber.setGeometry(QtCore.QRect(220, 90, 101, 41))
        self.monochromatorLcdNumber.setProperty("value", 400.0)
        self.monochromatorLcdNumber.setObjectName("lcdNumber")
        
        #set monochromator edit
        self.setMonochromatorPlainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.setMonochromatorPlainTextEdit.setGeometry(QtCore.QRect(270, 50, 51, 31))
        self.setMonochromatorPlainTextEdit.setObjectName("setMonochromatorPlainTextEdit")
        
        #set monochromator push button
        self.setMonochromatorPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.setMonochromatorPushButton.setGeometry(QtCore.QRect(220, 50, 51, 32))
        self.setMonochromatorPushButton.setObjectName("setMonochromatorPushButton")
        
        #scan min edit
        self.scanMinPlainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.scanMinPlainTextEdit.setGeometry(QtCore.QRect(578, 40, 41, 31))
        self.scanMinPlainTextEdit.setObjectName("scanMinPlainTextEdit")
        
        #scan max edit
        self.scanMaxPlainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.scanMaxPlainTextEdit.setGeometry(QtCore.QRect(578, 70, 41, 31))
        self.scanMaxPlainTextEdit.setObjectName("scanMaxPlainTextEdit")
        
        #scan step edit
        self.scanStepPlainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.scanStepPlainTextEdit.setGeometry(QtCore.QRect(578, 100, 41, 31))
        self.scanStepPlainTextEdit.setObjectName("scanStepPlainTextEdit")
        
        #scan duration edit
        self.scanDurationPlainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.scanDurationPlainTextEdit.setGeometry(QtCore.QRect(578, 130, 41, 31))
        self.scanDurationPlainTextEdit.setObjectName("scanDurationPlainTextEdit")
        
        #start scan push button
        self.startScanPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.startScanPushButton.setGeometry(QtCore.QRect(350, 50, 131, 32))
        self.startScanPushButton.setObjectName("startScanPushButton")
        
        #stop scan push button
        self.stopScanPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.stopScanPushButton.setGeometry(QtCore.QRect(350, 110, 131, 32))
        self.stopScanPushButton.setObjectName("stopScanPushButton")
        
        #start time scan push button
        self.startTimeScanPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.startTimeScanPushButton.setGeometry(QtCore.QRect(350, 80, 131, 32))
        self.startTimeScanPushButton.setObjectName("startTimeScanPushButton")
        
        #start multi scan push button
        self.startMultiScanPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.startMultiScanPushButton.setGeometry(QtCore.QRect(350, 170, 141, 32))
        self.startMultiScanPushButton.setObjectName("startMultiScanPushButton")
        
        #set number of multi scans edit
        self.setNumberMultiPlainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.setNumberMultiPlainTextEdit.setGeometry(QtCore.QRect(550, 180, 41, 31))
        self.setNumberMultiPlainTextEdit.setObjectName("setNumberMultiPlainTextEdit")
        
        #cancel multi scans push button
        self.cancelMultiScanPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.cancelMultiScanPushButton.setGeometry(QtCore.QRect(350, 200, 141, 32))
        self.cancelMultiScanPushButton.setObjectName("cancelMultiScanPushButton")
        
        #labels
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(498, 40, 71, 20))
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(498, 70, 71, 20))
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(488, 100, 81, 20))
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(478, 130, 91, 20))
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(348, 20, 301, 20))
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(19, 20, 171, 20))
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(220, 20, 111, 20))
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(490, 180, 51, 20))
        self.label_8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        
        ##########signals and slots###########
        self.connectMonochromatorPushButton.clicked.connect(self.spectrometer.initMonochromator)
        self.connectPhotonCounterPushButton.clicked.connect(self.spectrometer.initPhotonCounter)
        self.connectLaserArdPushButton.clicked.connect(self.spectrometer.initLaserArd)
        self.startScanPushButton.clicked.connect(self.startScanFunc)
        self.startTimeScanPushButton.clicked.connect(self.startTimeScanFunc)
        self.stopScanPushButton.clicked.connect(self.stopScanFunc)
        self.setMonochromatorPushButton.clicked.connect(self.setMonochromatorPositionFunc)
        self.startMultiScanPushButton.clicked.connect(self.startMultiScan)
        self.cancelMultiScanPushButton.clicked.connect(self.cancelMultiScan)
        self.laserCheckBox.stateChanged.connect(self.laserCheckboxFunc)
        
        #main
        spectrometerGUI.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(spectrometerGUI)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 678, 22))
        self.menubar.setObjectName("menubar")
        spectrometerGUI.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(spectrometerGUI)
        self.statusbar.setObjectName("statusbar")
        spectrometerGUI.setStatusBar(self.statusbar)

        self.retranslateUi(spectrometerGUI)
        QtCore.QMetaObject.connectSlotsByName(spectrometerGUI)

    def retranslateUi(self, spectrometerGUI):
        _translate = QtCore.QCoreApplication.translate
        spectrometerGUI.setWindowTitle(_translate("spectrometerGUI", "MainWindow"))
        self.connectMonochromatorPushButton.setText(_translate("spectrometerGUI", "Connect Monochromator"))
        self.connectPhotonCounterPushButton.setText(_translate("spectrometerGUI", "Connect Photon Counter"))
        self.scanMinPlainTextEdit.setPlainText(_translate("spectrometerGUI", "528"))
        self.connectLaserArdPushButton.setText(_translate("spectrometerGUI", "Connect Laser"))
        self.laserCheckBox.setText(_translate("spectrometerGUI", "Laser On"))
        self.scanMaxPlainTextEdit.setPlainText(_translate("spectrometerGUI", "726"))
        self.scanStepPlainTextEdit.setPlainText(_translate("spectrometerGUI", "2"))
        self.scanDurationPlainTextEdit.setPlainText(_translate("spectrometerGUI", "4"))
        self.label.setText(_translate("spectrometerGUI", "Min"))
        self.label_2.setText(_translate("spectrometerGUI", "Max"))
        self.label_3.setText(_translate("spectrometerGUI", "Step"))
        self.label_4.setText(_translate("spectrometerGUI", "Step Duration"))
        self.label_5.setText(_translate("spectrometerGUI", "Scans"))
        self.label_6.setText(_translate("spectrometerGUI", "Hardware Connections"))
        self.startScanPushButton.setText(_translate("spectrometerGUI", "Start Scan"))
        self.stopScanPushButton.setText(_translate("spectrometerGUI", "Stop Scan"))
        self.startTimeScanPushButton.setText(_translate("spectrometerGUI", "Start Time Scan"))
        self.setMonochromatorPlainTextEdit.setPlainText(_translate("spectrometerGUI", "400"))
        self.setMonochromatorPushButton.setText(_translate("spectrometerGUI", "Set"))
        self.label_7.setText(_translate("spectrometerGUI", "Monochromator"))
        self.startMultiScanPushButton.setText(_translate("spectrometerGUI", "Start Multi Scan"))
        self.cancelMultiScanPushButton.setText(_translate("spectrometerGUI", "Cancel Scans"))
        self.setNumberMultiPlainTextEdit.setPlainText(_translate("spectrometerGUI", "3"))
        self.label_8.setText(_translate("spectrometerGUI", "Number"))
        
    def startScanFunc(self):
        #create object to hold signal to report it is done
        sds = scanDoneSignal()
        #connect the signal to startScanFunc to start another scan if multiscan
        sds.connectTrigger(self.startScanFunc)
        #trigger the scan starting
        self.spectrometer.startScan(sds)
        print('Started scan.')
        
    def startTimeScanFunc(self):
        self.spectrometer.startTimeScan()
        print('Started timescan.')
        
    def stopScanFunc(self):
        self.spectrometer.stopScan()
        print('Stopped scan.')
        
    def startMultiScan(self):
        self.spectrometer.startMultiScan()
        print('Started multiscan.')
        
    def cancelMultiScan(self):
        self.spectrometer.cancelMultiScan()
        print('Canceled multiscan.')
        
    def laserCheckboxFunc(self):
        if self.laserCheckBox.isChecked():
            self.spectrometer.turnLaserOn()
        else:
            self.spectrometer.turnLaserOff()
          
    def getScanMin(self):
        return float(self.scanMinPlainTextEdit.toPlainText())
    
    def getScanMax(self):
        return float(self.scanMaxPlainTextEdit.toPlainText())

    def getScanStep(self):
        return float(self.scanStepPlainTextEdit.toPlainText())    

    def getScanDuration(self):
        return float(self.scanDurationPlainTextEdit.toPlainText())
    
    def getMultiScanNumber(self):
        return self.setNumberMultiPlainTextEdit.toPlainText()
    
    def updateMonochromatorLCD(self,position):
        self.monochromatorLcdNumber.display(position)
    
    def setMonochromatorPositionFunc(self):
        self.spectrometer.monochromatorGoTo(float(self.setMonochromatorPlainTextEdit.toPlainText()))
        
#object to hold signal that reports on when a scan has completed and 
#triggers another scan for multiscan
class scanDoneSignal(QObject):
    trigger = pyqtSignal()
    
    def connectTrigger(self,startscanfunc):
        self.trigger.connect(startscanfunc)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    spectrometerGUI = QtWidgets.QMainWindow()
    ui = Ui_spectrometerGUI()
    ui.setupUi(spectrometerGUI)
    spectrometerGUI.show()
    sys.exit(app.exec_())

