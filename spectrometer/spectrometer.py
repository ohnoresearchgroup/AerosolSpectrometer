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

class Spectrometer():
       
    def __init__(self):
        
        self.allscans = {}
        self.alltimescans = {}
        
            
    def assignWindow(self,window):
        self.window = window
            
    def initMonochromator(self):
        self.m = Monochromator('COM1')
        
    def initPhotonCounter(self):
        self.pc = PhotonCounter('COM5')
        
    def initLaserArd(self):
        self.l = Laser('COM4')
        
    def startScan(self):
        scan = Scan(self.m,self.pc,
                     self.window.getScanMin(),
                     self.window.getScanMax(),
                     self.window.getScanInterval(),
                     self.window.getScanDuration())
        
        self.allscans[scan.time] = scan
        self.currentscan = scan
        scan.start()
        
    def startTimeScan(self):
        ts = TimeScan(self.m,self.pc)
        self.alltimescans[ts.time] = ts
        self.currentscan = ts
        
    def stopScan(self):
        self.currentscan.stop()
        
    def startMultScans(self,number):
        for i in range(number):
            self.startScan()

        
    def close(self):
        self.pc.close()
        self.m.close()
        self.l.close()