# -*- coding: utf-8 -*-
"""
Created on Thu May 04 23:08:04 2017

@author: Abhishek
"""

class Animal(object):
    def __init__(self,age):
        self.age = age
        self.name = None
        
    def get_age(self):
        return self.age
    
    def get_name(self):
        return self.name
    
    def set_age(self, newage):
        self.age = newage
        
    def set_name(self, newname=""):
        self.name = newname
        
    def __str__(self):
        return "animal:"+str(self.name)+":"+str(self.age)
    
class Cat(Animal):
    def speak(self):
        print "meow"
    def __str__(self):
        return "cat:"+str(self.name)+":"+str(self.age)

class Dog(Animal):
    def speak(self):
        print "bhow bhow"
    def __str__(self):
        return "dog:"+str(self.name)+":"+str(self.age)
        
class person(Animal):
    def __init__(self, name, age):
        Animal.__init__(self, age)
        Animal.set_name(self, name)
        self.friends = []
    def get_friends(self):
        return self.friends
    def add_friend(self, fname):
        if fname not in self.get_friends:
            self.friends.append(fname)
    def speak(self):
        print("hello")
    def __str__(self):
        return "person: "+ str(self.get_name())+" : " + str(self.get_age())
        

    