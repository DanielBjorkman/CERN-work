# -*- coding: utf-8 -*-
"""
Created on Tue Aug 08 11:17:27 2017

@author: cbjorkma
"""

#Fluka geometry modifier

path = '//cern.ch/dfs/Users/c/cbjorkma/Documents/LSS 2'
filename = 'LSS2_exp.inp'


import os
os.chdir(path)

f = open(filename,"r+")
lines = f.readlines()

Str2Find = 'RPP WireBox'
idxs = []

for i in range(len(lines)):
    if lines[i][:11] == Str2Find:
        idxs.append(i)

idx = idxs[i]

step = (0.001,0,0)
NumSteps = 6

for i in range(NumSteps):
    lineCont = lines[idx].split(' ')
    lineCont[4] = str(float(lineCont[4]) + step[0]*(i+1))
    lineCont[5] = str(float(lineCont[4]) + step[0]*(i+1))
    

#idx = lines[0:][:11].index(Str2Find)