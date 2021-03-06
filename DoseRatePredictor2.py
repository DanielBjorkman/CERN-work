# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 15:10:09 2018

@author: cbjorkma
"""

#Doserate predictor


import matplotlib.pyplot as plt
plt.close()
plt.close()
plt.close()
plt.close()
plt.close()
plt.close()
plt.close()
plt.close()

#from PMIs import PMI
from USRBIN import USRBIN
from PMIs import PMI
from ManualClass import ManualClass
import datetime
from scipy.interpolate import interp1d

#filename = 'LSS2_exp_24.bnn.lis'
septaColor = 'limegreen'

def plotSepta(ax):
    from scipy import interp
    import math
    import matplotlib.patches as patches
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
    plt.axvline(x= 0 ,linestyle = '--', color = 'k', linewidth = 0.3)
    plt.axvline(x= quad217 - quad216 ,linestyle = '--', color = 'k', linewidth = 0.3)
    plt.axvline(x= quad218 - quad216 ,linestyle = '--', color = 'k', linewidth = 0.3)
    plt.axvline(x= quad219 - quad216 ,linestyle = '--', color = 'k', linewidth = 0.3)
#------------------------------------------------------------------------------------------------------------------------------


#Converts data to uSv/h and normalizes data to the number of exstracted particles
normfactor = 0.0036*1 / 0.1772837

import os






protonEnd = datetime.datetime(2017,10,23,06,00,00)
ionEnd = datetime.datetime(2017,12,18,06,00,00)
end2016 = datetime.datetime(2015,11,16,06,00,00)
end2017 = datetime.datetime(2016,11,14,06,00,00)
manualMeasurement = datetime.datetime(2017,10,24,12,00,00)


path = '//cern.ch/dfs/Users/c/cbjorkma/Documents/LSS 2/ActivationDetectors'

pmi = PMI(path, end2017)

pmi.read()
pathFluka = '//rpclustersrv1/cbjorkma/LSS2/FullActivation8/PMIs'
pmi.readFluka(pathFluka, normfactor)
pmi.calc()
#pmi.predictAmplitudes(0) #4




#Load Generic profile
path = '//rpclustersrv1/cbjorkma/LSS2/FullActivation8/Generic'
#os.chdir(path)
pmi.readGeneric('FlukaPMIgeneric', path)
filename = 'FlukaUSRBINgeneric'
generic = USRBIN(filename, path, normfactor)
generic.read()
generic.calc()
#x.read()
#x.calc()


pmi.predictAmplitudes2()


path = '//rpclustersrv1/cbjorkma/LSS2/FullActivation8/USRBINs'
os.chdir(path)
filenames = sorted(os.listdir(path))
try:
    print USRBINS
    print Predicted
except:
    print 'Loading USRBINs...'
    USRBINS = []
    Predicted = []
    for i in range(len(filenames)):
        x = USRBIN(filenames[i], path, normfactor)
        x.read()
        x.calc()
        USRBINS.append(x)
        y =  x#USRBIN(filenames[i], path, normfactor)
        #y.read()
        y.cube = x.cube + generic.cube*pmi.As[i]
        y.calc()
#        x = USRBIN(filenames[i], path, normfactor*(1 + pmi.As[i]))
#        x.read()
#        x.calc()
        Predicted.append(y)  


filename = 'ManualMeasurent.xlsx'
path = '//rpclustersrv1/cbjorkma/LSS2/'

manual = ManualClass(filename, path, normfactor)
manual.read()
path = '//rpclustersrv1/cbjorkma/LSS2/FullActivation8/Manual'
manual.readFluka(path)







import numpy as np



quad216 = 3.791*100
quad217 = 35.7887*100
quad218 = 67.7864*100
quad219 = 99.7841*100


print 'Starts plotting.....' 

fig = plt.figure()



for i in range(len(pmi.cooldowns)):

    ax = plt.subplot(3,2,i +1)
    
    cooldown = pmi.cooldowns[i]
    
#    for j in range(len(pmi.extrapolations)):
#        x = pmi.extrapolationsXes[j]
#        y = pmi.extrapolations[j]
#        f = interp1d(x,y)
#        if j == 0:
#            plt.errorbar(pmi.xpos[j],f(cooldown), color = 'c', label = 'Target',linestyle='None', fmt='o')
#        else:
#            plt.errorbar(pmi.xpos[j],f(cooldown), color = 'c',linestyle='None', fmt='o')
#            
#            
            
    plt.errorbar(pmi.xpos,pmi.targetdoseratepercooldown[i], color = 'c', label = 'Target PMIs',linestyle='None', fmt='o')        
            
    plt.title(pmi.cooldownsText[i])
    
    usrbin = USRBINS[i]
    predicted = Predicted[i]
#    smoothed = smoothListGaussian(usrbin.below)
#    plt.plot(np.arange(min(usrbin.xcoodinates),max(usrbin.xcoodinates),(max(usrbin.xcoodinates) + abs(min(usrbin.xcoodinates)))/len(smoothed) ) ,smoothed, label = 'Fluka, smoothed')
    plt.plot(usrbin.xcoodinates, usrbin.below, label = 'Fluka')
    plt.plot(generic.xcoodinates, generic.below*pmi.As[i], label = 'Predicted base activation')
    
    
    plt.errorbar(pmi.xpos,pmi.FlukaData[i,0:],yerr = pmi.FlukaData[i,0:]*pmi.FlukaSD[i,0:], label = 'Fluka PMI',linestyle='None', fmt='o', color = 'r')
    
    plt.ylabel('uSv/h',fontsize = 16)
    if i == len(pmi.cooldowns) -2 or i == len(pmi.cooldowns) -1:
        plt.xlabel('z [cm from quad216]')

    plt.legend()
    
   # plt.ylim(0,1000)
    
    ax2 = ax.twinx()
    plotSepta(ax2)
    ax2.get_yaxis().set_visible(False)
#plt.plot(pmi.extrapolations[2])


#ax.set_yscale("log", nonposy='clip')
plt.suptitle('Below beamline at PMI height. Simulation and baseline activation', fontsize = 22)
plt.show()


fig = plt.figure()
ax = plt.subplot(111)
i = 0
cooldown = pmi.cooldowns[i]
plt.errorbar(pmi.xpos,pmi.targetdoseratepercooldown[i], color = 'c', label = 'Target PMIs',linestyle='None', fmt='o')  
plt.plot(generic.xcoodinates, generic.below, label = 'Generic profile')
plt.errorbar(pmi.xpos,pmi.generic[0:],yerr = pmi.genericError[0:]*pmi.generic[0:], label = 'generic PMI',linestyle='None', fmt='o', color = 'r')
plt.plot(generic.xcoodinates, generic.below*pmi.As[i], label = 'Predicted base activation')
plt.ylabel('uSv/h',fontsize = 16)
plt.xlabel('z [cm from quad216]')
plt.legend()
plt.title('Below beamline at PMI height')
ax2 = ax.twinx()
plotSepta(ax2)
ax2.get_yaxis().set_visible(False)

plt.show()
#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------





fig = plt.figure()


ax = plt.subplot(221)
for i in range(len(pmi.cooldowns)):

    
    cooldown = pmi.cooldowns[i]
     
            
    plt.title('Predicted Baseline profiles. Sampled at PMI height', fontsize = 16)
    
#    usrbin = USRBINS[i]
#    predicted = Predicted[i]

    plt.plot(generic.xcoodinates, generic.below*pmi.As[i], label = pmi.cooldownsText[i])

    plt.legend()

#plt.plot(pmi.extrapolations[2])
    plt.ylim(10,2000)
plt.ylabel('uSv/h',fontsize = 16)
plt.xlabel('z [cm from quad216]')
plt.yscale("log", nonposy='clip')
ax2 = ax.twinx()
plotSepta(ax2)
ax2.get_yaxis().set_visible(False)

#ax.set_yscale("log", nonposy='clip')



ax = plt.subplot(222)
for i in range(len(pmi.cooldowns)):

    
    cooldown = pmi.cooldowns[i]
     
            
    plt.title('Normalized predicted baseline profiles. PMI height', fontsize = 16)
    
#    usrbin = USRBINS[i]
#    predicted = Predicted[i]

    plt.plot(generic.xcoodinates, generic.below*pmi.As[i]/max(generic.below*pmi.As[i]), label = pmi.cooldownsText[i])

    plt.legend()

#plt.plot(pmi.extrapolations[2])
plt.ylabel('uSv/h',fontsize = 16)
plt.xlabel('z [cm from quad216]')
ax2 = ax.twinx()
plotSepta(ax2)
ax2.get_yaxis().set_visible(False)



ax = plt.subplot(223)
for i in range(len(pmi.cooldowns)):

    
    cooldown = pmi.cooldowns[i]
     
            
    plt.title('Fluka profiles. 1m from beam axis', fontsize = 16)
    
    usrbin = USRBINS[i]

    plt.plot(usrbin.xcoodinates, usrbin.below, label = pmi.cooldownsText[i])

    plt.legend()

#plt.plot(pmi.extrapolations[2])
plt.ylabel('uSv/h',fontsize = 16)
plt.xlabel('z [cm from quad216]')
ax2 = ax.twinx()
plotSepta(ax2)
ax2.get_yaxis().set_visible(False)




ax = plt.subplot(224)
for i in range(len(pmi.cooldowns)):

    
    cooldown = pmi.cooldowns[i]
     
            
    plt.title('Normalized fluka profiles. 1m from beam axis', fontsize = 16)
    
    usrbin = USRBINS[i]

    plt.plot(usrbin.xcoodinates, usrbin.below/max(usrbin.below), label = pmi.cooldownsText[i])

    plt.legend()

#plt.plot(pmi.extrapolations[2])
plt.ylabel('uSv/h',fontsize = 16)
plt.xlabel('z [cm from quad216]')
ax2 = ax.twinx()
plotSepta(ax2)
ax2.get_yaxis().set_visible(False)






plt.show()
#
#fig = plt.figure()
#a = smoothListGaussian(usrbin.below)
#
#
#
#plt.plot(range(len(a)) ,a)
#
#plt.show()
#
#
#
#


#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------

from matplotlib.gridspec import GridSpec
gs = GridSpec(2, 2)

fig = plt.figure()




ax = fig.add_subplot(gs[0,0])
for i in range(len(pmi.cooldowns)):

    
    cooldown = pmi.cooldowns[i]
     
            
    plt.title('Absolut values', fontsize = 16)
    
    usrbin = USRBINS[i]

    plt.plot(usrbin.xcoodinates, usrbin.below, label = pmi.cooldownsText[i])

    plt.legend()

#plt.plot(pmi.extrapolations[2])

plt.ylabel('uSv/h',fontsize = 16)
plt.xlabel('z [cm from quad216]')
ax2 = ax.twinx()
plotSepta(ax2)
ax2.get_yaxis().set_visible(False)




ax = fig.add_subplot(gs[0,1])
for i in range(len(pmi.cooldowns)):

    
    cooldown = pmi.cooldowns[i]
     
            
    plt.title('Normalized fluka profiles', fontsize = 16)
    
    usrbin = USRBINS[i]

    plt.plot(usrbin.xcoodinates, usrbin.below/max(usrbin.below), label = pmi.cooldownsText[i])

    plt.legend()

plt.yscale("log", nonposy='clip')
plt.ylabel('uSv/h',fontsize = 16)
plt.xlabel('z [cm from quad216]')
ax2 = ax.twinx()
plotSepta(ax2)
ax2.get_yaxis().set_visible(False)




ax = fig.add_subplot(gs[1,0:2])
refUsrbin = USRBINS[len(USRBINS)-1]
for i in range(len(pmi.cooldowns) -1):

    
    cooldown = pmi.cooldowns[i]
     
            
    plt.title('Normalized fluka profiles / 80 days normalized profile', fontsize = 16)
    
    usrbin = USRBINS[i]
    ys = usrbin.below/max(usrbin.below)
    reference = refUsrbin.below/max(usrbin.below)
    
    
    plt.plot(usrbin.xcoodinates, ys / reference, label = pmi.cooldownsText[i])

    plt.legend()

plt.yscale("log", nonposy='clip')
#plt.plot(pmi.extrapolations[2])
plt.ylabel('Ratio',fontsize = 16)
plt.xlabel('z [cm from quad216]')
ax2 = ax.twinx()
plotSepta(ax2)
ax2.get_yaxis().set_visible(False)


plt.suptitle('Fluka profiles. 1m from beam axis', fontsize = 22)







#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------








#from matplotlib.gridspec import GridSpec
gs = GridSpec(5, 2)


xmin = -500
xmax = 10100

ymin = 5
ymax = 1.2*10**4


#xes = np.arange(-500,10100,(10100+500)/float(1000))

fig = plt.figure()

#ax = plt.subplot(221)
ax = fig.add_subplot(111)


plt.plot(manual.data[0:,0],manual.data[0:,1], label = 'Ring measurement')

#plt.errorbar(manual.xes, manual.fluka1, yerr = manual.fluka1*manual.errors1/100, label = 'Fluka only', color = 'r')
#plt.plot(Predicted[0].xcoodinates,Predicted[0].side[0:], label = 'Prediction', color = 'g')

plt.xlim(xmin, xmax)
plt.ylim(ymin,ymax)
plt.ylabel('uSv/h',fontsize = 22)
plt.xlabel('z [cm from quad216]',fontsize = 20)
#plt.xlabel('z [cm from quad216]')
#plt.yscale("log", nonposy='clip')


plt.legend( prop={'size': 16})


#plt.title('30h cool down', fontsize = 22)

ax2 = ax.twinx()
plotSepta(ax2)
plt.ylim(0,25)

ax2.get_yaxis().set_visible(False)
plt.legend(loc = 2, prop={'size': 16})





#ax = plt.subplot(222)
ax = fig.add_subplot(gs[0:2,1])


ymin = 0.8
ymax = 5.6*10**3



plt.plot(manual.data[0:,2],manual.data[0:,3], label = 'Manual measurement')

plt.errorbar(manual.xes, manual.fluka2, yerr = manual.fluka2*manual.errors2/100, color = 'r', label = 'Fluka only')
#plt.plot(Predicted[2].xcoodinates,Predicted[2].side[0:], color = 'g', label = 'Prediction')




plt.xlim(xmin, xmax)
plt.ylim(ymin,ymax)
plt.ylabel('uSv/h',fontsize = 16)
#plt.xlabel('z [cm from quad216]')
#plt.yscale("log", nonposy='clip')
plt.axvline(x= 0 ,linestyle = '--', color = 'k', linewidth = 0.3)
plt.axvline(x= quad217 - quad216 ,linestyle = '--', color = 'k', linewidth = 0.3)
plt.axvline(x= quad218 - quad216 ,linestyle = '--', color = 'k', linewidth = 0.3)
plt.axvline(x= quad219 - quad216 ,linestyle = '--', color = 'k', linewidth = 0.3)

plt.legend()

plt.title('1 month + 30h cool down', fontsize = 22)

ax2 = ax.twinx()
plotSepta(ax2)

plt.ylim(0,25)
ax2.get_yaxis().set_visible(False)








ax = fig.add_subplot(gs[2:4,0])
x = manual.data[0:,0]
y = manual.data[0:,1]
f = interp1d(x,y)


#plt.plot(manual.data[0:,0],f(manual.data[0:,0])/manual.data[0:,1], label = 'Predicted/Manual measurement')

#plt.errorbar(xes, Predicted[0].side[0:]/manual.fluka1, yerr = manual.fluka1*manual.errors1/100, label = 'Fluka')
#plt.plot(Predicted[0].xcoodinates,f(Predicted[0].xcoodinates) - Predicted[0].side[0:], label = 'Measured - Predicted', color = 'g')
plt.plot(manual.xes, f(manual.xes) - manual.fluka1 , label = 'Measured - Fluka only', color = 'r')


#textstr = 'Sum diff predicted/Fluka only: ' +  str( round(sum(abs(f(Predicted[0].xcoodinates) - Predicted[0].side[0:]))/sum(abs(f(manual.xes) - manual.fluka1)),5)) 
#props = dict(boxstyle='round', facecolor='white', alpha=1)
#
#ax.text(0.05, 0.95, textstr, transform=ax.transAxes, fontsize=10,
#    verticalalignment='top',bbox=props) 



plt.xlim(xmin, xmax)
#plt.ylim(ymin,ymax)
plt.ylabel('Measured - estimation [uSv/h]',fontsize = 12)
#plt.xlabel('z [cm from quad216]')
#plt.yscale("log", nonposy='clip')

plt.axvline(x= 0 ,linestyle = '--', color = 'k', linewidth = 0.3)
plt.axvline(x= quad217 - quad216 ,linestyle = '--', color = 'k', linewidth = 0.3)
plt.axvline(x= quad218 - quad216 ,linestyle = '--', color = 'k', linewidth = 0.3)
plt.axvline(x= quad219 - quad216 ,linestyle = '--', color = 'k', linewidth = 0.3)
plt.legend()
plt.axhline(y=0, color='k', linestyle='-')


#plt.title('30h cool down')

ax2 = ax.twinx()
plotSepta(ax2)
ax2.get_yaxis().set_visible(False)

ax = fig.add_subplot(gs[2:4,1])
x = manual.data[0:,2]
y = manual.data[0:,3]
f = interp1d(x,y)


#plt.plot(manual.data[0:,0],f(manual.data[0:,0])/manual.data[0:,1], label = 'Predicted/Manual measurement')

#plt.errorbar(xes, Predicted[0].side[0:]/manual.fluka1, yerr = manual.fluka1*manual.errors1/100, label = 'Fluka')
#plt.plot(Predicted[2].xcoodinates,f(Predicted[2].xcoodinates) - Predicted[2].side[0:] , label = 'Measured - Predicted', color = 'g')
plt.plot(manual.xes, f(manual.xes) - manual.fluka2, label = 'Measured - Fluka only', color = 'r')


#textstr = 'Sum diff predicted/Fluka only: ' +  str( round(sum(abs(f(Predicted[2].xcoodinates) - Predicted[2].side[0:]))/sum(abs(f(manual.xes) - manual.fluka2)),5)) 
#props = dict(boxstyle='round', facecolor='white', alpha=1)
#
#ax.text(0.05, 0.95, textstr, transform=ax.transAxes, fontsize=10,
#    verticalalignment='top',bbox=props) 


plt.xlim(xmin, xmax)
#plt.ylim(ymin,ymax)
plt.ylabel('Measured - estimation [uSv/h]',fontsize = 12)
#plt.xlabel('z [cm from quad216]')
#plt.yscale("log", nonposy='clip')

plt.axvline(x= 0 ,linestyle = '--', color = 'k', linewidth = 0.3)
plt.axvline(x= quad217 - quad216 ,linestyle = '--', color = 'k', linewidth = 0.3)
plt.axvline(x= quad218 - quad216 ,linestyle = '--', color = 'k', linewidth = 0.3)
plt.axvline(x= quad219 - quad216 ,linestyle = '--', color = 'k', linewidth = 0.3)
plt.legend()
plt.axhline(y=0, color='k', linestyle='-')

#plt.title('1month + 30h cool down')


ax2 = ax.twinx()
plotSepta(ax2)

ax2.get_yaxis().set_visible(False)





#plt.subplot(223)
ax = fig.add_subplot(gs[4,0])

x = manual.data[0:,0]
y = manual.data[0:,1]
f = interp1d(x,y)


#plt.plot(manual.data[0:,0],f(manual.data[0:,0])/manual.data[0:,1], label = 'Predicted/Manual measurement')

#plt.errorbar(xes, Predicted[0].side[0:]/manual.fluka1, yerr = manual.fluka1*manual.errors1/100, label = 'Fluka')
#plt.plot(Predicted[0].xcoodinates,f(Predicted[0].xcoodinates)/Predicted[0].side[0:], label = 'Measured/Predicted',color = 'g')
plt.plot(manual.xes, manual.fluka1/f(manual.xes), label = 'Fluka only/Measured', color = 'r')






plt.xlim(xmin, xmax)
#plt.ylim(ymin,ymax)
plt.ylabel('Ratio',fontsize = 16)
plt.xlabel('z [cm from quad216]')
#plt.yscale("log", nonposy='clip')

plt.axvline(x= 0 ,linestyle = '--', color = 'k', linewidth = 0.3)
plt.axvline(x= quad217 - quad216 ,linestyle = '--', color = 'k', linewidth = 0.3)
plt.axvline(x= quad218 - quad216 ,linestyle = '--', color = 'k', linewidth = 0.3)
plt.axvline(x= quad219 - quad216 ,linestyle = '--', color = 'k', linewidth = 0.3)
plt.legend()
plt.axhline(y=1, color='k', linestyle='-')


#plt.title('30h cool down')

ax2 = ax.twinx()
plotSepta(ax2)
ax2.get_yaxis().set_visible(False)






#plt.subplot(224)
ax = fig.add_subplot(gs[4,1])

x = manual.data[0:,2]
y = manual.data[0:,3]
f = interp1d(x,y)


#plt.plot(manual.data[0:,0],f(manual.data[0:,0])/manual.data[0:,1], label = 'Predicted/Manual measurement')

#plt.errorbar(xes, Predicted[0].side[0:]/manual.fluka1, yerr = manual.fluka1*manual.errors1/100, label = 'Fluka')
#plt.plot(Predicted[2].xcoodinates,f(Predicted[2].xcoodinates)/Predicted[2].side[0:], label = 'Measured/Predicted', color = 'g')
plt.plot(manual.xes, manual.fluka2/f(manual.xes), label = 'Fluka only/Measured', color = 'r')


plt.xlim(xmin, xmax)
#plt.ylim(ymin,ymax)
plt.ylabel('Ratio',fontsize = 16)
plt.xlabel('z [cm from quad216]')
#plt.yscale("log", nonposy='clip')

plt.axvline(x= 0 ,linestyle = '--', color = 'k', linewidth = 0.3)
plt.axvline(x= quad217 - quad216 ,linestyle = '--', color = 'k', linewidth = 0.3)
plt.axvline(x= quad218 - quad216 ,linestyle = '--', color = 'k', linewidth = 0.3)
plt.axvline(x= quad219 - quad216 ,linestyle = '--', color = 'k', linewidth = 0.3)
plt.legend()
plt.axhline(y=1, color='k', linestyle='-')

#plt.title('1month + 30h cool down')


ax2 = ax.twinx()
plotSepta(ax2)

ax2.get_yaxis().set_visible(False)



plt.suptitle('Validation of approach. Sampling 1 meter from beam axis', fontsize = 25)



plt.show()
















#------------------------------------


xmin = -500
xmax = 10100

ymin = 5
ymax = 1.8*10**4


#xes = np.arange(-500,10100,(10100+500)/float(1000))

fig = plt.figure()

#ax = plt.subplot(221)
ax = fig.add_subplot(211)


plt.plot(manual.data[0:,0],manual.data[0:,1], label = 'Ring measurement',linewidth = 4)

for i in range(1,5):
    plt.errorbar(manual.xes, i*manual.fluka1, yerr = manual.fluka1*manual.errors1/100, label = 'Fluka *' + str(i))
#plt.plot(Predicted[0].xcoodinates,Predicted[0].side[0:], label = 'Prediction', color = 'g')

plt.xlim(xmin, xmax)
plt.ylim(ymin,ymax)
plt.ylabel('uSv/h',fontsize = 16)
#plt.xlabel('z [cm from quad216]')
#plt.yscale("log", nonposy='clip')


plt.legend()


plt.title('30h cool down', fontsize = 22)

ax2 = ax.twinx()
plotSepta(ax2)
plt.ylim(0,25)

ax2.get_yaxis().set_visible(False)






#ax = plt.subplot(222)
ax = fig.add_subplot(212)


ymin = 0.8
ymax = 5*10**3



plt.plot(manual.data[0:,2],manual.data[0:,3], label = 'Ring measurement',linewidth = 4)
for i in range(1,5):
    plt.errorbar(manual.xes, i*manual.fluka2, yerr = manual.fluka2*manual.errors2/100, label = 'Fluka *' + str(i))
#plt.plot(Predicted[2].xcoodinates,Predicted[2].side[0:], color = 'g', label = 'Prediction')




plt.xlim(xmin, xmax)
plt.ylim(ymin,ymax)
plt.ylabel('uSv/h',fontsize = 16)
#plt.xlabel('z [cm from quad216]')
#plt.yscale("log", nonposy='clip')
plt.axvline(x= 0 ,linestyle = '--', color = 'k', linewidth = 0.3)
plt.axvline(x= quad217 - quad216 ,linestyle = '--', color = 'k', linewidth = 0.3)
plt.axvline(x= quad218 - quad216 ,linestyle = '--', color = 'k', linewidth = 0.3)
plt.axvline(x= quad219 - quad216 ,linestyle = '--', color = 'k', linewidth = 0.3)

plt.legend()

plt.title('1 month + 30h cool down', fontsize = 22)

ax2 = ax.twinx()
plotSepta(ax2)

plt.ylim(0,25)
ax2.get_yaxis().set_visible(False)




















