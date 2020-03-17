# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 16:22:44 2020

@author: ESL328
"""

from mfc import MFC

class TRHcontrol():
       
    def __init__(self):      
        #initialize MFCs
        self.dryMFC = MFC('COM7',10)
        self.wetMFC = MFC('COM8',20)

        
        #set total flow rate
        self.totalFlow = 10
        
        
    def setRH(self,RH):
        #equation from calibration
        wetRatio = (RH + 2.0955)/90.755
        
        wetFlow = wetRatio*self.totalFlow
        dryFlow = (1-wetRatio)*self.totalFlow
        
        print('Setting RH of ',RH,'%')
        print('Dry:',str(self.dryMFC.setSP(dryFlow)),'LPM')
        print('Wet:',str(self.wetMFC.setSP(wetFlow)),'LPM')
        
    def setRatio(self,ratio):
        wetFlow = ratio*self.totalFlow
        dryFlow = (1-ratio)*self.totalFlow
        
        print('Dry:',str(self.dryMFC.setSP(dryFlow)),'LPM')
        print('Wet:',str(self.wetMFC.setSP(wetFlow)),'LPM')
        
        
    def setTotalFlowRate(self,flowRate):
        self.totalFlow = flowRate
        print('TotalFlow = ',str(flowRate), 'LPM')
        
    def getTotalFlowRate(self):
        print('TotalFlow = ',str(self.totalFlow), 'LPM')
        
        
        
    