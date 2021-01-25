# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 17:41:43 2021

@author: paule
"""

import serial
import numpy as np

class RotronicTRH():
       
    def __init__(self,port):      
        #initialize the serial port
        ser = serial.Serial()
        ser.port = port

        #serial settings
        ser.bytesize = serial.EIGHTBITS
        ser.stopbits = serial.STOPBITS_ONE
        ser.parity = serial.PARITY_NONE
        ser.xonxoff = True
        ser.baudrate = 19200

        #timeout so don't wait forever
        ser.timeout = 1

        #open serial port
        ser.open()        
        ser.reset_input_buffer()
        ser.reset_output_buffer()
        
        #save serial port 
        self.ser = ser
        
    def getTRH(self):    
        t = np.nan
        rh = np.nan
        while np.isnan(t):
            #flush buffers
            self.ser.reset_input_buffer()
            self.ser.reset_output_buffer()
            
            #send command to get data
            self.ser.write(b'{ 99RDD}\r\n')
    
        
            result = self.ser.readline()
            try:
                t = float(result.split(b';')[5].decode())
                rh = float(result.split(b';')[1].decode())
            except ValueError:
                t = np.nan
                rh = np.nan
                
        return t, rh

    #get T data
    def getT(self):
        t = np.nan
        while np.isnan(t):
            #flush buffers
            self.ser.reset_input_buffer()
            self.ser.reset_output_buffer()
            
            #send command to get data
            self.ser.write(b'{ 99RDD}\r\n')
    
        
            result = self.ser.readline()
            try:
                t = float(result.split(b';')[5].decode())
            except ValueError:
                t = np.nan
                
        return t
    
    #get RH data    
    def getRH(self):
        rh = np.nan
        while np.isnan(rh):
            #flush buffers
            self.ser.reset_input_buffer()
            self.ser.reset_output_buffer()
            
            #send command to get data
            self.ser.write(b'{ 99RDD}\r\n')
            
            result = self.ser.readline()
            try:
                rh = float(result.split(b';')[1].decode())
            except ValueError:
                rh = np.nan

        return rh