#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 21:36:51 2019

@author: pohno
"""

import serial
import time

class Propeller():
       
    def __init__(self):      
        #initialize the serial port
        ser = serial.Serial()
        ser.port = "/dev/cu.usbserial-QS5KAR5"

        #serial settings
        ser.bytesize = serial.EIGHTBITS
        ser.stopbits = serial.STOPBITS_ONE
        ser.parity = serial.PARITY_NONE
        ser.xonxoff = False
        ser.baudrate = 115200

        #timeout so don't wait forever
        ser.timeout = 1

        #open serial port
        ser.open()        
        ser.reset_input_buffer()
        ser.reset_output_buffer()
        
        #save serial port 
        self.ser = ser


    def getData(self):
        #flush buffers
        self.ser.reset_input_buffer()
        self.ser.reset_output_buffer()
        
        #send command to get data
        self.ser.write(b'D')
        
        #wait just over 1 second
        time.sleep(1.01)
        
        #get result (should be 8 bytes, in hex), turn to int
        result = int(self.ser.read(8).decode(),16)
        return result

    def checkStatus(self):
        #flush buffers
        self.ser.reset_input_buffer()
        self.ser.reset_output_buffer()
        
        #send command to check status
        self.ser.write(b'C')
        
        #wait briefly
        time.sleep(0.001)
        
        #get status character, check if it is G
        char = self.ser.read(1).decode()
        if char == 'G':
            print("Counter connected.")
        else:
            print("Counter does not appear to be working.")
        
    def close(self):
        #close serial port
        self.ser.close()
            
        

    