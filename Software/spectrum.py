#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 17:22:45 2019

@author: pohno
"""

import numpy as np
from datetime import datetime

class Spectrum():
       
    def __init__(self,name,start,stop,step,time):
        self.name = name
        self.time = datetime.now()
        self.range = (start,stop,step)
        self.duration = time
        
        self.wavelengths = np.arange(start,stop+step,step)
        self.counts = np.zeros(len(self.wavelengths))