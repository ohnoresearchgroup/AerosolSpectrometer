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
import math

class Spectrometer():
       
    def __init__(self):
        
        self.allscans = {}
        self.alltimescans = {}
        
        self.stopFlag = False
        self.cancelMultiScanFlag = False
        
            
    def assignWindow(self,window):
        self.window = window
            
    def initMonochromator(self):
        #########self.m = Monochromator('COM1')############
        self.m = 'mono' #########delete########
        #######self.monochromatorGoTo(400)#########
        
    def initPhotonCounter(self):
        ######self.pc = PhotonCounter('COM5')#############
        self.pc = 'pc' ##########delete###########
        
    def initLaserArd(self):
        self.l = Laser('COM4')
        
    def startScan(self):
        #for starting one single scan, spins out a new thread and returns
        self.stopFlag = False
        self.currentscan = Scan(self.window.getScanMin(),
                                self.window.getScanMax(),
                                self.window.getScanStep(),
                                int(self.window.getScanDuration()),
                                self)        
        self.allscans[self.currentscan.time] = self.currentscan
        
        #open new thread to handle scan
        thread = threading.Thread(target=self.currentscan.startScan)
        thread.start()
       
    def startTimeScan(self):
        self.stopFlag = False
        self.currentscan = TimeScan(self)
        self.alltimescans[self.currentscan.time] = self.currentscan
        
        #open new thread to handle scan
        thread = threading.Thread(target=self.currentscan.startScan)
        thread.start()
        
    def updateMonochromatorWindow(self,position):
        self.window.updateMonochromatorLCD(position)
        
    def monochromatorGoTo(self,position):
        ##########self.m.goTo(position)################
        self.updateMonochromatorWindow(position)
        
    def stopScan(self):
        self.stopFlag = True
        
        
    def startMultiScan(self):
        #open new thread to handle multi scans?????
        ####threadMulti = threading.Thread(target=self.runMultiScan)
        ####threadMulti.start()
        self.runMultiScan()
        
    def startIndScan(self):
        #for starting each individual scan in multiscan, returns when scan done
        self.stopFlag = False
        self.currentscan = Scan(self.window.getScanMin(),
                                self.window.getScanMax(),
                                self.window.getScanStep(),
                                int(self.window.getScanDuration()),
                                self)        
        self.allscans[self.currentscan.time] = self.currentscan
        self.currentscan.startScan()
        
        
    def runMultiScan(self):
        self.cancelMultiScanFlag == False
        #get number of scans to run
        num = self.window.getMultiScanNumber()
        if num == 'Inf':
            num = math.inf
        else:
            num = int(num)
        
        #while loop for each scan
        index = 0    
        while index < num:
            self.startIndScan()
            print('started scan' + str(index))
            index = index + 1
            #check if cancel scan flag has been set
            if self.cancelMultiScanFlag == True:
                break
               
    def cancelMultiScan(self):
        self.cancelMultiScanFlag = True
     
    def close(self):
        self.pc.close()
        self.m.close()
        self.l.close()