# -*- coding: utf-8 -*-
"""
Created on Wed Nov 07 14:49:48 2018

@author: cbjorkma
"""

import matplotlib.patches as patches
import matplotlib.pyplot as plt


plt.close()
plt.close()
plt.close()
plt.close()
plt.close()
plt.close()
plt.close()
plt.close()

septaColor = 'limegreen'

def plotSepta(ax):
    from scipy import interp
    import math
    import matplotlib.patches as patches
#    positions = [511.95, 902.95, 1293.95, 1684.95 , 2075.95]
#    Xshift = math.sin(LindaAngle) *312/2
#    Yshift = math.cos(LindaAngle)*312/2  
    quad216 = 3.791*100
    quad217 = 35.7887*100
    quad218 = 67.7864*100
    quad219 = 99.7841*100

    
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








from USRBIN import USRBIN
import numpy as np

#Converts data to uSv/h and normalizes data to the number of exstracted particles
normfactor = 0.0036/0.19837024


import os
#







##
path = '//rpclustergw/cbjorkma/LSS2/ref2'
os.chdir(path)
filenames = sorted(os.listdir(path))
try:
    print ref
except:
    print 'Loading USRBINs...'
    ref = []
    for i in range(len(filenames)):
        x = USRBIN(filenames[i], path, normfactor)
        x.read()
        x.calc()
        ref.append(x)
        
   
##
path = '//rpclustergw/cbjorkma/LSS2/TPST15'
os.chdir(path)
filenames = sorted(os.listdir(path))
try:
    print TPST15
except:
    print 'Loading USRBINs...'
    TPST15 = []
    for i in range(len(filenames)):
        x = USRBIN(filenames[i], path, normfactor)
        x.read()
        x.calc()
        TPST15.append(x)

     
        
##
path = '//rpclustergw/cbjorkma/LSS2/TPST20'
os.chdir(path)
filenames = sorted(os.listdir(path))
try:
    print TPST20
except:
    print 'Loading USRBINs...'
    TPST20 = []
    for i in range(len(filenames)):
        x = USRBIN(filenames[i], path, normfactor)
        x.read()
        x.calc()
        TPST20.append(x)

path = '//rpclustergw/cbjorkma/LSS2/TPST25'
os.chdir(path)
filenames = sorted(os.listdir(path))
try:
    print TPST25
except:
    print 'Loading USRBINs...'
    TPST25 = []
    for i in range(len(filenames)):
        x = USRBIN(filenames[i], path, normfactor)
        x.read()
        x.calc()
        TPST25.append(x)




path = '//rpclustergw/cbjorkma/LSS2/aluCont2'
os.chdir(path)
filenames = sorted(os.listdir(path))
try:
    print cont2
except:
    print 'Loading USRBINs...'
    cont2 = []
    for i in range(len(filenames)):
        x = USRBIN(filenames[i], path, normfactor)
        x.read()
        x.calc()
        cont2.append(x)
        
    
path = '//rpclustergw/cbjorkma/LSS2/SepHoldTitanium'
os.chdir(path)
filenames = sorted(os.listdir(path))
try:
    print sepHold
except:
    print 'Loading USRBINs...'
    sepHold = []
    for i in range(len(filenames)):
        x = USRBIN(filenames[i], path, normfactor)
        x.read()
        x.calc()
        sepHold.append(x)
        
    

    
path = '//rpclustergw/cbjorkma/LSS2/Carbon Wire/USRBINs'
os.chdir(path)
filenames = sorted(os.listdir(path))
try:
    print carbon
except:
    print 'Loading USRBINs...'
    carbon = []
    for i in range(len(filenames)):
        x = USRBIN(filenames[i], path, normfactor)
        x.read()
        x.calc()
        carbon.append(x)
    

#path = '//rpclustergw/cbjorkma/LSS2/aluGirder'
#os.chdir(path)
#filenames = sorted(os.listdir(path))
#try:
#    print gird
#except:
#    print 'Loading USRBINs...'
#    gird = []
#    for i in range(len(filenames)):
#        x = USRBIN(filenames[i], path, normfactor)
#        x.read()
#        x.calc()
#        gird.append(x)
#        
    
    
path = '//rpclustergw/cbjorkma/LSS2/pipe'
os.chdir(path)
filenames = sorted(os.listdir(path))
try:
    print pipe
