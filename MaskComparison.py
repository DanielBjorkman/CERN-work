# -*- coding: utf-8 -*-




#MaskComparison


import matplotlib.patches as patches
import matplotlib.pyplot as plt



from USRBIN import USRBIN
import numpy as np

#Converts data to uSv/h and normalizes data to the number of exstracted particles
normfactor = 0.0036

import os
#
##
#path = '//rpclustersrv1/cbjorkma/Dump studies/MaskComparison/WithMask'
#os.chdir(path)
#filenames = sorted(os.listdir(path))
#try:
#    print normal
#except:
#    print 'Loading USRBINs...'
#    normal = []
#    for i in range(len(filenames)):
#        x = USRBIN(filenames[i], path, normfactor)
#        x.read()
#        x.calc()
#        normal.append(x)


#
#path = '//rpclustersrv1/cbjorkma/Dump studies/MaskComparison/WithoutMask'
#os.chdir(path)
#filenames = sorted(os.listdir(path))
#try:
#    print modi
#except:
#    print 'Loading USRBINs...'
#    modi = []
#    for i in range(len(filenames)):
#        x = USRBIN(filenames[i], path, normfactor)
#        x.read()
#        x.calc()
#        modi.append(x)
#
#
#
#path = '//rpclustersrv1/cbjorkma/Dump studies/Fill'
#os.chdir(path)
#filenames = sorted(os.listdir(path))
#try:
#    print fill
#except:
#    print 'Loading USRBINs...'
#    fill = []
#    for i in range(len(filenames)):
#        x = USRBIN(filenames[i], path, normfactor)
#        x.read()
#        x.calc()
#        fill.append(x)
#        
#        
#path = '//rpclustersrv1/cbjorkma/Dump studies/Radi'
#os.chdir(path)
#filenames = sorted(os.listdir(path))
#try:
#    print radi
#except:
#    print 'Loading USRBINs...'
#    radi = []
#    for i in range(len(filenames)):
#        x = USRBIN(filenames[i], path, normfactor)
#        x.read()
#        x.calc()
#        radi.append(x)
#
#
#path = '//rpclustersrv1/cbjorkma/Dump studies/Old'
#os.chdir(path)
#filenames = sorted(os.listdir(path))
#try:
#    print Old
#except:
#    print 'Loading USRBINs...'
#    Old = []
#    for i in range(len(filenames)):
#        x = USRBIN(filenames[i], path, normfactor)
#        x.read()
#        x.calc()
#        Old.append(x)
#
#
#
#path = '//rpclustersrv1/cbjorkma/Dump studies/Extend'
#os.chdir(path)
#filenames = sorted(os.listdir(path))
#try:
#    print extend
#except:
#    print 'Loading USRBINs...'
#    extend = []
#    for i in range(len(filenames)):
#        x = USRBIN(filenames[i], path, normfactor)
#        x.read()
#        x.calc()
#        extend.append(x)
#
#path = '//rpclustersrv1/cbjorkma/Dump studies/Dump16'
#os.chdir(path)
#filenames = sorted(os.listdir(path))
#try:
#    print dump16
#except:
#    print 'Loading USRBINs...'
#    dump16 = []
#    for i in range(len(filenames)):
#        x = USRBIN(filenames[i], path, normfactor)
#        x.read()
#        x.calc()
#        dump16.append(x)
#
#
#path = '//rpclustersrv1/cbjorkma/Dump studies/ExtraInnerIron'
#os.chdir(path)
#filenames = sorted(os.listdir(path))
#try:
#    print iron
#except:
#    print 'Loading USRBINs...'
#    iron = []
#    for i in range(len(filenames)):
#        x = USRBIN(filenames[i], path, normfactor)
#        x.read()
#        x.calc()
#        iron.append(x)
#
#
#path = '//rpclustersrv1/cbjorkma/Dump studies/Tungsten'
#os.chdir(path)
#filenames = sorted(os.listdir(path))
#try:
#    print tungsten
#except:
#    print 'Loading USRBINs...'
#    tungsten = []
#    for i in range(len(filenames)):
#        x = USRBIN(filenames[i], path, normfactor)
#        x.read()
#        x.calc()
#        tungsten.append(x)
#
#
#path = '//rpclustersrv1/cbjorkma/Dump studies/Impact'
#os.chdir(path)
#filenames = sorted(os.listdir(path))
#try:
#    print impact
#except:
#    print 'Loading USRBINs...'
#    impact = []
#    for i in range(len(filenames)):
#        x = USRBIN(filenames[i], path, normfactor)
#        x.read()
#        x.calc()
#        impact.append(x)


