# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 16:22:44 2020

RHcontrol object that holds RH sensors, two bubbler systems each with two 
MFCs each, and PID feedback control objects that control the two bubbler systems


@author: ESL328
"""

from aerosol.omegaTRH import OmegaTRH
from aerosol.rotronicTRH import RotronicTRH
from aerosol.logRH import LogRH
from aerosol.labjackdac import LabJackDAC
import threading
from lib.PID import PID

class RHcontrol():
       
    def __init__(self):      
        #initialize PID controls with default settings
        self.initFlow1_PID()
        self.initFlow2_PID()
        
        #set active PID control off
        self.pidFlag = False
        

        
    def assignWindow(self,window):
        #function to gives this object the window object for function calls
        self.window = window
        

    def initValveControl(self):
        #initialize LabJack DAC controller for valves
        self.labjack = LabJackDAC()
        
        print('Valve control initialized.')
   
    def initSensors(self):
        #initialize the three RH sensors
        RHsensor1 = OmegaTRH('COM4') #10, dry particles
        #RHsensor2 = RotronicTRH('COM7') #HC particles
        #RHsensor2 = OmegaTRH('COM10') #14 HC particles
        #RHsensor3 = RotronicTRH('COM8') #Sheath flow
        #RHsensor3 = OmegaTRH('COM11') #19 Sheath Flow (SF)
        #self.RHsensors = [RHsensor1,RHsensor2,RHsensor3]
        self.RHsensors = [RHsensor1]
        print('Sensors initialized.')
        
    def getRH(self,sensorNum):
        #function to get RH from sensor
        rh = self.RHsensors[sensorNum].getRH()
        return rh
    
    def getT(self,sensorNum):
        #function to get T from sensor
        t = self.RHsensors[sensorNum].getT()
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
        
    def initFlow1_PID(self):

        
        #tuned at 75 %RH (good at 80, 70, 20, 30)
        self.Flow1_Kp = 1.125
        self.Flow1_Ki = 0.0804
        self.Flow1_Kd = 3.9375
        
        #tuned at 60% RH (good at 60, 50, 40, 30)
        #self.Flow1_Kp = 0.5769
        #self.Flow1_Ki = 0.0412
        #self.Flow1_Kd = 2.01915
        self.Flow1_pid = PID(self.Flow1_Kp,self.Flow1_Ki,self.Flow1_Kd)
        self.Flow1_pid.SetPoint = 0.75
        
    def initFlow2_PID(self):
        self.Flow2_Kp = 0
        self.Flow2_Ki = 0
        self.Flow2_Kd = 0
        
        self.Flow2_pid = PID(self.Flow2_Kp,self.Flow2_Ki,self.Flow2_Kd)
        self.Flow2_pid.SetPoint = 0.75
  
    def setPIDsp(self,sp):
        #check to make sure sp is in range
        if 0 <= sp <= 100:
            #set sheath flow setpoint to 80 if above 80%
            #to avoid condensation in CPC
            limit = 80
            if sp > limit:
                self.Flow1_pid.SetPoint = limit/100
                self.Flow2_pid.SetPoint = limit/100
            else:
                self.Flow1_pid.SetPoint = sp/100
                self.Flow2_pid.SetPoint = sp/100
             
            if 35 < sp < 65:
                self.Flow1_pid.Kp = 0.5769
                self.Flow1_pid.Ki = 0.0412
                self.Flow1_pid.Kd = 2.01915     
            else:
                #divided by 2
                self.Flow1_pid.Kp = 0.5625
                self.Flow1_pid.Ki = 0.0402
                self.Flow1_pid.Kd = 1.969

        else:
            print('SP must be between 0 and 100')
                

    def startPID(self): 
        self.pidFlag = True
        
    def stopPID(self):
        self.pidFlag = False
        
    def setFlow1_Voltage(self,voltage):
        #set voltage for Flow 1
        if 0 <= voltage <= 2:

            self.labjack.writeVoltage(1,voltage)
 
        else:
            print('Ratio must be between 0 and 5')
        
    def setFlow2_Voltage(self,voltage):
        #set voltage for Flow 1
        if 0 <= voltage <= 2:

            self.labjack.writeVoltage(2,voltage)
 
        else:
            print('Ratio must be between 0 and 5')