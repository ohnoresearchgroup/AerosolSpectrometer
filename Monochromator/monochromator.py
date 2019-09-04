#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 15:13:12 2019

@author: pohno
"""

#our grating is 1200 G/mm

#serial communications
import serial

import time

class Monochromator():

    def __init__(self):
        
        #initialize serial port
        ser = serial.Serial()
        
        #port on computer
        ser.port = 'COM1'
        
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
    
    #execute 'ECHO' to check that monochromator is connected
    def echo(self):
        self.ser.write(str(27).encode())
        
        #wait for 30 ms to give it time to recover
        time.sleep(0.03)
        
        #get response and extract float
        string = self.ser.readline()
        print(string)
     
    #executes a query depending on the byte that you give it  
    def query(self,querybyte):
        print(querybyte)
    
    
        
    #returns the grating to home position    
    def reset(self):
        self.ser.write(str(255).encode(),str(255).encode(),str(255).encode())
     
    #scans the monochromator between start and stop, at speed set by speed 
    def scan(self, start, stop):
        (startByte1,startByte2) = self.convertToBytes(start)
        (stopByte1,stopByte2) = self.convertToBytes(stop)
        
    #sets the size that the step steps by
    def size(self,size):
        print(size)
        
        
    #sets the speed that the monochromator scans at    
    def speed(self,speed):
        #speeds for 1200 G/mm: 1000,500,250,125,62,31,15,7,3,1 in A/s
        (speedByte1,speedByte2) = self.convertToBytes(speed)
        
    #moves the monochromator by the step size
    def step(self):
        self.ser.write(str(54).encode())
    
    #sets the units used in the goto, scan, size, calibrate
    def units(self,unit):
        
        byte = None
        if unit == 'microns':
            byte = b'00'
        elif unit == 'nanometers':
            byte = b'01'
        elif unit == 'angstroms':
            byte = b'02'
        else:
            print('not a valid unit')
        if byte:
            self.ser.write(str(50).encode(),byte)
    
    #convert number into bytes the monochromator understands (from SP manual)    
    def convertToBytes(self,number):
        num1 = int(number/256)
        num2 = int(number - 256*num1)
        
        byte1 = str(num1).encode()
        byte2 = str(num2).encode()
        
        return(byte1,byte2)
        
    #convert from bytes into number, according to SP manual    
    def convertFromBytes(self,byte1,byte2):
        number = int(byte1)*256 + int(byte2)
        print(number)
        
    #close serial port
    def close(self):
        self.ser.close()