path = '//rpclustergw/cbjorkma/Dump studies/Dump19/Ref'
os.chdir(path)
filenames = sorted(os.listdir(path))

print 'Loading USRBINs...'
ref = []
for i in range(len(filenames)):
    x = USRBIN(filenames[i], path, normfactor)
    x.read()
    x.calc()
    ref.append(x)


path = '//rpclustergw/cbjorkma/Dump studies/Dump19/MaskMod'
os.chdir(path)
filenames = sorted(os.listdir(path))

print 'Loading USRBINs...'
mod = []
for i in range(len(filenames)):
    x = USRBIN(filenames[i], path, normfactor)
    x.read()
    x.calc()
    mod.append(x)





xes = ref[0].xcoodinates

cooldowns = ['1h','1d','1 week']


fig = plt.figure()

for i in range(3):
    ax = plt.subplot(3,1,i+1)
    
    cube1 = ref[i]
    cube2 = mod[i]
    
    plt.plot(xes, cube2.depthdeposition/cube1.depthdeposition, label = 'Smaller mask/Reference')
    
    #plt.plot(xes, cube1.depthdeposition, label = 'Reference')
    #plt.plot(xes, cube2.depthdeposition, label = 'Smaller mask')
 #   plt.axhline(y=1, color='k', linestyle='-')
    
    plt.title(cooldowns.pop(0), fontsize = 12)
    plt.legend(loc = 1)
    if i == 2:
        plt.xlabel('z [cm]')
    plt.axhline(y=1, color='k', linestyle='-')
    #plt.yscale("log", nonposy='clip')
    plt.ylabel('Fraction dose rate', fontsize = 12)
    #plt.yscale("log", nonposy='clip')
    #plt.ylim(0,1.2)
   # ax2 = ax.twinx()
#    plotSepta(ax2)
#    ax2.get_yaxis().set_visible(False)
#    plt.ylim([0,30])
#    plt.legend(loc = 2)
#    plt.xlim(-570,2800)
    ax2 = ax.twinx()
    
    r1 = patches.Rectangle((-860/2,0), 860,5, color = 'Brown', alpha = 0.3, label = 'Dump shielding')
    
    ax2.add_patch(r1)
    ax2.get_yaxis().set_visible(False)
    plt.legend(loc = 2)

plt.suptitle('Integrated residual dose rate', fontsize = 16)
#plt.suptitle('Residual dose rate at walking path', fontsize = 16)
plt.show()


