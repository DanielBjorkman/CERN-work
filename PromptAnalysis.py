# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 14:15:36 2017

@author: cbjorkma
"""

#Prompt analysis

import os
import numpy as np
#import math as math
#directory = "//cern.ch/dfs/Users/c/cbjorkma/Documents/LSS 2"

path = "//rpclustersrv1/cluster_temp/cbjorkma/2017-11-09_15h10m34s_Dump7Prompt"

os.chdir(path)

from os import listdir
from os.path import isfile, join         
        


onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]           
files = filter(lambda x: x[-4:] == '.out' , onlyfiles)             
files = sorted(files)      


maskG1 = np.zeros(len(files))
maskG3 = np.zeros(len(files))


for i in range(len(files)):
    foundA = False
    foundB = False
    filename = files[i]
    f = open(filename,"r+")
    lines = f.readlines()
    for j in range(10000,len(lines)):
        if lines[j][5:16] == '86 MSKSHDG1':
            info = lines[j].split(' ')
            info = filter(None,info)
            maskG1[i] = info[len(info)-2]
            foundA = True
        if lines[j][5:16] == '88 MSKSHDG3':
            info = lines[j].split(' ')
            info = filter(None,info)
            maskG3[i] = info[len(info)-2]
            foundB = True
    if foundA and foundB:
        pass
    else:
        print "ERROR"
        break
    
import matplotlib.pyplot as plt

import math

volume = 60 * 60* 60 - 60* math.pi *3.7*3.7


fig = plt.figure()
ax = fig.add_subplot(1,1,1)

plt.hist(maskG1, fc=(1, 0, 0, 0.8), label = '2nd mask', bins = 10, normed = 1)


plt.hist(maskG3, fc=(0, 0, 1, 0.5), label = '1st mask', bins = 20, normed = 1)

plt.xlabel('Energy [GeV]')
#plt.xlabel('Energy [GeV]')
ax.set_yscale('log')

plt.title('Energy deposited in masks')

plt.grid()
plt.legend()

plt.show()