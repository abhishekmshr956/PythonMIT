# -*- coding: utf-8 -*-
"""
Created on Thu May 04 09:23:48 2017

@author: Abhishek
"""

class Clock(object):
    def __init__(self, time):
        self.time = time
    def print_time(self):
        #time = '6:30'
        print(time)

class Wild(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    

    