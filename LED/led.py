#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 11:44:20 2019

@author: pohno
"""

from time import sleep
import serial


class LED():

    def __init__(self):
        
        #initialize serial port
        ser = serial.Serial()
        
        #port on computer
        ser.port = '/dev/tty.usbmodem14201'
        
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
        
        
    def turnON(self):
        self.ser.write(str('N').encode())
        print(self.ser.readline())
        
    def turnOFF(self):
        self.ser.write(str('F').encode())
        print(self.ser.readline())
        
    def check(self):
        self.ser.write(str('C').encode())
        print(self.ser.readline())
    
    def close(self):
        self.ser.close()