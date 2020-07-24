#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 17:22:45 2019

@author: pohno
"""
import matplotlib.pyplot as plt
from datetime import datetime
import os

class TimeScan():
       
    def __init__(self,spectrometer):       
        #photon counter to get data and spectrometer object
        self.spectrometer = spectrometer
        self.pc = self.spectrometer.pc
        
        #time triggered
        self.time = datetime.now().strftime('%Y%m%d_%H%M%S')
        
        #make path for day in spectra folder if needed        
        self.rootdatapath = 'C:\\Users\\ESL328\\Google Drive\\Data\\Spectra\\2020'
        self.day = datetime.now().strftime('%Y%m%d')
        self.fullpath = self.rootdatapath + '\\' + self.day        
        if not os.path.exists(self.fullpath):
            os.mkdir(self.fullpath)
         
        #get monochromator position
        self.position = self.spectrometer.m.position
        
        #create file
        self.file = open(self.fullpath + '\\' + self.time + '_timescan.txt','w+')
        self.file.write('time\t' + self.time + '\n')
        self.file.write('position\t' + str(self.position) + '\n')
        self.file.write('\n')
        self.file.write('time\tcounts\n')
        self.file.close()
        
        self.times = []
        self.counts = []

        # Create figure for plotting
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(1, 1, 1)
        self.ax.plot(self.times,self.counts)
        plt.show()
        plt.xlabel('Time')
        plt.ylabel('Intensity [c.p.s.]')
        plt.title(self.time)
        
        self.stop = False
 
        self.timeIndex = 1
    
    def startScan(self):
        
        while self.spectrometer.stopFlag == False:
            result = self.pc.getData()
            
            self.times.append(self.timeIndex)
            self.counts.append(result)
                   
            #write to file
            self.file = open(self.fullpath + '\\' + self.time + '_timescan.txt','a')
            self.file.write(str(self.timeIndex) + '\t' + str(result) + '\n')
            self.file.close()
        
            #clear the previous lines, replot the updated line
            self.ax.clear()
            self.ax.plot(self.times, self.counts)
            self.fig.canvas.draw()
            self.fig.canvas.flush_events()
            plt.xlabel('Time')
            plt.ylabel('Intensity [c.p.s.]')
            plt.title(self.time)

            self.timeIndex = self.timeIndex + 1
        
            