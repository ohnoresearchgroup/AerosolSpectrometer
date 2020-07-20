# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 16:22:44 2020

@author: ESL328
"""

from mfcmks import MFCmks
from omegaTRH import OmegaTRH
from logRH import LogRH
from ncddac import NCDDAC
import threading
from PID import PID

class RHcontrol():
       
    def __init__(self):      
        #set total flow rate
        self.HCtotalFlow = 5
        self.SFtotalFlow = 7
        
        #initialize PID control with Ki,Kp,Kd
        self.initHCPID()
        self.initSFPID()
        
        self.pidFlag = False
        
        self.ncddac = NCDDAC('COM13')
        
    def assignWindow(self,window):
        #function to gives this object the window object for function calls
        self.window = window
        

    def initMFCs(self):
        #initialize MFCs
        self.HCdryMFC = MFCmks(self.ncddac,1)
        self.HCwetMFC = MFCmks(self.ncddac,2)
        
        self.SFdryMFC = MFCmks(self.ncddac,4)
        self.SFwetMFC = MFCmks(self.ncddac,3)
        print('MFCs initialized.')
   
    def initSensors(self):
        #RH sensor
        RHsensor1 = OmegaTRH('COM6') #10, dry particles
        RHsensor2 = OmegaTRH('COM10') #14 HC particles
        RHsensor3 = OmegaTRH('COM11') #19 Sheath Flow (SF)
        self.RHsensors = [RHsensor1,RHsensor2,RHsensor3]
        print('Sensors initialized.')
        
    def getRH(self,sensorNum):
        rh = self.RHsensors[sensorNum-1].getRH()
        return rh
    
    def getT(self,sensorNum):
        t = self.RHsensors[sensorNum-1].getT()
        return t
        
    def updateWindow(self,rh):
        self.window.updateLCD(rh)
        
    def getWindowSetpoint(self):
        return self.window.getSetpoint()
        
    def startLog(self):
        self.log = LogRH(self.window.getInterval(),self)
        
        #open new thread to handle log
        thread = threading.Thread(target=self.log.start)
        thread.start()
        
    def stopLog(self):
        self.log.stop()
        
    def initSFPID(self):
        #7/15/2020 kp @0.1, oscillating with period 240 seconds
        #kp = 0.045, ki = 0.0005, kd = 1.8. works well at high RH but oscillating at low
        self.SFKp = 0.01
        self.SFKi = 0.00012
        self.SFKd = 0.45
        self.SFsetpoint = 30
        self.SFpid = PID(self.SFKp,self.SFKi,self.SFKd)
        self.SFpid.SetPoint = 30
        
    def initHCPID(self):
        #kp @ 0.6, oscillations at 500 seconds
        #kp = 0.36, ki = 0.00144, kd = 22.5
        self.HCKp = 0.18
        self.HCKi = 0.0007
        self.HCKd = 11
        self.HCsetpoint = 30
        self.HCpid = PID(self.HCKp,self.HCKi,self.HCKd)
        self.HCpid.SetPoint = 30
  
    def setPIDsp(self,sp):
        self.HCpid.SetPoint = sp
        self.SFpid.SetPoint = sp
              
    def startPID(self): 
        self.pidFlag = True
        
    def stopPID(self):
        self.pidFlag = False
        
    def setHCRatio(self,ratio):
        wetFlow = round(ratio*self.HCtotalFlow,3)
        dryFlow = round((1-ratio)*self.HCtotalFlow,3)

        self.HCdryMFC.setSP(dryFlow)
        self.HCwetMFC.setSP(wetFlow)    
        
    def setSFRatio(self,ratio):
        wetFlow = round(ratio*self.SFtotalFlow,3)
        dryFlow = round((1-ratio)*self.SFtotalFlow,3)

        self.SFdryMFC.setSP(dryFlow)
        self.SFwetMFC.setSP(wetFlow)  

        
        
    