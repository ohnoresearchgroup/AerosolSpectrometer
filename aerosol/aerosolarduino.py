#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 14:39:53 2020

@author: pohno
"""


import serial
import time

class AerosolArduino():

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
        
    def check(self):
        #flush buffers
        self.ser.reset_input_buffer()
        self.ser.reset_output_buffer()
        
        self.ser.write(str('C').encode())
        time.sleep(0.01)
        text = self.ser.readline().decode()
        if text.find('good') != -1:
            print('Aerosol arduino connected.')
        else:
            print('Aerosol arduino may not be connected.')
        
    def turnOnSyringePump(self):
        #flush buffers
        self.ser.reset_input_buffer()
        self.ser.reset_output_buffer()
        
        self.ser.write(str('A').encode())
        time.sleep(0.01)
        text = self.ser.readline().decode()
        if text.find('pumpon') != -1:
            print('Syringe pump on.')
        else:
            print('Syringe pump may not have turned on.')
        
    def turnOffSyringePump(self):
        #flush buffers
        self.ser.reset_input_buffer()
        self.ser.reset_output_buffer()
        
        self.ser.write(str('B').encode())
        time.sleep(0.01)
        text = self.ser.readline().decode()
        if text.find('pumpoff') != -1:
            print('Syringe pump off.')
        else:
            print('Syringe pump may not have turned off.')
            
            
    def turnOnAtomizer(self):
        #flush buffers
        self.ser.reset_input_buffer()
        self.ser.reset_output_buffer()
        
        self.ser.write(str('D').encode())
        time.sleep(0.01)
        text = self.ser.readline().decode()
        if text.find('atomon') != -1:
            print('Atomizer on.')
        else:
            print('Atomizer may not have turned on.')
            
    def turnOffAtomizer(self):
        #flush buffers
        self.ser.reset_input_buffer()
        self.ser.reset_output_buffer()
        
        self.ser.write(str('E').encode())
        time.sleep(0.01)
        text = self.ser.readline().decode()
        if text.find('atomoff') != -1:
            print('Atomizer off.')
        else:
            print('Atomizer may not have turned off.')
            
    def turnOnCellParticles(self):
        #flush buffers
        self.ser.reset_input_buffer()
        self.ser.reset_output_buffer()
        
        self.ser.write(str('F').encode())
        time.sleep(0.01)
        text = self.ser.readline().decode()
        if text.find('cellparton') != -1:
            print('Cell particles on.')
        else:
            print('Cell particles may not have turned on.')
            
    def turnOffCellParticles(self):
        #flush buffers
        self.ser.reset_input_buffer()
        self.ser.reset_output_buffer()
        
        self.ser.write(str('G').encode())
        time.sleep(0.01)
        text = self.ser.readline().decode()
        if text.find('cellpartoff') != -1:
            print('Cell particles off.')
        else:
            print('Cell particles may not have turned off.')

        
    def close(self):
        self.ser.close()