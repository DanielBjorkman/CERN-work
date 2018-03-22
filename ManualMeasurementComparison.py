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
#from Flukato3dMatrix import Flukato3dMatrix

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




data[0:,0] = (thefile.position -216)*(quad217 - quad216) -480
data[0:,1] = thefile.doserate
data[0:,2] = (thefile.position1m30h -216)*(quad217 - quad216) -630
data[0:,3] = thefile.doserate1m30h


#x = data[0:,0]
#y = data[0:,1]


#from scipy.interpolate import interp1d
#f = interp1d(x, y)
#
#print f(0)
#print f(quad217- quad216)
#print f(quad218- quad216)
#print f(quad219- quad216)

#datalines = []


def openFluka(filename,shift = 0):
    data = []
    fp = open(filename)
    lines = fp.readlines()
    for i in range(len(lines)):
        if i > 23 +shift and i < 124+shift:
    #        datalines.append(lines[i])
            for j in range(len(lines[i].split())):
                data.append(lines[i].split()[j])
    fp.close()
    
    dataout = np.zeros(len(data))
    for i in range(len(data)):
        dataout[i] = float(data[i])
    
    return dataout

def openFlukaErrors(filename,shift = 0):
    errors = []
    fp = open(filename)
    lines = fp.readlines()
    for i in range(len(lines)):
        if i > 126 +shift and i < 227 +shift:
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
#Volume = 20*20*(500+10100)/float(1000)
#data1 = data1 /Volume



filename = '1m30h'
data2 = openFluka(filename, -15)
errors2 = openFlukaErrors(filename, -15)


#Converts data to uSv/h
data2 = 0.0036*data2

#Normalization
normFactor = 1 / 0.1772837
data2 = normFactor * data2











#Volume compensation
#Volume = 20*20*(500+10100)/float(1000)
#data2 = data2 /Volume
import datetime #, timedelta
from scipy.interpolate import interp1d
import pandas as pd
protonEnd = datetime.datetime(2017,10,23,06,00,00)
ionEnd = datetime.datetime(2017,12,18,06,00,00)
end2016 = datetime.datetime(2015,11,16,06,00,00)
end2017 = datetime.datetime(2016,11,14,06,00,00)
manualMeasurement = datetime.datetime(2017,10,24,12,00,00)



path = '//cern.ch/dfs/Users/c/cbjorkma/Documents/LSS 2/ActivationDetectors'

os.chdir(path)

#protonEnd = '2017-11-23 06:00:00.940000'
protonEnd = datetime.datetime(2017,10,23,06,00,00)
ionEnd = datetime.datetime(2017,12,18,06,00,00)
end2016 = datetime.datetime(2015,11,16,06,00,00)
end2017 = datetime.datetime(2016,11,14,06,00,00)


#files = os.listdir(path)
#files = sorted(files)
#files = filter(lambda x: x[4:7].isdigit() , files)  
#files = filter(lambda x: not x[0] == '.' , files)  
#filenames = files
#thefile = pd.read_excel(files[0])
#
#dataPMI = np.zeros([len(thefile),2, len(files)])
#for j in range(len(files)):
#    thefile = pd.read_excel(files[j])
#    time = thefile.Timestamp
#    for i in range(len(thefile)):
#        instant = datetime.datetime( time[i].year, time[i].month, time[i].day, time[i].hour, time[i].minute, time[i].second)
#    #    print instant
#        timedifference = instant - manualMeasurement
#        amountOfSeconds = timedifference.total_seconds()/(60*60*24)
#      #  print 'file ' + str(j) + '. Seconds ' + str(amountOfSeconds) + '. value ' + str(thefile.Value[i] )
#        dataPMI[i,0,j] = amountOfSeconds
#        dataPMI[i,1,j] = thefile.Value[i]   
#assert dataPMI[1200,1,2] != dataPMI[1200,1,3]
#np.save('dataPMI', dataPMI)

xpos = [595, 1207, 1697 , 1992, 5351 , 5800,7096, 7743]

