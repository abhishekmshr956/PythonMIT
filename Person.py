# -*- coding: utf-8 -*-
"""
Created on Fri May 05 23:46:20 2017

@author: Abhishek
"""

class Person(object):
    def __init__(self, name):
        self.name = name
        self.birthday = None
        self.lastName = name.split(' ')[-1]
        
    def getLastName(self):
        return self.lastName
    
    def setBirthday(self, month, day,year):
        self.birthday = datetime.date(year,month,day)
     
    def getAge(self):
        if self.birthday == None:
            raise ValueError
        return (datetime.date.today() - self.birthday).days
    
    def __lt__(self, other):
        if self.lastName == other.lastName:
            return self.name < other.name
        return self.lastName < other.lastName
    
    def __str__(self):
        return self.name
    
    
class MITPerson(Person):
    nextIdnum = 1
    
    def __init__(self, name):
        Person.__init__(self, name)
        self.idNum = MITPerson.nextIdnum
        MITPerson.nextIdnum +=1
        
    def getid(self):
        return self.idNum
    
    def __lt__(self, other):
        return self.getid() < other.getid()
    
    def speak(self, utterance):
        return (self.getLastName() + "says: " + utterance)
    
        
class Student(MITPerson):
    pass    

class UG(Student):
    def __init__(self, name, classYear):
        MITPerson.__init__(self,name)
        self.year = classYear
        
    def getClass(self):
        return self.year
    
    def speak(self, utterance):
        return MITPerson.speak(self, " Dude, "+ utterance)
    
class Grad(Student):
    pass



class TransferStudent(Student):
    pass

def isStudent(obj):
    return isinstance(obj, Student)


class Professor(MITPerson):
    def __init__(self, name, department):
        MITPerson.__init__(self, name)
        self.department = department
        
    def speak(self, utterance):
        new = 'In course ' + self.department +' we say'
        return MITPerson.speak(self, new + utterance)
    
    def lecture(self, topic):
        return self.speak('it is obvious that ' + topic)
    


    