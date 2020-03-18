# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 15:48:56 2020

Serial communications with Omega USB-RH

@author: ESL328
"""


import serial

class OmegaTRH():
       
    def __init__(self,port):      
        #initialize the serial port
        ser = serial.Serial()
        ser.port = port

        #serial settings
        ser.bytesize = serial.EIGHTBITS
        ser.stopbits = serial.STOPBITS_ONE
        ser.parity = serial.PARITY_NONE
        ser.xonxoff = False
        ser.baudrate = 9600

        #timeout so don't wait forever
        ser.timeout = 1

        #open serial port
        ser.open()        
        ser.reset_input_buffer()
        ser.reset_output_buffer()
        
        #save serial port 
        self.ser = ser

    #get T data
    def getT(self):
        #flush buffers
        self.ser.reset_input_buffer()
        self.ser.reset_output_buffer()
        
        #send command to get data
        self.ser.write(b'C\r\n')
    
        
        result = self.ser.read(50).decode()
        t = float(result.split(' ')[0])
        return t
    
    #get RH data    
    def getRH(self):  
        #flush buffers
        self.ser.reset_input_buffer()
        self.ser.reset_output_buffer()
        
        #send command to get data
        self.ser.write(b'H\r\n')
        
        result = self.ser.read(50).decode()
        rh = float(result.split(' ')[0])
        return rh
        