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



#from Phasespaceplot import readPhaseDirectory

def readPhaseDirectory(path):

    from os import listdir
    from os.path import isfile, join       
    
    onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]           
    files = filter(lambda x: x[-3:] == '.90' , onlyfiles)             
    files = sorted(files)      
    
    print 'Found ' + str(len(files)) + ' files'
    
    data = []
    os.chdir(path)
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





directory = "//rpclustersrv1/cbjorkma/LSS2"
os.chdir(directory)

plt.close()
plt.close()
#plt.clf()
#plt.close()
##load MADX------------------------------
#
##
#import pickle
#with open('data_tpst.pkl', 'rb') as f:
#    data = pickle.load(f)
#   
#
#madxListed = data.values()
#
#keys = data.keys()
#print keys
#madx = np.zeros([len(madxListed[0]),5])
#
#for i in range(len(madxListed)):
#    madx[0:,i] = madxListed[i]
#
#np.save('madx',madx)
##------------------------------------------------
#Keys = [>> >'ptdata', 'ydata', 'xdata', 'pxdata', 'pydata']

madx = np.load('madx.npy')






#print 'Creating subset'
#condition = fluka[0:,1] >= 3.716
#subsetFluka = np.zeros([np.sum(condition),fluka.shape[1]])
#for i in range(fluka.shape[1]):
#    subsetFluka[0:,i] = np.extract(condition, fluka[0:,i])
#print 'Subset Created'
#np.save('PCgreaterthan3.716', subsetFluka)
#fluka = np.load('PCgreaterthan3.716.npy')








#Pycollimate Study--------------------------------------------------
#path = "//rpclustersrv1/cbjorkma/LSS2/PyCollimateStudy/NoPC"
###madx = readPhaseDirectory(path) 
###np.save('NoPC', madx)
#os.chdir(path)
#madx = np.load('NoPc.npy')


#path = "//rpclustersrv1/cbjorkma/LSS2/PyCollimateStudy/UsingPC"
##fluka = readPhaseDirectory(path)
##np.save('UsingPC', fluka)
#os.chdir(path)
#fluka = np.load('UsingPc.npy')
#primaries = fluka.shape[0]
#------------------------------------------------------------------------



path = "//rpclustersrv1/cbjorkma/LSS2/Run Inelastic"
#fluka = readPhaseDirectory(path)
#np.save('UsingPC', fluka)
os.chdir(path)
fluka = np.load('90.npy')
primaries = fluka.shape[0]






#path = "//rpclustersrv1/cbjorkma/LSS2/run09"          
#os.chdir(path)        
#fluka1 = readPhaseDirectory(path)           
#np.save('run09', fluka1)
#  


#path = "//rpclustersrv1/cbjorkma/LSS2/run09"   
###filename = 'LSS2_exp001_fort.90' 
####filename = 'fort.90' 
#os.chdir(path)
#madx = np.load('run09.npy')
    
end = int(1*fluka.shape[0])

#print 'Plotting ' + str(end) + ' primaries'





#primaries = fluka.shape[0]

madxPrim = 10980000 

#madxPrim = madx.shape[0]

##Normal Setup
#zoom = 0
#spatial = 0
#title1 = '200 um Ribbon'
#title2 = 'Aligned Wires'
#ylabel = ["$x^p$" , "$y^p$"]
#xlabel = ['x [cm]', 'y [cm]']
#histTitle1 = 'Position comparison'
#histTitle2 = 'Angle comparison'


zoom = 1
spatial = 0
title1 = '200 um Ribbon'
title2 = 'MADX'
ylabel = ["$x^p$" , "$y^p$"]
xlabel = ['x [cm]', 'y [cm]']
histTitle1 = 'Position comparison'
histTitle2 = 'Angle comparison'



##Spatial
spatial = 0
##title1 = 'Fluka subset, 200 um ribbon'
##title2 = 'MADX'
#ylabel = ["y [cm]"]
#xlabel = ['x [cm]']
#histTitle1 = 'X comparison'
#histTitle2 = 'Y comparison'


print 'Displayed Particles = ' +str(float(fluka.shape[0])/primaries)
for i in range(1): #range(2 - spatial):


#Normal    
    if i == 0:
    #Fluka-----------------------------
        xF = fluka[0:,1]
        yF = fluka[0:,3]
        
        #MADX----------------------
        xM = madx[0:,2]*100
        yM = madx[0:,3]
    else:
        xF = fluka[0:,2]
        yF = fluka[0:,4]
        
        #MADX----------------------
        xM = madx[0:,1]*100
        yM = madx[0:,4]       
