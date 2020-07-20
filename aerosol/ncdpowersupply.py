# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 12:43:23 2020

        #API header \xAA
        #API payloud byte count (write byte + # to write) = \x05
        #API write command \xBE
        #address bit = \x60
        #write DAC output = \x40
        #two bytes sixteen bit DAC value
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
        
    def setVoltage(self,volt):
        cmd = 'aa 05 be 60 40'
        
        w = bytearray.fromhex(cmd)
        
        num = int(volt/10*65535)
        twoBytes = struct.pack('>H',num)
        
        w.extend(twoBytes) 
        #calculate checksum
        w.append(sum(w)&255)
        self.ser.write(w)
        time.sleep(0.01) #need to wait before sending another ser cmd too fast
        