# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 15:05:25 2020

Serial control of Alicat MC-Series MFCs

MFC must be set to be controlled by RS232.

@author: ESL328
"""

import serial
import numpy as np

class MFC():
       
    def __init__(self,port,maxFlow):      
        #initialize the serial port
        ser = serial.Serial()
        ser.port = port

        #serial settings
        ser.bytesize = serial.EIGHTBITS
        ser.stopbits = serial.STOPBITS_ONE
        ser.parity = serial.PARITY_NONE
        ser.xonxoff = False
        ser.baudrate = 19200

        #timeout so don't wait forever
        ser.timeout = 1

        #open serial port
        ser.open()        
        ser.reset_input_buffer()
        ser.reset_output_buffer()
        
        #save serial port 
        self.ser = ser
        
        #save max flow rate
        self.maxFlow = maxFlow

    #get data from MFC
    def getData(self):
        #flush buffers
        self.ser.reset_input_buffer()
        self.ser.reset_output_buffer()
        
        #send command to get data
        self.ser.write(b'A\r\n')
    
        
        result = self.ser.read(50).decode()
        return result
        
    #set set point on MFC.    
    def setSP(self,setPoint):
        #put set point in format for MFC
        sp = int(setPoint/self.maxFlow*64000)
        cmd = 'A' + str(sp) + '\r\n'
        
        sp = np.nan
        while np.isnan(sp):
            #flush buffers
            self.ser.reset_input_buffer()
            self.ser.reset_output_buffer()
        
            #send command to get data
            self.ser.write(cmd.encode())
        
            result = self.ser.read(50).decode()
            try:
                sp = float(result.split(' ')[5])
            except ValueError:
                sp = np.nan
            except IndexError:
                sp = np.nan
        
        return str(sp)
        