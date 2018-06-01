# -*- coding: utf-8 -*-
"""
Created on Thu May 31 11:08:36 2018

@author: cbjorkma
"""

#ActiwizCompareer

class Machine:

    def __init__(self, name):
        self.name = name

#    def Name(self):
#        return self.firstname + " " + self.lastname

class ZS(Machine):

    def __init__(self):
        self.shell = []
        self.Cath = []
        self.SeptHolder = []
        self.wires = []
        
#70 ZShell
#71 Cathode electric
#72 Septholder
#73 Wires        
        
#    def GetEmployee(self):
#        return self.Name() + ", " +  self.staffnumber