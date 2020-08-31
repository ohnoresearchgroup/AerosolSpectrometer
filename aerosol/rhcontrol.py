# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 16:22:44 2020

RHcontrol object that holds RH sensors, two bubbler systems each with two 
MFCs each, and PID feedback control objects that control the two bubbler systems


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
        #set total flow rate for each bubbler system
        self.HCtotalFlow = 5
        #sheath flow = 7 if using both, 3.5 if using 1
        self.SFtotalFlow = 3.5
        
        #initialize PID controls with default settings
        self.initHCPID()
        self.initSFPID()
        
        #set active PID control off
        self.pidFlag = False
        
        #initialize DAC controller for MKS MFCs
        self.ncddac = NCDDAC('COM13')
        
    def assignWindow(self,window):
        #function to gives this object the window object for function calls
        self.window = window
        

    def initMFCs(self):
        #initialize MFCs for each of the two bubbler systems
        #HC is humidity control for nafion dryer for particles
        #SF is sheath flow for SMPS
        self.HCdryMFC = MFCmks(self.ncddac,1)
        self.HCwetMFC = MFCmks(self.ncddac,2)
        
        self.SFdryMFC = MFCmks(self.ncddac,4)
        self.SFwetMFC = MFCmks(self.ncddac,3)
        print('MFCs initialized.')
   
    def initSensors(self):
        #initialize the three RH sensors
        RHsensor1 = OmegaTRH('COM6') #10, dry particles
        RHsensor2 = OmegaTRH('COM10') #14 HC particles
        RHsensor3 = OmegaTRH('COM11') #19 Sheath Flow (SF)
        self.RHsensors = [RHsensor1,RHsensor2,RHsensor3]
        print('Sensors initialized.')
        
    def getRH(self,sensorNum):
        #function to get RH from sensor
        rh = self.RHsensors[sensorNum-1].getRH()
        return rh
    
    def getT(self,sensorNum):
        #function to get T from sensor
        t = self.RHsensors[sensorNum-1].getT()
        return t
        
    def updateWindow(self,rh):
        #update the window with the RH
        self.window.updateLCD(rh)
        
    def startLog(self):
        #intialize a new log object that gets and save the data
        self.log = LogRH(self.window.getInterval(),self)
        
        #open new thread to handle log
        thread = threading.Thread(target=self.log.start)
        thread.start()
        
    def stopLog(self):
        #stop the log
        self.log.stop()
        
    def initSFPID(self):
        #7/20/20
        #kp - 0.01, ki = 0.00012, kd = 0.45 (no windup) matches at low, oscillates at high
        #7/22/20 kp = 0.021, ki = 0.00014, kd = 0.78, windup +- 0.6 (-0.1 to 1.1)
        self.SFKp = 0.021
        self.SFKi = 0.00014
        self.SFKd = .78
        self.SFpid = PID(self.SFKp,self.SFKi,self.SFKd)
        self.SFpid.SetPoint = 75
        
    def initHCPID(self):
        #7/20/20
        #kp = 0.18, ki = 0.0007, kd = 11 (no windup), works at low, oscillates at high
        #trying with no derivative because time constant is so slow and change is discrete
        #kp = 0.13, ki = 0.00016, kd = 0 eventually stabilizes but takes long time 
        #for oscillations to damp down at sp = 75
        #kp = 0.13, ki = 0.00016, kd = 3 works sp 68, 75, oscillates at 80
        #7/23/2020: p=0.13,i=0.00016,d=3 at sp<75, p=0.065,i=0.00008,d=1.5 sp>=75
        #windup = =- 0.6 (-0.1 to 1.1)
        #8/26/20, switching sensor to be after fluorescence cell/HEPA:
        #Kp = 0.2, Ki = 0.0001, Kd = 10 works well, but small changes after cell
        #lead to oscillations before cell as it corrects, probably best to focus PID 
        #after cell 
        self.HCKp = 0.065
        self.HCKi = 0.00008
        self.HCKd = 1.5
        self.HCpid = PID(self.HCKp,self.HCKi,self.HCKd)
        self.HCpid.SetPoint = 75
  
    def setPIDsp(self,sp):
        #check to make sure sp is in range
        if 0 <= sp <= 100:
            self.SFpid.SetPoint = sp
            self.HCpid.SetPoint = sp
            #adjust PID settings for humidity control nafion dryer
            if sp >= 70:
                self.HCpid.Kp = 0.065
                self.HCpid.Ki = 0.00008
                self.HCpid.Kd = 1.5
            elif sp < 70:
                self.HCpid.Kp = 0.13
                self.HCpid.Ki = 0.00016
                self.HCpid.Kd = 3
        else:
            print('SP must be between 0 and 100')
                

    def startPID(self): 
        self.pidFlag = True
        
    def stopPID(self):
        self.pidFlag = False
        
    def setHCRatio(self,ratio):
        #set wet ratio of HC, must be between 0.04 and 1
        if 0.04 <= ratio <= 1:
            #calculate wet flows and dry flows
            wetFlow = round(ratio*self.HCtotalFlow,3)
            dryFlow = round((1-ratio)*self.HCtotalFlow,3)
            
            #set wetflows and dry flows
            self.HCdryMFC.setSP(dryFlow)
            self.HCwetMFC.setSP(wetFlow)
        else:
            print('Ratio must be between 0.04 and 1')
        
    def setSFRatio(self,ratio):
        #set wet ratio of SF, must be between 0.04 and 1
        if 0.04 <= ratio <= 1:
            #calculate wet flows and dry flows
            wetFlow = round(ratio*self.SFtotalFlow,3)
            dryFlow = round((1-ratio)*self.SFtotalFlow,3)
            
            #set wet flows and dry flows
            self.SFdryMFC.setSP(dryFlow)
            self.SFwetMFC.setSP(wetFlow)
        else:
            print('Ratio must be between 0.04 and 1')