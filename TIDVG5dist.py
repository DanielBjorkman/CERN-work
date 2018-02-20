# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 15:21:55 2018

@author: cbjorkma
"""

#TIDVG5 distribution

import os
import numpy as np
import matplotlib.pyplot as plt

path = '//rpclustersrv1/cbjorkma/Dump studies'

os.chdir(path)


file1 = 'BEAM-72b-Xa.dat'

file2 = 'BEAM-72b-Y.dat'


f1 = np.loadtxt(file1)

#f2 = np.loadtxt(file2)


fig = plt.figure()

plt.hist2d(f1[0:,0],f1[0:,1])

plt.show()