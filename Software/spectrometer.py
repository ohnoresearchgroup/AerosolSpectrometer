#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 16:23:12 2019

@author: pohno
"""

from monochromator import Monochromator
from photoncounter import PhotonCounter
from spectrum import Spectrum

class Spectrometer():
       
    def __init__(self):
        self.m = Monochromator('COM5')
        self.pc = PhotonCounter('COM4')
        
        self.scanrange = (400,700,10)
        self.duration = 10
        self.allscans = {}
        
       
    def startSpectrum(self,name):
        sp = Spectrum(self.m,self.pc,name,
                     self.scanrange[0],self.scanrange[1],self.scanrange[2],
                     self.duration)
        
        self.allscans[sp.time] = sp
        
    def getScanRange(self):
        print(self.scanrange)
        
    def setScanRange(self,scanrange):
        self.range = scanrange
        
    def getDuration(self):
        print(self.duration)
        
    def setDuration(self):
        self.duration = duration