#
#
#
#xes = normal[0].xcoodinates
#
#cooldowns = ['1h','1d','1 week','1month']
#
#
#fig = plt.figure()
#
#for i in range(3):
#    ax = plt.subplot(4,1,i+1)
#    
#    cube1 = normal[i]
#    cube2 = modi[i]
#    
#    plt.plot(xes, cube1.depthdeposition/cube2.depthdeposition, label = '2 masks/1 mask')
#    plt.axhline(y=1, color='k', linestyle='-')
#    #plt.plot(xes, cube2.depthdeposition, label = '1 mask')
# #   plt.axhline(y=1, color='k', linestyle='-')
#    
#    plt.title(cooldowns.pop(0), fontsize = 12)
#    plt.legend(loc = 1)
#    if i == 3:
#        plt.xlabel('z [cm]')
#    #plt.yscale("log", nonposy='clip')
#   # plt.ylabel('Fraction dose rate', fontsize = 12)
#    #plt.yscale("log", nonposy='clip')
#    #plt.ylim(0,1.2)
#   # ax2 = ax.twinx()
##    plotSepta(ax2)
##    ax2.get_yaxis().set_visible(False)
##    plt.ylim([0,30])
##    plt.legend(loc = 2)
##    plt.xlim(-570,2800)
#    ax2 = ax.twinx()
#    
#    r1 = patches.Rectangle((-925,0), 860,5, color = 'Brown', alpha = 0.3)
#    
#    ax2.add_patch(r1)
#    ax2.get_yaxis().set_visible(False)
#
##plt.suptitle('Improvement for Graphite wires for ZS 1 and 2. Sampling 1 meter from beam axis', fontsize = 16)
#plt.show()
#
#i = 0
#
#cube1 = normal[i]
#cube2 = modi[i]
#
#
#sum1 = 0
#sum2 = 0
#for j in range(65,len(cube1.depthdeposition)):
#    sum1 = sum1 + cube1.depthdeposition[j]
#    sum2 = sum2 + cube2.depthdeposition[j]
#
#print 'Normal/modi = ' + str(sum1/sum2)
##print 'Modi = ' + str(sum2)
#
#
#
#start = 0
#maxVal = 0
#
#def calcThis(cube):
#    vector = np.zeros([cube.shape[2]])
#    for z in range( cube.shape[2]):
#        tot = 0
#        numberBins = 0
#        for x in range( cube.shape[0]):
#            for y in range( cube.shape[1]):
#    #            if math.pow(xbin*(x - i),2) + math.pow(ybin*(y - j),2) < math.pow(outerRadi,2) and math.pow(xbin*(x - i),2) + math.pow(ybin*(y - j),2) > math.pow(innerRadi,2):
#                #if abs(xbin*(x - i)) < 20 and y < j and ybin*abs(y - j) < 100 and ybin*abs(y - j) > 70:
#                if x  > 8 and x < 12 and y > 55 and y < 60:
#                    tot = tot + cube[x,y,z]
#                    numberBins = numberBins + 1
##        print tot
##        print numberBins
#        val = tot/numberBins
#        vector[z] = val
##        if val > maxVal and z >= start:
##            maxVal = val
#    return vector
#
#
#def calcWalkingPath(dump16, plot = 0):
#    zes = dump16[0].xcoodinates
#    xes = dump16[0].realxcoodinates
#    
#    vector = np.ones(len(zes))*(-100)
#    
#    indecies = (zes > -10000).astype(int) - (zes > 520).astype(int) - (zes < -500).astype(int)
#    
#    vector = vector - np.ones(len(zes))*indecies*200
#    
#    
#    
#    indecies = (zes > -10000).astype(int) - (zes > -520).astype(int) - (zes < -600).astype(int)
#    #indecies[30] = 1/3
#    #indecies[31] = 1/2
#    #indecies[32] = 1*2/3
#    
#    vector[30] = vector[30] - 200/3
#    vector[31] = vector[31] - 200/2
#    vector[32] = vector[32] - 200*2/3
#    vector[33] = vector[33] - 200*5/6
#    
#    
#    
#    indecies = (zes > -10000).astype(int) - (zes < 520).astype(int) - (zes > 603).astype(int)
#    
#    vector[71] = vector[71] - 200/3
#    vector[70] = vector[70] - 200/2
#    vector[69] = vector[69] - 200*2/3
#    vector[68] = vector[68] - 200*5/6
#    
#    #vector = vector - np.ones(len(zes))*indecies*200
#    
#    
#    
#    
#    zmin,zmax = -1500, 1500
#    xmin, xmax = -400, 400
#    
#    if plot:
#        fig = plt.figure()
#        
#        ax = plt.subplot(111)
#        
#        plt.axhline(y=-100, color='k', linestyle='-', label = 'Line1')
#        plt.axhline(y=-300, color='k', linestyle='-', label = 'Line2')
#        
#        plt.plot(zes,vector, label = 'Walking path')
#        
#        
#        plt.xlim(zmin,zmax)
#        plt.ylim(xmin,xmax)
#        
#        
#        #ax2 = ax.twinx()
#        
#        r1 = patches.Rectangle((-430,-230), 860,460, color = 'Brown', alpha = 0.3, label = 'Beam Dump')
#        #
#        ax.add_patch(r1)
#        plt.legend()
#        plt.ylabel('cm from beam axis')
#        plt.xlabel('cm from TIDVG5 center')
#        #ax2.get_yaxis().set_visible(False)
#        #plt.legend(loc = 2)
#        
#        #plt.xlim(zmin,zmax)
#        #plt.ylim(xmin,xmax)
#    
#        plt.show()
#    
#    path = vector
#    return path
#
#
#walkingpath = calcWalkingPath(dump16,1)
#
#
#
#
#
#
#def calcThis2(cube,path):
#    #cube = dump16[0].cube
#    vector = np.zeros(len(path))
##    xbinsize = cube1.info['xwidth']
#    #print range( cube.shape[2])
#    for z in range(0, len(path)):
#        #print int(path[z]/xbinsize)
##        x = int(path[z]/xbinsize)
##        y = int(cube.cube.shape[1]/2)
#        tot = 0
#        numberBins = 0     
#        for i in range(-1,2):
#            for j in range(-1,2):            
#                    tot = tot + cube1.cube[x +i,y + j,z]
#                    numberBins = numberBins + 1       
#        
#        vector[z] = tot/numberBins
#        
#    print len(vector)
#        
##        tot = 0
##        numberBins = 0
##        for x in range( cube.shape[0]):
##            for y in range( cube.shape[1]):
##    #            if math.pow(xbin*(x - i),2) + math.pow(ybin*(y - j),2) < math.pow(outerRadi,2) and math.pow(xbin*(x - i),2) + math.pow(ybin*(y - j),2) > math.pow(innerRadi,2):
##                #if abs(xbin*(x - i)) < 20 and y < j and ybin*abs(y - j) < 100 and ybin*abs(y - j) > 70:
##                if x  > 8 and x < 12 and y > 55 and y < 60:
##                    tot = tot + cube[x,y,z]
##                    numberBins = numberBins + 1
##        print tot
###        print numberBins
##        val = tot/numberBins
##        vector[z] = val
##        if val > maxVal and z >= start:
##            maxVal = val
#    return vector
#

