#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 17:22:45 2019

@author: pohno
"""
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
import os

class TimeScan():
       
    def __init__(self,m,pc,name,duration,path):       
        self.m = m
        self.pc = pc
        
        self.name = name
        self.time = datetime.now().strftime('%Y%m%d_%H%M%S')
        self.duration = duration
        self.path = path
          
        self.dirpath = self.path + '\\' + self.time
        os.mkdir(self.dirpath)
        
        self.runScan()
        
    
    def runScan(self):
        #file for information about the scan and the average counts
        f = open(self.dirpath + '\\' + self.time + '_ave.txt','w+')
        f.write('name\t' + self.name + '\n')
        f.write('time\t' + self.time + '\n')
        f.write('duration\t' + str(self.duration) + ' s\n')
        f.write('\n')
        f.write('time\tcounts\n')

        
        time = np.arange(self.duration)
        counts = np.zeros(self.duration)
        
        #create figure, store it
        fig = plt.figure()
        ax = fig.add_subplot(1,1,1)
        ax.plot(time, counts, 'r-')
        
        #for each second, get the data
        for (index,value) in enumerate(counts):
                #get one data point
                result = self.pc.getData()
                # if its nan, execute until gets data point that is a number
                while np.isnan(result):
                    result = self.pc.getData()
                #record data point
                counts[index] = result
                
                #clear the previous lines, replot the updated line
                ax.clear()
                ax.plot(time, counts, 'r-')
                plt.xlabel('Time')
                plt.ylabel('Intensity [c.p.s.]')
                plt.title('Alignment')
                fig.canvas.draw()
                fig.canvas.flush_events()
        
                f.write(str(index))
                f.write('\t' + str(result) + '\n')

        f.close()         
        
            