#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 16:23:12 2019

@author: pohno
"""

from monochromator import Monochromator
from photoncounter import PhotonCounter
from laser import Laser
from spectrum import Spectrum

import os
from datetime import datetime

class Spectrometer():
       
    def __init__(self):
        self.m = Monochromator('COM1')
        self.pc = PhotonCounter('COM3')
        self.l = Laser('COM4')
        self.scanrange = (400,700,10)
        self.duration = 10
        self.allscans = {}
        
        
        self.rootdatapath = 'C:\\Users\\martin_lab\\Documents\\Data'
        self.day = datetime.now().strftime('%Y%m%d')
        self.fullpath = self.rootdatapath + '\\' + self.day 
        
        if not os.path.exists(self.fullpath):
            os.mkdir(self.fullpath)
        
       
    def startSpectrum(self,name):
        sp = Spectrum(self.m,self.pc,name,
                     self.scanrange[0],self.scanrange[1],self.scanrange[2],
                     self.duration,
                     self.fullpath)
        
        self.allscans[sp.time] = sp
        
    def getScanRange(self):
        print(self.scanrange)
        
    def setScanRange(self,scanrange):
        self.scanrange = scanrange
        
    def getDuration(self):
        print(self.duration)
        
    def setDuration(self,duration):
        self.duration = duration
        
    def close(self):
        self.pc.close()
        self.m.close()
        self.l.close()