# -*- coding: utf-8 -*-
"""
Created on Wed May 02 15:35:30 2018

@author: cbjorkma
"""

#IonFilter

import os

path = '//cern.ch/dfs/Users/c/cbjorkma/Documents/Dump TIDGV5' 

os.chdir(path)

filename = 'IonFilterRawData.txt'

import numpy as np

data = np.loadtxt(filename, skiprows = 4)

data[0:,0] = data[0:,0]/(60*60)

import matplotlib.pyplot as plt


fig = plt.figure()

plt.plot(data[0:,0], data[0:,1], marker = 'o', color = 'c', linewidth = 3, linestyle = '--')
plt.yscale("log", nonposy='clip')

plt.ylabel('Dose rate [uSv/h]', fontsize = 14)
plt.xlabel('Hours since end of operations [h]', fontsize = 14)
plt.grid(linewidth = 0.3)

plt.title('Evolution of estimated hazard 1 meter from ion filter ', fontsize = 14)

plt.show()