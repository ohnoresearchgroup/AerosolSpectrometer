#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 16:23:12 2019

@author: pohno
"""

from spectrometer.monochromator import Monochromator
from spectrometer.photoncounter import PhotonCounter
from spectrometer.laser import Laser
from spectrometer.scan import Scan
from spectrometer.timescan import TimeScan
import threading

class Spectrometer():
       
    def __init__(self):
        
        self.allscans = {}
        self.alltimescans = {}
        
            
    def assignWindow(self,window):
        self.window = window
            
    def initMonochromator(self):
        #########self.m = Monochromator('COM1')############
        self.m = 'mono' #########delete########
        
    def initPhotonCounter(self):
        ######self.pc = PhotonCounter('COM5')#############
        self.pc = 'pc' ##########delete###########
        
    def initLaserArd(self):
        self.l = Laser('COM4')
        
    def startScan(self):
        self.currentscan = Scan(self.m,self.pc,
                     self.window.getScanMin(),
                     self.window.getScanMax(),
                     self.window.getScanStep(),
                     int(self.window.getScanDuration()),self)        
        self.allscans[self.currentscan.time] = self.currentscan
        
        #open new thread to handle scan
        thread = threading.Thread(target=self.currentscan.startScan)
        thread.start()
       
    def startTimeScan(self):
        self.currentscan = TimeScan(self.m,self.pc)
        self.alltimescans[self.currentscan.time] = self.currentscan
        self.currentscan.start()
        
    def updateMonochromatorWindow(self,position):
        self.window.updateMonochromatorLCD(position)
        
    def monochromatorGoTo(self,position):
        ##########self.m.goTo(position)################
        self.updateMonochromatorWindow(position)
        
    def stopScan(self):
        self.currentscan.stop()
        
    def startMultScans(self,number):
        for i in range(number):
            self.startScan()

        
    def close(self):
        self.pc.close()
        self.m.close()
        self.l.close()