# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 15:22:03 2017

@author: cbjorkma
"""

#ResAlongZDiffplots


from Flukato3dMatrix import Flukato3dMatrix 

#filename = 'Dump5Res_21.bnn.lis'
#path = '//cern.ch/dfs/Users/c/cbjorkma/Documents/Dump TIDGV5/WithMask'

import os



import numpy as np

#------Load Data-------------------------------------
#path = '//cern.ch/dfs/Users/c/cbjorkma/Documents/Dump TIDGV5/WithMask'
#os.chdir(path)
#filename = 'Dump5Res_21.bnn.lis'
#cube = 0.0036* Flukato3dMatrix(filename, path,0 )
#np.save(filename, cube)

#filename = 'Dump5Res_22.bnn.lis'
#cube = 0.0036* Flukato3dMatrix(filename, path,0 )
#np.save(filename, cube)

#filename = 'Dump5Res_23.bnn.lis'
#cube = 0.0036* Flukato3dMatrix(filename, path,0 )
#np.save(filename, cube)

#path = '//cern.ch/dfs/Users/c/cbjorkma/Documents/Dump TIDGV5/WithoutMask'
#os.chdir(path)
#filename = 'Dump5ResNoMask2_21.bnn.lis'
#cube = 0.0036* Flukato3dMatrix(filename, path,0 )
#np.save(filename, cube)

#filename = 'Dump5ResNoMask2_22.bnn.lis'
#cube = 0.0036* Flukato3dMatrix(filename, path,0 )
#np.save(filename, cube)

#filename = 'Dump5ResNoMask2_23.bnn.lis'
#cube = 0.0036* Flukato3dMatrix(filename, path,0 )
#np.save(filename, cube)

#-----------------------------------------------










#------------Extracting meta info
path = '//cern.ch/dfs/Users/c/cbjorkma/Documents/Dump TIDGV5/WithMask'
os.chdir(path)
cube = np.load('tmpCube.npy')
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

fig = plt.figure()



ax = fig.add_subplot(111)
#-------With mask-------1h cool down------------
path = '//cern.ch/dfs/Users/c/cbjorkma/Documents/Dump TIDGV5/WithMask'
os.chdir(path)
filename = 'Dump5Res_21.bnn.lis'
cube = np.load(filename +'.npy')

vmax = cube.max()
vmin = math.pow(10,-5) #np.min(cube[np.nonzero(cube)])


image = cube[0:,j,0:]
plt.pcolor(image,norm=LogNorm(vmin=vmin, vmax=vmax), cmap='jet')
cbar = plt.colorbar()
cbar.set_label('Intensity')

hml = 0.01666*cube.shape[2] # half mask length
hmw = 0.059*cube.shape[0] # half mask width

r2 = patches.Rectangle((0.688*cube.shape[2] -hml,j -hmw), 2* hml,2* hmw,fc=(0,1,1,1), label = 'Mask')
ax.add_patch(r2)

r3 = patches.Rectangle((0.777*cube.shape[2] -hml,j - hmw), 2* hml,2* hmw,fc=(0,1,1,1))
ax.add_patch(r3)


plt.show()











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



