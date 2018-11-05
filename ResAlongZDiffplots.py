# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 15:22:03 2017

@author: cbjorkma
"""

#ResAlongZDiffplots


from Flukato3dMatrix import Flukato3dMatrix 
import matplotlib.pyplot as plt
#filename = 'Dump5Res_21.bnn.lis'
#path = '//cern.ch/dfs/Users/c/cbjorkma/Documents/Dump TIDGV5/WithMask'

import os

plt.clf()

import numpy as np

path = '//rpclustersrv1/cbjorkma/Dump studies'
os.chdir(path)

###------Load Data-------------------------------------
#
#filename = 'Dump10Res_21.bnn.lis'
#cube = 0.0036* Flukato3dMatrix(filename, path,0)
#np.save(filename, cube)
#
#filename = 'Dump10Res_22.bnn.lis'
#cube = 0.0036* Flukato3dMatrix(filename, path,0)
#np.save(filename, cube)
#
#filename = 'Dump10Res_23.bnn.lis'
#cube = 0.0036* Flukato3dMatrix(filename, path,0)
#np.save(filename, cube)
#
#
#filename = 'Dump10ResMarbleDownstream3_21.bnn.lis'
#cube = 0.0036* Flukato3dMatrix(filename, path,0)
#np.save(filename, cube)
#
#filename = 'Dump10ResMarbleDownstream3_22.bnn.lis'
#cube = 0.0036* Flukato3dMatrix(filename, path,0)
#np.save(filename, cube)
#
#filename = 'Dump10ResMarbleDownstream3_23.bnn.lis'
#cube = 0.0036* Flukato3dMatrix(filename, path,0)
#np.save(filename, cube)
##

#filename = 'Dump5Res_21.bnn.lis'
#cube = 0.0036* Flukato3dMatrix(filename, path,0)
#np.save(filename, cube)
#
#filename = 'Dump5Res_22.bnn.lis'
#cube = 0.0036* Flukato3dMatrix(filename, path,0)
#np.save(filename, cube)
#
#filename = 'Dump5Res_23.bnn.lis'
#cube = 0.0036* Flukato3dMatrix(filename, path,0)
#np.save(filename, cube)
#
#filename = 'Dump10ResLongerMask_21.bnn.lis'
#cube = 0.0036* Flukato3dMatrix(filename, path,0)
#np.save(filename, cube)
#
#filename = 'Dump10ResLongerMask_22.bnn.lis'
#cube = 0.0036* Flukato3dMatrix(filename, path,0)
#np.save(filename, cube)
#
#filename = 'Dump10ResLongerMask_23.bnn.lis'
#cube = 0.0036* Flukato3dMatrix(filename, path,0)
#np.save(filename, cube)
#

##-----------------------------------------------
#
#




#------------Extracting meta info
#path = '//cern.ch/dfs/Users/c/cbjorkma/Documents/Dump TIDGV5/WithMask'
#os.chdir(path)
cube = np.load('Dump9ResIronCamStructureConcrete1_21.bnn.lis.npy')
#
#
#Determines center voxels
i = int(cube.shape[0]/2)
j = int(cube.shape[1]*0.58)
#-------------------------------------------



import matplotlib.pyplot as plt
import math
import matplotlib.patches as patches
from matplotlib.colors import LogNorm
plt.close()
plt.close()
plt.close()
fig = plt.figure()
#
#
#
#ax = fig.add_subplot(111)
#-------With mask-------1h cool down------------
#path = '//cern.ch/dfs/Users/c/cbjorkma/Documents/Dump TIDGV5/WithMask'
#os.chdir(path)
#filename = 'Dump9ResIronCamStructureConcrete1_21.bnn.lis'
#cube = np.load(filename +'.npy')
#
#vmax = cube.max()
#vmin = math.pow(10,-5) #np.min(cube[np.nonzero(cube)])
#
#
#image = cube[0:,j,0:]
#plt.pcolor(image,norm=LogNorm(vmin=vmin, vmax=vmax), cmap='jet')
#cbar = plt.colorbar()
#cbar.set_label('Intensity')


#
#r2 = patches.Rectangle((0.688*cube.shape[2] -hml,j -hmw), 2* hml,2* hmw,fc=(0,1,1,1), label = 'Mask')
#ax.add_patch(r2)
#
#r3 = patches.Rectangle((0.777*cube.shape[2] -hml,j - hmw), 2* hml,2* hmw,fc=(0,1,1,1))
#ax.add_patch(r3)
#
#
#plt.show()

xbin = 9 #cm
ybin = 5.3 #cm
zbin = 15 #cm
start = cube.shape[2]*0.645
start = cube.shape[2]*0.6448
maxVal = 0
hml = 0.01666*cube.shape[2] # half mask length
hmw = 0.059*cube.shape[0] # half mask width

innerRadi = math.ceil(math.sqrt(math.pow(53.1,2) + math.pow(55.45,2)))

outerRadi = innerRadi + 10

def calcThis(cube,maxVal):
    for z in range( cube.shape[2]):
        tot = 0
        numberBins = 0
        for x in range( cube.shape[0]):
            for y in range( cube.shape[1]):
                #if math.pow(xbin*(x - i),2) + math.pow(ybin*(y - j),2) < math.pow(outerRadi,2) and math.pow(xbin*(x - i),2) + math.pow(ybin*(y - j),2) > math.pow(innerRadi,2):
                if abs(xbin*(x - i)) < 20 and y < j and ybin*abs(y - j) < 100 and ybin*abs(y - j) > 70:
                #if abs(ybin*(y - i)) < 20 and x < i and xbin*abs(x - i) < 100 and xbin*abs(x - i) > 70:
                    tot = tot + cube[x,y,z]
                    numberBins = numberBins + 1
        val = tot/numberBins
        vector[z] = val
        if val > maxVal and z >= start:
            maxVal = val
    return vector, maxVal





def curiosa(ax):
#    r1 = patches.Rectangle((0.827*cube.shape[2],0), 0.894*cube.shape[2] -0.827*cube.shape[2],8000,fc=(0,0,1,0.1), label = 'QD519')
#    ax.add_patch(r1)
    
#    hmw = 0.01666*cube.shape[2] # half mask width
#    r2 = patches.Rectangle((0.688*cube.shape[2] -hmw,0), 2* hmw,8000,fc=(0,0.2,0.8,0.3), label = 'Mask')
#    ax.add_patch(r2)
    
    r3 = patches.Rectangle((0.777*cube.shape[2] -hmw,0), 2* hmw,8000,fc=(0,0.2,0.8,0.3))
    ax.add_patch(r3)
    

    #plt.xlim( start, cube.shape[2] )

    plt.ylim(0, maxVal*1.1)
    plt.ylabel('uSv/h', fontsize = 15)
    plt.grid()
    #from 0 -> 200 to -2000 to 1000 in 200 steps
    initialrange = np.arange(0,cube.shape[2],10)
    newrange = initialrange*30/2 -2000 + 65
    plt.xticks(initialrange, newrange)
#    ax.axvline(x=143.7,linestyle = '--', color = 'black', label = 'Marble floor ends' )
#    ax.axvline(x=float(1950)/3000 * 200,linestyle = ':', color = 'black', label = 'Platform starts' )
    plt.legend(loc = 1, prop={'size': 10})


def drawings(ax2):
    
    transp = 0.45
    

    r2 = patches.Rectangle((0.586*cube.shape[2],14.25), 12,8000,fc='maroon', alpha = 0.5*transp)
    ax2.add_patch(r2)

    r3 = patches.Rectangle((0.586*cube.shape[2],-14.25), 12,-120 +14.25,fc='maroon', alpha = 0.5*transp)
    ax2.add_patch(r3)
    
    
    hmw = 0.01666*cube.shape[2] # half mask width
    r4 = patches.Rectangle((0.688*cube.shape[2] -hmw,-50), 2* hmw,100,fc='maroon', alpha = 0.5*transp, label = 'Mask')
    ax2.add_patch(r4)    
    
    r5 = patches.Rectangle((0.688*cube.shape[2] -hmw*0.6,-30), 2* hmw*0.6,60,fc='slategrey', alpha = 0.5*transp, label = 'Mask')
    ax2.add_patch(r5)        

    r7 = patches.Rectangle((0.60*cube.shape[2],-150), 100,17,fc='lightgrey', alpha = 0.8*transp)
    ax2.add_patch(r7) 

    r6 = patches.Rectangle((0.65*cube.shape[2],-150), 100,38,fc='lightgrey', alpha = 0.8*transp)
    ax2.add_patch(r6) 

#    r6 = patches.Rectangle((0.65*cube.shape[2],-141), 143.7 -float(1950)/3000 * 200,30,fc='maroon', alpha = 0.4*transp)
#    ax2.add_patch(r6) 

print 'Plotting...'


end = 146

#fig = plt.figure()


plt.suptitle('Residual dose rates after downstream exit of dump shielding, below beamline', fontsize = 22)

# 1h cool down
#-------------------------------------------------------------------------------------------
ax = fig.add_subplot(311)



#-------Concrete1-------1h cool down------------

filename = 'Dump10Res_21.bnn.lis.npy'
cube = np.load(filename)
vector = np.zeros([cube.shape[2]])
vector, maxVal = calcThis(cube,maxVal)


plt.plot(range(0,cube.shape[2]),vector, color='r', label = 'Reference')
#----------------------------------------------------

#-------Concrete2-------1h cool down------------

filename = 'Dump10ResMarbleDownstream_21.bnn.lis.npy'
cube = np.load(filename)
vector = np.zeros([cube.shape[2]])
vector, maxVal = calcThis(cube,maxVal)        
        
        
        
plt.plot(range(0,cube.shape[2]),vector, color='k',linestyle = ':', label = 'Marble platform 10 cm',linewidth=3)
#----------------------------------------------------

#-------Concrete2-------1h cool down------------

filename = 'Dump10ResMarbleDownstream2_21.bnn.lis.npy'
cube = np.load(filename)
vector = np.zeros([cube.shape[2]])
vector, maxVal = calcThis(cube,maxVal)        
        
        
        
plt.plot(range(0,cube.shape[2]),vector, color='k',linestyle = '--', label = 'Marble platform 30 cm',linewidth=3)
#----------------------------------------------------


##--------------1h cool down------------
#
#filename = 'Dump10ResLongerMask_21.bnn.lis.npy'
#cube = np.load(filename)
#vector = np.zeros([cube.shape[2]])
#vector, maxVal = calcThis(cube,maxVal)        
#        
#        
#        
#plt.plot(range(0,cube.shape[2]),vector, color='y',linestyle = ':', label = 'Elongated Mask 20 cm extra',linewidth=3)
##----------------------------------------------------
#
##-------Concrete2-------1h cool down------------
#
#filename = 'Dump10ResMarbleDownstream3_21.bnn.lis.npy'
#cube = np.load(filename)
#vector = np.zeros([cube.shape[2]])
#vector, maxVal = calcThis(cube,maxVal)        
#        
#        
#        
#plt.plot(range(0,cube.shape[2]),vector, color='c',linestyle = '--', label = 'Marble platform 30 cm + Elongated mask',linewidth=3)


##os.chdir('//cern.ch/dfs/Users/c/cbjorkma/Documents/Dump TIDGV5/WithMask')
#filename = 'Dump5Res_21.bnn.lis'
#cube = np.load(filename +'.npy')
#vector = np.zeros([cube.shape[2]])
#vector, maxVal = calcThis(cube,maxVal)   
#plt.plot(range(0,cube.shape[2]),vector, color='b',linestyle = '-', label = 'Old source',linewidth=3)
#

curiosa(ax)
#end = cube.shape[2]*0.8

#print start, end
plt.xlim( start, end )
plt.title('1h cool down')



ax2 = ax.twinx()

ax2.set_ylim(-150,100)


drawings(ax2)

plt.ylabel('y [cm]')


#---------------


plt.show()










os.chdir(path)
maxVal = 0

# 1 day cool down
#-------------------------------------------------------------------------------------------
ax = fig.add_subplot(312)
#-------Concrete1-------1 day cool down------------

filename = 'Dump10Res_22.bnn.lis.npy'
cube = np.load(filename)
vector = np.zeros([cube.shape[2]])
vector, maxVal = calcThis(cube,maxVal)


plt.plot(range(0,cube.shape[2]),vector, color='r', label = 'Reference')
#----------------------------------------------------

#-------Concrete2-------1 day cool down------------

filename = 'Dump10ResMarbleDownstream_22.bnn.lis.npy'
cube = np.load(filename)
vector = np.zeros([cube.shape[2]])
vector, maxVal = calcThis(cube,maxVal)        
        
        
        
plt.plot(range(0,cube.shape[2]),vector, color='k',linestyle = ':', label = 'Marble 10 cm',linewidth=3)
#----------------------------------------------------

#-------Concrete2-------1 day cool down------------

filename = 'Dump10ResMarbleDownstream2_22.bnn.lis.npy'
cube = np.load(filename)
vector = np.zeros([cube.shape[2]])
vector, maxVal = calcThis(cube,maxVal)        
        
        
        
plt.plot(range(0,cube.shape[2]),vector, color='k',linestyle = '--', label = 'Marble 30 cm',linewidth=3)

##--------------1 day cool down------------
#
#filename = 'Dump10ResLongerMask_22.bnn.lis.npy'
#cube = np.load(filename)
#vector = np.zeros([cube.shape[2]])
#vector, maxVal = calcThis(cube,maxVal)        
#        
#        
#        
#plt.plot(range(0,cube.shape[2]),vector, color='y',linestyle = ':', label = 'Mask 20 cm extra',linewidth=3)
##----------------------------------------------------
#filename = 'Dump10ResMarbleDownstream3_22.bnn.lis.npy'
#cube = np.load(filename)
#vector = np.zeros([cube.shape[2]])
#vector, maxVal = calcThis(cube,maxVal)        
#        
#        
#        
#plt.plot(range(0,cube.shape[2]),vector, color='c',linestyle = '--', label = 'Marble platform 30 cm + Elongated mask',linewidth=3)

##path = 
##os.chdir('//cern.ch/dfs/Users/c/cbjorkma/Documents/Dump TIDGV5/WithMask')
#filename = 'Dump5Res_22.bnn.lis'
#cube = np.load(filename +'.npy')
#vector = np.zeros([cube.shape[2]])
#vector, maxVal = calcThis(cube,maxVal)   
#plt.plot(range(0,cube.shape[2]),vector, color='b',linestyle = '-', label = 'Old Source',linewidth=3)
#

curiosa(ax)
plt.xlim( start, end )
plt.title('1 day cool down')

ax2 = ax.twinx()

ax2.set_ylim(-150,100)


drawings(ax2)

plt.ylabel('y [cm]')



#---------------

#
#
#
#
#
#
#

os.chdir(path)
maxVal = 0

# 1 week cool down
#-------------------------------------------------------------------------------------------
ax = fig.add_subplot(313)
#-------Concrete1-------1 day cool down------------

filename = 'Dump10Res_23.bnn.lis.npy'
cube = np.load(filename)
vector = np.zeros([cube.shape[2]])
vector, maxVal = calcThis(cube,maxVal)


plt.plot(range(0,cube.shape[2]),vector, color='r', label = 'Reference')
#----------------------------------------------------

#-------Concrete2-------1 day cool down------------

filename = 'Dump10ResMarbleDownstream_23.bnn.lis.npy'
cube = np.load(filename)
vector = np.zeros([cube.shape[2]])
vector, maxVal = calcThis(cube,maxVal)        
        
        
        
plt.plot(range(0,cube.shape[2]),vector, color='k',linestyle = ':', label = 'Marble 10 cm',linewidth=3)
#----------------------------------------------------

#-------Concrete2-------1 day cool down------------

filename = 'Dump10ResMarbleDownstream2_23.bnn.lis.npy'
cube = np.load(filename)
vector = np.zeros([cube.shape[2]])
vector, maxVal = calcThis(cube,maxVal)        
        
        
        
plt.plot(range(0,cube.shape[2]),vector, color='k',linestyle = '--', label = 'Marble 30 cm',linewidth=3)
#----------------------------------------------------

#
##-------Concrete2-------1 day cool down------------
#
#filename = 'Dump10ResLongerMask_23.bnn.lis.npy'
#cube = np.load(filename)
#vector = np.zeros([cube.shape[2]])
#vector, maxVal = calcThis(cube,maxVal)        
#        
#        
#        
#plt.plot(range(0,cube.shape[2]),vector, color='y',linestyle = ':', label = 'Mask 20 cm extra',linewidth=3)
##----------------------------------------------------
#
#
#filename = 'Dump10ResMarbleDownstream3_23.bnn.lis.npy'
#cube = np.load(filename)
#vector = np.zeros([cube.shape[2]])
#vector, maxVal = calcThis(cube,maxVal)        
#        
#        
#        
#plt.plot(range(0,cube.shape[2]),vector, color='c',linestyle = '--', label = 'Marble platform 30 cm + Elongated mask',linewidth=3)
###path = 
##os.chdir('//cern.ch/dfs/Users/c/cbjorkma/Documents/Dump TIDGV5/WithMask')
#filename = 'Dump5Res_23.bnn.lis'
#cube = np.load(filename +'.npy')
#vector = np.zeros([cube.shape[2]])
#vector, maxVal = calcThis(cube,maxVal)   
#plt.plot(range(0,cube.shape[2]),vector, color='b',linestyle = '-', label = 'Old Source',linewidth=3)
#

curiosa(ax)
plt.title('1 week cool down')
plt.xlim( start, end )
plt.xlabel('z [cm]', fontsize = 15)

ax2 = ax.twinx()

ax2.set_ylim(-150,100)


drawings(ax2)

plt.ylabel('y [cm]')



#---------------

print 'Done'











fig = plt.figure()

ax = fig.add_subplot(111)

os.chdir(path)
maxVal = 0


filename = 'Dump10Res_21.bnn.lis.npy'
cube = np.load(filename)
vector = np.zeros([cube.shape[2]])
vector, maxVal = calcThis(cube,maxVal)


plt.plot(range(0,cube.shape[2]),vector, color='r', label = '1 hour', linewidth = 3)



filename = 'Dump10Res_22.bnn.lis.npy'
cube = np.load(filename)
vector = np.zeros([cube.shape[2]])
vector, maxVal = calcThis(cube,maxVal)


plt.plot(range(0,cube.shape[2]),vector, color='b', label = '1 day', linewidth = 3)
#





filename = 'Dump10Res_23.bnn.lis.npy'
cube = np.load(filename)
vector = np.zeros([cube.shape[2]])
vector, maxVal = calcThis(cube,maxVal)


plt.plot(range(0,cube.shape[2]),vector, color='g', label = '1 week', linewidth = 3)





curiosa(ax)
plt.title('Dose rates at downstream exit, below beamline', fontsize = 22)
plt.xlim( start, end )
plt.xlabel('z [cm from downstream exit]', fontsize = 15)

plt.yscale("log", nonposy='clip')
plt.ylim(10,10000)
ax2 = ax.twinx()

ax2.set_ylim(-150,100)


drawings(ax2)
ax2.set_yticklabels([])

plt.show()




#
#os.chdir(path)
#maxVal = 0
#
## 1 week cool down
##-------------------------------------------------------------------------------------------
#ax = fig.add_subplot(313)
##-------Concrete1-------1 day cool down------------
#
#filename = 'Dump9ResIronCamStructureConcrete1_23.bnn.lis.npy'
#cube = np.load(filename)
#vector = np.zeros([cube.shape[2]])
#vector, maxVal = calcThis(cube,maxVal)
#
#
#plt.plot(range(0,cube.shape[2]),vector, color='r', label = 'Mask 80 cm')
##----------------------------------------------------
#
##-------Concrete2-------1 day cool down------------
#
#filename = 'Dump9ResIronCamStructureConcrete2_23.bnn.lis.npy'
#cube = np.load(filename)
#vector = np.zeros([cube.shape[2]])
#vector, maxVal = calcThis(cube,maxVal)        
#        
#        
#        
#plt.plot(range(0,cube.shape[2]),vector, color='k',linestyle = ':', label = 'Mask 80 cm + iron platform',linewidth=3)
##----------------------------------------------------
#
##path = 
#os.chdir('//cern.ch/dfs/Users/c/cbjorkma/Documents/Dump TIDGV5/WithMask')
#filename = 'Dump5Res_23.bnn.lis'
#cube = np.load(filename +'.npy')
#vector = np.zeros([cube.shape[2]])
#vector, maxVal = calcThis(cube,maxVal)   
#plt.plot(range(0,cube.shape[2]),vector, color='b',linestyle = '-', label = 'Old Source',linewidth=3)
#
#
#curiosa()
#plt.title('1 week cool down')
#
##---------------
#
#














#
#
#
#xbin = 9 #cm
#ybin = 5.3 #cm
#zbin = 15 #cm
#
#
#
#start = cube.shape[2]*0.645
#
#innerRadi = math.ceil(math.sqrt(math.pow(53.1,2) + math.pow(55.45,2)))
#
#outerRadi = innerRadi + 10
#maxVal = 0
#
#fig = plt.figure()
#
#
#
##-------------------------------------------------------------------------------------------
#ax = fig.add_subplot(311)
##-------With mask-------1h cool down------------
#path = '//cern.ch/dfs/Users/c/cbjorkma/Documents/Dump TIDGV5/WithMask'
#os.chdir(path)
#filename = 'Dump5Res_21.bnn.lis'
#cube = np.load(filename +'.npy')
#vector = np.zeros([cube.shape[2]])
#for z in range( cube.shape[2]):
#    tot = 0
#    numberBins = 0
#    for x in range( cube.shape[0]):
#        for y in range( cube.shape[1]):
##            if math.pow(xbin*(x - i),2) + math.pow(ybin*(y - j),2) < math.pow(outerRadi,2) and math.pow(xbin*(x - i),2) + math.pow(ybin*(y - j),2) > math.pow(innerRadi,2):
#            if abs(xbin*(x - i)) < 20 and y < j and ybin*abs(y - j) < 100 and ybin*abs(y - j) > 70:
#                tot = tot + cube[x,y,z]
#                numberBins = numberBins + 1
#    val = tot/numberBins
#    vector[z] = val
#    if val > maxVal and z >= start:
#        maxVal = val
#
#
#plt.plot(range(0,cube.shape[2]),vector, color='r', label = 'With first mask')
##----------------------------------------------------
#
##-------WithOut mask-------1h cool down------------
#path = '//cern.ch/dfs/Users/c/cbjorkma/Documents/Dump TIDGV5/WithoutMask'
#os.chdir(path)
#filename = 'Dump5ResNoMask2_21.bnn.lis'
#cube = np.load(filename +'.npy')
#vector = np.zeros([cube.shape[2]])
#for z in range( cube.shape[2]):
#    tot = 0
#    numberBins = 0
#    for x in range( cube.shape[0]):
#        for y in range( cube.shape[1]):
#            #print x,y,z            
##            if math.pow(xbin*(x - i),2) + math.pow(ybin*(y - j),2) < math.pow(outerRadi,2) and math.pow(xbin*(x - i),2) + math.pow(ybin*(y - j),2) > math.pow(innerRadi,2):
#            if abs(xbin*(x - i)) < 20 and y < j and ybin*abs(y - j) < 100 and ybin*abs(y - j) > 70:
#                tot = tot + cube[x,y,z]
#                numberBins = numberBins + 1
#    val = tot/numberBins
#    vector[z] = val
#    if val > maxVal and z >= start:
#        maxVal = val
#
#
#plt.plot(range(0,cube.shape[2]),vector, color='k',linestyle = ':', label = 'Without first mask',linewidth=3)
##----------------------------------------------------
#
#r1 = patches.Rectangle((0.827*cube.shape[2],0), 0.894*cube.shape[2] -0.827*cube.shape[2],2000,fc=(0,0,1,0.1), label = 'QD519')
#ax.add_patch(r1)
#
#
#hmw = 0.01666*cube.shape[2] # half mask width
#r2 = patches.Rectangle((0.688*cube.shape[2] -hmw,0), 2* hmw,2000,fc=(0,1,0,0.1), label = 'Mask')
#ax.add_patch(r2)
#
#r3 = patches.Rectangle((0.777*cube.shape[2] -hmw,0), 2* hmw,2000,fc=(0,1,0,0.1))
#ax.add_patch(r3)
#
#plt.legend()
#plt.xlim( start, cube.shape[2] )
#plt.ylim(0, maxVal*1.1)
#plt.ylabel('uSv/h', fontsize = 15)
#plt.title('1h cool down')
#plt.grid()
##plt.xlabel('cm', fontsize = 15)
#plt.xticks( range(int(start), int(cube.shape[2]),int((cube.shape[2] - start)/10)), range(0,1035,1035/10) )
##-------------------------------------------------------------------------------------------
#
#
#maxVal = 0
##-------------------------------------------------------------------------------------------
#ax = fig.add_subplot(312)
##-------With mask-------1d cool down------------
#path = '//cern.ch/dfs/Users/c/cbjorkma/Documents/Dump TIDGV5/WithMask'
#os.chdir(path)
#filename = 'Dump5Res_22.bnn.lis'
#cube = np.load(filename +'.npy')
#vector = np.zeros([cube.shape[2]])
#for z in range( cube.shape[2]):
#    tot = 0
#    numberBins = 0
#    for x in range( cube.shape[0]):
#        for y in range( cube.shape[1]):
##            if math.pow(xbin*(x - i),2) + math.pow(ybin*(y - j),2) < math.pow(outerRadi,2) and math.pow(xbin*(x - i),2) + math.pow(ybin*(y - j),2) > math.pow(innerRadi,2):
#            if abs(xbin*(x - i)) < 20 and y < j and ybin*abs(y - j) < 100 and ybin*abs(y - j) > 70:
#                tot = tot + cube[x,y,z]
#                numberBins = numberBins + 1
#    val = tot/numberBins
#    vector[z] = val
#    if val > maxVal and z >= start:
#        maxVal = val
#
#
#plt.plot(range(0,cube.shape[2]),vector, color='r', label = 'With first mask')
##----------------------------------------------------
#
##-------WithOut mask-------1d cool down------------
#path = '//cern.ch/dfs/Users/c/cbjorkma/Documents/Dump TIDGV5/WithoutMask'
#os.chdir(path)
#filename = 'Dump5ResNoMask2_22.bnn.lis'
#cube = np.load(filename +'.npy')
#vector = np.zeros([cube.shape[2]])
#for z in range( cube.shape[2]):
#    tot = 0
#    numberBins = 0
#    for x in range( cube.shape[0]):
#        for y in range( cube.shape[1]):
##            if math.pow(xbin*(x - i),2) + math.pow(ybin*(y - j),2) < math.pow(outerRadi,2) and math.pow(xbin*(x - i),2) + math.pow(ybin*(y - j),2) > math.pow(innerRadi,2):
#            if abs(xbin*(x - i)) < 20 and y < j and ybin*abs(y - j) < 100 and ybin*abs(y - j) > 70:
#                tot = tot + cube[x,y,z]
#                numberBins = numberBins + 1
#    val = tot/numberBins
#    vector[z] = val
#    if val > maxVal and z >= start:
#        maxVal = val
#
#
#plt.plot(range(0,cube.shape[2]),vector, color='k',linestyle = ':', label = 'Without first mask',linewidth=3)
##----------------------------------------------------
#
#r1 = patches.Rectangle((0.827*cube.shape[2],0), 0.894*cube.shape[2] -0.827*cube.shape[2],2000,fc=(0,0,1,0.1), label = 'QD519')
#ax.add_patch(r1)
#
#
#hmw = 0.01666*cube.shape[2] # half mask width
#r2 = patches.Rectangle((0.688*cube.shape[2] -hmw,0), 2* hmw,2000,fc=(0,1,0,0.1), label = 'Mask')
#ax.add_patch(r2)
#
#r3 = patches.Rectangle((0.777*cube.shape[2] -hmw,0), 2* hmw,2000,fc=(0,1,0,0.1))
#ax.add_patch(r3)
#
##plt.axvline(x=0.688*cube.shape[2],linestyle = '--' ,label='Mask positions')
##plt.axvline(x=0.777*cube.shape[2],linestyle = '--')
#
#plt.legend()
#plt.xlim( start, cube.shape[2] )
#plt.ylim(0, maxVal*1.1)
#plt.ylabel('uSv/h', fontsize = 15)
#plt.title('1 day cool down')
#plt.grid()
##plt.xlabel('cm', fontsize = 15)
#plt.xticks( range(int(start), int(cube.shape[2]),int((cube.shape[2] - start)/10)), range(0,1035,1035/10) )
##-------------------------------------------------------------------------------------------
#
#
#
#maxVal = 0
##-------------------------------------------------------------------------------------------
#ax = fig.add_subplot(313)
##-------With mask-------1d cool down------------
#path = '//cern.ch/dfs/Users/c/cbjorkma/Documents/Dump TIDGV5/WithMask'
#os.chdir(path)
#filename = 'Dump5Res_23.bnn.lis'
#cube = np.load(filename +'.npy')
#vector = np.zeros([cube.shape[2]])
#for z in range( cube.shape[2]):
#    tot = 0
#    numberBins = 0
#    for x in range( cube.shape[0]):
#        for y in range( cube.shape[1]):
#            #print x,y,z            
##            if math.pow(xbin*(x - i),2) + math.pow(ybin*(y - j),2) < math.pow(outerRadi,2) and math.pow(xbin*(x - i),2) + math.pow(ybin*(y - j),2) > math.pow(innerRadi,2):
#            if abs(xbin*(x - i)) < 20 and y < j and ybin*abs(y - j) < 100 and ybin*abs(y - j) > 70:
#                tot = tot + cube[x,y,z]
#                numberBins = numberBins + 1
#    val = tot/numberBins
#    vector[z] = val
#    if val > maxVal and z >= start:
#        maxVal = val
#
#
#plt.plot(range(0,cube.shape[2]),vector, color='r', label = 'With first mask')
##----------------------------------------------------
#
##-------WithOut mask-------1d cool down------------
#path = '//cern.ch/dfs/Users/c/cbjorkma/Documents/Dump TIDGV5/WithoutMask'
#os.chdir(path)
#filename = 'Dump5ResNoMask2_23.bnn.lis'
#cube = np.load(filename +'.npy')
#vector = np.zeros([cube.shape[2]])
#for z in range( cube.shape[2]):
#    tot = 0
#    numberBins = 0
#    for x in range( cube.shape[0]):
#        for y in range( cube.shape[1]):
##            if math.pow(xbin*(x - i),2) + math.pow(ybin*(y - j),2) < math.pow(outerRadi,2) and math.pow(xbin*(x - i),2) + math.pow(ybin*(y - j),2) > math.pow(innerRadi,2):
#            if abs(xbin*(x - i)) < 20 and y < j and ybin*abs(y - j) < 100 and ybin*abs(y - j) > 70:
#                tot = tot + cube[x,y,z]
#                numberBins = numberBins + 1
#    val = tot/numberBins
#    vector[z] = val
#    if val > maxVal and z >= start:
#        maxVal = val
#
#
#plt.plot(range(0,cube.shape[2]),vector, color='k',linestyle = ':', label = 'Without first mask', linewidth=3)
##----------------------------------------------------
#
#r1 = patches.Rectangle((0.827*cube.shape[2],0), 0.894*cube.shape[2] -0.827*cube.shape[2],2000,fc=(0,0,1,0.1), label = 'QD519')
#ax.add_patch(r1)
#
#
#hmw = 0.01666*cube.shape[2] # half mask width
#r2 = patches.Rectangle((0.688*cube.shape[2] -hmw,0), 2* hmw,2000,fc=(0,1,0,0.1), label = 'Mask')
#ax.add_patch(r2)
#
#r3 = patches.Rectangle((0.777*cube.shape[2] -hmw,0), 2* hmw,2000,fc=(0,1,0,0.1))
#ax.add_patch(r3)
#
#
#plt.legend()
#plt.xlim( start, cube.shape[2] )
#plt.ylim(0, maxVal*1.1)
#plt.ylabel('uSv/h', fontsize = 15)
#plt.title('1 week cool down')
#plt.grid()
#plt.xlabel('cm', fontsize = 15)
#plt.xticks( range(int(start), int(cube.shape[2]),int((cube.shape[2] - start)/10)), range(0,1035,1035/10) )
##-------------------------------------------------------------------------------------------
#






#
#
#plt.suptitle('Residual dose rates along Z downstream of dump shielding. Sampling area between ' + str(-100) + ' and ' +  str(-70) + ' cm in y and -20 to 20 cm in x, in relation to circulating beam', fontsize = 15 ,fontweight='bold')
#
#plt.show()