#MADX Keys = [>> >'ptdata', 'ydata', 'xdata', 'pxdata', 'pydata']    
# FLuka # IJ               X               Y              CX              CY            PTOT     ISAMPLE  LLOUSE   

#Spatial
    if spatial:
        xF = fluka[0:,1]
        yF = fluka[0:,2]
    
        xM = madx[0:,1]#*100
        yM = madx[0:,2]#*100



##Start plotting------------------------------------------------------
    fig = plt.figure()
    fig.patch.set_facecolor('white')
    if i == 0:
        if zoom == 0:
            plt.suptitle('Horizontal phase space, overview', fontsize=22)
        else:
            plt.suptitle('Horizontal phase space, zoom', fontsize=22)
    else:
        plt.suptitle('Vertical phase space, overview', fontsize=22)    


    if spatial:
        plt.suptitle('Spatial distribution', fontsize=22) 
        
        
    gs = GridSpec(18,8)
    
    
    
    
#    #Fluka-----------------------------
#    if i == 0:
#        x = fluka[0:,1]
#        y = fluka[0:,3]
#    else:
#        x = fluka[0:,2]
#        y = fluka[0:,4]    

#    if i == 0:
#        x = fluka[0:,1]
#        y = fluka[0:,2]


    
    ax = fig.add_subplot(gs[3:11,0:3])
    
    
  #  weights = 100* np.ones_like([x,y])/float(primaries)
   # H, xedges, yedges = np.histogram2d(x, y, bins=300, weights = weights) #,cmap="viridis"
    out = plt.hist2d(xF,yF, bins=300,norm = LogNorm() ,cmap="viridis") #,cmap="viridis"
    xedges = out[1]
    yedges = out[2]
    
    if i == 0:
        if zoom:
            #Zoom
            ymin, ymax = 0.0003 ,0.0033
            xmin, xmax = 0.0367*100, 0.11*100
        else:
            #Overview
            ymin, ymax = -0.003 ,0.0033
            xmin, xmax = -0.05*100, 0.11*100
    else:
        ymin, ymax = -0.00065 ,0.0006
        xmin, xmax = -2,2    
        
    if spatial:
       #Spatial
        ymin, ymax = -2 ,2
        #xmin, xmax = 3.716, 8        
        xmin, xmax = -2.5, 8    
        
    plt.ylim(ymin, ymax)
    plt.xlim(xmin, xmax)
    
    
    plt.xlabel(xlabel[i], fontsize=12)
    h = plt.ylabel(ylabel[i], fontsize=18)    
    
    
#    if i == 0:
#        plt.xlabel('x [cm]', fontsize=12)
#        h = plt.ylabel("$x^p$", fontsize=18)
#    else:
#        plt.xlabel('y [cm]', fontsize=12)
#        h = plt.ylabel("$y^p$", fontsize=18)

#    plt.xlabel('x [cm]', fontsize=12)
#    h = plt.ylabel("$y$", fontsize=18)        
    
    h.set_rotation(0)
    plt.grid()
    #plt.colorbar()
    
    textstr = 'Primaries: ' + str(float(primaries)/1000000) + ' million'
    props = dict(boxstyle='round', facecolor='white', alpha=1)
    
    if i == 0:
        ax.text(0.05, 0.95, textstr, transform=ax.transAxes, fontsize=14,
            verticalalignment='top',bbox=props) 
    else:
        ax.text(0.50, 0.95, textstr, transform=ax.transAxes, fontsize=14,
                verticalalignment='top',bbox=props)                
    
    ax_marg_x = fig.add_subplot(gs[0:3,0:3])

    plt.title(title1,fontsize=18)    
#    plt.title('Fluka subset (x>3.716), 200um ribbon and PyCollimate',fontsize=18)
 #   plt.title('With PyCollimate',fontsize=18)
#    plt.title('200 um ribbon ZS septa',fontsize=18)    
    
    
    weights = 100* np.ones_like(xF)/float(primaries)
    histx, xbins, patches = plt.hist(xF,weights = weights, bins = 100,fc=(1, 0, 0, 1))
   # binWidthX = histx[1][1] - histx[1][0]
    
    
    plt.xlim(xmin, xmax )
    ax_marg_x.set_yscale("log", nonposy='clip')
    
    plt.tick_params(
        axis='x',          # changes apply to the x-axis
        bottom='off',      # ticks along the bottom edge are off
        labelbottom='off') # labels along the bottom edge are off
    h = plt.ylabel('%')
    h.set_rotation(0)
    
    plt.grid()
    
    
    
    
    ax = fig.add_subplot(gs[3:11,3])
    fig = plt.figure()
    weights = 100* np.ones_like(yF)/float(primaries)
    histy, ybins, patches = plt.barh(yF,weights = weights, bins = 100,fc=(1, 0, 0, 1))
 #   histy, ybins, patches = plt.hist(yF,weights = weights, bins = 100, orientation='horizontal',fc=(1, 0, 0, 1))
    #binWidthY = histy[1][1] - histy[1][0]
    
      
    plt.ylim(ymin, ymax )
    #ax.set_xscale("log", nonposy='clip')
    plt.xscale('log')
    plt.xlabel('%')
    #ax.tick_params(labelsize=10)
    plt.grid()
    
    #plt.setp( ax.get_yticklabels(), visible=False)
    
    
    
    #---------------------------------------------------------------
    
    
    
    
