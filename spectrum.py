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

class Spectrum():
       
    def __init__(self,m,pc,name,start,stop,step,duration,path):       
        self.m = m
        self.pc = pc
        
        self.name = name
        self.time = datetime.now().strftime('%Y%m%d_%H%M%S')
        self.start = start
        self.stop = stop
        self.step = step
        self.duration = duration
        self.path = path
        
        self.wavelengths = np.arange(start,stop+step,step)
        self.counts = []
        self.aves = np.zeros(len(self.wavelengths))
        self.aves[:] = np.nan
          
        self.dirpath = self.path + '\\' + self.time
        os.mkdir(self.dirpath)
        
        self.createDetailsFile()
        self.runScan()
        
    def createDetailsFile(self):  
        f_details  = open(self.dirpath + '\\' + self.time +'_details.txt','w')
        f_details.write('name\t' + self.name + '\n')
        f_details.write('time\t' + self.time + '\n')
        f_details.write('start\t' + str(self.start) + ' nm\n')
        f_details.write('stop\t' + str(self.stop) + ' nm\n')
        f_details.write('step\t' + str(self.step) + ' nm\n')
        f_details.write('duration\t' + str(self.duration) + ' s\n')
        f_details.close()
    
    def runScan(self):
        f_ave = open(self.dirpath + '\\' + self.time + '_ave.txt','w+')
        f_data = open(self.dirpath + '\\' + self.time + '_data.txt','w+')
        
        #create figure, store it
        self.fig = plt.figure()
        ax = self.fig.add_subplot(1,1,1)
        ax.plot(self.wavelengths, self.aves, 'r-')

        
        for (i,wl) in enumerate(self.wavelengths):
            #go to wavelength
            self.m.goTo(wl)
            print('Moved to ' + str(wl) + ' nm.')
            
            #write wavelength to file
            f_ave.write(str(wl))
            f_data.write(str(wl))
            
            #initialize array to hold data
            data = np.zeros(self.duration)
            
            #for each second, get the data
            for (index,value) in enumerate(data):
                data[index] = self.pc.getData()
                
            #add the array of data to counts, write to file          
            self.counts.append(data)            
            string = np.array2string(data,separator='\t')[1:][:-1]
            f_data.write('\t' + string + '\n')
            
            #add the mean to aves, write to file
            ave = np.mean(data)
            self.aves[i] = ave
            f_ave.write('\t' + str(ave) + '\n')
            print('Ave = ' + str(ave) + ' c.p.s.')
            
            #clear the previous lines, replot the updated line
            ax.clear()
            ax.plot(self.wavelengths, self.aves, 'r-')
            plt.xlabel('Wavelength [nm]')
            plt.ylabel('Intensity [c.p.s.]')
            plt.title(self.name)
            self.fig.canvas.draw()
            self.fig.canvas.flush_events()
              
        f_ave.close()
        f_data.close()
            
        
            