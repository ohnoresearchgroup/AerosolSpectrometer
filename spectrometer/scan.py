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

class Scan():
       
    def __init__(self,m,pc,start,stop,step,duration):       
        self.m = m
        self.pc = pc
        
        self.time = datetime.now().strftime('%Y%m%d_%H%M%S')
        self.start = start
        self.stop = stop
        self.step = step
        self.duration = duration
        
        self.wavelengths = np.arange(start,stop+step,step)
        self.counts = []
        self.aves = np.zeros(len(self.wavelengths))
        self.aves[:] = np.nan
        
        #make path for day in spectra folder if needed        
        self.rootdatapath = 'C:\\Users\\ESL328\\Google Drive\\Data\\Spectra\\2020'
        self.day = datetime.now().strftime('%Y%m%d')
        self.fullpath = self.rootdatapath + '\\' + self.day        
        if not os.path.exists(self.fullpath):
            os.mkdir(self.fullpath)

        
    
    def start(self):
        #file for information about the scan and the average counts
        f_ave = open(self.dirpath + '\\' + self.time + '_ave.txt','w+')
        f_ave.write('name\t' + self.name + '\n')
        f_ave.write('time\t' + self.time + '\n')
        f_ave.write('start\t' + str(self.start) + ' nm\n')
        f_ave.write('stop\t' + str(self.stop) + ' nm\n')
        f_ave.write('step\t' + str(self.step) + ' nm\n')
        f_ave.write('duration\t' + str(self.duration) + ' s\n')
        f_ave.write('\n')
        f_ave.write('wl\tcounts\n')
        
        #file to hold all the data
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
                #get one data point
                result = self.pc.getData()
                # if its nan, execute until gets data point that is a number
                while np.isnan(result):
                    result = self.pc.getData()
                #record data point
                data[index] = result
                
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
        
        #close the two files
        f_ave.close()
        f_data.close()
            
        
            