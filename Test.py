# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 14:51:42 2017

@author: cbjorkma
"""




import os
#import numpy as np
#import math
#from matplotlib.colors import LogNorm
#from matplotlib.gridspec import GridSpec
#import matplotlib.pyplot as plt
#import matplotlib.ticker as tk
#import matplotlib.patches as patches
##plt.close()


import pandas as pd
import glob




path = '/scratch/cbjorkma/LSS2'

basedir = '/Volumes/clueet_scratch/luillo/LSS2/2018-01-10_200umRibbonZS_full_abd_z2232cm_ZSrho/'

os.chdir(basedir)












##path = "//rpclustersrv1/cbjorkma/LSS2/run09"      
#path = "//rpclustersrv1/cbjorkma/LSS2/PyCollimateStudy/UsingPC"    
#os.chdir(path)        
##fluka1 = readPhaseDirectory(path)           
##np.save('run09', fluka1)
##  
#
#plt.clf()
#  
##filename = 'LSS2_exp001_fort.90' 
###filename = 'fort.90' 
###fluka1 = readPhase(filename)    
#
#print 'Start'
#
#
#x = np.random.rand(1600000)
#y = np.random.rand(16000)
#y = np.random.normal(0.5,2,10000)
#fluka = np.load('run09.npy')
#fluka = np.load('PCgreaterthan3.716.npy')
#x = fluka[0:,1]
#y = fluka[0:,3]
#primaries = fluka.shape[0]*0.01
#condition = x >= 5
#x = np.extract(condition,x)
#primaries = len(x)
#condition = fluka[0:,1] >= 3.5
#subsetFluka = np.zeros([np.sum(condition),fluka.shape[1]])
#for i in range(fluka.shape[1]):
#    subsetFluka[0:,i] = np.extract(condition, fluka[0:,i])
#print 'Subset Created'
#




#import subprocess
#import sys
#
#HOST="cbjorkma@clueet.ch"
## Ports are handled in ~/.ssh/config since we use OpenSSH
#COMMAND="ls"
#
#ssh = subprocess.Popen(["ssh", "%s" % HOST, COMMAND],
#                       shell=False,
#                       stdout=subprocess.PIPE,
#                       stderr=subprocess.PIPE)
#result = ssh.stdout.readlines()
##if result == []:
##    error = ssh.stderr.readlines()
##    print >>sys.stderr, "ERROR: %s" % error
##else:
##    print result
#
#
#
#












#x = fluka[0:,1]
#y = fluka[0:,3]

#newvec = x/y

#plt.subplot(211)
#
#histx1, xbins1, patches1 = plt.hist(y, bins = 10,fc=(1, 0, 0, 0.8))
#histx2, xbins2, patches2 = plt.hist(x, bins = xbins1,fc=(0, 1, 0, 0.8))
#
#plt.subplot(212)
#
#newvec = histx1/histx2
#
#binwidth = xbins1[1] - xbins1[0]
#
#plt.bar( xbins1[:-1], newvec,binwidth ,fc=(0, 0, 1, 0.8))

#out = plt.hist2d(x,y, bins=300,normed = True,cmap="viridis")
#
#ax1 = plt.subplot(111)
#
##x = fluka[0:,5]
#weights = 100* np.ones_like(x)/float(len(x))
#histx, xbins, Placeholder = plt.hist(x,weights = weights, bins = 100,fc=(1, 0, 0, 0.8), label = 'Fluka')
#
##y = fluka[0:,5]
#weights = 100* np.ones_like(y)/float(len(y))
#histx, xbins, Placeholder = plt.hist(y,weights = weights, bins = 100,fc=(0, 0, 1, 0.8), label = 'MADX')
#
#plt.legend()
##plt.yscale('log')
#ax1.set_yscale("log", nonposy='clip')
#
#
#
#
#
#
#
#ax = ax1.twinx()
#
#ax.plot(range(10),3*np.ones(len(range(10))),  'r.')
#
#r1 = patches.Rectangle((2,6.8), 313, 5, angle= -0.0861284, color = 'g')
#ax.add_patch(r1)
#
#plt.show()






#
#weights = np.transpose(100* np.ones_like([x,y])/float(primaries))
##H, xedges, yedges = np.histogram2d(x, y, bins=[300,300],weights = weights) #, weights = weights) #,cmap="viridis"
##myextent  =[xedges[0],xedges[-1],yedges[0],yedges[-1]]
#out = plt.hist2d(x,y, bins= 300,weights = weights, cmap="viridis")




#new = np.zeros([len(x),fluka.shape[1]])
#vec = np.zeros([1,fluka.shape[1]])
#for i in range(fluka.shape[1]):
#    vec[0,0:] = fluka[i,0:]
#    if vec[0,1] >= 3.5:
#        new = np.concatenate( (new, vec), axis = 0) 


#x = np.extract(fluka[0:,1]>3.7, fluka)
#
#new = np.zeros([len(x),fluka.shape[1]])
#idx = 0
#for i in range(len(x)):
#    if fluka[i,1] >= 3.5:
#        new[idx,0:] = fluka[i,0:]
#        idx = idx +1

        
        
        
        
        
#normfactor = 1
#
#fig = plt.figure()
#
#plt.clf()
#
#plt.subplot(121)
#
#plt.hist2d(fluka[0:1], fluka[0:3], bins=300, norm=LogNorm(),cmap="viridis")
#
#plt.subplot(122)
#plt.hist2d(new[0:1], new[0:3], bins=300, norm=LogNorm(),cmap="viridis")


#weights = 100* np.ones_like(y)/float(len(y))
#n, bins, patches =plt.hist(y,weights = weights, bins = 10, fc = (1,0,0, 0.5))
#
#weights = 100* np.ones_like(x)/float(len(x))
#plt.hist(x, weights = weights, bins = 100)



#histx[1][1] - histx[1][0]

#print sum(a[0])
#plt.yscale('log')
#results, edges = np.histogram(x, bins = 100, weights = weights)  
#results = results*100
 
 
#print sum(results)
#plt.yscale('log')
#binWidth = edges[1] - edges[0]
#plt.bar(edges[:-1], results*binWidth, binWidth, fc=(0, 0, 1, 0.8), label = 'MADX')

plt.show()




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
#import math
#septaColor = 'green'
#import matplotlib.pyplot as plt
##from ActiwizFluence import ActiwizFluence
##from ActiwizFluence import ActiwizFluencePlot
##import math
#import numpy as np
#
#plt.close()
#
#fig = plt.figure()
#ax1 = fig.add_subplot(1,1,1)
#
#x = np.random.rand(1000000)*1000
#
#results, edges = np.histogram(x, normed=True, bins = 40)    
#binWidth = edges[1] - edges[0]    
#
#x,y = results*binWidth, edges[:-1]
#
#x = edges[:-1]
#y = results*binWidth
#plt.bar(x, y, binWidth)   
#
#
##ax = fig.add_subplot(1,2,2)
#
##plt.barh(x, y, binWidth)   
##
#ax2 = ax1.twinx()
#
#import matplotlib.patches as patches
#
#
##Quads
#plt.axvline(x=0,linestyle = '--' ,label='Quadrupoles', color = 'black')
#plt.axvline(x=3199.77,linestyle = '--', color = 'black' )
#plt.axvline(x=6399.54,linestyle = '--', color = 'black' )
#plt.axvline(x=9599.31,linestyle = '--', color = 'black' )
#
##ZSs
#r1 = patches.Rectangle((355.45,6.8), 313,0.006, angle= -0.0861284)
#r2 = patches.Rectangle((746.45,6.212), 313,0.006, angle= -0.0861284)
#r3 = patches.Rectangle((1137.45,5.623), 313,0.006, angle= -0.0861284)
#r4 = patches.Rectangle((1528.45,5.035), 313,0.006, angle= -0.0861284)
#r5 = patches.Rectangle((1919.45,4.446), 313,0.006, angle= -0.0861284)
#ax2.add_patch(r1)
#ax2.add_patch(r2)
#ax2.add_patch(r3)
#ax2.add_patch(r4)
#ax2.add_patch(r5)
#
#
#
#
#plt.ylim(0,10)
#
#
#plt.show()

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
#
#tunnelVolume = 2.8*math.pow(10,8)
#cavernVolume = 6.82*math.pow(10,9)
#
##With first mask
#path = '//rpclustersrv1/cbjorkma/Dump studies/Uppstream Hole study/Fluence/Cavern_dir'
#data1 = ActiwizFluence(path, cavernVolume)
#
#path = '//rpclustersrv1/cbjorkma/Dump studies/Uppstream Hole study/Fluence/AirTunnel_dir'
#data2 = ActiwizFluence(path, tunnelVolume)
#
#Mask = []
#for i in range(len(data1)-1):
#    tmp = data1[i]
#    tmp[0:,2] = data1[i][0:,2] + data2[i][0:,2]
#    tmp[0:,3] = map(lambda x, y: math.sqrt( math.pow(x,2) + math.pow(y,2)), data1[i][0:,3], data2[i][0:,3])
#    Mask.append( tmp )
#Mask.append( data1[4])
#
#
##Without first mask
#path = '//rpclustersrv1/cbjorkma/Dump studies/Uppstream Hole study/Fluence/CavernNoMASK_dir'
#data1 = ActiwizFluence(path, cavernVolume)
#
#path = '//rpclustersrv1/cbjorkma/Dump studies/Uppstream Hole study/Fluence/AirTunnelNoMASK_dir'
#data2 = ActiwizFluence(path, tunnelVolume)
#
#NoMask = []
#for i in range(len(data1)-1):
#    tmp = data1[i]
#    tmp[0:,2] = data1[i][0:,2] + data2[i][0:,2]
#    tmp[0:,3] = map(lambda x, y: math.sqrt( math.pow(x,2) + math.pow(y,2)), data1[i][0:,3], data2[i][0:,3])
#    NoMask.append( tmp )
#NoMask.append( data1[4])
#
#
#
#
#
#
#
#prim = 2 *math.pow(10,18)
#
#fig = plt.figure()
#ax = plt.subplot(211)
#ActiwizFluencePlot(Mask, ax, prim)
#plt.title('With first mask', fontsize = 20)
##plt.ylim([math.pow(10,-9), 2*math.pow(10,-6)])
#
#
#ax = plt.subplot(212)
#ActiwizFluencePlot(NoMask, ax, prim)
#plt.title('Without first mask', fontsize = 20)
##plt.ylim([math.pow(10,-9), 2*math.pow(10,-6)])
#
#plt.show()
#
##Combination
#combo = []
#for i in range(len(Mask)-1):
#    tmp = Mask[i]
#    tmp[0:,2] = NoMask[i][0:,2] - Mask[i][0:,2] 
#    tmp[0:,3] = map(lambda x, y: math.sqrt( math.pow(x,2) + math.pow(y,2)), Mask[i][0:,3], NoMask[i][0:,3])
#    combo.append( tmp )
#combo.append( Mask[4])
#
#fig = plt.figure()
#ax = plt.subplot(111)
#ActiwizFluencePlot(Mask, ax, prim)
#plt.title('Difference plot / Additional hadrons to activate the ECX5 air volume when first mask is absent', fontsize = 20)
#plt.ylabel('Without Mask - With mask [cm-2]')
##plt.ylim([math.pow(10,-11), math.pow(10,-6)])
#
#
#
#plt.show()
#
#
#
#print 'Zsa1 = ' + str((680 + 342)/2 )
#print 'BLM1 = ' + str((680 + 342)/2 + 51)


