except:
    print 'Loading USRBINs...'
    pipe = []
    for i in range(len(filenames)):
        x = USRBIN(filenames[i], path, normfactor)
        x.read()
        x.calc()
        pipe.append(x)
        
path = '//cern.ch/dfs/Users/c/cbjorkma/Documents/LSS 2/dwnshld'
os.chdir(path)
filenames = sorted(os.listdir(path))
try:
    print mod
except:
    print 'Loading USRBINs...'
    mod = []
    for i in range(len(filenames)):
        x = USRBIN(filenames[i], path, normfactor)
        x.read()
        x.calc()
        mod.append(x)


path = '//cern.ch/dfs/Users/c/cbjorkma/Documents/LSS 2/dwnshld6'
os.chdir(path)
filenames = sorted(os.listdir(path))
try:
    print mod2
except:
    print 'Loading USRBINs...'
    mod2 = []
    for i in range(len(filenames)):
        x = USRBIN(filenames[i], path, normfactor)
        x.read()
        x.calc()
        mod2.append(x)

path = '//rpclustergw/cbjorkma/LSS2/2alu'
os.chdir(path)
filenames = sorted(os.listdir(path))
try:
    print alu2
except:
    print 'Loading USRBINs...'
    alu2 = []
    for i in range(len(filenames)):
        x = USRBIN(filenames[i], path, normfactor)
        x.read()
        x.calc()
        alu2.append(x)


import matplotlib.pyplot as plt
import os
import pandas as pd
#        import datetime #, timedelta
#        import matplotlib.pyplot as plt

path =  '//cern.ch/dfs/Users/c/cbjorkma/Documents/LSS 2'

os.chdir(path)

filename = '2018rate.xlsx'

thefile = pd.read_excel(filename)

data = np.zeros(thefile.shape)

quad216 = 3.791*100
quad217 = 35.7887*100
quad218 = 67.7864*100
quad219 = 99.7841*100

data[0:,0] = (thefile.Position -216)*(quad217 - quad216) -580
data[0:,1] = thefile.rate
data[0:,2] = (thefile.position2 -216)*(quad217 - quad216) -480
data[0:,3] = thefile.rate2


#import math
import matplotlib.pyplot as plt

fig = plt.figure()

ax = plt.subplot(111)
    

plt.plot(data[0:,0], data[0:,1], label = '2018 Ring measurement', linewidth = 2)



#plt.plot(data[0:,2], data[0:,3], label = '2017')

#plt.plot(ref[1].xcoodinates, ref[1].side*20, label = 'Fluka')

#plt.plot(xes, cube3.side/cube1.side, label = 'Al6061 tanks + beampipe/Current setup')
#plt.axhline(y=1, color='k', linestyle='-')


#plt.title('', fontsize = 12)
#plt.legend(loc = 1)

plt.legend(loc = 1, prop={'size': 18})

plt.xlabel('z [cm from quad 216]', fontsize = 22)
plt.ylabel('[uSv/h]', fontsize = 18)
plt.xlim(0,11000)
#plt.yscale("log", nonposy='clip')
ax2 = ax.twinx()
plotSepta(ax2)
ax2.get_yaxis().set_visible(False)
plt.ylim([3.5,12])
plt.legend(loc = 2, prop={'size': 18})
#plt.xlim(-570,2800)


ax2.text(812, 4.7, '5 ZSs', fontsize = 12 ) #math.degrees(1.414490E-3)
ax2.text(4200, 4.4, 'TPST', fontsize = 12 )
ax2.text(5150, 3.8, '3 MSTs', fontsize = 12 )
ax2.text(7850, 6, '5 MSEs', fontsize = 12 )


xlength = 9

fig.set_size_inches(xlength, xlength/(1.618*1))

plt.show()
#
#plt.savefig('RingMeasurement2018.pdf')
#




    
xes = ref[0].xcoodinates
    

#cooldowns = ['1h','30h','1 week']

cooldowns = ['1h','30h', '1 week']

fig = plt.figure()

count = 1
for i in [0,2]:
    
    ax = plt.subplot(2,1,count)
    count = count +1

    cube1 = ref[i]
    cube2 = cont2[i]
    cube3 = alu2[i]
    #cube3 = alu[i]
    
