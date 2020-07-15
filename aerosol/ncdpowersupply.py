# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 12:43:23 2020

        #API header \xAA
        #API payloud byte count (write byte + # to write) = \x05
        #API write command \xBE
        #address bit = \x0c
        #ch A = \x31
        #ch B = \x32
        #ch C = \x34
        #ch D = \x38
        #two bytes sixteen bit ADC value
        #final byte = checksum


@author: ESL328
"""

import serial
import struct
import time

class NCDpowerSupply():
    
    def __init__(self,port):
        #initialize serial port
        ser = serial.Serial()
        ser.port = port
        
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