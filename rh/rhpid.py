#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 15:28:54 2020

@author: pohno
"""
from simple_pid import PID

class RHpid():
    def __init__(self,Kp,Ki,Kd,setpoint):
        self.Kp = Kp
        self.Ki = Ki
        self.Kd = Kd
        
        self.pid = PID(Kp,Ki,Kd,setpoint)
        
        #lower limit wet flow ratio of 0.02
        self.pid.output_limits(0.02,1)