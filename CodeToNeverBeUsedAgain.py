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


#70 ZShell
#71 Cathode electric
#72 Septholder
#73 Wires        

#78 Zshellc
#79 CathElec
#80 Septholdc
#81 Wiresc
#
#
#path = '//rpclustersrv1/cbjorkma/LSS2/Fluence/ZSa/Out73_dir'
#
#
#data = ActiwizFluence(path, 1)
#
#prim = 1
#fig = plt.figure()
#ax = plt.subplot(111)
#ActiwizFluencePlot(data, ax, prim, '-')
#plt.title('ZSa', fontsize = 20)
##plt.ylim([math.pow(10,-9), math.pow(10,-1)])
#
#
#
#
#
#path = '//rpclustersrv1/cbjorkma/LSS2/Fluence/ZSb/Out73_dir'
#data2 = ActiwizFluence(path, 1)
#ax = plt.subplot(212)
#ActiwizFluencePlot(data2, ax, prim, '--')
#plt.title('ZSb', fontsize = 20)
##plt.ylim([math.pow(10,-9), math.pow(10,-1)])
#plt.show()
#
#
#
#path = '//rpclustersrv1/cbjorkma/LSS2/Fluence/ZSd/Out81_dir'
#
#
#data3 = ActiwizFluence(path, 1)
#
#prim = 1
#fig = plt.figure()
#ax = plt.subplot(111)
#ActiwizFluencePlot(data3, ax, prim, '-')
#plt.title('ZSd', fontsize = 20)
##plt.ylim([math.pow(10,-9), math.pow(10,-1)])
#
#
#
#
#
#path = '//rpclustersrv1/cbjorkma/LSS2/Fluence/ZSe/Out81_dir'
#data4 = ActiwizFluence(path, 1)
#ax = plt.subplot(212)
#ActiwizFluencePlot(data4, ax, prim, '--')
#plt.title('ZSe', fontsize = 20)
##plt.ylim([math.pow(10,-9), math.pow(10,-1)])
#plt.show()
#
#
#
#
#
#
#fig = plt.figure()
#
#
#import matplotlib.pyplot as plt
#
#for i in range(len(data)-1):
#    ax =plt.subplot(2,2,i+1)
#    info = data[i]
#    info2 = data2[i]
#    info3 = data3[i]
#    info4 = data4[i]
#    particle = data[len(data)-1][i]        
#    
#    #plt.loglog((data[0:,0] +  data[0:,1])/2, data[0:,2],label= particle)
#    xes = (info[0:,0] +  info[0:,1])/2
#    plt.errorbar(xes, xes*prim*info[0:,2], yerr = xes*info[0:,3]*info[0:,2], label= 'ZS1', linestyle = '-')
#    plt.errorbar(xes, xes*prim*info2[0:,2], yerr = xes*info2[0:,3]*info2[0:,2], label= 'ZS2', linestyle = '--')
#    plt.errorbar(xes, xes*prim*info3[0:,2], yerr = xes*info3[0:,3]*info3[0:,2], label= 'ZS4', linestyle = ':')
#    plt.errorbar(xes, xes*prim*info4[0:,2], yerr = xes*info4[0:,3]*info4[0:,2], label= 'ZS5', linestyle = '-.')
#    plt.title(particle , fontsize = 16)
#    ax.set_xscale("log", nonposx='clip')
#    ax.set_yscale("log", nonposy='clip')
#    if i == 2 or i == 3 :
#        plt.xlabel('E [GeV]', fontsize = 13)
#    plt.ylabel('E * Fluence /pp [cm-2]', fontsize = 16)
#    plt.grid(True)
#    plt.legend()
#    plt.suptitle('Wire septa fluences comparison', fontsize = 18)
#    
#    
#    
#    
#
#
#
#print 'Done'





path = '//rpclustersrv1/cbjorkma/LSS2/Fluence/ZSa/Out73_dir'


data3 = ActiwizFluence(path, 1)

prim = 1
fig = plt.figure()
ax = plt.subplot(111)
ActiwizFluencePlot(data3, ax, prim, '-')
plt.title('ZSd', fontsize = 20)
#plt.ylim([math.pow(10,-9), math.pow(10,-1)])





path = '//rpclustersrv1/cbjorkma/LSS2/Fluence/Carbon wire/ZSa/Out73_dir'
data4 = ActiwizFluence(path, 1)
ax = plt.subplot(212)
ActiwizFluencePlot(data4, ax, prim, '--')
plt.title('ZSe', fontsize = 20)
#plt.ylim([math.pow(10,-9), math.pow(10,-1)])
plt.show()



fig = plt.figure()


import matplotlib.pyplot as plt

for i in range(len(data3)-1):
    ax =plt.subplot(2,2,i+1)
#    info = data[i]
#    info2 = data2[i]
    info3 = data3[i]
    info4 = data4[i]
    particle = data3[len(data3)-1][i]        
    
    #plt.loglog((data[0:,0] +  data[0:,1])/2, data[0:,2],label= particle)
    xes = (info3[0:,0] +  info3[0:,1])/2
#    plt.errorbar(xes, xes*prim*info[0:,2], yerr = xes*info[0:,3]*info[0:,2], label= 'ZS1', linestyle = '-')
#    plt.errorbar(xes, xes*prim*info2[0:,2], yerr = xes*info2[0:,3]*info2[0:,2], label= 'ZS2', linestyle = '--')
    plt.errorbar(xes, xes*prim*info3[0:,2], yerr = xes*info3[0:,3]*info3[0:,2], label= 'Rhenium/Tungsten', linestyle = '-')
    plt.errorbar(xes, xes*prim*info4[0:,2], yerr = xes*info4[0:,3]*info4[0:,2], label= 'Graphite wire', linestyle = '--')
    plt.title(particle , fontsize = 16)
    ax.set_xscale("log", nonposx='clip')
    ax.set_yscale("log", nonposy='clip')
    if i == 2 or i == 3 :
        plt.xlabel('E [GeV]', fontsize = 13)
    plt.ylabel('E * Fluence /pp [cm-2]', fontsize = 16)
    plt.grid(True)
    plt.legend()
    plt.suptitle('Wire septa fluences comparison', fontsize = 18)
    
    
    
    















##This is used to compare the spectras
#Mask = []
#for i in range(len(data1)-1):
#    tmp = data1[i]
#    tmp[0:,2] = data1[i][0:,2] + data2[i][0:,2]
#    tmp[0:,3] = map(lambda x, y: math.sqrt( math.pow(x,2) + math.pow(y,2)), data1[i][0:,3], data2[i][0:,3])
#    Mask.append( tmp )
#Mask.append( data1[4])







