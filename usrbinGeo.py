# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 11:19:27 2019

@author: cbjorkma
"""

#

from USRBIN import USRBIN
import os


path = '//rpclustergw/cbjorkma/ATLAS'
os.chdir(path)

import copy

	
def loadGeometryFile(filename, firstIndex = 2, lastIndex = 4):
	""" Reads in a geometry file from FLUKA 
	x Axis -> Index 2
	y Axis -> Index 3
	z Axis -> Index 4
	Default: x and z Axis
	"""
	X = []	
	Y = []
	Xs = []	
	Ys = []
	for line in file(filename):
		if line[0] == "#":
			continue
		if line.strip() == "":
			if X:
				Xs.append(copy.copy(X))
				Ys.append(copy.copy(Y))				

				X = []	
				Y = []
		else:
			splitted = map(float, line.split())
			X.append(splitted[firstIndex])
			Y.append(splitted[lastIndex])
        

	if X:
		Xs.append(copy.copy(X))
		Ys.append(copy.copy(Y))				
		X = []	
		Y = []

	return Xs, Ys

filename = 'ATLAS2_JTTcontours.dat'


#b = load(filename)
Xs, Ys = loadGeometryFile(filename, 3,4)


import glob


## Carmona
#path = '//rpclustergw/cluster_temp/cbjorkma/OpeningScenarios/DECAY/Carmona/2019-02-07_11h02m53s_ATLAS2_JTTPrep'
#os.chdir(path)


normfactor = 0.0036



#
#
## Master
#path = '//rpclustergw/cluster_temp/cbjorkma/OpeningScenarios/DECAY/Master/2019-02-06_14h21m55s_ATLAS2_JTTPrep'
#os.chdir(path)
##
#
#
#
##try:
##    print danielold
##except:
#print 'Loading USRBINs...'
#
#
#filenames = sorted(glob.glob('*.lis'))
#
##filenames.append('ATLAS1_28.bnn.lis')
#
#master = []
#
#
#for i in [0,5,11]: #range(0,len(filenames),4):
#    filename = filenames.pop(0)
#    
#    x = USRBIN(filename, path, normfactor)
#    x.read()
#    image = x.cube[0:,int(x.cube.shape[1]/2),0:]
#    master.append(image)
#
#
#
#
## Carmona
#path = '//rpclustergw/cluster_temp/cbjorkma/OpeningScenarios/DECAY/Carmona/2019-02-07_11h02m53s_ATLAS2_JTTPrep'
#os.chdir(path)
#
#
#filenames = sorted(glob.glob('*.lis'))
#
#
#carmonaIM = []
##carmonaIntegrated = []
#
#for i in [0,5,11]: #for i in range(len(filenames)):
#    filename = filenames.pop(0)
#    
#    x = USRBIN(filename, path, normfactor)
#    x.read()
#    image = x.cube[0:,int(x.cube.shape[1]/2),0:]
#    carmonaIM.append(image)   
#

# Carmona
path = '//rpclustergw/cluster_temp/cbjorkma/OpeningScenarios/DECAY/Carmona/2019-02-07_11h02m53s_ATLAS2_JTTPrep'
os.chdir(path)



filenames = sorted(glob.glob('*.lis'))

carmona = USRBIN(filenames[0], path, normfactor)
carmona.read()
carmona.calc()


# Master
path = '//rpclustergw/cluster_temp/cbjorkma/OpeningScenarios/DECAY/Master/2019-02-06_14h21m55s_ATLAS2_JTTPrep'
os.chdir(path)
filenames = sorted(glob.glob('*.lis'))

master = USRBIN(filenames[0], path, normfactor)
master.read()
master.calc()


carmonaIM = carmona.cube[0:,int(carmona.cube.shape[1]/2),0:]

masterIM = master.cube[0:,int(master.cube.shape[1]/2),0:]



import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
import numpy as np


#fig = plt.figure()



maxY = int(carmona.info['rmax'][0])
widthY = int(carmona.info['rwidth'][0])
maxX = int(carmona.info['zmax'][0])
widthX = int(carmona.info['zwidth'][0])


X, Y = np.meshgrid(range(0,maxX, widthX),range(-maxY,maxY, widthY))

#vmin = np.min(carmona.cube[np.nonzero(carmona.cube)])
#vmin = 1E-2
#vmax = np.max(carmona.cube)
#
#image = carmona.cube[0:,int(carmona.cube.shape[1]/2),0:]
#plt.pcolor(X, Y, image,norm=LogNorm(vmin=vmin, vmax=vmax), cmap='viridis')
#plt.colorbar()
#
#
#for i in range(len(Xs)):
#    #plt.plot(Xs[i],Ys[i], 'k-',  linewidth=1)
#    plt.plot(Ys[i],Xs[i], 'k-',  linewidth=0.5)
#
#
#
#plt.xlim(0,maxX )
#
#plt.xlabel('z [cm from IP]', fontsize = 22)
#plt.ylabel('r [cm from IP]', fontsize = 22)
#plt.show()




#fig = plt.figure()



cooldowns = ['28d', '56d', '84d', '112d', '140d', '181d', '196d', '224d', '254d', '280d', '308d', '336d']
cooldowns = [cooldowns[0], cooldowns[5], cooldowns[11]]

for i in [0]: #range(len(master)):
    fig = plt.figure()
    image = carmonaIM/masterIM
    vmin = 1 #np.min(image[np.nonzero(image)])
    vmax = 1.5
    plt.pcolor(X, Y, image,vmin=vmin, vmax=vmax)


    cbar = plt.colorbar()
    cbar.set_label('Carmona/Master', rotation=90, fontsize = 22)


    for j in range(len(Xs)):
        #plt.plot(Xs[i],Ys[i], 'k-',  linewidth=1)
        plt.plot(Ys[j],Xs[j], 'k-',  linewidth=1)



    plt.xlim(0,maxX )
    
    plt.title('Ratio , ' + cooldowns[i], fontsize = 26)
    plt.xlabel('z [cm from IP]', fontsize = 22)
    plt.ylabel('r [cm from IP]', fontsize = 22)
    plt.show()




for i in [0]: #range(len(master)):
    fig = plt.figure()
    image = carmonaIM - masterIM
    vmin = np.min(image) #np.min(image[np.nonzero(image)])
    vmax = np.max(image)
    bound = max(abs(vmin), abs(vmax))
    bound = 100
    
    plt.pcolor(X, Y, image, vmin = -bound, vmax = bound ,cmap = 'seismic')


    cbar = plt.colorbar()
    cbar.set_label('Carmona - Master [uSv/h]', rotation=90, fontsize = 22)


    for j in range(len(Xs)):
        #plt.plot(Xs[i],Ys[i], 'k-',  linewidth=1)
        plt.plot(Ys[j],Xs[j], 'k-',  linewidth=1)



    plt.xlim(0,maxX )
    
    plt.title('Subtraction, ' + cooldowns[i], fontsize = 26)
    plt.xlabel('z [cm from IP]', fontsize = 22)
    plt.ylabel('r [cm from IP]', fontsize = 22)
    plt.show()





fig = plt.figure()
i = 0
image = carmonaIM
vmin = 0.01
vmax = np.max(image)
bound = max(abs(vmin), abs(vmax))
#bound = 100

plt.pcolor(X, Y, image, norm=LogNorm(vmin=vmin, vmax=vmax), cmap = 'gnuplot')


cbar = plt.colorbar()
cbar.set_label('Carmona - Master [uSv/h]', rotation=90, fontsize = 22)


for j in range(len(Xs)):
    #plt.plot(Xs[i],Ys[i], 'k-',  linewidth=1)
    plt.plot(Ys[j],Xs[j], 'k-',  linewidth=1)



plt.xlim(0,maxX )

plt.title('Plain ' + cooldowns[i], fontsize = 26)
plt.xlabel('z [cm from IP]', fontsize = 22)
plt.ylabel('r [cm from IP]', fontsize = 22)
plt.show()





































#
#carmonaCentre = []
#carmonaIntegrated = []
#
#for i in range(len(filenames)):
#    filename = filenames.pop(0)
#    
#    x = USRBIN(filename, path, normfactor)
#    x.read()
#    x.calc()
#    carmonaCentre.append(x.centre)
#    carmonaIntegrated.append(x.depthdeposition)

