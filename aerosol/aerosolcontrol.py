#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 14:48:26 2020

@author: pohno
"""

from aerosol.aerosolarduino import AerosolArduino

class AerosolControl():
       
    def __init__(self):     
        #placeholder
        self.placeholder = 'True'
        
        
    def connectArd(self):
        #initialize arduino to control
        self.aerosolarduino = AerosolArduino('COM12')
        print("Aerosol arduino connected.")
        
    def turnOnAtomizer(self):
        self.aerosolarduino.turnOnAtomizer()
        
    def turnOffAtomizer(self):
        self.aerosolarduino.turnOffAtomizer()

    def turnOnCellParticles(self):
        self.aerosolarduino.turnOnCellParticles()
        
    def turnOffCellParticles(self):
        self.aerosolarduino.turnOffCellParticles()
        
    def turnOnSyringePump(self):
        self.aerosolarduino.turnOnSyringePump()
        
    def turnOffSyringePump(self):
        self.aerosolarduino.turnOffSyringePump()