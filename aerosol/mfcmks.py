# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 13:57:49 2020

@author: ESL328
"""


class MFCmks():
       
    def __init__(self,ncddac,ch):      
        #give mkscontrol unit
        self.control = ncddac
        self.ch = ch
        
    #set set point on MFC.    
    def setSP(self,setPoint):        
        #send setpoint
        self.control.setFlow(setPoint,self.ch)