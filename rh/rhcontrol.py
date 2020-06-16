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
        self.totalFlow = 10
        
        self.pidFlag = False
        
    def assignWindow(self,window):
        #function to gives this object the window object for function calls
        self.window = window
        

    def initMFCs(self):
        #initialize MFCs
        self.dryMFC = MFC('COM7',10)
        self.wetMFC = MFC('COM8',20)
        print('MFCs initialized.')
   
    def initSensor(self):
        #RH sensor
        self.RHsensor = OmegaTRH('COM6')
        print('Sensor initialized.')
        
    def getRH(self):
        rh = self.RHsensor.getRH()
        return rh
        
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
        
        
    def startPID(self):
        self.Kp = 0.14
        self.Ki = 0.0015
        self.Kd = 0
        self.setpoint = self.getWindowSetpoint()
        self.pid = PID(self.Kp,self.Ki,self.Kd,self.setpoint)
        #lower limit wet flow ratio of 0.02
        self.pid.output_limits = (0.02,1)
        
        self.pidFlag = True
        
        #open new thread to run PID control
        thread = threading.Thread(target=self.runPID)
        thread.start()
        
    def runPID(self):
        while self.pidFlag:
            self.setRatio(self.pid(self.getRH()))
            sleep(2)

        
    def stopPID(self):
        self.pidFlag = False
        
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
        
        
        
    