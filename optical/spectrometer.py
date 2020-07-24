#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 16:23:12 2019

@author: pohno
"""

from optical.monochromator import Monochromator
from optical.photoncounter import PhotonCounter
from optical.laser import Laser
from optical.scan import Scan
from optical.timescan import TimeScan
import threading
import math


class Spectrometer():
       
    def __init__(self):
        self.stopFlag = False
        
        self.multiScanFlag = False
        self.multiScanIndex = 1
        self.multiScanNumber = 1
        
            
    def assignWindow(self,window):
        self.window = window
            
    def initMonochromator(self):
        self.m = Monochromator('COM1')
        self.monochromatorGoTo(400)
        
    def initPhotonCounter(self):
        self.pc = PhotonCounter('COM5')
        
    def initLaserArd(self):
        self.l = Laser('COM4')
        
    def turnLaserOn(self):
        self.l.turnOn()
        
    def turnLaserOff(self):
        self.l.turnOff()
        
    def startScan(self,sds):
        #object that holds signal for when scan is done
        self.sds = sds
        #sets flag for stopping scan in middle to false
        self.stopFlag = False
        #initializes scan
        self.currentscan = Scan(self.window.getScanMin(),
                                self.window.getScanMax(),
                                self.window.getScanStep(),
                                int(self.window.getScanDuration()),
                                self,self.sds)        
        
        #spins out thread to run scan
        thread = threading.Thread(target=self.currentscan.startScan)
        thread.start()
       
    def startTimeScan(self):
        self.stopFlag = False
        self.currentscan = TimeScan(self)
        
        #open new thread to handle scan
        thread = threading.Thread(target=self.currentscan.startScan)
        thread.start()
        
    def updateMonochromatorWindow(self,position):
        self.window.updateMonochromatorLCD(position)
        
    def monochromatorGoTo(self,position):
        self.m.goTo(position)
        self.updateMonochromatorWindow(position)
        
    def stopScan(self):
        self.stopFlag = True
                
    def startMultiScan(self):
        self.multiScanFlag = True
        self.multiScanIndex = 1
        #get either number of scans or set it to infinite from GUI
        num = self.window.getMultiScanNumber()
        if num == 'Inf':
            num = math.inf
        else:
            num = int(num)
        self.multiScanNumber = num
        
        #calls function to start first scan, will trigger more scans at the end
        #of each individual scan
        self.window.startScanFunc()
           
    def cancelMultiScan(self):
        self.multiScanFlag = False