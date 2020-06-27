# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rhControlGUI.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets

class Ui_RHcontrolGUI(object):
    def setupUi(self, RHcontrolGUI, rhcontrol):
        #give it rhcontrol object
        self.rhcontrol = rhcontrol
        
        #central widget
        RHcontrolGUI.setObjectName("RHcontrolGUI")
        RHcontrolGUI.resize(488, 273)
        self.centralwidget = QtWidgets.QWidget(RHcontrolGUI)
        self.centralwidget.setObjectName("centralwidget")
        
        #connect sensor
        self.connectSensorPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.connectSensorPushButton.setGeometry(QtCore.QRect(20, 40, 131, 51))
        self.connectSensorPushButton.setObjectName("connectSensorPushButton")
        
        #start push button
        self.startPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.startPushButton.setGeometry(QtCore.QRect(350, 30, 113, 32))
        self.startPushButton.setObjectName("startPushButton")
                
        #stop push button
        self.stopPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.stopPushButton.setGeometry(QtCore.QRect(350, 60, 113, 32))
        self.stopPushButton.setObjectName("stopPushButton")
        
        #interval edit
        self.intervalEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.intervalEdit.setGeometry(QtCore.QRect(380, 100, 81, 21))
        self.intervalEdit.setObjectName("intervalEdit")
        self.intervalEdit.insertPlainText('5')
        
        #rh display
        self.rhDisplay = QtWidgets.QLCDNumber(self.centralwidget)
        self.rhDisplay.setGeometry(QtCore.QRect(160, 30, 141, 61))
        self.rhDisplay.setObjectName("rhDisplay")
        
        #connect mfc
        self.connectMFCpushButton = QtWidgets.QPushButton(self.centralwidget)
        self.connectMFCpushButton.setGeometry(QtCore.QRect(20, 150, 131, 51))
        self.connectMFCpushButton.setObjectName("connectMFCpushButton")
         
        #set point check box
        self.setPointcheckBox = QtWidgets.QCheckBox(self.centralwidget)
        self.setPointcheckBox.setGeometry(QtCore.QRect(340, 160, 111, 20))
        self.setPointcheckBox.setObjectName("setPointcheckBox")
             
        #set point edit
        self.setPointEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.setPointEdit.setGeometry(QtCore.QRect(180, 150, 101, 41))
        self.setPointEdit.setObjectName("setPointEdit")
        self.setPointEdit.insertPlainText('30')
 
        #labels
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(200, 10, 60, 16))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(380, 10, 60, 16))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(310, 100, 60, 16))
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(200, 130, 60, 16))
        self.label_4.setObjectName("label_4")
        
        ############signals and slots######
        self.connectSensorPushButton.clicked.connect(self.initSensors)
        self.connectMFCpushButton.clicked.connect(self.initMFCs)
        self.startPushButton.clicked.connect(self.startFunc)
        self.stopPushButton.clicked.connect(self.stopFunc)
        self.setPointEdit.textChanged.connect(self.setPIDsp)
        self.setPointcheckBox.stateChanged.connect(self.spCheckBoxFunc)
        
        #central widget
        RHcontrolGUI.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(RHcontrolGUI)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 488, 22))
        self.menubar.setObjectName("menubar")
        RHcontrolGUI.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(RHcontrolGUI)
        self.statusbar.setObjectName("statusbar")
        RHcontrolGUI.setStatusBar(self.statusbar)

        self.retranslateUi(RHcontrolGUI)
        QtCore.QMetaObject.connectSlotsByName(RHcontrolGUI)
        

    def retranslateUi(self, RHcontrolGUI):
        _translate = QtCore.QCoreApplication.translate
        RHcontrolGUI.setWindowTitle(_translate("RHcontrolGUI", "MainWindow"))
        self.startPushButton.setText(_translate("RHcontrolGUI", "Start"))
        self.setPointcheckBox.setText(_translate("RHcontrolGUI", "PID Control"))
        self.label_3.setText(_translate("RHcontrolGUI", "Interval"))
        self.label.setText(_translate("RHcontrolGUI", "RH"))
        self.label_4.setText(_translate("RHcontrolGUI", "Set Point"))
        self.label_2.setText(_translate("RHcontrolGUI", "Log"))
        self.stopPushButton.setText(_translate("RHcontrolGUI", "Stop"))
        self.connectSensorPushButton.setText(_translate("RHcontrolGUI", "Connect Sensor"))
        self.connectMFCpushButton.setText(_translate("RHcontrolGUI", "Connect MFCs"))

    def initSensors(self):
        self.rhcontrol.initSensors()
    
    def initMFCs(self):
        self.rhcontrol.initMFCs()
        
    def startFunc(self):
        self.rhcontrol.startLog()
        print('Started log.')
        
    def stopFunc(self):
        self.rhcontrol.stopLog()
        print('Stopped log.')
        
    def updateLCD(self,rh):
        self.rhDisplay.display(rh)
        
    def getInterval(self):
        return float(self.intervalEdit.toPlainText())
    
    def getSetpoint(self):
        return float(self.setPointEdit.toPlainText())
    
    def setPIDsp(self):
        self.rhcontrol.setPIDsp(self.getSetpoint())
    
    def spCheckBoxFunc(self):
        if self.setPointcheckBox.isChecked():
            self.rhcontrol.startPID()
        else:
            self.rhcontrol.stopPID()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    RHcontrolGUI = QtWidgets.QMainWindow()
    ui = Ui_RHcontrolGUI()
    ui.setupUi(RHcontrolGUI)
    RHcontrolGUI.show()
    sys.exit(app.exec_())