dataPMI = np.load('dataPMI.npy')









from scipy.interpolate import interp1d




xmin = -500
xmax = 10100


ymin = 1
ymax = max(data[0:,1])*5



useshift = 0







fig = plt.figure()

ax = plt.subplot(211)

plt.plot(data[0:,0],data[0:,1], label = 'Manual measurement')


plt.axvline(x= 0 ,linestyle = '--', color = 'k', linewidth = 0.3)
plt.axvline(x= quad217 - quad216 ,linestyle = '--', color = 'k', linewidth = 0.3)
plt.axvline(x= quad218 - quad216 ,linestyle = '--', color = 'k', linewidth = 0.3)
plt.axvline(x= quad219 - quad216 ,linestyle = '--', color = 'k', linewidth = 0.3)
plt.legend(loc = 2)

plt.ylim(ymin , ymax)

plt.xlim(xmin , xmax)

plt.ylabel('uSv/h',fontsize = 16)
plt.xlabel('z [cm from quad216]')
plt.yscale("log", nonposy='clip')
#plt.xlim(data[0,0],max(data[0:,0]))

for i in range(dataPMI.shape[2]):
#    i = 0
    x = dataPMI[0:,0,i]
    y = dataPMI[0:,1,i]
    f = interp1d(x, y)
    timeval = -1.15741e-05
    
    if i == 0:
        plt.errorbar(xpos[i], f(timeval), color = 'b', linestyle='None', fmt='o', label = 'PMI data',yerr = f(timeval)*0.2)
    else:
        plt.errorbar(xpos[i], f(timeval), color = 'b', linestyle='None', fmt='o',yerr = f(timeval)*0.2)
    print f(timeval)

FlukaData  =  np.load('FlukaPMIdata.npy')
FlukaSD =    np.load('FlukaPMIerrors.npy')


plt.errorbar(xpos,FlukaData[1,0:],yerr = FlukaData[1,0:]*FlukaSD[1,0:]/100, linestyle='None', fmt='o', color = 'r', label = 'Fluka PMI 1 day cool down')


#yerr = FlukaData[1,0:]*FlukaSD[1,0:]/100?

print 'How are we on the errors here?'

plt.legend(loc = 1)



ax3 = ax.twinx()
plotSepta(ax3)
plt.legend(loc = 3)
plt.ylim(2,18)
ax3.yaxis.set_ticklabels([])



ax2 = ax.twinx()

#plotSepta(ax2)

shift = 40000

plt.xlim(xmin,xmax)
#plt.ylim(0,15)

xes = np.arange(-500,10100,(10100+500)/float(1000))
if useshift:
    plt.plot(xes,shift*data1, color = 'r', label = "Fluka")
else:
    #plt.plot(xes,data1, color = 'r', label = "Fluka")
    plt.errorbar(xes,data1,yerr =data1*errors1/100, color = 'r', label = "Fluka")

plt.yscale("log", nonposy='clip')
plt.ylim(ymin , ymax)
plt.legend(loc = 2)
ax2.yaxis.set_ticklabels([])
#


if useshift:
    plt.title('30h after 2017 operations. Amplitude difference at TPST = ' + str(shift))
else:
    plt.title('30h after 2017 operations')



ax = plt.subplot(212)

plt.plot(data[0:,2],data[0:,3], label = 'Manual measurement')


plt.axvline(x= 0 ,linestyle = '--', color = 'k', linewidth = 0.3)
plt.axvline(x= quad217 - quad216 ,linestyle = '--', color = 'k', linewidth = 0.3)
plt.axvline(x= quad218 - quad216 ,linestyle = '--', color = 'k', linewidth = 0.3)
plt.axvline(x= quad219 - quad216 ,linestyle = '--', color = 'k', linewidth = 0.3)
plt.legend(loc = 2)

plt.ylim(ymin , ymax)
#
plt.xlim(xmin , xmax)
#
plt.ylabel('uSv/h',fontsize = 16)
plt.xlabel('z [cm from quad216]')
plt.yscale("log", nonposy='clip')
plt.xlim(data[0,0],max(data[0:,0]))