#print calcThis2(dump16,walkingpath)



#plt.xticks


#def calcThis2(cube):
#    vector = np.zeros([cube.shape[2]])


#
#xes = dump16[0].xcoodinates
#
#cooldowns = ['1h','1d','1 week']
#
#
#fig = plt.figure()
#
#for i in range(4):
#    ax = plt.subplot(4,1,i+1)
#    
#    cube1 = normal[i]
#    cube2 = modi[i]
#    
#    plt.plot(xes, calcThis2(cube1,walkingpath), label = '2 masks')
#    plt.plot(xes, calcThis2(cube2,walkingpath), label = '1 mask')
# #   plt.axhline(y=1, color='k', linestyle='-')
#    
#    plt.title(cooldowns.pop(0), fontsize = 12)
#    plt.legend(loc = 1)
#    if i == 3:
#        plt.xlabel('z [cm]')
#    plt.yscale("log", nonposy='clip')
#   # plt.ylabel('Fraction dose rate', fontsize = 12)
#    #plt.yscale("log", nonposy='clip')
#    #plt.ylim(0,1.2)
#   # ax2 = ax.twinx()
##    plotSepta(ax2)
##    ax2.get_yaxis().set_visible(False)
##    plt.ylim([0,30])
##    plt.legend(loc = 2)
##    plt.xlim(-570,2800)
#    ax2 = ax.twinx()
#    
#    r1 = patches.Rectangle((-925,0), 860,5, color = 'Brown', alpha = 0.3, label = 'Beam Dump')
#    
#    ax2.add_patch(r1)
#    ax2.get_yaxis().set_visible(False)
##
#plt.suptitle('Improvement for Graphite wires for ZS 1 and 2. Sampling 1 meter from beam axis', fontsize = 16)
#plt.show()
#






#val = calcThis(normal[0].cube)/calcThis(modi[0].cube)
#print 'Normal/Modi = ' + str(val)







#
#fig = plt.figure()
#cooldowns = ['1h','1d','1 week','1month']
#
#for i in range(4):
#    ax = plt.subplot(4,1,i+1)
#    
#    cube1 = normal[i]
#    cube2 = modi[i]
#    
#    plt.plot(xes, calcThis2(cube1.cube,walkingpath), label = '2 masks')
#    plt.plot(xes, calcThis2(cube2.cube,walkingpath), label = '1 mask')
# #   plt.axhline(y=1, color='k', linestyle='-')
#    
#    plt.title(cooldowns.pop(0), fontsize = 12)
#    plt.legend(loc = 1)
#    if i == 3:
#        plt.xlabel('z [cm]')
#    plt.yscale("log", nonposy='clip')
#   # plt.ylabel('Fraction dose rate', fontsize = 12)
#    #plt.yscale("log", nonposy='clip')
#    #plt.ylim(0,1.2)
##    plotSepta(ax2)
##    ax2.get_yaxis().set_visible(False)
##    plt.ylim([0,30])
##    plt.legend(loc = 2)
##    plt.xlim(-570,2800)
#    ax2 = ax.twinx()
#    
#    r1 = patches.Rectangle((-925,0), 860,5, color = 'Brown', alpha = 0.3)
#    
#    ax2.add_patch(r1)
#    ax2.get_yaxis().set_visible(False)
#
##plt.suptitle('Improvement for Graphite wires for ZS 1 and 2. Sampling 1 meter from beam axis', fontsize = 16)
#plt.show()
#