#    #MADX-----------------------------------------------------------


#    if i == 0:
#        x = madx[0:,2]*100
#        y = madx[0:,3]
#    else:
#        x = madx[0:,1]*100
#        y = madx[0:,4]

#    x = madx[0:,2]*100
#    y = madx[0:,1]*100
#    if i == 0:
#        x = madx[0:,1]
#        y = madx[0:,3]
#    else:
#        x = madx[0:,2]
#        y = madx[0:,4]        
    
    ax = fig.add_subplot(gs[3:11,4:7])
    
  #  weights = 100* np.ones_like([x,y])/float(primaries)
  #  np.histogram2d(x, y, bins=(xedges, yedges), weights = weights) #,cmap="viridis"
 #   plt.hist2d(x,y, bins=300,normed = True,cmap="viridis")    
    plt.hist2d(xM,yM, bins=[xedges , yedges],norm = LogNorm(),cmap="viridis")    


    plt.ylim(ymin, ymax)
    plt.xlim(xmin, xmax)
#    if i == 0:
#        plt.xlabel('x [cm]', fontsize=12)
#    else:
#        plt.xlabel('y [cm]', fontsize=12)
    plt.xlabel(xlabel[i], fontsize=12)    
 #   plt.xlabel('x [cm]', fontsize=12)
  #  h = plt.ylabel("$x^p$", fontsize=18)        
        
    plt.grid()
    plt.setp( ax.get_yticklabels(), visible=False) 
 #   textstr = 'Data points: ' + str(madx.shape[0])
    textstr = 'Primaries: ' + str(float(madxPrim)/1000000) + ' million'
    
    if i == 0:
        ax.text(0.05, 0.95, textstr, transform=ax.transAxes, fontsize=14,
            verticalalignment='top',bbox=props) 
    else:
        ax.text(0.50, 0.95, textstr, transform=ax.transAxes, fontsize=14,
                verticalalignment='top',bbox=props)                
    
    
                  
    ax_marg_x = fig.add_subplot(gs[0:3,4:7])
    
    plt.title(title2,fontsize=18)
#    plt.title('WITHOUT',fontsize=18)    
 #   plt.title('Aligned wire ZS septa',fontsize=18)     

    
#    spectrum = max(x) - min(x)
    #print spectrum
#    binstoBeUsed = round(spectrum / binWidthX  )
    weights = 100* np.ones_like(xM)/float(madxPrim)
    plt.hist(xM,weights = weights, bins = xbins)
    
    
    
    
    
    plt.xlim(xmin, xmax )
    ax_marg_x.set_yscale("log", nonposy='clip')
    
    plt.tick_params(
        axis='x',          # changes apply to the x-axis
        bottom='off',      # ticks along the bottom edge are off
        labelbottom='off') # labels along the bottom edge are off
    h = plt.ylabel('%')
    h.set_rotation(0)
    
    plt.grid()
    
    
    
    
    ax = fig.add_subplot(gs[3:11,7])
    #fig = plt.figure()
 #   spectrum = max(y) - min(y)
#    binstoBeUsed = round(spectrum / binWidthY  )
    
    
    weights = 100* np.ones_like(yM)/float(madxPrim)
    #plt.hist(y,weights = weights, bins = binstoBeUsed)
    histy = plt.hist(yM,weights = weights, bins = ybins, orientation='horizontal')
    
    
    plt.ylim(ymin, ymax )
    ax.set_xscale("log", nonposy='clip')
    plt.xlabel('%')
    ax.tick_params(labelsize=10)
    plt.grid()
    
    #plt.setp( ax.get_yticklabels(), visible=False)
    
    
    
    
    #1D Histogram comparisons--------------------------------------
    

    ax = fig.add_subplot(gs[12:16,0:3])
    

    
    weights = 100* np.ones_like(xM)/float(madxPrim)
    #plt.hist(y,weights = weights, bins = binstoBeUsed)
    histxM, xbinsM, patchesM = plt.hist(xM,weights = weights, bins = xbins, label = title2)
 #   plt.hist(xM,weights = weights, bins = xbins, label = 'WITHOUT')    
