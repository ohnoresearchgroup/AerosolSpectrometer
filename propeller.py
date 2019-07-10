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
        ser.timeout = 0.05

        #open serial port
        ser.open()
        
        self.ser = ser
        
    def read(self):
        print(self.ser.readline())

    def getData(self):
        self.ser.write(b'00111111')
        print(self.ser.readline().decode())
        print(self.ser.readline().decode())

    