#
#
#
#fig = plt.figure()
#
#ax = plt.subplot(211)
#
#cube1 = normal[i]
#cube2 = modi[i]
#
#
#plt.plot(xes, cube1.depthdeposition, label = '2 masks')
#plt.plot(xes, cube2.depthdeposition, label = '1 mask')
# #   plt.axhline(y=1, color='k', linestyle='-')
#
#plt.title('Integrated dose rate along z', fontsize = 12)
#plt.legend()
#
#plt.yscale("log", nonposy='clip')
#
#plt.ylabel('Integrated dose rate [uSv/h]', fontsize = 12)
#plt.grid(linewidth =0.15)
#
##
#ax.text(0.01, 0.05, 'colored text in axes coords', color='black')
#
#
#
#
#ax2 = ax.twinx()
#
#r1 = patches.Rectangle((-925,0), 860,5, color = 'Brown', alpha = 0.3, label = 'Beam Dump')
#
#ax2.add_patch(r1)
#ax2.get_yaxis().set_visible(False)
#plt.legend(loc = 2)
##plt.legend()
#
#
#
#
#
##
##ax = plt.subplot(312)
##
##plt.plot(xes, cube1.depthdeposition/cube2.depthdeposition, label = '2 masks/1 mask')
##plt.axhline(y=1, color='k', linestyle='-')
##plt.ylabel('Ratio')
##plt.grid(linewidth =0.15)
##plt.title('Ratio integrated dose rate along z')
##plt.legend()
##
##ax2 = ax.twinx()
##
##r1 = patches.Rectangle((-925,0), 860,5, color = 'Brown', alpha = 0.3)
##
##ax2.add_patch(r1)
##ax2.get_yaxis().set_visible(False)
##plt.legend()
##
##
##
#
#
#
#
#
#
#
#ax = plt.subplot(212)
#
#plt.plot(xes, calcThis2(cube1.cube,walkingpath), label = '2 masks')
#plt.plot(xes, calcThis2(cube2.cube,walkingpath), label = '1 mask')
#
#plt.title('Sampling 2.5 meters from beam axis', fontsize = 12)
#plt.legend(loc = 1)
#if i == 3:
#    plt.xlabel('z [cm]')
#plt.yscale("log", nonposy='clip')
#plt.xlabel('z [cm]', fontsize = 16)
#plt.ylabel('uSv/h', fontsize = 16)
#plt.grid(linewidth =0.15)
#
#ax2 = ax.twinx()
#
#r1 = patches.Rectangle((-925,0), 860,5, color = 'Brown', alpha = 0.3, label = 'Beam Dump')
##
#ax2.add_patch(r1)
#ax2.get_yaxis().set_visible(False)
#plt.legend(loc = 2)
#
##plt.legend()
#
#
#plt.suptitle('Motivation for first downstream mask', fontsize = 22)
#
#plt.show()
#
#
#
#
#
#
#for i in range(4):
#    cubeN = normal[i].cube
#    cubeM = modi[i].cube
#    
#    val = sum(calcThis(cubeN))/sum(calcThis(cubeM))
#    print 'Normal/modi = ' + str(val)
#
#
#for i in range(4):
##    cubeN = normal[i].cube
##    cubeM = modi[i].cube
#    
#    val = sum(normal[i].depthdeposition)/sum(modi[i].depthdeposition)
#    print 'Normal/modi = ' + str(val)
#
#
#

