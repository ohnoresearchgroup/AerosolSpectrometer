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

class RHacquisition():
       
    def __init__(self,name,sensor,path):       

        
        self.name = name
        self.time = datetime.now().strftime('%Y%m%d_%H%M%S')

        self.path = path
        
        self.times = []
        self.RHs = []

          
        self.dirpath = self.path + '\\' + self.time
        os.mkdir(self.dirpath)
        
        self.runAcq()
        
    
    def runAcq(self):
        #file for information about the scan and the average counts
        f_ave = open(self.dirpath + '\\' + self.time + '_RH.txt','w+')
        f_ave.write('name\t' + self.name + '\n')
        f_ave.write('time\t' + self.time + '\n')
        f_ave.write('\n')
        f_ave.write('time\tRH\n')
        
        #create figure, store it
        self.fig = plt.figure()
        ax = self.fig.add_subplot(1,1,2)
        ax.plot(self.times, self.RHs, 'r-')

        
#        for (i,wl) in enumerate(self.wavelengths):
#            #go to wavelength
#            self.m.goTo(wl)
#            print('Moved to ' + str(wl) + ' nm.')
#            
#            #write wavelength to file
#            f_ave.write(str(wl))
#            f_data.write(str(wl))
#            
#            #initialize array to hold data
#            data = np.zeros(self.duration)
#            
#            #for each second, get the data
#            for (index,value) in enumerate(data):
#                #get one data point
#                result = self.pc.getData()
#                # if its nan, execute until gets data point that is a number
#                while np.isnan(result):
#                    result = self.pc.getData()
#                #record data point
#                data[index] = result
#                
#            #add the array of data to counts, write to file          
#            self.counts.append(data)            
#            string = np.array2string(data,separator='\t')[1:][:-1]
#            f_data.write('\t' + string + '\n')
#            
#            #add the mean to aves, write to file
#            ave = np.mean(data)
#            self.aves[i] = ave
#            f_ave.write('\t' + str(ave) + '\n')
#            print('Ave = ' + str(ave) + ' c.p.s.')
#            
#            #clear the previous lines, replot the updated line
#            ax.clear()
#            ax.plot(self.wavelengths, self.aves, 'r-')
#            plt.xlabel('Wavelength [nm]')
#            plt.ylabel('Intensity [c.p.s.]')
#            plt.title(self.name)
#            self.fig.canvas.draw()
#            self.fig.canvas.flush_events()
#        
#        #close the two files
#        f_ave.close()
#        f_data.close()
            
        
            