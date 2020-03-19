#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 11:28:19 2020

@author: pohno
"""

from repeattimer import RepeatTimer
import random
from datetime import datetime
import os
import matplotlib.pyplot as plt
import matplotlib.animation as animation

class AcquisitionRH():
    
    def __init__(self,interval,window):
        self.interval = interval
        self.window = window
        
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
        self.f = open(self.fullpath + '/' + self.time + '.txt','w+')
        self.f.write('starttime\t' + self.time + '\n')
        self.f.write('interval\t' + str(self.interval) + ' s\n')
        self.f.write('\n')
        self.f.write('time\tRH\n')
        self.f.close()

        # Create figure for plotting
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(1, 1, 1)
        # Set up plot to call animate() function periodically
        self.ani = animation.FuncAnimation(self.fig, self.animateFig, interval=1000)
        plt.show()
        
        
        self.times = []
        self.rhs = []
        
    def start(self):
        self.timer.start()
        
    def stop(self):
        self.timer.cancel()
        
        
    def getRHdata(self):
        time = datetime.now().strftime('%Y_%m%d_%H:%M:%S')
        rh = round(random.random(),3)
        
        self.times.append(time)
        self.rhs.append(rh)
           
        self.f = open(self.fullpath + '/' + self.time + '.txt','a')
        self.f.write(time + '\t' + str(rh) + '\n')
        self.f.close()
        self.window.updateLCD(rh)
        
    def animateFig(self,i):
        # Draw x and y lists
        self.ax.clear()
        self.ax.plot(self.times,self.rhs)

        # Format plot
        plt.xticks(rotation=45, ha='right')
        plt.subplots_adjust(bottom=0.30)
        plt.title('TMP102 Temperature over Time')
        plt.ylabel('Temperature (deg C)')
            
        