#
#color = 'viridis'
#
#import numpy as np
#
#start = 63
#
#from matplotlib.colors import LogNorm
#
#fig = plt.figure()
#
#plt.subplot(221)
#
#cube1 = normal[0]
#cube2 = modi[0]
##cube = data[1]
#
#vmax = 10**4
#vmin = 10**-1
#
#image = cube1.horizontal[0:,start:]
#plt.pcolor(image, norm=LogNorm(vmin=vmin, vmax=vmax), cmap= color)
#cbar = plt.colorbar()
#cbar.set_label('uSv/h')
#plt.xlabel('z [~cm]')
#plt.ylabel('x [bins]')
#
#plt.title('New Fluka verison')
#
#plt.subplot(222)
##cube = data[3]
#image = cube2.horizontal[0:,start:]
#plt.pcolor(image, norm=LogNorm(vmin=vmin, vmax=vmax), cmap=color)
#cbar = plt.colorbar()
#cbar.set_label('uSv/h')
#plt.title('Old Fluka verison')
#
#plt.xlabel('z [~cm]')
#plt.ylabel('x [bins]')
#
#
#
#plt.subplot(223)
#
#
#image = cube2.horizontal[0:,start:] - cube1.horizontal[0:,start:]
#
#vmax = np.amax(image)
#vmin = np.amin(image)
#
#
#plt.pcolor(image, cmap=color,vmin=vmin, vmax=vmax)
#cbar = plt.colorbar()
#cbar.set_label('Old - New [uSv/h]')
#plt.title('Old Fluka - New Fluka')
#
#plt.xlabel('z [~cm]')
#plt.ylabel('x [bins]')
#
#
#
#
#plt.suptitle('Horizontal sampling at beam height. Dose rate comparison. 1 h cool down', fontsize = 20)
#
#plt.show()
#
#
#
##----------------------------------------------------------------------------
#
#
#fig = plt.figure()
#
#plt.subplot(221)
#
#cube1 = normal[2]
#cube2 = modi[2]
##cube = data[1]
#
#vmax = 3*10**3
#vmin = 10**-1
#
#image = cube1.horizontal[0:,start:]
#plt.pcolor(image, norm=LogNorm(vmin=vmin, vmax=vmax), cmap=color)
#cbar = plt.colorbar()
#cbar.set_label('uSv/h')
#plt.xlabel('z [~cm]')
#plt.ylabel('x [bins]')
#
#plt.title('New Fluka verison')
#
#plt.subplot(222)
##cube = data[3]
#image = cube2.horizontal[0:,start:]
#plt.pcolor(image, norm=LogNorm(vmin=vmin, vmax=vmax), cmap=color)
#cbar = plt.colorbar()
#cbar.set_label('uSv/h')
#plt.title('Old Fluka verison')
#
#plt.xlabel('z [~cm]')
#plt.ylabel('x [bins]')
#
#
#
#plt.subplot(223)
#
#image = cube2.horizontal[0:,start:] - cube1.horizontal[0:,start:]
#plt.pcolor(image, cmap=color)
#cbar = plt.colorbar()
#cbar.set_label('Old - New [uSv/h]')
#plt.title('Old Fluka - New Fluka')
#
#plt.xlabel('z [~cm]')
#plt.ylabel('x [bins]')
#
#
#
#
#plt.suptitle('Horizontal sampling at beam height. Dose rate comparison. 1 week cool down', fontsize = 20)
#
#plt.show()
#
#



#
#
#xes = normal[0].xcoodinates
#
#cooldowns = ['1h','1d','1 week','1month']
#
#
#fig = plt.figure()
#
#for i in range(3):
#    ax = plt.subplot(3,1,i+1)
#    
#    cube1 = normal[i]
#    cube2 = fill[i]
#    
#    plt.plot(xes, cube1.depthdeposition, label = 'Normal')
#    plt.plot(xes, cube2.depthdeposition, label = 'Fill')
# #   plt.axhline(y=1, color='k', linestyle='-')
#    
#    plt.title(cooldowns.pop(0), fontsize = 12)
#    plt.legend(loc = 1)
#    if i == 3:
#        plt.xlabel('z [cm]')
#    plt.yscale("log", nonposy='clip')
#   # plt.ylabel('Fraction dose rate', fontsize = 12)
#    #plt.yscale("log", nonposy='clip')
#    #plt.ylim(0,1.2)
#   # ax2 = ax.twinx()
##    plotSepta(ax2)
##    ax2.get_yaxis().set_visible(False)
##    plt.ylim([0,30])
##    plt.legend(loc = 2)
##    plt.xlim(-570,2800)
#    ax2 = ax.twinx()
#    
#    r1 = patches.Rectangle((-925,0), 860,5, color = 'Brown', alpha = 0.3)
#    
#    ax2.add_patch(r1)
#    ax2.get_yaxis().set_visible(False)
#
##plt.suptitle('Improvement for Graphite wires for ZS 1 and 2. Sampling 1 meter from beam axis', fontsize = 16)
#plt.show()
#
#
#xes = normal[0].xcoodinates
#
#cooldowns = ['1h','1d','1 week','1month']
#
#
#fig = plt.figure()
#
#for i in range(3):
#    ax = plt.subplot(3,1,i+1)
#    
#    cube1 = normal[i]
#    cube2 = Old[i]
#    cube3 = dump16[i]
#    
##    plt.plot(xes, cube1.depthdeposition, label = 'Final dump model')
##    plt.plot(xes, cube2.depthdeposition, label = 'Original dump model')
#    
##    plt.plot(xes, cube1.depthdeposition, label = 'Dump version 15')
##    plt.plot(xes, cube2.depthdeposition, label = 'Original dump model')
##    
##    plt.plot(xes, cube3.depthdeposition, label = 'Dump version 16')
#    
#    plt.plot(xes, calcThis2(cube1.cube, walkingpath), label = 'Dump version 15')
#    plt.plot(xes, calcThis2(cube2.cube, walkingpath), label = 'Original dump model')
#    
#    plt.plot(xes, calcThis2(cube3.cube, walkingpath), label = 'Dump version 16')   
#    
#    
# #   plt.axhline(y=1, color='k', linestyle='-')
#    
#    plt.title(cooldowns.pop(0), fontsize = 12)
#    plt.legend(loc = 1)
#    if i == 2:
#        plt.xlabel('z [cm]')
#    plt.yscale("log", nonposy='clip')
#    plt.ylabel('Integrated dose rate [uSv/h]', fontsize = 12)
#    plt.grid(linewidth =0.15)
#    #plt.yscale("log", nonposy='clip')
#    #plt.ylim(0,1.2)
#   # ax2 = ax.twinx()
##    plotSepta(ax2)
##    ax2.get_yaxis().set_visible(False)
##    plt.ylim([0,30])
##    plt.legend(loc = 2)
##    plt.xlim(-570,2800)
#    ax2 = ax.twinx()
#    
#    r1 = patches.Rectangle((-925,0), 860,5, color = 'Brown', alpha = 0.3, label = 'Beam dump')
#    
#    ax2.add_patch(r1)
#    ax2.get_yaxis().set_visible(False)
#    plt.legend(loc =2)
#
##plt.suptitle('Improvement for Graphite wires for ZS 1 and 2. Sampling 1 meter from beam axis', fontsize = 16)
#plt.show()