#    plt.plot(xes, cube1.side, label = 'Current setup')
#    plt.plot(xes, cube2.side, label = 'Modified setup')
    
    plt.plot(xes, cube2.side/cube1.side, label = 'Al6061')
    plt.plot(xes, cube3.side/cube1.side, label = 'Al2219')
    #plt.plot(xes, cube3.side/cube1.side, label = 'Al6061 tanks + beampipe/Current setup')
    plt.axhline(y=1, color='k', linestyle='-')
    
    
    plt.title(cooldowns[i], fontsize = 12)
    plt.legend(loc = 1)
    if i == 2:
        plt.xlabel('z [cm from quad 216]')
    plt.ylabel('Fraction dose rate', fontsize = 12)
    plt.ylim(0.3,1.4)
    #plt.yscale("log", nonposy='clip')
    ax2 = ax.twinx()
    plotSepta(ax2)
    ax2.get_yaxis().set_visible(False)
    plt.ylim([0,30])
    plt.legend(loc = 2)
    plt.xlim(3173,9566)


plt.suptitle('Al6061 and Al2219 comparison for vacuum tanks', fontsize = 16)
plt.show()
    
    
    
    
    
cooldowns = ['1h','1 week']
    

#    
#    
#    cooldowns = ['1h','1 week']
#    
#    fig = plt.figure()
#    
#    for i in range(0,3,2):
#        
#        if i ==0:
#            ax = plt.subplot(2,1,1)
#        else:
#            ax = plt.subplot(2,1,2)
#        cube1 = ref[i]
#        cube2 = gird[i]
#        #cube3 = TPST25[i]
#        #cube3 = alu[i]
#        
#    #    plt.plot(xes, cube1.side, label = 'Current setup')
#    #    plt.plot(xes, cube2.side, label = 'Modified setup')
#        
#        plt.plot(xes, cube2.feetdose/cube1.feetdose, label = 'Al6061 Girder/Reference')
#        #plt.plot(xes, cube3.side/cube1.side, label = '25 cm shielding/Reference')
#        #plt.plot(xes, cube3.side/cube1.side, label = 'Al6061 tanks + beampipe/Current setup')
#        plt.axhline(y=1, color='k', linestyle='-')
#        
#        
#        plt.title(cooldowns.pop(0), fontsize = 12)
#        plt.legend(loc = 1)
#        if i == 2:
#            plt.xlabel('cm from quad 216')
#        plt.ylabel('Fraction dose rate', fontsize = 12)
#        plt.ylim(0.5,1.4)
#        plt.xlim(141,8300)
#        #plt.yscale("log", nonposy='clip')
#        ax2 = ax.twinx()
#        plotSepta(ax2)
#        ax2.get_yaxis().set_visible(False)
#        plt.ylim([0,30])
#        plt.legend(loc = 2)
#        #plt.xlim(-570,2800)
#    
#    
#    plt.suptitle('Alu6061 Girder. Sampling next to girder at girder height', fontsize = 16)
#    plt.show()
#    
#    
#    
#    
#    
    
    cooldowns = ['1h','1 week']
    
    fig = plt.figure()
    
    for i in range(0,3,2):
        
        if i ==0:
            ax = plt.subplot(2,1,1)
        else:
            ax = plt.subplot(2,1,2)
        cube1 = ref[i]
        cube3 = pipe[i]
        cube2 = cont2[i]
        #cube3 = TPST25[i]
        #cube3 = alu[i]
        
    #    plt.plot(xes, cube1.side, label = 'Current setup')
    #    plt.plot(xes, cube2.side, label = 'Modified setup')
        
        #plt.plot(xes, cube2.side/cube1.side, label = '1 meter from beam axis')
        plt.plot(xes, cube3.pipe/cube1.pipe, label = 'Contact with beampipe')
        plt.plot(xes, cube2.side/cube1.side, label = 'Contact with beampipe')
        #plt.plot(xes, cube3.side/cube1.side, label = 'Al6061 tanks + beampipe/Current setup')
        plt.axhline(y=1, color='k', linestyle='-')
        
        
        plt.title(cooldowns.pop(0), fontsize = 12)
        plt.legend(loc = 1)
        if i == 2:
            plt.xlabel('cm from quad 216')
        plt.ylabel('Fraction dose rate', fontsize = 12)
        plt.ylim(0.05,1.3)
        plt.xlim(200,10000)
        #plt.yscale("log", nonposy='clip')
        ax2 = ax.twinx()
        plotSepta(ax2)
        ax2.get_yaxis().set_visible(False)
        plt.ylim([0,30])
        plt.legend(loc = 2)
        #plt.xlim(-570,2800)
    
    
    plt.suptitle('Alu6061 Pipe', fontsize = 16)
    plt.show()
    










