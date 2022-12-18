#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 11:28:19 2020

@author: pohno
"""

from datetime import datetime
import os
import matplotlib.pyplot as plt
from lib.repeattimer import RepeatTimer
import numpy as np

class LogRH():    
    def __init__(self,interval,rhcontrol):
        self.interval = interval
        self.rhcontrol = rhcontrol
        
        #create timer to trigger RH reading
        self.timer = RepeatTimer(interval, self.getRHdata)  
        
        #make path for day in RH folder if needed
        self.rootdatapath = 'C:\\Users\\csmpeo1\\OneDrive\\RHLogs\\2022'
        self.day = datetime.now().strftime('%Y%m%d')
        self.fullpath = os.path.join(self.rootdatapath, self.day)    
        if not os.path.exists(self.fullpath):
            os.makedirs(self.fullpath)
            
        #time when called
        self.time = datetime.now().strftime('%Y%m%d_%H%M%S')
        
        #file name after time started
        self.file = open(self.fullpath + '\\' + self.time + '.txt','w+')
        self.file.write('starttime\t' + self.time + '\n')
        self.file.write('interval\t' + str(self.interval) + ' s\n')
        self.file.write('\n')
        self.file.write('time\ts1_RH\ts1_T\ts2_RH\ts2_T\ts3_RH\ts3_T\n')
        self.file.close()

        self.times = []
        
        self.rhs = [[],[],[]]
        self.ts = [[],[],[]]


        # Create figure for plotting
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(1, 1, 1)
        self.ax.plot(self.times,self.rhs[0])
        self.ax.plot(self.times,self.rhs[1])
        self.ax.plot(self.times,self.rhs[2])
        plt.show()
        plt.xlabel('Time')
        plt.ylabel('RH [%]')
        plt.title(self.time)
              
    def start(self):
        self.timer.start()
        
    def stop(self):
        self.timer.cancel()
                
    def getRHdata(self):
        #get new data
        currtime = datetime.now()
        
        currRHs = np.zeros(3)
        currTs = np.zeros(3)
        for i in range(1):
            currRHs[i] = self.rhcontrol.getRH(i)
            currTs[i] = self.rhcontrol.getT(i)

        #append new data
        self.times.append(currtime)
        
        for i in range(3):
            self.rhs[i].append(currRHs[i])
            self.ts[i].append(currTs[i])
        
        #write to file
        self.file = open(self.fullpath + '\\' + self.time + '.txt','a')
        
        string = ('\t' + str(currRHs[0]) + '\t' + str(currTs[0]) + 
                  '\t' + str(currRHs[1]) + '\t' + str(currTs[1]) +
                  '\t' + str(currRHs[2]) + '\t' + str(currTs[2]))
        self.file.write(currtime.strftime('%Y-%m-%dT%H:%M:%S') + string + '\n')
        self.file.close()
        
        #clear the previous lines, replot the updated line
        self.ax.clear()
        self.ax.plot(self.times, self.rhs[0])
        self.ax.plot(self.times, self.rhs[1])
        self.ax.plot(self.times, self.rhs[2])
        self.fig.canvas.draw()
        self.fig.canvas.flush_events()
        plt.xlabel('Time')
        plt.ylabel('RH [%]')
        #plt.legend()
        plt.title(self.time)
        
        #update the GUI
        self.rhcontrol.updateWindow(currRHs[0])
        
        #if PID control is enabled
        if self.rhcontrol.pidFlag:

            #calculate pid output
            self.rhcontrol.Flow1_pid.update(currRHs[0]/100)
            Flow1_controlVoltage = 1-self.rhcontrol.Flow1_pid.output
            self.rhcontrol.Flow2_pid.update(currRHs[1]/100)
            Flow2_controlVoltage = 1-self.rhcontrol.Flow2_pid.output
            
            #make sure it is between 0 and 1 and add it to setpoint
            Flow1_controlVoltage = max(0,min(Flow1_controlVoltage,1))
            Flow2_controlVoltage = max(0,min(Flow2_controlVoltage,1))
            
            #set new process variable
            self.rhcontrol.setFlow1_Voltage(Flow1_controlVoltage)
            print('flow 1 voltage =',Flow1_controlVoltage, ' ',currRHs[0])
            self.rhcontrol.setFlow2_Voltage(Flow2_controlVoltage)
            print('flow 2 voltage =',Flow2_controlVoltage, ' ',currRHs[1])
            
        
        