# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 14:03:30 2017

@author: cbjorkma
"""

#USERMED analysis


import os
import numpy as np
#import math as math
directory = "//cern.ch/dfs/Users/c/cbjorkma/Documents/LSS 2"
os.chdir(directory)

#Read fluka output
filenameFluka = 'LSS2_exp001_TRAKFILE'
fluka = np.loadtxt(filenameFluka , skiprows = 1)


import matplotlib.pyplot as plt


plt.