fig = plt.figure()


ax = plt.subplot(211)
    

plt.plot(data[0:,0], data[0:,1], label = '2018 Ring measurement', linewidth = 2)



#plt.plot(data[0:,2], data[0:,3], label = '2017')

#plt.plot(ref[1].xcoodinates, ref[1].side*20, label = 'Fluka')

#plt.plot(xes, cube3.side/cube1.side, label = 'Al6061 tanks + beampipe/Current setup')
#plt.axhline(y=1, color='k', linestyle='-')


#plt.title('', fontsize = 12)
#plt.legend(loc = 1)

plt.legend(loc = 1, prop={'size': 18})

#plt.xlabel('z [cm from quad 216]', fontsize = 22)
#plt.ylabel('[uSv/h]', fontsize = 18)
plt.xlim(3200,6770)
#plt.yscale("log", nonposy='clip')
ax2 = ax.twinx()
plotSepta(ax2)
ax2.get_yaxis().set_visible(False)
plt.ylim([3.5,12])
plt.legend(loc = 2, prop={'size': 18})
#plt.xlim(-570,2800)


ax2.text(1150, 4.7, '5 ZSs', fontsize = 12 ) #math.degrees(1.414490E-3)
ax2.text(4650, 4.6, 'TPST', fontsize = 12 )
ax2.text(5150, 5.0, '3 MSTs', fontsize = 12 )
ax2.text(7850, 6, '5 MSEs', fontsize = 12 )


xlength = 9

fig.set_size_inches(xlength, xlength/(1.618*1))




#for i in [1]: #range(0,3,2):
i = 1
#    if i ==0:
#        ax = plt.subplot(2,1,1)
#    else:
#        ax = plt.subplot(2,1,2)
ax = plt.subplot(2,1,2) 
    
cube1 = ref[i]
#cube2 = TPST15[i]
cube2 = TPST20[i]
cube3 = mod2[i]
#cube4 = TPST25[i]
#cube3 = alu[i]

#    plt.plot(xes, cube1.side, label = 'Current setup')
#    plt.plot(xes, cube2.side, label = 'Modified setup')

#plt.plot(xes, cube2.side/cube1.side, label = '15 cm shielding/Reference')
plt.plot(xes, cube2.side/cube1.side, label = 'TPST shielding/Reference', linewidth = 2) #'20 cm shielding/Reference'
plt.plot(xes, cube3.side/cube1.side, label = 'Quad218 shielding/Reference', linewidth = 2)
#plt.plot(xes, cube4.side/cube1.side, label = '25 cm shielding/Reference')
#plt.plot(xes, cube3.side/cube1.side, label = 'Al6061 tanks + beampipe/Current setup')
plt.axhline(y=1, color='k', linestyle='-')


#plt.title(cooldowns.pop(0), fontsize = 12)
#plt.title('Reduced residual dose rate from Shielding implementation', fontsize = 12)

plt.legend(loc = 1, prop={'size': 12})
#if i == 2:
plt.xlabel('z [cm from quad 216]', fontsize = 16)
#plt.ylabel('Fraction residual ambient dose equivalent rate', fontsize = 18)
plt.ylim(0.05,1.4)
plt.xlim(3200,6770)
#plt.yscale("log", nonposy='clip')
ax2 = ax.twinx()
plotSepta(ax2)
ax2.text(1150, 4.7, '5 ZSs', fontsize = 12 ) #math.degrees(1.414490E-3)
ax2.text(4650, 4.6, 'TPST', fontsize = 12 )
ax2.text(5150, 5.0, '3 MSTs', fontsize = 12 )
ax2.text(7850, 6, '5 MSEs', fontsize = 12 )

ax2.get_yaxis().set_visible(False)
plt.ylim([3.5,12])
plt.legend(loc = 2, prop={'size': 16})
#plt.xlim(-570,2800)


#plt.title('1 week cool down, 1 meter from beam axis', fontsize = 12)
#plt.suptitle('Reduced residual dose rate from shielding implementation', fontsize = 18)
xlength = 12

