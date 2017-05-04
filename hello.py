# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def distance(self, other):
        x_diff_sq = (self.x-other.x)**2
        y_diff_sq = (self.y-other.y)**2
        return (x_diff_sq + y_diff_sq)**0.5
    
    def __str__(self):
        return "<"+str(self.x)+","+str(self.y)+">"
    
    def __sub__(self, other):
        return Coordinate(self.x-other.x,self.y-other.y)
    
    
class Fraction(object):
    def __init__(self, num, den):
        self.num = num
        self.den = den
        
    def __str__(self):
        return str(self.num)+" / " + str(self.den)
    
    def getNum(self):
        return self.num
    
    def getDen(self):
        return self.den
    
    def __add__(self, other):
        x = self.getNum() + other.getNum()
        y = self.getDen() + other.getDen()
        return Fraction(x,y)
        
    def __sub__(self, other):
        x = self.num - other.num
        y = self.den - other.den
        return Fraction(x,y)
        
    def get_float(self):
        return float(float(self.num)/float(self.den))
    

class Rep_Invar(object):
    """ Insert Set of integers """
    def __init__(self):
        self.list = []
    
    def getlist(self):
        return self.list
        
    def member(self, n):
        if n in self.getlist():
            return True
        else :
            return False
        
    def insert(self, num):
        """ Insert Elements """
        if not(self.member(num)):
            self.list.append(num)
        else :
            print "Already there"
            
    def remove(self, num):
        try:
            self.list.remove(num)
        except:
            raise ValueError(str(num)+ ' not found')
        
        
    def __str__(self):
        return str(self.list)
        
        
    