# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 15:10:26 2018

@author: cbjorkma
"""

#ManualMeasurementComparison



import os
import numpy as np
import pandas as pd
import datetime #, timedelta
import matplotlib.pyplot as plt
import math
import matplotlib.patches as patches
from Flukato3dMatrix import Flukato3dMatrix

plt.close()
plt.close()
plt.close()
plt.close()
plt.close()
plt.close()

path = '//rpclustersrv1/cbjorkma/LSS2/'

os.chdir(path)

septaColor = 'limegreen'

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



filename = 'ManualMeasurent.xlsx'

thefile = pd.read_excel(filename)

data = np.zeros(thefile.shape)

quad216 = 3.791*100
quad217 = 35.7887*100
quad218 = 67.7864*100
quad219 = 99.7841*100




data[0:,0] = (thefile.position -216)*(quad217 - quad216) -500
data[0:,1] = thefile.doserate

x = data[0:,0]
y = data[0:,1]


#from scipy.interpolate import interp1d
#f = interp1d(x, y)
#
#print f(0)
#print f(quad217- quad216)
#print f(quad218- quad216)
#print f(quad219- quad216)

#datalines = []


def openFluka(filename):
    data = []
    fp = open(filename)
    lines = fp.readlines()
    for i in range(len(lines)):
        if i > 23 and i < 124:
    #        datalines.append(lines[i])
            for j in range(len(lines[i].split())):
                data.append(lines[i].split()[j])
    fp.close()
    
    dataout = np.zeros(len(data))
    for i in range(len(data)):
        dataout[i] = float(data[i])
    
    return dataout

def openFlukaErrors(filename):
    errors = []
    fp = open(filename)
    lines = fp.readlines()
    for i in range(len(lines)):
        if i > 126 and i < 227:
    #        datalines.append(lines[i])
            for j in range(len(lines[i].split())):
                errors.append(lines[i].split()[j])
    fp.close()
    dataout = np.zeros(len(errors))
    for i in range(len(errors)):
        dataout[i] = float(errors[i])
    
    return dataout

filename = '30h'
data1 = openFluka(filename)
errors1 = openFlukaErrors(filename)


#Converts data to uSv/h
data1 = 0.0036*data1

#Normalization
normFactor = 1 / 0.1772837
data1 = normFactor * data1

#Volume compensation
Volume = 20*20*(90+10100)/float(1000)
data1 = data1 /Volume














xmin = -500
xmax = 12000

fig = plt.figure()

ax = plt.subplot(111)

plt.plot(data[0:,0],data[0:,1])



plt.axvline(x= 0 ,linestyle = '--', color = 'k', linewidth = 0.3)
plt.axvline(x= quad217 - quad216 ,linestyle = '--', color = 'k', linewidth = 0.3)
plt.axvline(x= quad218 - quad216 ,linestyle = '--', color = 'k', linewidth = 0.3)
plt.axvline(x= quad219 - quad216 ,linestyle = '--', color = 'k', linewidth = 0.3)



plt.yscale("log", nonposy='clip')
#plt.xlim(data[0,0],max(data[0:,0]))






ax2 = ax.twinx()

#plotSepta(ax2)

plt.xlim(xmin,xmax)
#plt.ylim(0,15)

xes = np.arange(-500,10100,(10100+500)/float(1000))

plt.plot(xes,data1)
#plt.errorbar(xes,data1,yerr = errors1)

plt.yscale("log", nonposy='clip')
plt.show()











