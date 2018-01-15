# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 10:42:36 2017

@author: cbjorkma
"""

#Loss map


import os
import numpy as np
import matplotlib.pyplot as plt
import math
#from matplotlib.colors import LogNorm
#import pandas
#import math as math
#directory = "//cern.ch/dfs/Users/c/cbjorkma/Documents/LSS 2"

plt.close()
plt.close()
plt.close()
#plt.clf()

septaColor = 'limegreen'

#filename = 'LSS2_exp001_usrmed(3).dat'

#filename = 'usrmed(3).dat'
#
#data = np.loadtxt(filename , skiprows = 1)
#np.save(filename, data)
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


def plotSepta(ax):
    from scipy import interp  
#    positions = [511.95, 902.95, 1293.95, 1684.95 , 2075.95]
#    Xshift = math.sin(LindaAngle) *312/2
#    Yshift = math.cos(LindaAngle)*312/2  
    
    
    #ZSs
    ZSangle = math.degrees(1.414490E-3)
    r1 = patches.Rectangle((355.96,6.79), 313,0.020, angle= -ZSangle, color = septaColor) #, label = 'septa'
    r2 = patches.Rectangle((746.95,6.241), 313,0.020, angle= -ZSangle, color = septaColor)
    r3 = patches.Rectangle((1137.95,5.688), 313,0.020, angle= -ZSangle, color = septaColor)
    r4 = patches.Rectangle((1528.95,5.1349), 313,0.020, angle= -ZSangle, color = septaColor)
    r5 = patches.Rectangle((1919.95,4.582), 313,0.020, angle= -ZSangle, color = septaColor)
    ax.add_patch(r1)
    ax.add_patch(r2)
    ax.add_patch(r3)
    ax.add_patch(r4)
    ax.add_patch(r5)
    
    
    #TPST
    #TPST = [4792.27, 2.77]
    TPSTangle = math.degrees(0.533948362E-03)
#    MADXoffset = 1665.4231
    length = 215 #214
    width1 = 0.46  
    width2 = 0.52  
    Zcorner1 = 4684.768
    Xcorner1 = 3.760495
    Zcorner2 = 4771.96852
    Xcorner2 = 3.77706
#    r6 = patches.Rectangle((4685.26,3.94), 214 , 0.46, angle= TPSTangle, color = septaColor, alpha = 0.75)
#    ax.add_patch(r6)

    r1 = patches.Rectangle((Zcorner1 ,Xcorner1), length,width1, angle= TPSTangle, label = 'septa', color = septaColor)
    ax.add_patch(r1)
    r2 = patches.Rectangle((Zcorner2 ,Xcorner2), length - (Zcorner2 - Zcorner1),width2, angle= TPSTangle, color = septaColor)
    ax.add_patch(r2)
    
    #MST
    MADXoffset = 1665.4231
    Zs = [5093.02,5416.42,5739.82 ]
    width = 0.414
    length = 240
    
    point1 = []
    point2 = []

    #Defines the baselines
    point1.append( [100*(1715.1633 - MADXoffset) , 0.1*39.41577])
    point2.append( [100*(1717.5433 - MADXoffset), 0.1*40.96990])
    
    point1.append(  [100*(1718.3973 - MADXoffset) , 0.1*41.52756])
    point2.append( [100*(1720.7773 - MADXoffset), 0.1*43.08169])
    
    point1.append( [100*(1721.6313 - MADXoffset) , 0.1*43.63934])
    point2.append( [100*(1724.0113 - MADXoffset), 0.1*45.19347])

    MSTangle = math.degrees(0.65299570E-03)
    for i in range(len(Zs)):
    
        
        z = np.zeros(2)
        x = np.zeros(2)
        z[0] = point1[i][0]
        z[1] = point2[i][0]
        x[0] = point1[i][1]
        x[1] = point2[i][1]    
#        f = interpolate.interp1d(z, x)
        newZ = Zs[i] - math.cos(MSTangle)*length/2
        newX = interp(newZ, z,x)
        r7 = patches.Rectangle((newZ,newX), length,width, angle= MSTangle, color = septaColor,alpha = 0.75)
        ax.add_patch(r7)
    
#    "MSTangle = math.degrees(0.65299570E-03)
#    r7 = patches.Rectangle((4973.016812,4.079), length,width, angle= MSTangle, color = septaColor,alpha = 0.75)
#    r8 = patches.Rectangle((5296.416982,4.240), length,width, angle= MSTangle, color = septaColor,alpha = 0.75)
#    r9 = patches.Rectangle((5619.816971,4.401), length,width, angle= MSTangle, color = septaColor,alpha = 0.75)
#    ax.add_patch(r7)
#    ax.add_patch(r8)
#    ax.add_patch(r9)
    
    #MSE
    Zs = [6838.29,7161.69,7485.09, 7808.49, 8131.89 ]
    length = 241.32
    width = 1.72
    
    point1 = []
    point2 = []
    
    #Defines the baselines
    point1.append( [100*(1732.616                 - MADXoffset) , 0.1*48.26604])
    point2.append( [100*(1734.996                - MADXoffset), 0.1*47.46876])
    
    point1.append(  [100*(1735.85                  - MADXoffset) , 0.1*47.89989])
    point2.append( [100*(1738.23                 - MADXoffset), 0.1*50.14024])
    
    point1.append( [100*(1739.084                - MADXoffset) , 0.1*51.30396])
    point2.append( [100*(1741.464               - MADXoffset), 0.1*56.57150])
    
    point1.append(  [100*(1742.318                - MADXoffset) , 0.1*59.18803])
    point2.append( [100*(1744.698                - MADXoffset), 0.1*67.48276])
    
    point1.append( [100*(1745.552                - MADXoffset) , 0.1*70.83187])
    point2.append( [100*(1747.932                - MADXoffset), 0.1*82.16424])
    for i in range(len(Zs)):
    
        
        z = np.zeros(2)
        x = np.zeros(2)
        z[0] = point1[i][0]
        z[1] = point2[i][0]
        x[0] = point1[i][1]
        x[1] = point2[i][1]    
#       
        MSEangle = math.atan((x[1] - x[0])/ (z[1] - z[0]))
#        print MSEangle
        newZ = Zs[i] - math.cos(MSTangle)*length/2
        newX = interp(newZ, z,x)
        r7 = patches.Rectangle((newZ,newX), length,width, angle= math.degrees(MSEangle), color = septaColor,alpha = 0.75)
        ax.add_patch(r7)    
    
#    r10 = patches.Rectangle((6717.6328,4.825), 241.32,1.775, angle= -0.025632321, color = septaColor,alpha = 0.75)
#    r11 = patches.Rectangle((7041.0248,4.777), 241.32,1.775, angle= 0.047495174, color = septaColor,alpha = 0.75)
#    r12 = patches.Rectangle((7364.41710,5.142), 241.32,1.775, angle= 0.12062252, color = septaColor,alpha = 0.75)
#    r13 = patches.Rectangle((7687.809591,5.918), 241.32,1.775, angle= 0.193498169, color = septaColor,alpha = 0.75)
#    r14 = patches.Rectangle((8011.202246,7.107), 241.32,1.775, angle= 0.266624488, color = septaColor,alpha = 0.75)
#    ax.add_patch(r10)
#    ax.add_patch(r11)
#    ax.add_patch(r12)
#    ax.add_patch(r13)
#    ax.add_patch(r14)
#------------------------------------------------------------------------------------------------------------------------------






path = "//rpclustersrv1/cbjorkma/LSS2/Run02"          
os.chdir(path)        
#data = readPhaseDirectory(path)           
#np.save('Run02usermed', data)
fluka = np.load('Run02usermed.npy')
#primaries = 0.72*fluka.shape[0]

#condition = fluka[0:,5] <= 10000
#subsetFluka = np.zeros([np.sum(condition),fluka.shape[1]])
#for i in range(fluka.shape[1]):
#    subsetFluka[0:,i] = np.extract(condition, fluka[0:,i])
#print 'Subset Created'
#np.save('FlukaSlessthan100m', subsetFluka)
#fluka = np.load('FlukaSlessthan100m.npy')
##  NCASE  IJ               PLA                 X                 Y                 Z               TXX               TYY               TZZ            WEIGHT LTRACK     ISAMPLE
#primaries = fluka.shape[0]





directory = "//rpclustersrv1/cbjorkma/LSS2"
os.chdir(directory)

##load MADX------------------------------

#
#import pickle
#with open('lost.pkl', 'rb') as f:
#    data = pickle.load(f)
#   
#
##madxListed = data.values()
#
#keys = data.keys()
#print keys
#madx = np.zeros([data.shape[0],3])
#
#for i in range(data.shape[0]):
#    madx[0:,0] = data.S
#    madx[0:,1] = data.X*100
#    madx[0:,2] = data.Y*100
#np.save('madxLost',madx)
##------------------------------------------------
#Index([u'TURN', u'X', u'PX', u'Y', u'PY', u'T', u'PT', u'S', u'E', u'ELEMENT'], dtype='object')
madx = np.load('madxLost.npy')
madx[0:,0] = 100*(madx[0:,0] - np.ones([madx.shape[0]])*1665.4231)
#madxPrim = madx.shape[0]



#------------Run inelastic--------------------------------------
path = "//rpclustersrv1/cluster_temp/cbjorkma/LSS2/Run inelastic"   
os.chdir(path)        
#data = readPhaseDirectory(path, 'dat')    
#data = np.concatenate( (readPhaseDirectory(path, 'dat'), readPhaseDirectory(path, '.99')), axis = 0)    
#np.save('Runinelastic', data)
#madx = np.load('Runinelastic.npy')
fluka = np.load('Runinelastic.npy')
#primaries = 0.72*fluka.shape[0]



directory = "//rpclustersrv1/cbjorkma/LSS2"
os.chdir(directory)



import pickle
with open('LSS2_exp001_fort.99.pkl', 'rb') as f:
    data = pickle.load(f)

#madxListed = data.values()

keys = data.keys()
print keys
fluka1 = np.zeros([data.shape[0],3])

for i in range(data.shape[0]):
    fluka1[0:,0] = data.X*100
    fluka1[0:,1] = data.Y*100
    fluka1[0:,2] = data.Z*100

with open('LSS2_exp001_usrmed.pkl', 'rb') as f:
    data = pickle.load(f)

#madxListed = data.values()

keys = data.keys()
print keys
fluka2 = np.zeros([data.shape[0],3])

for i in range(data.shape[0]):
    fluka2[0:,0] = data.X*100
    fluka2[0:,1] = data.Y*100
    fluka2[0:,2] = data.Z*100

fluka = np.concatenate((fluka1,fluka2), axis = 0)

np.save('FlukaInelasticAdjustedDensity',fluka )

normFluka = 20000000

#toPlot =normHist( data[0:,5])    

#end = math.floor(1* fluka.shape[0])

#primaries = fluka.shape[0]
#madxPrim = 10980000


#ax1 = fig.add_subplot(111)
#plot = plt.hist(data[0:,5]/1, log = True, bins = 80, normed = True)






print 'Plotting...'



#----------------------------------------------------------------------------------------
xlim =10200

suptitle1 = 'LSS2 Lost particles in aperture. Horizontal comparison'

suptitle2 = 'LSS2 Lost particles in aperture. Vertical comparison'

title1 = 'Fluka, inelastic at ZSs, adjusted wire density'
title2 = 'MADX'
histTitle = 'Full loss map. Binning normalized to # of simulated particles'
#----------------------------------------------------------------------------------------

##----------------------------------------------------------------------------------------
#xlim =10200
#
#suptitle1 = 'LSS2 Lost particles in aperture. Horizontal comparison'
#
#suptitle2 = 'LSS2 Lost particles in aperture. Vertical comparison'
#
#title1 = 'First touch only'
#title2 = 'Inelastic int at ZSs'
#histTitle = 'Full loss map. Binning normalized to # of simulated particles'
##----------------------------------------------------------------------------------------
#




#normFluka = fluka.shape[0]
#madxPrim = madx.shape[0]
madxPrim = 10980000



import matplotlib.patches as patches
for i in range(2):
    
    fig = plt.figure()
    
    
    if i == 0:
        plt.suptitle(suptitle1, fontsize=22)

    else:
        plt.suptitle(suptitle2, fontsize=22)      
    
    
#    #Read data
#    xF = fluka[0:,5]    
#    if i == 0:
#        yF = fluka[0:,3]
##        count = 0
##        for j in range(len(xF)):
##            if xF[j] > 10000 and yF[j] < 10:
##                count = count +1
##        print count
##        normFluka = primaries - count
##        print normFluka
#    else:
#        yF = fluka[0:,4]
#

    #Read picled data
    xF = fluka[0:,2]    
    if i == 0:
        yF = fluka[0:,0]
#        count = 0
#        for j in range(len(xF)):
#            if xF[j] > 10000 and yF[j] < 10:
#                count = count +1
#        print count
#        normFluka = primaries - count
#        print normFluka
    else:
        yF = fluka[0:,1]





    #Real madx    
    xM = madx[0:,0]
    if i ==0:
        yM = madx[0:,1]

    else:
        yM = madx[0:,2]    

#    #Fake Madx
#    xM = madx[0:,5]    
#    if i == 0:
#        yM = madx[0:,3]
#
#    else:
#        yM = madx[0:,4]
#
#



    
    
    ymax = max(max(yM), max(yF))*1.1
    ymin = min(min(yM), min(yF))*1.1
    

    
    
    
    
    #Fluka---------------------------------------
    ax = plt.subplot(311)
    if i == 0:
        plt.ylabel('x [cm]')
        plotSepta(ax)
    else:
        plt.ylabel('y [cm]')



    plt.title(title1)
    plt.scatter(xF,yF ,c = 'r', edgecolors = None, s = 0.5, label = title1)
    plt.grid(linewidth=0.2)
    #plt.ylim(0, 35 )
    plt.xlim(0, xlim )
    plt.ylim(ymin, ymax )
    
    
    #Quads
    plt.axvline(x=0,linestyle = '--' ,label='Quadrupoles', color = 'black')
    plt.axvline(x=3199.77,linestyle = '--', color = 'black' )
    plt.axvline(x=6399.54,linestyle = '--', color = 'black' )
    plt.axvline(x=9599.31,linestyle = '--', color = 'black' )
    plt.legend(loc = 2)
    
    
    
    
    
    #MADX-----------------------------------------
    ax = plt.subplot(312)
    plt.title(title2)
    if i == 0:
        plt.ylabel('x [cm]')
        plotSepta(ax)
    else:
        plt.ylabel('y [cm]')    


    
    plt.scatter(xM,yM ,c = 'b', edgecolors = None, s = 0.5, label = title2)
    plt.grid(linewidth=0.2)
    #plt.ylim(0, 35 )
    plt.xlim(0, xlim )
    plt.ylim(ymin, ymax )
    
    #Quads
    plt.axvline(x=0,linestyle = '--' ,label='Quadrupoles', color = 'black')
    plt.axvline(x=3199.77,linestyle = '--', color = 'black' )
    plt.axvline(x=6399.54,linestyle = '--', color = 'black' )
    plt.axvline(x=9599.31,linestyle = '--', color = 'black' )
    plt.legend(loc = 2)

    #plt.legend(loc = 2)
    #plt.setp( ax.get_yticklabels(), visible=False)
    #--------------------------------------------------
    ax1 = plt.subplot(313)
    
    #x = fluka[0:,5]
    weights = 100* np.ones_like(xF)/float(normFluka)
    histx, xbins, Placeholder = plt.hist(xF,weights = weights, bins = 200,fc=(1, 0, 0, 0.8), label = title1)
    
    
    
    #x = madx[0:,0]
    weights = 100* np.ones_like(xM)/float(madxPrim)
    histx, xbins, Placeholder = plt.hist(xM,weights = weights, bins = xbins,fc=(0, 0, 1, 0.4), label = title2)
    
    

    
    h = plt.ylabel('%')
    h.set_rotation(0)
    plt.title(histTitle)
    #plt.title('LSS2 Lossmap')
    ax1.set_yscale("log", nonposy='clip')
    #plt.grid()
    #plt.xlim(0, 10400 )
    plt.xlim(0, xlim )
    plt.grid(linewidth=0.2)
    plt.xlabel('Z [cm]')    
    
    #Quads
    plt.axvline(x=0,linestyle = '--' ,label='Quadrupoles', color = 'black')
    plt.axvline(x=3199.77,linestyle = '--', color = 'black' )
    plt.axvline(x=6399.54,linestyle = '--', color = 'black' )
    plt.axvline(x=9599.31,linestyle = '--', color = 'black' )
    plt.legend(loc = 1)
    
        
    
plt.show()


#fig = plt.figure()
#
#ax1 = plt.subplot(111)
#
##xF = fluka[0:,5]
#weights = 100* np.ones_like(xF)/float(normFluka)
#histx, xbins, Placeholder = plt.hist(xF,weights = weights, bins = 200,fc=(1, 0, 0, 0.8), label = title1)
#
#
#
##xM = madx[0:,0]
#weights = 100* np.ones_like(xM)/float(madxPrim)
#histx, xbins, Placeholder = plt.hist(xM,weights = weights, bins = xbins,fc=(0, 0, 1, 0.4), label = title2)
#
#
#
#
##plt.isinteractive()
#
#
#h = plt.ylabel('%')
#h.set_rotation(0)
#plt.title(histTitle)
##plt.title('LSS2 Lossmap')
#ax1.set_yscale("log", nonposy='clip')
##plt.grid()
##plt.xlim(0, 10400 )
#plt.xlim(0, xlim )
#plt.grid(linewidth=0.2)
#plt.xlabel('Z [cm]')    
#
##Quads
#plt.axvline(x=0,linestyle = '--' ,label='Quadrupoles', color = 'black')
#plt.axvline(x=3199.77,linestyle = '--', color = 'black' )
#plt.axvline(x=6399.54,linestyle = '--', color = 'black' )
#plt.axvline(x=9599.31,linestyle = '--', color = 'black' )
#plt.legend(loc = 2)
#
#    
#plt.show()    

print 'Done'