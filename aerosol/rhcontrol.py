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
from simple_pid import PID

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
        #6/30/2020 settings for humid air flow kp = 0.02, ki = 0.0003, kd = 0.04
        self.Kp = 0.02
        self.Ki = 0.0003
        self.Kd = 0.0004
        self.setpoint = 30
        self.SFpid = PID(self.Kp,self.Ki,self.Kd,self.setpoint)
        #lower limit wet flow ratio of 0.04
        self.SFpid.output_limits = (-1,1)
        
    def initHCPID(self):
        #kp @ 0.6, oscillations at 500 seconds
        #kp = 0.36, ki = 0.00144, kd = 22.5
        self.Kp = 0.6
        self.Ki = 0
        self.Kd = 0
        self.setpoint = 30
        self.HCpid = PID(self.Kp,self.Ki,self.Kd,self.setpoint)
        #lower limit wet flow ratio of 0.04
        self.HCpid.output_limits = (-1,1)
        
    def setPIDsp(self,sp):
        self.HCpid.setpoint = sp
        self.SFpid.setpoint = sp
              
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

        
        
    