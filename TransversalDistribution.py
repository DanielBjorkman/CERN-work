# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 17:05:58 2017

@author: cbjorkma
"""

#Transversal distribution

import os
import numpy as np
#import math as math
#directory = "//cern.ch/dfs/Users/c/cbjorkma/Documents/LSS 2"

directory = "//rpclustersrv1/cbjorkma/LSS2"

os.chdir(directory)




def readPhase(filename):
    try:
        print "Attempting to load file..."
        out = np.loadtxt(filename , skiprows = 1)
        print "File loaded"
        np.save(filename, out)
        return out
    except ValueError:
        print "Repairing file... "
        f = open(filename,"r+")
        lines = f.readlines()
        for i in range(len(lines)):
            string = lines[i]
            #print 'Before ' + string
            tmp = list(string)
            try:
                tmp[-5] = ' '
                string = "".join(tmp)
                lines[i] = string
            except:
                pass
        f.seek(0)
        f.writelines(lines)
        f.truncate()
        f.close()
        print "Loading file..."
        out = np.loadtxt(filename , skiprows = 1)
        np.save(filename, out)
        print "File loaded"
        return out        
                   
        
        
    
filename = 'LSS2_exp001_fortLarge.90' 
#fluka1 = readPhase(filename)    
fluka1 = np.load(filename + '.npy')

filename = 'LSS2_exp001_fortLarge.91' 
fluka2 = readPhase(filename)   
#fluka2 = np.load(filename + '.npy')  

from matplotlib.colors import LogNorm
import matplotlib.pyplot as plt

fig = plt.figure()


plt.subplot(121)
x = fluka1[0:,1]
y = fluka1[0:,2]

plt.hist2d(x, y, bins=100, norm=LogNorm())

plt.xlabel('x [cm]', fontsize = 12)
plt.ylabel('y [cm]', fontsize = 12)
plt.title('Before TPST')
cbar = plt.colorbar()
cbar.set_label('Intensity')

plt.subplot(122)
x = fluka2[0:,1]
y = fluka2[0:,2]

plt.hist2d(x, y, bins=100, norm=LogNorm())

plt.xlabel('x [cm]', fontsize = 12)
plt.ylabel('y [cm]', fontsize = 12)
plt.title('After TPST')
cbar = plt.colorbar()
cbar.set_label('Intensity')

plt.show()


















