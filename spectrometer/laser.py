#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 11:44:20 2019

@author: pohno
"""

import serial
import time

class Laser():

    def __init__(self,port):
        
        #initialize serial port
        ser = serial.Serial()
        
        #port on computer
        ser.port = port
        
        #serial settings
        ser.bytesize = serial.EIGHTBITS
        ser.baudrate = 9600
        ser.stopbits = serial.STOPBITS_ONE
        ser.parity = serial.PARITY_NONE
        ser.xonxoff = False
           
        #timeout after 0.3 second so don't wait forever
        ser.timeout = 0.3
        
        #open serial port
        ser.open()
        self.ser = ser
        
        time.sleep(2)
        
        #flush buffers
        self.ser.reset_input_buffer()
        self.ser.reset_output_buffer()
        
        #make sure laser is connected and off
        self.check()
        self.turnOFF()
        
        
    def turnON(self):
        #flush buffers
        self.ser.reset_input_buffer()
        self.ser.reset_output_buffer()
        
        self.ser.write(str('N').encode())
        text = self.ser.readline().decode()
        if text.find('on') != -1:
            print('Laser on.')
        else:
            print('Laser may not have turned on.')
        
    def turnOFF(self):
        #flush buffers
        self.ser.reset_input_buffer()
        self.ser.reset_output_buffer()
        
        self.ser.write(str('F').encode())
        text = self.ser.readline().decode()
        if text.find('off') != -1:
            print('Laser off.')
        else:
            print('Laser may not have turned off.')
        
    def check(self):
        #flush buffers
        self.ser.reset_input_buffer()
        self.ser.reset_output_buffer()
        
        self.ser.write(str('C').encode())
        text = self.ser.readline().decode()
        if text.find('good') != -1:
            print('Laser connected.')
        else:
            print('Laser may not be connected.')
    
    def close(self):
        self.ser.close()