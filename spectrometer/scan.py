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
import time

class Scan():
       
    def __init__(self,m,pc,start,stop,step,duration,spectrometer):       
        #get monochromator and pc objects
        self.m = m
        self.pc = pc
        
        #get scan parameters
        self.start = start
        self.stop = stop
        self.step = step
        self.duration = duration
        
        #get spectrometer object
        self.spectrometer = spectrometer
        
        #calculate wavelengths and initialize arrays for data
        self.wavelengths = np.arange(start,stop+step,step)
        self.counts = []
        self.aves = np.zeros(len(self.wavelengths))
        self.aves[:] = np.nan
        
        #time when called
        self.time = datetime.now().strftime('%Y%m%d_%H%M%S')
        
        #make path for day in spectra folder if needed        
        self.rootdatapath = '/Users/pohno/Desktop/python/spectra/2020'
        self.day = datetime.now().strftime('%Y%m%d')
        self.fullpath = self.rootdatapath + '/' + self.day        
        if not os.path.exists(self.fullpath):
            os.mkdir(self.fullpath)
            
        #create file
        self.file = open(self.fullpath + '/' + self.time + '_scan.txt','w+')
        self.file.write('time\t' + self.time + '\n')
        self.file.write('start\t' + str(self.start) + ' nm\n')
        self.file.write('stop\t' + str(self.stop) + ' nm\n')
        self.file.write('step\t' + str(self.step) + ' nm\n')
        self.file.write('duration\t' + str(self.duration) + ' s\n')
        self.file.write('\n')
        
        title = 'wl\tcounts'
        for i in range(self.duration):
            title = title + '\tpt' + str(i+1)
        title = title + '\n'
        self.file.write(title)
        self.file.close()
            
        #create figure, store it
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(1,1,1)
        self.ax.plot(self.wavelengths, self.aves, 'r-')
        
    def startScan(self):
        self.file = open(self.fullpath + '/' + self.time + '_scan.txt','a')
        for (i,wl) in enumerate(self.wavelengths):
            #go to wavelength
            ################self.m.goTo(wl)#############
            #update spectrometer window
            self.spectrometer.updateMonochromatorWindow(wl)         
            #write wavelength to file
            self.file.write(str(wl))
            
            #initialize array to hold data
            data = np.zeros(self.duration)
            #for each second, get the data
            for (index,value) in enumerate(data):
                #get one data point
                time.sleep(0.5)
                result = 1
                ###########result = self.pc.getData()###############
                # if its nan, execute until gets data point that is a number
                while np.isnan(result):
                    result = self.pc.getData()
                #record data point
                data[index] = result
            #add the mean to aves, write to file
            ave = np.mean(data)
            self.aves[i] = ave
            self.file.write('\t' + str(ave))
            print('Ave = ' + str(ave) + ' c.p.s.')
                                 
            #add the array of data to counts, write to file          
            self.counts.append(data)            
            string = np.array2string(data,separator='\t')[1:][:-1]
            self.file.write('\t' + string + '\n')
            
            #clear the previous lines, replot the updated line
            self.ax.clear()
            self.ax.plot(self.wavelengths, self.aves, 'r-')
            plt.xlabel('Wavelength [nm]')
            plt.ylabel('Intensity [c.p.s.]')
            plt.title(self.time)
            self.fig.canvas.draw()
            self.fig.canvas.flush_events()
        #close the file
        self.file.close()
              
    def stop(self):
        print('Scan stopped.')

            