#    plt.hist(xM,weights = weights, bins = xbins, label = 'Wires') 

    
 #   spectrum = max(xF) - min(xF)
 #   binstoBeUsed = round(spectrum / binWidthX  )
    
    
    weights = 100* np.ones_like(xF)/float(primaries)
    #plt.hist(y,weights = weights, bins = binstoBeUsed)
    histxF, xbinsF, patchesF = plt.hist(xF,weights = weights, bins = xbins, fc = (1,0,0,0.5), label = title1)
 #   plt.hist(xF,weights = weights, bins = xbins, fc = (1,0,0,0.5), label = 'Using PyCollimate')    
  #  plt.hist(xF,weights = weights, bins = xbins, fc = (1,0,0,0.5), label = '200 um ribbon')        
    ax.set_yscale("log", nonposy='clip')
    plt.xlim(xmin, xmax )

    h = plt.ylabel('%')
    h.set_rotation(0)
    plt.title(histTitle1)
    plt.legend(prop={'size': 12})
    plt.grid()
    plt.ylim((None, 100))    
    plt.tick_params(
        axis='x',          # changes apply to the x-axis
        bottom='off',      # ticks along the bottom edge are off
        labelbottom='off') # labels along the bottom edge are off

                    
                    
    fig.add_subplot(gs[16:,0:3])

    
    binwidth = xbinsM[1] - xbinsM[0]
    plt.bar( xbinsM[:-1], histxM/histxF,binwidth, label = title2 +'/' + title1, color = 'darkcyan')    
    plt.xlim(xmin, xmax )
    plt.grid()
    plt.plot(range(-20,20), np.ones(len(range(-20,20))), color = 'k')
    plt.legend(prop={'size': 10})
    plt.ylabel('Ratio')
    
#    if i == 0:
#        plt.xlabel('x [cm]', fontsize=12)
#    else:
#        plt.xlabel('y [cm]', fontsize=12)
#    
    plt.xlabel(xlabel[i])    
  #  plt.xlabel('x [cm]', fontsize=12)
        

    
    
    
    ax = fig.add_subplot(gs[12:16,4:7])
    
 #   spectrum = max(yM) - min(yM)
#    binstoBeUsed = round(spectrum / binWidthY  )
    
    
    weights = 100* np.ones_like(yM)/float(madxPrim)
    
    histxM, xbinsM, patchesM = plt.hist(yM,weights = weights, bins = ybins, label = title2)
  #  plt.hist(yM,weights = weights, bins = ybins, label = 'WITHOUT')    
 #   plt.hist(yM,weights = weights, bins = ybins, label = 'Wires')        
    
    
    
#    spectrum = max(yF) - min(yF)
#    binstoBeUsed = round(spectrum / binWidthY  )
    
    
    weights = 100* np.ones_like(yF)/float(primaries)
    
    histxF, xbinsF, patchesF = plt.hist(yF,weights = weights, bins = ybins, fc = (1,0,0,0.5), label = title1)
  #  plt.hist(yF,weights = weights, bins = ybins, fc = (1,0,0,0.5), label = 'Using PyCollimate')    
#    plt.hist(yF,weights = weights, bins = ybins, fc = (1,0,0,0.5), label = '200 um ribbon')   
    
#    plt.ylim((None, 100) )
    plt.xlim(ymin, ymax )
    ax.set_yscale("log", nonposy='clip')
    h = plt.ylabel('%')
    h.set_rotation(0)
    plt.grid()
    plt.legend(prop={'size': 12})    
    plt.title(histTitle2)    
    plt.tick_params(
        axis='x',          # changes apply to the x-axis
        bottom='off',      # ticks along the bottom edge are off
        labelbottom='off') # labels along the bottom edge are off    
    
    
    
    fig.add_subplot(gs[16:,4:7])

    
    binwidth = xbinsM[1] - xbinsM[0]
    plt.bar( xbinsM[:-1], histxM/histxF,binwidth, label = title2 +'/' + title1, color = 'darkcyan')    
    plt.xlim(ymin, ymax )
    plt.grid()
    plt.plot(range(-20,20), np.ones(len(range(-20,20))), color = 'k')
    plt.legend(prop={'size': 10})
    plt.ylabel('Ratio')  
    
    
#    if i == 0:
#        plt.xlabel("$x^p$", fontsize=18)
#    else:
#        plt.xlabel("$y^p$", fontsize=18)

    plt.xlabel(ylabel[i])
#    plt.xlabel("$y$", fontsize=18)   
        

    


    
    
    
    
    
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








