#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 17:36:51 2020

@author: pohno
"""

import sys
from rhControlWindow import Ui_rhControlMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets

app = QtWidgets.QApplication(sys.argv)
rhControlMainWindow = QtWidgets.QMainWindow()
ui = Ui_rhControlMainWindow()
ui.setupUi(rhControlMainWindow)
rhControlMainWindow.show()
sys.exit(app.exec_())
