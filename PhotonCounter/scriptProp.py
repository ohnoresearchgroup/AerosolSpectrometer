#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 22:02:00 2019

@author: pohno
"""
from propeller import Propeller
p = Propeller()
import numpy as np
from datetime import datetime

n = 4

a = np.zeros(n)

startTime = datetime.now()
for i in range(n):
    a[i] = p.getData()
print(datetime.now()-startTime)
print(a)
    