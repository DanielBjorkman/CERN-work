# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 14:51:42 2017

@author: cbjorkma
"""


#import os as os
#
#dir = '//rpclustersrv1/cbjorkma/Dump studies/Uppstream Hole study/Fluence/Halloutput_dir'
#
#filename = 'HallAirproduction.nuc'
#
#os.chdir(dir)
#
#import numpy as np
#
#print np.loadtxt(filename, skiprows = 12, usecols = (1,2))
#

import matplotlib.pyplot as plt
from ActiwizFluence import ActiwizFluence
from ActiwizFluence import ActiwizFluencePlot
import math


plt.close()

#path = '//rpclustersrv1/cbjorkma/Dump studies/Uppstream Hole study/Fluence/AirTunnel_dir'
#
#
##fig = plt.figure()
##ax = fig.add_subplot(211)
##path = '//rpclustersrv1/cbjorkma/Dump studies/Uppstream Hole study/Fluence/Deepscore1_dir'
#data = ActiwizFluence(path, 15912)
#
#prim = 1
#fig = plt.figure()
#ax = plt.subplot(211)
#ActiwizFluencePlot(data, ax, prim)
#plt.title('Downstream tunnel fluence, with first downstream mask', fontsize = 20)
#plt.ylim([math.pow(10,-9), math.pow(10,-1)])
#
#path = '//rpclustersrv1/cbjorkma/Dump studies/Uppstream Hole study/Fluence/AirTunnelNoMASK_dir'
#data = ActiwizFluence(path, 15912)
#ax = plt.subplot(212)
#ActiwizFluencePlot(data, ax, prim)
#plt.title('Downstream tunnel fluence, WITHOUT first downstream mask', fontsize = 20)
#plt.ylim([math.pow(10,-9), math.pow(10,-1)])
#plt.show()
#
##
#ax = fig.add_subplot(212)
#path = '//rpclustersrv1/cbjorkma/Dump studies/Uppstream Hole study/Fluence/Deepscore2_dir'
#obj = ActiwizFluence(path)


#plt.show()

tunnelVolume = 2.8*math.pow(10,8)
cavernVolume = 6.82*math.pow(10,9)

#With first mask
path = '//rpclustersrv1/cbjorkma/Dump studies/Uppstream Hole study/Fluence/Cavern_dir'
data1 = ActiwizFluence(path, cavernVolume)

path = '//rpclustersrv1/cbjorkma/Dump studies/Uppstream Hole study/Fluence/AirTunnel_dir'
data2 = ActiwizFluence(path, tunnelVolume)

Mask = []
for i in range(len(data1)-1):
    tmp = data1[i]
    tmp[0:,2] = data1[i][0:,2] + data2[i][0:,2]
    tmp[0:,3] = map(lambda x, y: math.sqrt( math.pow(x,2) + math.pow(y,2)), data1[i][0:,3], data2[i][0:,3])
    Mask.append( tmp )
Mask.append( data1[4])


#Without first mask
path = '//rpclustersrv1/cbjorkma/Dump studies/Uppstream Hole study/Fluence/CavernNoMASK_dir'
data1 = ActiwizFluence(path, cavernVolume)

path = '//rpclustersrv1/cbjorkma/Dump studies/Uppstream Hole study/Fluence/AirTunnelNoMASK_dir'
data2 = ActiwizFluence(path, tunnelVolume)

NoMask = []
for i in range(len(data1)-1):
    tmp = data1[i]
    tmp[0:,2] = data1[i][0:,2] + data2[i][0:,2]
    tmp[0:,3] = map(lambda x, y: math.sqrt( math.pow(x,2) + math.pow(y,2)), data1[i][0:,3], data2[i][0:,3])
    NoMask.append( tmp )
NoMask.append( data1[4])







prim = 2 *math.pow(10,18)

fig = plt.figure()
ax = plt.subplot(211)
ActiwizFluencePlot(Mask, ax, prim)
plt.title('With first mask', fontsize = 20)
#plt.ylim([math.pow(10,-9), 2*math.pow(10,-6)])


ax = plt.subplot(212)
ActiwizFluencePlot(NoMask, ax, prim)
plt.title('Without first mask', fontsize = 20)
#plt.ylim([math.pow(10,-9), 2*math.pow(10,-6)])

plt.show()

#Combination
combo = []
for i in range(len(Mask)-1):
    tmp = Mask[i]
    tmp[0:,2] = NoMask[i][0:,2] - Mask[i][0:,2] 
    tmp[0:,3] = map(lambda x, y: math.sqrt( math.pow(x,2) + math.pow(y,2)), Mask[i][0:,3], NoMask[i][0:,3])
    combo.append( tmp )
combo.append( Mask[4])

fig = plt.figure()
ax = plt.subplot(111)
ActiwizFluencePlot(Mask, ax, prim)
plt.title('Difference plot / Additional hadrons to activate the ECX5 air volume when first mask is absent', fontsize = 20)
plt.ylabel('Without Mask - With mask [cm-2]')
#plt.ylim([math.pow(10,-11), math.pow(10,-6)])



plt.show()



print 'Zsa1 = ' + str((680 + 342)/2 )
print 'BLM1 = ' + str((680 + 342)/2 + 51)


















