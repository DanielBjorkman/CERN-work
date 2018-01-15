# -*- coding: utf-8 -*-
"""
Created on Mon Jan 08 13:53:27 2018

@author: cbjorkma
"""

import numpy as np
import os
import matplotlib.pyplot as plt
#from LossMap import readPhaseDirectory

plt.close()
plt.close()
plt.close()
from os import listdir
from os.path import isfile, join    
def readPhaseDirectory(path, identifier):



    onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]           
    files = filter(lambda x: x[-3:] == identifier , onlyfiles)             
    files = sorted(files)      
    
    print 'Found ' + str(len(files)) + ' files'
    
    data = []
    print "Attempting to load files..."    
    for i in range(len(files)): #
      
        filename = files[i]

        try:
            data.append( np.loadtxt(filename , skiprows = 1))
        except ValueError:
            print "Repairing " + filename
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
            data.append( np.loadtxt(filename , skiprows = 1))     
    
    out = data[0]
    for i in range(1,len(data)):
        out = np.concatenate( (out, data[i]), axis = 0)    
    print 'Data loaded'
    return out




## Run with inelastic interactions for ZS wires and adjusted density for wire ribbin
##----------------------------------------------------------------------
#path = "//rpclustersrv1/cluster_temp/cbjorkma/LSS2/Run Inelastic/AdjustedDensity"    
##os.chdir(path)        
##data = readPhaseDirectory(path, 'dat')    
#data = np.concatenate( (readPhaseDirectory(path, 'dat'), readPhaseDirectory(path, '.99')), axis = 0)    
#np.save('RuninelasticAdjustedDensity', data)
#fluka = np.load('RuninelasticAdjustedDensity.npy')
##primaries = 0.72*fluka.shape[0]
#
#
#normFluka = fluka.shape[0]
##  NCASE  IJ               PLA                 X                 Y                 Z               TXX               TYY               TZZ            WEIGHT LTRACK     ISAMPLE
#condition = fluka[0:,5] <= 2400
#subsetFluka = np.zeros([np.sum(condition),fluka.shape[1]])
#for i in range(fluka.shape[1]):
#    subsetFluka[0:,i] = np.extract(condition, fluka[0:,i])
#print 'Fluka Subset Created'
#fluka = subsetFluka
#
#np.save('flukasubsetZSonlyAdjustedDensity',fluka)
#fluka = np.load('flukasubsetZSonlyAdjustedDensity.npy')
##----------------------------------------------------------------------
#






directory = "//rpclustersrv1/cbjorkma/LSS2"
os.chdir(directory)


## Run with inelastic interactions for ZS wires and adjusted density for wire ribbin
#import pickle
#with open('LSS2_exp001_fort.99.pkl', 'rb') as f:
#    data = pickle.load(f)
#
##madxListed = data.values()
#
#keys = data.keys()
#print keys
#fluka = np.zeros([data.shape[0],3])
#
#for i in range(data.shape[0]):
#    fluka[0:,0] = data.X*100
#    fluka[0:,1] = data.Y*100
#    fluka[0:,2] = data.Z*100
#np.save('InelasticAdjustedDensity',fluka)

fluka = np.load('InelasticAdjustedDensity.npy')

normFluka = 20000000


#Index([u'TURN', u'X', u'PX', u'Y', u'PY', u'T', u'PT', u'S', u'E', u'ELEMENT'], dtype='object')
#madx = np.load('madxLost.npy')
#madx[0:,0] = 100*(madx[0:,0] - np.ones([madx.shape[0]])*1665.4231)
##madxPrim = madx.shape[0]
#
#condition = madx[0:,0] <= 2400
#subsetMADX = np.zeros([np.sum(condition),madx.shape[1]])
#for i in range(madx.shape[1]):
#    subsetMADX[0:,i] = np.extract(condition, madx[0:,i])
#print 'MADX subset Created'
#madx = subsetMADX
#np.save('madxsubsetZSonly',madx)


madx = np.load('madxsubsetZSonly.npy')

#madxPrim = madx.shape[0]
madxPrim = 10980000