fig.set_size_inches(xlength, xlength/1.618)

plt.show()
#
#plt.savefig('AllShielding.pdf')  

    







import statsmodels.api as sm
import matplotlib.gridspec as gridspec    
cooldowns = ['1h','1 week']

fig = plt.figure()

#gs1 = gridspec.GridSpec(4, 1)
#gs1.update(wspace=0.025, hspace=0.05)
#for i in [1]: #range(0,3,2):
i = 2
#    
#    if i ==0:
#        ax = plt.subplot(2,1,1)
#    else:
#        ax = plt.subplot(2,1,2)
#        
ax = plt.subplot(1,1,1)
#ax = plt.subplot(gs1[0:-1,0])
#ax.set_xticklabels([])

cube1 = ref[i]
cube2 = cont2[i]
cube3 = pipe[i]
cube4 = sepHold[i]
cube5 = carbon[i]

stop = 300
stop2 = 1000

#cube3 = TPST25[i]
#cube3 = alu[i]
linewidth = 3
#    plt.plot(xes, cube1.side, label = 'Current setup')
#    plt.plot(xes, cube2.side, label = 'Modified setup')
#lowess = sm.nonparametric.lowess(cube2.side/cube1.side, xes, frac=0.05)
#plt.plot(lowess[:, 0], lowess[:, 1], label = 'Al6061 vacuum tanks @ 1 meter from beam axis', linewidth = linewidth)



#plt.plot(xes, cube2.side/cube1.side, label = 'Al6061 vacuum tanks @ 1 meter from beam axis')

#lowess = sm.nonparametric.lowess(cube3.pipe/cube1.pipe, xes, frac=0.05)
plt.plot(xes, cube3.pipe/cube1.pipe, label = 'Al6061 beampipe @ contact with beampipe', linewidth = linewidth)
#plt.plot(xes, cube3.pipe/cube1.pipe, label = 'Al6061 beampipe @ contact with beampipe')

#lowess = sm.nonparametric.lowess(cube4.side/cube1.side, xes, frac=0.05)
#plt.plot(lowess[:, 0], lowess[:, 1], label = 'Titanium ZS anode support @ 1 meter from beam axis', linewidth = linewidth)

#lowess = sm.nonparametric.lowess(cube4.pipe/cube1.pipe, xes, frac=0.05)
#plt.plot(lowess[:, 0], lowess[:, 1], label = 'Titanium ZS anode support @ Contact with vacuum tank', linewidth = linewidth)


#plt.plot(xes[:stop], cube4.side[:stop]/cube1.side[:stop], label = 'Titanium ZS anode support @ 1 meter from beam axis')

#lowess = sm.nonparametric.lowess(cube5.side[:stop2]/cube1.side[:stop2], xes[:stop2], frac=0.05)
#plt.plot(lowess[:, 0], lowess[:, 1], label = 'Carbon ZS anode septa @ 1 meter from beam axis', linewidth = linewidth)
##plt.plot(xes[:stop2], cube5.side[:stop2]/cube1.side[:stop2], label = 'Carbon ZS anode septa @ 1 meter from beam axis')
##plt.plot(xes, cube3.side/cube1.side, label = 'Al6061 tanks + beampipe/Current setup')


plt.axhline(y=1, color='k', linestyle='-')


#plt.title(cooldowns.pop(0), fontsize = 12)
plt.legend(loc = 1, prop={'size': 12})
plt.xlabel('z [cm from quad 216]', fontsize = 18)
plt.ylabel('Fraction residual ambient dose equivalent rate', fontsize = 18)
plt.ylim(0.001,1.3)
plt.xlim(200,9586)

#plt.yscale("log", nonposy='clip')
ax2 = ax.twinx()
plotSepta(ax2)
ax2.get_yaxis().set_visible(False)

ax2.text(1150, 4.7, '5 ZSs', fontsize = 12 ) #math.degrees(1.414490E-3)
ax2.text(4400, 4.4, 'TPST', fontsize = 12 )
ax2.text(5150, 3.8, '3 MSTs', fontsize = 12 )
ax2.text(7850, 6, '5 MSEs', fontsize = 12 )