instant = datetime.datetime(2017,11,24,12,00,00)
timedifference = instant - manualMeasurement

for i in range(dataPMI.shape[2]):
#    i = 0
    x = dataPMI[0:,0,i]
    y = dataPMI[0:,1,i]
    f = interp1d(x, y)
    timeval = 30.9167
    
    if i == 0:
        plt.errorbar(xpos[i], f(timeval), color = 'b', linestyle='None', fmt='o', label = 'PMI data',yerr = f(timeval)*0.2)
    else:
        plt.errorbar(xpos[i], f(timeval), color = 'b', linestyle='None', fmt='o',yerr = f(timeval)*0.2)
    print f(timeval)

plt.errorbar(xpos,FlukaData[3,0:],yerr = FlukaData[3,0:]*FlukaSD[3,0:]/100, linestyle='None', fmt='o', color = 'r', label = 'Fluka PMI 1 month cool down')

plt.legend(loc = 1)





ax3 = ax.twinx()
plotSepta(ax3)
plt.legend(loc = 3)
plt.ylim(2,18)
ax3.yaxis.set_ticklabels([])


ax2 = ax.twinx()

#plotSepta(ax2)

shift = 400

plt.xlim(xmin,xmax)
#plt.ylim(0,15)

xes = np.arange(-500,10100,(10100+500)/float(1000))

if useshift:
    plt.plot(xes,shift*data2, color = 'r', label = "Fluka")
else:
#    plt.plot(xes,data2, color = 'r', label = "Fluka")
    print 'No shift'
    plt.errorbar(xes,data2,yerr =data2*errors2/100, color = 'r', label = "Fluka")

plt.yscale("log", nonposy='clip')
plt.ylim(ymin , ymax)
plt.legend(loc = 2)
ax2.yaxis.set_ticklabels([])
#


if useshift:
    plt.title('1 month and 30h after 2017 operations. Amplitude difference at TPST = ' + str(shift) )
    plt.suptitle('Dose rate comparison in LSS2 after 2017 operations. NOTE: Fluka data plotted with adjusted amplitudes',fontsize = 22)
else:
    plt.title('1 month and 30h after 2017 operations' )
    plt.suptitle('LSS2 Dose rate 1 meter from beam axis after 2017 operations. ',fontsize = 22)




#plt.suptitle('Dose rate comparison in LSS2 after 2017 operations. NOTE: Fluka data plotted with adjusted amplitudes',fontsize = 22)

plt.show()






#----------------------------------------------------------------------------------------




from matplotlib.gridspec import GridSpec

every = 10

fig = plt.figure()


gs = GridSpec(2,3)

ax = fig.add_subplot(gs[0:2,0:2])
plt.plot(data[0:,0],data[0:,1], label = 'Manual measurement 30h' ,color = 'b')
plt.errorbar(xes,data1,yerr = data1*errors1/100, color = 'b', label = "Fluka. 30h",errorevery=every,linestyle = '--')

plt.plot(data[0:,2],data[0:,3], label = 'Manual measurement 1 month + 30h',color = 'r')
plt.errorbar(xes,data2,yerr =data2*errors2/100, color = 'r', label = "Fluka. 1month + 30h",linestyle = '--',errorevery=every) 


plt.xlim(xmin , xmax)
plt.yscale("log", nonposy='clip')
plt.ylabel('uSv/h',fontsize = 16)
plt.xlabel('z [cm from quad216]')
plt.legend()
plt.axvline(x= 0 ,linestyle = '--', color = 'k', linewidth = 0.3)
plt.axvline(x= quad217 - quad216 ,linestyle = '--', color = 'k', linewidth = 0.3)
plt.axvline(x= quad218 - quad216 ,linestyle = '--', color = 'k', linewidth = 0.3)
plt.axvline(x= quad219 - quad216 ,linestyle = '--', color = 'k', linewidth = 0.3)
plt.ylim(ymin , ymax)




