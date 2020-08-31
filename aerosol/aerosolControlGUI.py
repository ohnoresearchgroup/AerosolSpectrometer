# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'aerosolControlGUI.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets

class Ui_aerosolControlGUI(object):
    def setupUi(self, AerosolControlGUI, aerosolcontrol):
        #store aerosolcontrol object
        self.aerosolcontrol = aerosolcontrol
        
        #central widget
        AerosolControlGUI.setObjectName("AerosolControlGUI")
        AerosolControlGUI.resize(442, 159)
        self.centralwidget = QtWidgets.QWidget(AerosolControlGUI)
        self.centralwidget.setObjectName("centralwidget")
        
        #atomizer checkbox
        self.atomizerCheck = QtWidgets.QCheckBox(self.centralwidget)
        self.atomizerCheck.setGeometry(QtCore.QRect(30, 50, 121, 41))
        self.atomizerCheck.setObjectName("atomizerCheck")
        
        #cell particles checkbox
        self.cellParticlesCheck = QtWidgets.QCheckBox(self.centralwidget)
        self.cellParticlesCheck.setGeometry(QtCore.QRect(170, 60, 111, 20))
        self.cellParticlesCheck.setObjectName("cellParticlesCheck")
        
        #syringe pump checkbox
        self.syringePumpCheck = QtWidgets.QCheckBox(self.centralwidget)
        self.syringePumpCheck.setGeometry(QtCore.QRect(290, 60, 111, 20))
        self.syringePumpCheck.setObjectName("syringePumpCheck")
        
        #connect arduino pushbutton
        self.connectArdpushButton = QtWidgets.QPushButton(self.centralwidget)
        self.connectArdpushButton.setGeometry(QtCore.QRect(142, 10, 151, 32))
        self.connectArdpushButton.setObjectName("connectArdpushButton")
        
        ###signal and slots###
        self.atomizerCheck.clicked.connect(self.atomizerCheckFunc)
        self.cellParticlesCheck.clicked.connect(self.cellParticlesCheckFunc)
        self.syingePumpCheck.clicked.connect(self.syringePumpCheckFunc)
        self.connectArdpushButton.clicked.connect(self.connectArdFunc)
        
        
        #central widget
        AerosolControlGUI.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(AerosolControlGUI)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 442, 22))
        self.menubar.setObjectName("menubar")
        AerosolControlGUI.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(AerosolControlGUI)
        self.statusbar.setObjectName("statusbar")
        AerosolControlGUI.setStatusBar(self.statusbar)

        self.retranslateUi(AerosolControlGUI)
        QtCore.QMetaObject.connectSlotsByName(AerosolControlGUI)

    def retranslateUi(self, AerosolControlGUI):
        _translate = QtCore.QCoreApplication.translate
        AerosolControlGUI.setWindowTitle(_translate("AerosolControlGUI", "AerosolControlGUI"))
        self.atomizerCheck.setText(_translate("AerosolControlGUI", "Atomizer Valve"))
        self.cellParticlesCheck.setText(_translate("AerosolControlGUI", "Cell Particles"))
        self.syringePumpCheck.setText(_translate("AerosolControlGUI", "Syringe Pump"))
        self.connectArdpushButton.setText(_translate("AerosolControlGUI", "Connect Arduino"))
        
    def atomizerCheckFunc(self):
        if self.atomizerCheck.isChecked():
            self.aerosolcontrol.turnOnAtomizer()
        else:
            self.aerosolcontrol.turnOffAtomizer()
            
    def cellParticlesCheckFunc(self):
        if self.cellParticlesCheck.isChecked():
            self.aerosolcontrol.turnOnCellParticles()
        else:
            self.aerosolcontrol.turnOnCellParticles()
            
    def syringePumpCheckFunc(self):
        if self.syringePumpCheck.isChecked():
            self.aerosolcontrol.turnOnSyringePump()
        else:
            self.aerosolcontrol.turnOffSyringePump()
            
    def connectArdFunc(self):
        self.aerosolcontrol.connectArd()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AerosolControlGUI = QtWidgets.QMainWindow()
    ui = Ui_aerosolControlGUI()
    ui.setupUi(AerosolControlGUI)
    AerosolControlGUI.show()
    sys.exit(app.exec_())

