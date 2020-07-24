"""
basic PID controller
"""
import time

class PID:
    def __init__(self, P, I, D):

        self.Kp = P
        self.Ki = I
        self.Kd = D
        
        self.last_time = None
        self.last_error = 0
        
        self.SetPoint = 0.0

        self.PTerm = 0.0
        self.ITerm = 0.0
        self.DTerm = 0.0

        # Windup Guard
        self.windup_guardL = -0.6
        self.windup_guardH = 0.6

        self.output = 0.0

    def update(self, feedback_value):
        #calculate error
        error = self.SetPoint - feedback_value

        #get current time
        self.current_time = time.time()
        
        #calculate proportional term
        self.PTerm = self.Kp * error
        
        #if you have a previous error and previous time, calculate int/der terms
        if self.last_time is not None:
            delta_time = self.current_time - self.last_time
            delta_error = error - self.last_error
            
            #calculate integral term
            self.ITerm += error * delta_time * self.Ki
            
            #integral windup guard
            if (self.ITerm < self.windup_guardL):
                self.ITerm = self.windup_guardL
            elif (self.ITerm > self.windup_guardH):
                self.ITerm = self.windup_guardH
                
            #calculate derivative term    
            self.DTerm = 0.0
            if delta_time > 0:
                self.DTerm = delta_error / delta_time * self.Kd
                
        else:
            self.DTerm = 0
            self.ITerm = 0

        # Remember last time and last error for next calculation
        self.last_time = self.current_time
        self.last_error = error

        self.output = self.PTerm + self.ITerm + self.DTerm
        #print('p ',self.PTerm)
        #print('i ',self.ITerm)
        #print('d ',self.DTerm)