ax3 = ax.twinx()
plotSepta(ax3)
plt.legend(loc = 3)
plt.ylim(2,18)
ax3.yaxis.set_ticklabels([])



every = 50



# 30h
ax = fig.add_subplot(gs[0,2])

x = data[0:,0]
y = data[0:,1]
f = interp1d(x, y)

plt.axvline(x= 0 ,linestyle = '--', color = 'k', linewidth = 0.3)
plt.axvline(x= quad217 - quad216 ,linestyle = '--', color = 'k', linewidth = 0.3)
plt.axvline(x= quad218 - quad216 ,linestyle = '--', color = 'k', linewidth = 0.3)
plt.axvline(x= quad219 - quad216 ,linestyle = '--', color = 'k', linewidth = 0.3)


plt.errorbar( xes, f(xes)/data1,yerr =f(xes)/data1*errors1/100, label ='Manual / Fluka', color = 'darkcyan',errorevery=every)
plt.axhline(y=1, color='k', linestyle='-')

plt.title('Ratios: 30h after 2017 operations')
plt.ylabel('Manual / Fluka')
plt.xlabel('z [cm from quad216]')
plt.legend()

# 30h
ax = fig.add_subplot(gs[1,2])

x = data[0:,2]
y = data[0:,3]
f = interp1d(x, y)
plt.axvline(x= 0 ,linestyle = '--', color = 'k', linewidth = 0.3)
plt.axvline(x= quad217 - quad216 ,linestyle = '--', color = 'k', linewidth = 0.3)
plt.axvline(x= quad218 - quad216 ,linestyle = '--', color = 'k', linewidth = 0.3)
plt.axvline(x= quad219 - quad216 ,linestyle = '--', color = 'k', linewidth = 0.3)

plt.errorbar( xes, f(xes)/data2,yerr = f(xes)/data2*errors2/100, label ='Manual / Fluka', color = 'darkcyan',errorevery=every)
plt.axhline(y=1, color='k', linestyle='-')

plt.title('Ratios: 1 month and 30h after 2017 operations')
plt.ylabel('Manual / Fluka')
plt.xlabel('z [cm from quad216]')
plt.legend()

plt.suptitle('LSS2 Residual dose rate comparison along Z', fontsize = 30)

plt.show()










#----------------------------------------------------------------------------------------


fig = plt.figure()


ax = plt.subplot(211)

plt.plot(data[0:,0],data[0:,1]/max(data[0:,1]), label = 'Manual measurement')
#plt.plot(data[0:,0],data[0:,1], label = 'Manual measurement')
plt.errorbar(xes,data1/max(data1), yerr =data1/max(data1)*errors1/100,  color = 'r', label = "Fluka")
#plt.errorbar(xes,data1, color = 'r', label = "Fluka")

plt.axvline(x= 0 ,linestyle = '--', color = 'k', linewidth = 0.3)
plt.axvline(x= quad217 - quad216 ,linestyle = '--', color = 'k', linewidth = 0.3)
plt.axvline(x= quad218 - quad216 ,linestyle = '--', color = 'k', linewidth = 0.3)
plt.axvline(x= quad219 - quad216 ,linestyle = '--', color = 'k', linewidth = 0.3)
plt.legend(loc = 2)

#plt.ylim(ymin , ymax)

plt.xlim(xmin , xmax)

plt.ylabel('Dose rate [a.u]',fontsize = 16)
plt.xlabel('z [cm from quad216]')
#plt.yscale("log", nonposy='clip')
#plt.xlim(data[0,0],max(data[0:,0]))
plt.legend(loc = 1)



ax3 = ax.twinx()
plotSepta(ax3)
plt.legend(loc = 3)
plt.ylim(2,18)
ax3.yaxis.set_ticklabels([])



