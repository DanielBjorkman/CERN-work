# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 15:49:02 2018

@author: cbjorkma
"""

#CodeToNeverBeUsedAgain
#





import matplotlib.pyplot as plt
from ActiwizFluence import ActiwizFluence
from ActiwizFluence import ActiwizFluencePlot
import math
import numpy as np


path = '//rpclustersrv1/cbjorkma/LSS2/Fluence/ZSa/Out73_dir'


data = ActiwizFluence(path, 1)

prim = 1
fig = plt.figure()
ax = plt.subplot(211)
ActiwizFluencePlot(data, ax, prim)
plt.title('ZSa', fontsize = 20)
#plt.ylim([math.pow(10,-9), math.pow(10,-1)])





path = '//rpclustersrv1/cbjorkma/LSS2/Fluence/ZSb/Out73_dir'
data2 = ActiwizFluence(path, 1)
ax = plt.subplot(212)
ActiwizFluencePlot(data2, ax, prim)
plt.title('ZSb', fontsize = 20)
#plt.ylim([math.pow(10,-9), math.pow(10,-1)])
plt.show()



##This is used to compare the spectras
#Mask = []
#for i in range(len(data1)-1):
#    tmp = data1[i]
#    tmp[0:,2] = data1[i][0:,2] + data2[i][0:,2]
#    tmp[0:,3] = map(lambda x, y: math.sqrt( math.pow(x,2) + math.pow(y,2)), data1[i][0:,3], data2[i][0:,3])
#    Mask.append( tmp )
#Mask.append( data1[4])







