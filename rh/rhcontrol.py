# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 16:22:44 2020

@author: ESL328
"""

from rh.mfc import MFC
from rh.omegaTRH import OmegaTRH
from rh.logRH import LogRH
import threading
from simple_pid import PID
from time import sleep

class RHcontrol():
       
    def __init__(self):      
        #set total flow rate
        self.totalFlow = 5
        
        #initialize PID control with Ki,Kp,Kd
        self.initPID()
        self.pidFlag = False
        
    def assignWindow(self,window):
        #function to gives this object the window object for function calls
        self.window = window
        

    def initMFCs(self):
        #initialize MFCs
        self.dryMFC = MFC('COM7',10)
        self.wetMFC = MFC('COM8',20)
        print('MFCs initialized.')
   
    def initSensors(self):
        #RH sensor
        RHsensor1 = OmegaTRH('COM6')
        RHsensor2 = OmegaTRH('COM10')
        RHsensor3 = OmegaTRH('COM11')
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
        
    def initPID(self):
        #function to call everytime you set new setpoint
        #kp @ 0.3 gives oscillations with 150 second period
        #before 6/27/2020 used 0.18, 0.0024, 6.75
        #6/27/2020 set at 0.09,0.0012,3
        self.Kp = 0.09
        self.Ki = 0.0012
        self.Kd = 3
        self.setpoint = 30
        self.pid = PID(self.Kp,self.Ki,self.Kd,self.setpoint)
        #lower limit wet flow ratio of 0.02
        self.pid.output_limits = (0.02,1)
        
    def setPIDsp(self,sp):
        self.pid.setpoint = sp
              
    def startPID(self): 
        self.pidFlag = True
        
    def stopPID(self):
        self.pidFlag = False
        
    def setRatio(self,ratio):
        wetFlow = ratio*self.totalFlow
        dryFlow = (1-ratio)*self.totalFlow

        self.dryMFC.setSP(dryFlow)
        self.wetMFC.setSP(wetFlow)    
        
    def setTotalFlowRate(self,flowRate):
        self.totalFlow = flowRate
        #print('TotalFlow = ',str(flowRate), 'LPM')
        
    def getTotalFlowRate(self):
        print('TotalFlow = ',str(self.totalFlow), 'LPM')
        
        
        
    