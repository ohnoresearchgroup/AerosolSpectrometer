# -*- coding: utf-8 -*-
"""
Created on Sat Dec 17 15:33:25 2022

@author: csmpeo1
"""

import u3

class LabJackDAC():
    
    def __init__(self):
        
        #open the first LabJack U3 connected
        self.lj = u3.U3()
        
    def writeVoltage(self,channel,voltage):
        
        DAC0_REGISTER = 5000
        DAC1_REGISTER = 5002
        
        if channel == 1:
            self.lj.writeRegister(DAC0_REGISTER,voltage)
        elif channel == 2:
            self.lj.writeRegister(DAC1_REGISTER,voltage)

