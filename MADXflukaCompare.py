# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 17:00:05 2017

@author: cbjorkma
"""

#MADXflukaCompare

import os
import numpy as np
import math
from matplotlib.colors import LogNorm
from matplotlib.gridspec import GridSpec
import matplotlib.pyplot as plt
import matplotlib.ticker as tk

directory = "//rpclustersrv1/cbjorkma/LSS2"
os.chdir(directory)

plt.close()
plt.close()
plt.close()
##load MADX------------------------------
#
#
#import pickle
#with open('data_tpst.pkl', 'rb') as f:
#    data = pickle.load(f)
#   
#
#madxListed = data.values()
#
#keys = data.keys()
#
#madx = np.zeros([len(madxListed[0]),5])
#
#for i in range(len(madxListed)):
#    madx[0:,i] = madxListed[i]
#
#np.save('madx',madx)
##------------------------------------------------

madx = np.load('madx.npy')





path = "//rpclustersrv1/cbjorkma/LSS2/run09"          
os.chdir(path)        
#fluka1 = readPhaseDirectory(path)           
#np.save('run09', fluka1)
#  


  
#filename = 'LSS2_exp001_fort.90' 
##filename = 'fort.90' 
  
fluka = np.load('run09.npy')
    
end = int(1*fluka.shape[0])

#print 'Plotting ' + str(end) + ' primaries'

primaries = fluka.shape[0]

#Temporary code
madxPrim = madx.shape[0]*10


##Horizontal phace space--------------------------------------------------------------
fig = plt.figure()


plt.suptitle('Horizontal phase space, overview', fontsize=22)


gs = GridSpec(6,8)




#Fluka-----------------------------
x = fluka[0:,1]
y = fluka[0:,3]

ax = fig.add_subplot(gs[1:4,0:3])

plt.hist2d(x, y, bins=200, norm=LogNorm(),cmap="viridis")

#Zoom
#ymin, ymax = 0.0003 ,0.0033
#xmin, xmax = 0.0367*100, 0.11*100

#Overview
ymin, ymax = -0.003 ,0.0033
xmin, xmax = -0.05*100, 0.11*100

plt.ylim(ymin, ymax)
plt.xlim(xmin, xmax)

plt.xlabel('x [cm]', fontsize=12)
h = plt.ylabel("$x^p$", fontsize=18)
h.set_rotation(0)
plt.grid()
#plt.colorbar()

textstr = 'Primaries: ' + str(end)
props = dict(boxstyle='round', facecolor='white', alpha=1)

ax.text(0.05, 0.95, textstr, transform=ax.transAxes, fontsize=14,
        verticalalignment='top',bbox=props) 

ax_marg_x = fig.add_subplot(gs[0,0:3])

plt.title('Fluka',fontsize=18)




#weights = np.ones_like(x)/float(primaries)
#results, edges = np.histogram(x, bins = 100, weights = weights)  
#results = results*100
##results, edges = np.histogram(x, normed=primaries, bins = 60)    
#print 'sum ' + str(sum(results))
#binWidth = edges[1] - edges[0]
#binWidthX = binWidth  
#plt.bar(edges[:-1], results*binWidth, binWidth,fc=(1, 0, 0, 1))   
#


weights = 100* np.ones_like(x)/float(primaries)
histx = plt.hist(x,weights = weights, bins = 100,fc=(1, 0, 0, 1))
binWidthX = histx[1][1] - histx[1][0]


plt.xlim(xmin, xmax )
plt.yscale('log')

plt.tick_params(
    axis='x',          # changes apply to the x-axis
    bottom='off',      # ticks along the bottom edge are off
    labelbottom='off') # labels along the bottom edge are off
h = plt.ylabel('%')
h.set_rotation(0)

plt.grid()




ax = fig.add_subplot(gs[1:4,3])
#
#weights = np.ones_like(y)/float(primaries)
#results, edges = np.histogram(y, bins = 100, weights = weights)  
#results = results*100
#print 'sum ' + str(sum(results))
#
##results, edges = np.histogram(y, normed=primaries, bins = 60)    
#binWidth = edges[1] - edges[0]
#binWidthY = binWidth 
#plt.barh(edges[:-1], results*binWidth , binWidth,fc=(1, 0, 0, 1)) 

weights = 100* np.ones_like(y)/float(primaries)
histy = plt.hist(y,weights = weights, bins = 100, orientation='horizontal',fc=(1, 0, 0, 1))
binWidthY = histy[1][1] - histy[1][0]

  
plt.ylim(ymin, ymax )
plt.xscale('log')
plt.xlabel('%')
ax.tick_params(labelsize=10)
plt.grid()

plt.setp( ax.get_yticklabels(), visible=False)

#---------------------------------------------------------------




#MADX-----------------------------------------------------------
x = madx[0:,2]*100
y = madx[0:,3]

ax = fig.add_subplot(gs[1:4,4:7])

plt.hist2d(x, y, bins=400, norm=LogNorm(),cmap="viridis")
plt.ylim(ymin, ymax)
plt.xlim(xmin, xmax)
plt.xlabel('x [cm]', fontsize=12)
plt.grid()
plt.setp( ax.get_yticklabels(), visible=False) 
textstr = 'Data points: ' + str(madx.shape[0])
ax.text(0.05, 0.95, textstr, transform=ax.transAxes, fontsize=14,
        verticalalignment='top',bbox=props)                


              
ax_marg_x = fig.add_subplot(gs[0,4:7])

plt.title('MADX',fontsize=18)


spectrum = max(x) - min(x)
#print spectrum
binstoBeUsed = round(spectrum / binWidthX  )
weights = 100* np.ones_like(x)/float(madxPrim)
plt.hist(x,weights = weights, bins = binstoBeUsed)
#weights = np.ones_like(x)/float(madxPrim)
#results, edges = np.histogram(x, bins = binstoBeUsed, weights = weights)  
#results = results*100
#print 'sum ' + str(sum(results))
##results, edges = np.histogram(x, normed=madxPrim, bins = binstoBeUsed)    
#binWidth = edges[1] - edges[0]
#
#plt.bar(edges[:-1], results*binWidth, binWidth,fc=(0, 0, 1, 1))   





plt.xlim(xmin, xmax )
plt.yscale('log')

plt.tick_params(
    axis='x',          # changes apply to the x-axis
    bottom='off',      # ticks along the bottom edge are off
    labelbottom='off') # labels along the bottom edge are off
h = plt.ylabel('%')
h.set_rotation(0)

plt.grid()




ax = fig.add_subplot(gs[1:4,7])
#
spectrum = max(y) - min(y)
binstoBeUsed = round(spectrum / binWidthY  )

#weights = np.ones_like(y)/float(madxPrim)
#results, edges = np.histogram(y, bins = binstoBeUsed, weights = weights)  
#results = results*100
#print 'sum ' + str(sum(results))
##results, edges = np.histogram(y, normed=madxPrim, bins = binstoBeUsed)    
#binWidth = edges[1] - edges[0]    
#
#plt.barh(edges[:-1], results*binWidth , binWidth,fc=(0, 0, 1, 1))   
weights = 100* np.ones_like(y)/float(madxPrim)
#plt.hist(y,weights = weights, bins = binstoBeUsed)
histy = plt.hist(y,weights = weights, bins = binstoBeUsed, orientation='horizontal')


plt.ylim(ymin, ymax )
plt.xscale('log')
plt.xlabel('%')
ax.tick_params(labelsize=10)
plt.grid()

plt.setp( ax.get_yticklabels(), visible=False)




#1D Histogram comparisons--------------------------------------



#Fluka-----------------------------
xF = fluka[0:end,1]
yF = fluka[0:end,3]

#MADX----------------------
xM = madx[0:,2]*100
yM = madx[0:,3]





fig.add_subplot(gs[5,0:3])

spectrum = max(xM) - min(xM)
binstoBeUsed = round(spectrum / binWidthX  )

weights = 100* np.ones_like(xM)/float(madxPrim)
#plt.hist(y,weights = weights, bins = binstoBeUsed)
plt.hist(xM,weights = weights, bins = binstoBeUsed, label = 'MADX')



#results, edges = np.histogram(xM, normed=madxPrim, bins = binstoBeUsed)    
#weights = np.ones_like(xM)/float(madxPrim)
#results, edges = np.histogram(xM, bins = binstoBeUsed, weights = weights)  
#results = results*100
#
#binWidth = edges[1] - edges[0]
#print 'sum ' + str(sum(results))
#plt.bar(edges[:-1], results*binWidth, binWidth, fc=(0, 0, 1, 0.8), label = 'MADX')




spectrum = max(xF) - min(xF)
binstoBeUsed = round(spectrum / binWidthX  )

#weights = np.ones_like(xF)/float(primaries)
#results, edges = np.histogram(xF, bins = 100, weights = weights)  
#results = results*100
##results, edges = np.histogram(xF, normed=primaries, bins = binstoBeUsed)    
#binWidth = edges[1] - edges[0]
##print binWidth / binWidthX
#plt.bar(edges[:-1], results*binWidth, binWidth, fc=(1, 0, 0, 0.5), label = 'Fluka')

weights = 100* np.ones_like(xF)/float(primaries)
#plt.hist(y,weights = weights, bins = binstoBeUsed)
plt.hist(xF,weights = weights, bins = binstoBeUsed, fc = (1,0,0,0.5), label = 'Fluka')






plt.xlim(xmin, xmax )
plt.yscale('log')
h = plt.ylabel('%')
h.set_rotation(0)

plt.xlabel('x [cm]', fontsize=12)
plt.title('Position comparison')
plt.legend()
plt.grid()

#textstr = 'Position comparison'

#ax.text(0.05, 1.0, textstr, transform=ax.transAxes, fontsize=14,
#        verticalalignment='top',bbox=props)      



fig.add_subplot(gs[5,4:7])

spectrum = max(yM) - min(yM)
binstoBeUsed = round(spectrum / binWidthY  )

##results, edges = np.histogram(yM, normed=madxPrim, bins = binstoBeUsed)    
#weights = np.ones_like(yM)/float(madxPrim)
#results, edges = np.histogram(yM, bins = binstoBeUsed, weights = weights)  
#results = results*100
#binWidth = edges[1] - edges[0]
##print binWidth / binWidthY 
#plt.bar(edges[:-1], results*binWidth, binWidth, fc=(0, 0, 1, 0.8), label = 'MADX')
#
weights = 100* np.ones_like(yM)/float(madxPrim)
#plt.hist(y,weights = weights, bins = binstoBeUsed)
plt.hist(yM,weights = weights, bins = binstoBeUsed, label = 'MADX')





spectrum = max(yF) - min(yF)
binstoBeUsed = round(spectrum / binWidthY  )

#weights = np.ones_like(yF)/float(primaries)
#results, edges = np.histogram(yF, bins = binstoBeUsed, weights = weights)  
#results = results*100
##results, edges = np.histogram(yF, normed=primaries, bins = binstoBeUsed)    
#binWidth = edges[1] - edges[0]    
##print binWidth / binWidthY
#plt.bar(edges[:-1], results*binWidth, binWidth, fc=(1, 0, 0, 0.5), label = 'Fluka')


weights = 100* np.ones_like(yF)/float(primaries)
#plt.hist(y,weights = weights, bins = binstoBeUsed)
plt.hist(yF,weights = weights, bins = binstoBeUsed, fc = (1,0,0,0.5), label = 'Fluka')


plt.xlim(ymin, ymax )
plt.yscale('log')
#h = plt.ylabel('%')
#h.set_rotation(0)
plt.xlabel("$x^p$", fontsize=18)
plt.grid()

plt.title('Angle comparison')
plt.legend()
#textstr = 'Angle comparison'


#ax.text(0.05, 0.0, textstr, transform=ax.transAxes, fontsize=14,
#        verticalalignment='top',bbox=props)   






plt.show()





#--------------------------------------------------------------------
#--------------------------------------------------------------------
#--------------------------------------------------------------------
#--------------------------------------------------------------------
#--------------------------------------------------------------------
#--------------------------------------------------------------------
#--------------------------------------------------------------------

#
#
###Verticall phace space--------------------------------------------------------------
#fig = plt.figure()
#
#
#plt.suptitle('Vertical phase space, overview', fontsize=22)
#
#
#gs = GridSpec(6,8)
#
#
##Fluka-----------------------------
#x = fluka[0:end,2]
#y = fluka[0:end,4]
#
#ax = fig.add_subplot(gs[1:4,0:3])
#
#plt.hist2d(x, y, bins=250, norm=LogNorm(),cmap="viridis")
#
#ymin, ymax = -0.00065 ,0.0006
#xmin, xmax = -2,2
#
#plt.ylim(ymin, ymax)
#plt.xlim(xmin, xmax)
#
#plt.xlabel('y [cm]', fontsize=12)
#h = plt.ylabel("$y^p$", fontsize=18)
#h.set_rotation(0)
#plt.grid()
##plt.colorbar()
#
#textstr = 'Primaries: ' + str(end)
#props = dict(boxstyle='round', facecolor='white', alpha=1)
#
#ax.text(0.65, 0.95, textstr, transform=ax.transAxes, fontsize=14,
#        verticalalignment='top',bbox=props) 
#
#ax_marg_x = fig.add_subplot(gs[0,0:3])
#
#plt.title('Fluka',fontsize=18)
#spectrum = max(x) - min(x)
#binstoBeUsed = round(spectrum / binWidthX  )
#
#results, edges = np.histogram(x, normed=madxPrim, bins = binstoBeUsed)    
#binWidth = edges[1] - edges[0]
#print binWidth / binWidthX   
#plt.bar(edges[:-1], results*binWidth, binWidth,fc=(1, 0, 0, 1))   
#plt.xlim(xmin, xmax )
#plt.yscale('log')
#
#plt.tick_params(
#    axis='x',          # changes apply to the x-axis
#    bottom='off',      # ticks along the bottom edge are off
#    labelbottom='off') # labels along the bottom edge are off
##h = plt.ylabel('%')
##h.set_rotation(0)
#
#plt.grid()
#
#
#
#
#ax = fig.add_subplot(gs[1:4,3])
##
#
#spectrum = max(y) - min(y)
#binstoBeUsed = round(spectrum / binWidthY  )
#
#results, edges = np.histogram(y, normed=madxPrim, bins = binstoBeUsed)    
#binWidth = edges[1] - edges[0]    
#print binWidth / binWidthY 
#plt.barh(edges[:-1], results*binWidth , binWidth,fc=(1, 0, 0, 1))   
#plt.ylim(ymin, ymax )
#plt.xscale('log')
##plt.xlabel('%')
#ax.tick_params(labelsize=10)
#plt.grid()
#
#plt.setp( ax.get_yticklabels(), visible=False)
#
##---------------------------------------------------------------
#
#
#
#
##MADX-----------------------------------------------------------
#x = madx[0:,1]*100
#y = madx[0:,4]
#
#ax = fig.add_subplot(gs[1:4,4:7])
#
#plt.hist2d(x, y, bins=250, norm=LogNorm(),cmap="viridis")
#plt.ylim(ymin, ymax)
#plt.xlim(xmin, xmax)
#
#plt.xlabel('y [cm]', fontsize=12)
##h = plt.ylabel("$p^p$", fontsize=18)
##h.set_rotation(0)
#plt.grid()
##plt.colorbar()
#plt.setp( ax.get_yticklabels(), visible=False)
#    
#textstr = 'Data points: ' + str(madx.shape[0])
#
#ax.text(0.65, 0.95, textstr, transform=ax.transAxes, fontsize=14,
#        verticalalignment='top',bbox=props)                
#                
#ax_marg_x = fig.add_subplot(gs[0,4:7])
#
#plt.title('MADX',fontsize=18)
#
#spectrum = max(x) - min(x)
#binstoBeUsed = round(spectrum / binWidthX  )
#
#results, edges = np.histogram(x, normed=madxPrim, bins = binstoBeUsed)    
#binWidth = edges[1] - edges[0]
#print binWidth / binWidthX   
#plt.bar(edges[:-1], results*binWidth, binWidth,fc=(0, 0, 1, 1))   
#plt.xlim(xmin, xmax )
#plt.yscale('log')
#
#plt.tick_params(
#    axis='x',          # changes apply to the x-axis
#    bottom='off',      # ticks along the bottom edge are off
#    labelbottom='off') # labels along the bottom edge are off
##h = plt.ylabel('%')
##h.set_rotation(0)
#
#plt.grid()
#
#
#
#
#ax = fig.add_subplot(gs[1:4,7])
##
#spectrum = max(y) - min(y)
#binstoBeUsed = round(spectrum / binWidthY  )
#
#results, edges = np.histogram(y, normed=madxPrim, bins = binstoBeUsed)    
#binWidth = edges[1] - edges[0]    
#print binWidth / binWidthY   
#plt.barh(edges[:-1], results*binWidth , binWidth,fc=(0, 0, 1, 1))   
#plt.ylim(ymin, ymax )
#plt.xscale('log')
##plt.xlabel('%')
#ax.tick_params(labelsize=10)
#plt.grid()
#
#plt.setp( ax.get_yticklabels(), visible=False)
#
#
#
#
##1D Histogram comparisons--------------------------------------
#
#
#
##Fluka-----------------------------
#xF = fluka[0:end,2]
#yF = fluka[0:end,4]
#
##MADX
#xM = madx[0:,1]*100
#yM = madx[0:,4]
#
#fig.add_subplot(gs[5,0:3])
#
#spectrum = max(xM) - min(xM)
#binstoBeUsed = round(spectrum / binWidthX  )
#
#results, edges = np.histogram(xM, normed=madxPrim, bins = binstoBeUsed)    
#binWidth = edges[1] - edges[0]
#print binWidth / binWidthX
#plt.bar(edges[:-1], results*binWidth, binWidth, fc=(0, 0, 1, 0.8), label = 'MADX')
#
#
#
#
#spectrum = max(xF) - min(xF)
#binstoBeUsed = round(spectrum / binWidthX  )
#
#results, edges = np.histogram(xF, normed=primaries, bins = binstoBeUsed)    
#binWidth = edges[1] - edges[0]
#print binWidth / binWidthX
#plt.bar(edges[:-1], results*binWidth, binWidth, fc=(1, 0, 0, 0.5), label = 'Fluka')
#
#plt.xlim(xmin, xmax )
#plt.yscale('log')
##h = plt.ylabel('%')
##h.set_rotation(0)
#
#plt.xlabel('y [cm]', fontsize=12)
#plt.title('Position comparison')
#plt.legend()
#plt.grid()
#
##textstr = 'Position comparison'
#
##ax.text(0.05, 1.0, textstr, transform=ax.transAxes, fontsize=14,
##        verticalalignment='top',bbox=props)      
#
#
#
#fig.add_subplot(gs[5,4:7])
#
#
#spectrum = max(yM) - min(yM)
#binstoBeUsed = round(spectrum / binWidthY  )
#
#results, edges = np.histogram(yM, normed=madxPrim, bins = binstoBeUsed)    
#binWidth = edges[1] - edges[0]
#print binWidth / binWidthY 
#plt.bar(edges[:-1], results*binWidth, binWidth, fc=(0, 0, 1, 0.8), label = 'MADX')
#
#
#spectrum = max(yF) - min(yF)
#binstoBeUsed = round(spectrum / binWidthY  )
#
#results, edges = np.histogram(yF, normed=primaries, bins = binstoBeUsed)    
#binWidth = edges[1] - edges[0]    
#print binWidth / binWidthY
#plt.bar(edges[:-1], results*binWidth, binWidth, fc=(1, 0, 0, 0.5), label = 'Fluka')
#
#
#plt.xlim(ymin, ymax )
#plt.yscale('log')
##h = plt.ylabel('%')
##h.set_rotation(0)
#plt.xlabel("$y^p$", fontsize=18)
#plt.grid()
#
#plt.title('Angle comparison')
#plt.legend()
##textstr = 'Angle comparison'
#
#
##ax.text(0.05, 0.0, textstr, transform=ax.transAxes, fontsize=14,
##        verticalalignment='top',bbox=props)   
#
#
#
#
#
#
#plt.show()
#








