#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 15:13:12 2019

@author: pohno
"""

#our grating is 1200 G/mm

#serial communications
import serial

class Monochromator():

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
           
        #timeout
        ser.timeout = 1;
        
        #open serial port
        ser.open()

        #store serial port        
        self.ser = ser
        
        #default setting of units angstroms
        self.setUnits('angstroms')
        
        #check status
        self.checkStatus()
        
                        
    #goto position in nanometers
    def goTo(self,position):
        self.ser.reset_input_buffer()
        
        #convert to angstroms
        position = position*10
        
        #convert to format for monochromator
        (posByte1,posByte2) = self.convertToBytes(position)
        
        #start with empty byte array, build up command
        cmd = bytearray()
        cmd.append(0x10)
        cmd.append(posByte1)
        cmd.append(posByte2)
        
        self.ser.write(cmd)
        
        #get reply by waiting for last byte expected
        reply = self.ser.read_until(b'\x18',None)
        statusByte = reply[0:1]
        if (int.from_bytes(statusByte,byteorder='big') >= 128):
            print('Command not excepted.')

            
    #executes a query for position, returns in nanometers
    def queryPosition(self):
        self.ser.reset_input_buffer()
        
        #start with empty byte array, build up command
        cmd = bytearray()
        cmd.append(0x38)
        cmd.append(0x00)        
        self.ser.write(cmd)
        
        #get reply by waiting for last byte expected
        reply = self.ser.read_until(b'\x18',None)
        posByte1 = reply[0:1]
        posByte2 = reply[1:2]
        
        pos = self.convertFromBytes(posByte1,posByte2)
        pos = pos/10 #put back in nanometers
        return pos       

            
    #set the units to 'microns','nanometers',or 'angstroms'      
    def setUnits(self,units):
        self.ser.reset_input_buffer()
        
        byte = None
        if units == 'microns':
            byte = 0x00
        elif units == 'nanometers':
            byte = 0x01
        elif units == 'angstroms':
            byte = 0x02
        
        if byte is not None:
            #start with empty byte array, build up command
            cmd = bytearray()
            cmd.append(0x32)
            cmd.append(byte)
            self.ser.write(cmd)
        else:
            print('Incorrect units. Units can be microns, nanometers, or angstroms')
    
    #ask what units it is using, prints to console
    def queryUnits(self):
        self.ser.reset_input_buffer()
        
        #start with empty byte array, build up command
        cmd = bytearray()
        cmd.append(0x38)
        cmd.append(0x0E)
        self.ser.write(cmd)
        
        #get reply by waiting for last byte expected
        reply = self.ser.read_until(b'\x18',None)
        unitsByte = reply[1:2]
        if unitsByte == b'\x00':
            print('Units are microns')
        elif unitsByte == b'\x01':
            print('Units are nanometers.')
        elif unitsByte == b'\x02':
            print('Units are Angstroms.')
        
    #convert number into bytes the monochromator understands (from SP manual)    
    def convertToBytes(self,number):
        num1 = int(number/256)
        num2 = int(number - 256*num1)
        
        return(num1,num2)
        
    #convert from bytes into number, according to SP manual    
    def convertFromBytes(self,byte1,byte2):
        number = (int.from_bytes(byte1,byteorder='big')*256 + 
                  int.from_bytes(byte2,byteorder='big'))
        print(number)
              
    #execute 'ECHO' to check that monochromator is connected
    def checkStatus(self):
        try:
            self.ser.reset_input_buffer()
            
            #start with empty byte array, build up command
            cmd = bytearray()
            cmd.append(0x1B)
            
            #write command to serial port
            self.ser.write(cmd)
            
            #get reply by waiting for last byte expected
            reply = self.ser.read_until(b'\x1B',None)
            if reply == b'\x1B':
                print('Monochromator connected.')
            else:
                print('Monochromator not communicating.')
        except serial.SerialException:
            print('Serial not connected.')
            
        
    #returns the grating to home position    
    def reset(self):        
        self.ser.write(b'\xFF\xFF\xFF')    
         
    #close serial port
    def close(self):       
        self.ser.close()