plt.ylim([3.5,12])
plt.legend(loc = 2, prop={'size': 12})
#plt.xlim(-570,2800)
#
#
#ax = plt.subplot(gs1[-1,0])
#
#plt.plot(data[0:,0], data[0:,1], label = 'Ring measurement', linewidth = 2)
#
#plt.legend(loc = 1, prop={'size': 18})
#
#plt.xlabel('z [cm from quad 216]', fontsize = 22)
#plt.ylabel('[uSv/h]', fontsize = 18)
#plt.xlim(200,9586)
##plt.yscale("log", nonposy='clip')
#ax2 = ax.twinx()
#plotSepta(ax2)
#ax2.get_yaxis().set_visible(False)
#plt.ylim([3.5,12])
##plt.legend(loc = 2, prop={'size': 18})


xlength = 12

fig.set_size_inches(xlength, xlength/1.618)

plt.show()
#
#plt.savefig('MaterialReduction.pdf')  
    








fig = plt.figure()

ax = plt.subplot(111)
    

plt.plot(data[0:,0], data[0:,1], label = 'Ring measurement', linewidth = 2)

factor = 3

plt.plot(xes, factor*cube1.side, label = 'Ref')
plt.plot(xes, factor*cube2.side, label = 'Vacuum tanks')
plt.plot(xes, factor*cube3.side, label = 'Pipe')
plt.plot(xes, factor*cube4.side, label = 'Septum support')
plt.plot(xes, factor*cube4.side, label = 'Carbon wires')


plt.legend(loc = 1, prop={'size': 18})

plt.xlabel('z [cm from quad 216]', fontsize = 22)
plt.ylabel('[uSv/h]', fontsize = 18)
plt.xlim(0,11000)
#plt.yscale("log", nonposy='clip')
ax2 = ax.twinx()
plotSepta(ax2)
ax2.get_yaxis().set_visible(False)
plt.ylim([3.5,12])
plt.legend(loc = 2, prop={'size': 18})
#plt.xlim(-570,2800)

xlength = 9

fig.set_size_inches(xlength, xlength/(1.618*1))

plt.show()
#



i = 1

cube1 = ref[i]
cube2 = cont2[i]
cube3 = pipe[i]
cube4 = sepHold[i]
cube5 = carbon[i]

cube6 = TPST20[i]
cube7 = mod2[i]



from scipy.interpolate import interp1d
xring = data[0:,0]
yring = data[0:,1]
ring = interp1d(xring,yring)


x = xes
y = cube2.side/cube1.side
reductionTanks = interp1d(x,y)

y = cube3.side/cube1.side
reductionPipes = interp1d(x,y)

y = cube4.side/cube1.side
reductionSeptasupport = interp1d(x,y)

y = cube5.side/cube1.side
reductionSepta = interp1d(x,y)


y = cube6.side/cube1.side
reductionTPST = interp1d(x,y)

y = cube7.side/cube1.side
reductionShield2 = interp1d(x,y)



now = sum(ring(xes))

tankBenefit = np.nansum(reductionTanks(xes)*ring(xes))/now
print str(tankBenefit) + ' from tanks'
print str((now - np.nansum(reductionTanks(xes)*ring(xes)))/1000) + ' fom'

print ' '

pipeBenefit = np.nansum(reductionPipes(xes)*ring(xes))/now
print str(pipeBenefit) + ' from Pipes'
#print str(np.nansum(reductionPipes(xes)*ring(xes))/500) + ' fom'



print ' '
#
septaSupportBenefit = np.nansum(reductionSeptasupport(xes)*ring(xes))/now
print str(pipeBenefit) + ' from Septa Support'
print str((now - np.nansum(reductionSeptasupport(xes)*ring(xes)))/500) + ' fom'



print ' '

septatBenefit = np.nansum(reductionSepta(xes)*ring(xes))/now
print str(septatBenefit) + ' from Septa'
print str((now - np.nansum(reductionSepta(xes)*ring(xes)))/500) + ' fom'




print ' '

TPSTbenefit = np.nansum(reductionTPST(xes)*ring(xes))/now
print str(TPSTbenefit) + ' from TPST shielding'
print str((now - np.nansum(reductionTPST(xes)*ring(xes)))/100) + ' fom'

print ' '

shield2Benefit = np.nansum(reductionShield2(xes)*ring(xes))/now
print str(shield2Benefit) + ' from Quad218 shielding'

