#ax2 = ax.twinx()
#
##plotSepta(ax2)
#
#shift = 40000
#
#plt.xlim(xmin,xmax)
##plt.ylim(0,15)
#
#xes = np.arange(-500,10100,(10100+500)/float(1000))
#
#
#
##plt.yscale("log", nonposy='clip')
##plt.ylim(ymin , ymax)
#plt.legend(loc = 2)
#ax2.yaxis.set_ticklabels([])
#



plt.title('30h after 2017 operations')



ax = plt.subplot(212)

plt.plot(data[0:,2],data[0:,3]/max(data[0:,3]), label = 'Manual measurement')
plt.errorbar(xes,data2/max(data2),yerr =data2/max(data2)*errors2/100, color = 'r', label = "Fluka")

plt.axvline(x= 0 ,linestyle = '--', color = 'k', linewidth = 0.3)
plt.axvline(x= quad217 - quad216 ,linestyle = '--', color = 'k', linewidth = 0.3)
plt.axvline(x= quad218 - quad216 ,linestyle = '--', color = 'k', linewidth = 0.3)
plt.axvline(x= quad219 - quad216 ,linestyle = '--', color = 'k', linewidth = 0.3)
plt.legend(loc = 2)

#plt.ylim(ymin , ymax)
#
plt.xlim(xmin , xmax)
#
plt.ylabel('Dose rate [a.u]',fontsize = 16)
plt.xlabel('z [cm from quad216]')
#plt.yscale("log", nonposy='clip')
plt.xlim(data[0,0],max(data[0:,0]))


plt.legend(loc = 1)





ax3 = ax.twinx()
plotSepta(ax3)
plt.legend(loc = 3)
plt.ylim(2,18)
ax3.yaxis.set_ticklabels([])
plt.xlim(xmin , xmax)
#

plt.title('1 month and 30h after 2017 operations' )





#plt.suptitle('Dose rate comparison in LSS2 after 2017 operations. NOTE: Fluka data plotted with adjusted amplitudes',fontsize = 22)

plt.suptitle('LSS2 Normalized dose rates 1 meter from beam axis after 2017 operations. ',fontsize = 22)

plt.show()





#----------------------------------------------------------------------------------------


fig = plt.figure()


ax = plt.subplot(111)

x = data[0:,0]
y = data[0:,1]
f = interp1d(x, y)

startIndex = 5
endIndex = 2837

plt.plot(data[startIndex:endIndex,2],f(data[startIndex:endIndex,2])/data[startIndex:endIndex,3], label = 'Manual/Manual measurement')

plt.plot(xes, data1/data2, label = 'Fluka/Fluka', color = 'r')





#plt.plot(data[0:,0],data[0:,1], label = 'Manual measurement')
#plt.errorbar(xes,data1/max(data1), yerr =data1/max(data1)*errors1/100,  color = 'r', label = "Fluka")
#plt.errorbar(xes,data1, color = 'r', label = "Fluka")

plt.axvline(x= 0 ,linestyle = '--', color = 'k', linewidth = 0.3)
plt.axvline(x= quad217 - quad216 ,linestyle = '--', color = 'k', linewidth = 0.3)
plt.axvline(x= quad218 - quad216 ,linestyle = '--', color = 'k', linewidth = 0.3)
plt.axvline(x= quad219 - quad216 ,linestyle = '--', color = 'k', linewidth = 0.3)
plt.legend(loc = 1)

#plt.ylim(ymin , ymax)

plt.xlim(xmin , xmax)

plt.ylim(0.1,10)

plt.axhline(y=1, color='k', linestyle='-')

#plt.ylabel('Dose rate [a.u]',fontsize = 16)
plt.xlabel('z [cm from quad216]')
plt.yscale("log", nonposy='clip')
#plt.xlim(data[0,0],max(data[0:,0]))
#plt.legend(loc = 1)
plt.ylabel('30hours/(1month+30hours)',fontsize = 16)


ax3 = ax.twinx()
plotSepta(ax3)
plt.legend(loc = 3)
plt.ylim(2,14)
ax3.yaxis.set_ticklabels([])

plt.title('Ratio comparison: Manual measurement vs. Fluka',fontsize = 22)



plt.show()




















