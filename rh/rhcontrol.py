# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 16:22:44 2020

@author: ESL328
"""

from rh.mfc import MFC
from rh.omegaTRH import OmegaTRH
from rh.acquisitionRH import AcquisitionRH

class RHcontrol():
       
    def __init__(self):      
        #set total flow rate
        self.totalFlow = 10
        
    def assignWindow(self,window):
        #function to gives this object the window object for function calls
        self.window = window
        

    def initMFCs(self):
        #initialize MFCs
        #self.dryMFC = MFC('COM7',10)
        #self.wetMFC = MFC('COM8',20)
        print('MFCs initialized.')
   
    def initSensor(self):
        #RH sensor
        #self.RHsensor = OmegaTRH('COM6')
        print('Sensor initialized.')
        
    def getRH(self):
        rh = self.RHsensor.getRH()
        print('RH =',rh)
        
    def updateWindow(self,rh):
        self.window.updateLCD(rh)
        
    def startAcquisition(self):
        self.acq = AcquisitionRH(self.window.getInterval(),self)
        self.acq.start()
        
    def stopAcquisition(self):
        self.acq.stop()
        
    def setRatio(self,ratio):
        wetFlow = ratio*self.totalFlow
        dryFlow = (1-ratio)*self.totalFlow
        
        print('Dry:',str(self.dryMFC.setSP(dryFlow)),'LPM')
        print('Wet:',str(self.wetMFC.setSP(wetFlow)),'LPM')        
        
    def setTotalFlowRate(self,flowRate):
        self.totalFlow = flowRate
        print('TotalFlow = ',str(flowRate), 'LPM')
        
    def getTotalFlowRate(self):
        print('TotalFlow = ',str(self.totalFlow), 'LPM')
        
        
        
    