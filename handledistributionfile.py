# -*- coding: utf-8 -*-
"""
Created on Wed Nov 08 13:59:00 2017

@author: cbjorkma
"""

#Handle particle distribution file

import os
#import numpy as np
#import math as math
directory = "//rpclustersrv1/cbjorkma/LSS2"
os.chdir(directory)


import matplotlib.pyplot as plt


filename = 'distribution_full.txt'
    
#f = open(filename,"r+")
#lines = f.readlines()

#print lines[0]
#
#print lines[0]
#print lines[1]

from random import randint
import numpy as np

#f = open('DistRand.dat', 'w')
#indecies = np.zeros(len(lines))
#for i in range(int(0.1*len(lines))):
#    idx = randint(1,len(lines))
#    indecies[idx] = indecies[idx] +1
#    f.write(lines[i])
#f.close()
#
#plt.plot(indecies)
#plt.show()
#




data1 = np.loadtxt('DistRand.dat' , skiprows = 1)# np.loadtxt(filename , skiprows = 1)

print 1

data2 = np.loadtxt(filename , skiprows = 1)

print 2

#data2 = data1

#data2 = np.loadtxt('DistRand.dat' , skiprows = 1)



#from matplotlib.colors import LogNorm


fig = plt.figure()
ax = fig.add_subplot(1,1,1)

plt.hist(data1[0:,2], fc=(1, 0, 0, 0.8), label = 'Sampled', bins = 40, normed = 1)


plt.hist(data2[0:,2], fc=(0, 0, 1, 0.5), label = 'Lindas', bins = 40, normed = 1)

plt.xlabel('Energy [GeV]')
ax.set_yscale('log')

plt.title('Source energy distribution')

plt.grid()
plt.legend()

plt.show()



#f = open('DistFull.dat', 'w')
#for i in range(0,len(lines)):
#    f.write(lines[i])
#f.close()