## First run with inelastic interactions for ZS wires
##----------------------------------------------------------------------
#path = "//rpclustersrv1/cluster_temp/cbjorkma/LSS2/Run inelastic"   
#os.chdir(path)        
##data = readPhaseDirectory(path, 'dat')    
##data = np.concatenate( (readPhaseDirectory(path, 'dat'), readPhaseDirectory(path, '.99')), axis = 0)    
##np.save('Runinelastic', data)
##madx = np.load('Runinelastic.npy')
#fluka = np.load('Runinelastic.npy')
##primaries = 0.72*fluka.shape[0]
#
#
#normFluka = fluka.shape[0]
###  NCASE  IJ               PLA                 X                 Y                 Z               TXX               TYY               TZZ            WEIGHT LTRACK     ISAMPLE
##condition = fluka[0:,5] <= 2400
##subsetFluka = np.zeros([np.sum(condition),fluka.shape[1]])
##for i in range(fluka.shape[1]):
##    subsetFluka[0:,i] = np.extract(condition, fluka[0:,i])
##print 'Fluka Subset Created'
##fluka = subsetFluka
##
##np.save('flukasubsetZSonly',fluka)
#fluka = np.load('flukasubsetZSonly.npy')
##----------------------------------------------------------------------

from matplotlib.gridspec import GridSpec
gs = GridSpec(3, 2)







fig = plt.figure()

ax = fig.add_subplot(gs[0,0])

weights = 100* np.ones_like(madx[0:,2])/float(madxPrim)
histx, ybins, Placeholder = plt.hist(madx[0:,2],weights = weights, bins = 200,fc=(0, 0, 1, 0.8), label = 'Madx')


#yF = fluka[0:,4]
yF = fluka[0:,1]

weights = 100* np.ones_like(yF)/float(normFluka)
histy, ybins, Placeholder = plt.hist(yF,weights = weights, bins = ybins,color = 'red', label = 'Fluka',histtype = 'step',linewidth=2)

plt.title('Vertical distribution')
h = plt.ylabel('%')
h.set_rotation(0)
plt.xlabel('y [cm]')
plt.xlim(-0.4,0.4)


#ax.yaxis.set_visible(False)

plt.legend()
plt.grid(linewidth=0.2)


ax = fig.add_subplot(gs[0,1])

weights = 100* np.ones_like(madx[0:,1])/float(madxPrim)
histx, ybins, Placeholder = plt.hist(madx[0:,1],weights = weights, bins = 200,fc=(0, 0, 1, 0.8), label = 'Madx')


#yF = fluka[0:,4]
xF = fluka[0:,0]

weights = 100* np.ones_like(xF)/float(normFluka)
histy, ybins, Placeholder = plt.hist(xF,weights = weights, bins = ybins,color = 'red', label = 'Fluka',histtype = 'step',linewidth=2)

plt.title('Horizontal distribution')
h = plt.ylabel('%')
h.set_rotation(0)
plt.xlabel('x [cm]')
plt.xlim(4.15,7)
ax.set_yscale("log", nonposy='clip')

#ax.yaxis.set_visible(False)

plt.legend()
plt.grid(linewidth=0.2)







#ax1 = plt.subplot(3,2,2)
ax = fig.add_subplot(gs[1,0:2])


xM = madx[0:,0]
#zF = fluka[0:,5]   
zF = fluka[0:,2]   

weights = 100* np.ones_like(zF)/float(normFluka)
hist1, xbins, Placeholder = plt.hist(zF, weights = weights,bins = 50,fc=(1, 0, 0, 0.8), label = 'Fluka')
    
    
    
    #x = madx[0:,0]
weights = 100* np.ones_like(xM)/float(madxPrim)
hist2, xbins, Placeholder = plt.hist(xM,weights = weights, bins = xbins,fc=(0, 0, 1, 0.4), label = 'Madx')

h = plt.ylabel('%')
h.set_rotation(0)
#plt.title(histTitle)
#plt.ylabel('# Interactions')
#ax1.set_yscale("log", nonposy='clip')
plt.title('Distribution along Z, linear y-axis')
plt.grid(linewidth=0.2)
plt.xlabel('Z [cm]')    

plt.legend()


#ax2 = plt.subplot(3,2,5:6)
ax2 = fig.add_subplot(gs[2,0:2])

#xM = madx[0:,0]
#xF = fluka[0:,5]   

weights = 100* np.ones_like(zF)/float(normFluka)
hist1, xbins, Placeholder = plt.hist(zF, weights = weights,bins = 50,fc=(1, 0, 0, 0.8), label = 'Fluka')
    
    
    
    #x = madx[0:,0]
weights = 100* np.ones_like(xM)/float(madxPrim)
hist2, xbins, Placeholder = plt.hist(xM,weights = weights, bins = xbins,fc=(0, 0, 1, 0.4), label = 'Madx')

h = plt.ylabel('%')
h.set_rotation(0)
#plt.title(histTitle)
#plt.ylabel('# Interactions')
ax2.set_yscale("log", nonposy='clip')
plt.title('Distribution along Z, logged y-axis',x=0.25)
plt.grid(linewidth=0.2)
plt.xlabel('Z [cm]')    

plt.legend()







plt.suptitle('ZS wire septa interaction comparison', fontsize=20)
plt.show()