#
#
#cooldowns = ['1h','30h','1 week']
#
#
#fig = plt.figure()
#
#for i in range(3):
#    ax = plt.subplot(3,1,i+1)
#    
#    cube1 = normal[i]
#    cube2 = modi[i]
#    
##    plt.plot(xes, cube1.side, label = 'Current setup')
##    plt.plot(xes, cube2.side, label = 'Modified setup')
#    
#    plt.plot(xes, cube2.side/cube1.side, label = 'Modified/Current setup')
#    plt.axhline(y=1, color='k', linestyle='-')
#    
#    
#    plt.title(cooldowns.pop(0), fontsize = 12)
#    plt.legend(loc = 1)
#    if i == 2:
#        plt.xlabel('cm from quad 216')
#    plt.ylabel('Fraction dose rate', fontsize = 12)
#    plt.ylim(0,1.2)
#    #plt.yscale("log", nonposy='clip')
#    ax2 = ax.twinx()
#    plotSepta(ax2)
#    ax2.get_yaxis().set_visible(False)
#    plt.ylim([0,30])
#    plt.legend(loc = 2)
#    plt.xlim(-570,2800)
#
#
#plt.suptitle('Current vs modified setup. Sampling 1 meter from beam axis', fontsize = 16)
#plt.show()
#
#
#
#
#cooldowns = ['1h','1d','1 week']
#
#for i in range(0,3):
#    
#    xes = Dump17[0].xcoodinates
#    
#    cooldown = cooldowns.pop(0)
#    
#    fig = plt.figure()
#    
#    ax = plt.subplot(211)
#    
#    #cube1 = normal[i]
#    #cube2 = fill[i]
#    #cube3 = radi[i]
#    #cube4 = extend[i]
#    #
#    #plt.plot(xes, cube1.depthdeposition, label = 'No fill')
#    #plt.plot(xes, cube2.depthdeposition, label = 'Bottom fill')
#    #plt.plot(xes, cube3.depthdeposition, label = 'Radial fill')
#    #plt.plot(xes, cube4.depthdeposition, label = 'Extended shielding')
#     #   plt.axhline(y=1, color='k', linestyle='-')
#    
#    
#    
#    #cube1 = normal[i]
#    #cube2 = dump16[i]
#    
#    cube1 = Dump17[i]
#    cube2 = radius17[i]
#    #cube3 = tungsten[i]
#    
#    plt.plot(xes, cube1.depthdeposition, label = 'Reference')
#    plt.plot(xes, cube2.depthdeposition, label = 'Reduced inner shielding')
#    
#    val = sum(cube2.depthdeposition)/sum(cube1.depthdeposition)
#    
#    print 'Reduced inner shielding/Reference for ' + cooldown + ' = ' + str(val) 
#    #plt.plot(xes, cube2.depthdeposition, label = 'Inner Tungsten')
#    
#    
#    plt.title('Integrated dose rate along z', fontsize = 12)
#    plt.legend()
#    
#    plt.yscale("log", nonposy='clip')
#    
#    plt.ylabel('Integrated dose rate [uSv/h]', fontsize = 12)
#    plt.grid(linewidth =0.15)
#    
#    #
#    #ax.text(0.01, 0.05, 'colored text in axes coords', color='black')
#    
#    
#    
#    
#    ax2 = ax.twinx()
#    
#    r1 = patches.Rectangle((-425,0), 860,5, color = 'Brown', alpha = 0.3, label = 'Beam Dump')
#    
#    ax2.add_patch(r1)
#    ax2.get_yaxis().set_visible(False)
#    plt.legend(loc = 2)
#    #plt.legend()
#    
#    
#    
#    
#    
#    
#    ax = plt.subplot(212)
#    
#    #plt.plot(xes, cube2.depthdeposition/cube1.depthdeposition, label = 'Bottom fill/No fill')
#    #plt.plot(xes, cube3.depthdeposition/cube1.depthdeposition, label = 'Radial fill/No fill')
#    #plt.plot(xes, cube4.depthdeposition/cube1.depthdeposition, label = 'Extended shielding/No fill')
#    
#    plt.plot(xes, cube2.depthdeposition/cube1.depthdeposition, label = 'Reduced inner shielding/Reference')
#    #plt.plot(xes, cube3.depthdeposition/cube1.depthdeposition, label = 'Inner Tungsten/Reference')
#    
#    
#    plt.axhline(y=1, color='k', linestyle='-')
#    plt.ylabel('Ratio')
#    plt.grid(linewidth =0.15)
#    plt.title('Ratio integrated dose rate along z')
#    plt.legend()
#    plt.xlabel('z [cm from TIDVG5 center]')
#
#    
#    ax2 = ax.twinx()
#    
#    r1 = patches.Rectangle((-425,0), 860,5, color = 'Brown', alpha = 0.3)
#    
#    ax2.add_patch(r1)
#    ax2.get_yaxis().set_visible(False)
#    plt.legend()
#    plt.suptitle('Reduced inner shielding for ' + cooldown + ' cool down')
#





    
    
    
#    ax = plt.subplot(313)
#    
#    #plt.plot(xes, calcThis(cube1.cube), label = 'No fill')
#    #plt.plot(xes, calcThis(cube2.cube), label = 'Bottom fill')
#    #plt.plot(xes, calcThis(cube3.cube), label = 'Radial fill')
#    #plt.plot(xes, calcThis(cube4.cube), label = 'Extended shielding')
#    
#    
#    plt.plot(xes, calcThis2(cube1.cube,walkingpath), label = 'Reference')
#    #plt.plot(xes, calcThis2(cube2.cube, walkingpath), label = 'Inner Iron: ' + str(sum(calcThis2(cube2.cube, walkingpath))/sum(calcThis2(cube1.cube, walkingpath))))
#    plt.plot(xes, calcThis2(cube3.cube, walkingpath), label = 'Inner Tungsten: ' + str(sum(calcThis2(cube3.cube, walkingpath))/sum(calcThis2(cube1.cube, walkingpath))))
#    
#    
#    plt.title('Sampling along walking path', fontsize = 12)
#    plt.legend(loc = 1)
#    if i == 3:
#        plt.xlabel('z [cm]')
#    plt.yscale("log", nonposy='clip')
#    plt.xlabel('z [cm from TIDVG5 center]', fontsize = 16)
#    plt.ylabel('uSv/h', fontsize = 16)
#    plt.grid(linewidth =0.15)
#    
#    ax2 = ax.twinx()
#    
#    r1 = patches.Rectangle((-425,0), 860,5, color = 'Brown', alpha = 0.3, label = 'Beam Dump')
#    #
#    ax2.add_patch(r1)
#    ax2.get_yaxis().set_visible(False)
#    plt.legend(loc = 2)
    
    #plt.legend()
    
    
    #plt.suptitle('Motivation for first downstream mask', fontsize = 22)
    
#    plt.show()









#
#
#
#
#for i in range(3):
#    cubeN = normal[i].cube
#    cubeF = fill[i].cube
#    cubeR = radi[i].cube
#    
#    val = sum(calcThis(cubeF))/sum(calcThis(cubeN))
#    print 'Normal/Bottom fill = ' + str(val)
#    val = sum(calcThis(cubeR))/sum(calcThis(cubeN))
#    print 'Normal/radial fill = ' + str(val)
#
#for i in range(3):
##    cubeN = normal[i].cube
##    cubeM = modi[i].cube
#    
#    val = sum(fill[i].depthdeposition)/sum(normal[i].depthdeposition)
#    print 'Bottomfill/No fill = ' + str(val)
#
#    val = sum(radi[i].depthdeposition)/sum(normal[i].depthdeposition)
#    print 'Radial fill/No fill = ' + str(val)
#
#



