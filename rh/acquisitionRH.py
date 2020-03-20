#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 11:28:19 2020

@author: pohno
"""

import random
from datetime import datetime
import os
import matplotlib.pyplot as plt
from lib.repeattimer import RepeatTimer

class AcquisitionRH():    
    def __init__(self,interval,rhcontrol):
        self.interval = interval
        self.rhcontrol = rhcontrol
        
        #create timer to trigger RH reading
        self.timer = RepeatTimer(interval, self.getRHdata)  
        
        #make path for day in RH folder if needed
        self.rootdatapath = '/Users/pohno/Desktop/python/rh/2020'
        self.day = datetime.now().strftime('%Y%m%d')
        self.fullpath = self.rootdatapath + '/' + self.day    
        if not os.path.exists(self.fullpath):
            os.makedirs(self.fullpath)
            
            
        self.time = datetime.now().strftime('%Y%m%d_%H%M%S')
        #file name after time started
        self.file = open(self.fullpath + '/' + self.time + '.txt','w+')
        self.file.write('starttime\t' + self.time + '\n')
        self.file.write('interval\t' + str(self.interval) + ' s\n')
        self.file.write('\n')
        self.file.write('time\tRH\n')
        self.file.close()

        self.times = []
        self.rhs = []

        # Create figure for plotting
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(1, 1, 1)
        self.ax.plot(self.times,self.rhs)
        plt.show()
        plt.xlabel('Time')
        plt.ylabel('RH [%]')
        plt.title(self.time)
              
    def start(self):
        self.timer.start()
        
    def stop(self):
        self.timer.cancel()
                
    def getRHdata(self):
        #get new data and append
        time = datetime.now().strftime('%Y_%m%d_%H:%M:%S')
        rh = self.rhcontrol.getRH()   
        
        self.times.append(time)
        self.rhs.append(rh)
        
        #write to file
        self.file = open(self.fullpath + '/' + self.time + '.txt','a')
        self.file.write(time + '\t' + str(rh) + '\n')
        self.file.close()
        
        #clear the previous lines, replot the updated line
        self.ax.clear()
        self.ax.plot(self.times, self.rhs)
        self.fig.canvas.draw()
        self.fig.canvas.flush_events()
        plt.xlabel('Time')
        plt.ylabel('RH [%]')
        plt.title(self.time)
        
        #update the GUI
        self.rhcontrol.updateWindow(rh)
        