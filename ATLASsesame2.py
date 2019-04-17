# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 12:42:52 2019

@author: cbjorkma
"""

#AtlasSesame2


import os
import glob
from USRBIN import USRBIN


def loadGeometryFile(filename, firstIndex = 2, lastIndex = 4):

	""" Reads in a geometry file from FLUKA 
	x Axis -> Index 2
	y Axis -> Index 3
	z Axis -> Index 4
	Default: x and z Axis
	"""
	import copy
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
path = '//rpclustergw/cbjorkma/ATLAS'
os.chdir(path)
filename = 'ATLAS2_JTTcontours.dat'


#b = load(filename)
Xs, Ys = loadGeometryFile(filename, 3,4)

def bin_ndarray(ndarray, new_shape, operation='sum'):
    """
    Bins an ndarray in all axes based on the target shape, by summing or
        averaging.

    Number of output dimensions must match number of input dimensions and 
        new axes must divide old ones.

    Example
    -------
    >>> m = np.arange(0,100,1).reshape((10,10))
    >>> n = bin_ndarray(m, new_shape=(5,5), operation='sum')
    >>> print(n)

    [[ 22  30  38  46  54]
     [102 110 118 126 134]
     [182 190 198 206 214]
     [262 270 278 286 294]
     [342 350 358 366 374]]

    """
    operation = operation.lower()
    if not operation in ['sum', 'mean']:
        raise ValueError("Operation not supported.")
    if ndarray.ndim != len(new_shape):
        raise ValueError("Shape mismatch: {} -> {}".format(ndarray.shape,
                                                           new_shape))
    compression_pairs = [(d, c//d) for d,c in zip(new_shape,
                                                  ndarray.shape)]
    flattened = [l for p in compression_pairs for l in p]
    ndarray = ndarray.reshape(flattened)
    for i in range(len(new_shape)):
        op = getattr(ndarray, operation)
        ndarray = op(-1*(i+1))
    return ndarray




normfactor = 0.0036

idx = 0
cool = '28 days'

Master = 'v2.1.3'
Carmona = 'dev. branch'
Ref = 'Fluka only'

# Carmona
path = '//rpclustergw/cluster_temp/cbjorkma/OpeningScenarios/DECAY/Carmona/2019-03-18_15h20m16s_ATLAS2_JTTPrep'
os.chdir(path)

filenames = sorted(glob.glob('*.lis'))


carmona = USRBIN(filenames[0], path, normfactor)
carmona.read()
carmona.calc()

filename = 'ATLAS2_JTTPrep_22Error.lis'

carmonaError = USRBIN(filename, path, 1)
carmonaError.read()




# Master
path = '//rpclustergw/cluster_temp/cbjorkma/OpeningScenarios/DECAY/Master/2019-03-18_13h40m05s_ATLAS2_JTTPrep'
os.chdir(path)
filenames = sorted(glob.glob('*.lis'))

filename = 'ATLAS2_JTTPrep_22.bnn.lis'

master = USRBIN(filename, path, normfactor)
master.read()
master.calc()

filename = 'ATLAS2_JTTPrep_22.bnnError.lis'

masterError = USRBIN(filename, path, 1)
masterError.read()



#Reference
path = '//rpclustergw/cluster_temp/cbjorkma/2019-02-15_16h44m29s_ATLAS2'
os.chdir(path)
filenames = sorted(glob.glob('*.lis'))

ref = USRBIN(filenames[0], path, normfactor)
ref.read()
ref.calc()

filename = 'ATLAS2_22.bnnError.lis'

refError = USRBIN(filename, path, 1)
refError.read()











import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
import numpy as np

import numpy as np

factor = 10

shape = np.asarray(carmona.cube.shape)/factor

carmonaRed = bin_ndarray(carmona.cube, shape)

masterRed = bin_ndarray(carmona.cube, shape)

refRed = bin_ndarray(carmona.cube, shape)


maxY = int(carmona.info['rmax'][0])
widthY = int(carmona.info['rwidth'][0])*factor
maxX = int(carmona.info['zmax'][0])
widthX = int(carmona.info['zwidth'][0])*factor


X, Y = np.meshgrid(range(0,maxX, widthX),range(-maxY,maxY, widthY))


carmonaIM = carmonaRed[0:,int(carmonaRed.shape[1]/2),0:]
carmonaCentre = carmona.centre
carmonaDepth = carmona.depthdeposition
carmona = []
carmonaRed = []

masterIM = masterRed[0:,int(masterRed.shape[1]/2),0:]
masterCentre = master.centre
masterDepth = master.depthdeposition
master = []
masterRed = []

refIM = refRed[0:,int(refRed.shape[1]/2),0:]
refCentre = ref.centre
refDepth = ref.depthdeposition
ref = []
refRed = []

import numpy as np


path = '//rpclustergw/cbjorkma/ATLAS'
os.chdir(path)


np.save('carmonaIM', carmonaIM)
np.save('carmonaCentre', carmonaCentre)
np.save('carmonaDepth', carmonaDepth)


np.save('masterIM', masterIM)
np.save('masterCentre', masterCentre)
np.save('masterDepth', masterDepth)


np.save('refIM', refIM)
np.save('refCentre', refCentre)
np.save('refDepth', refDepth)


import os
path = '//rpclustergw/cbjorkma/ATLAS'
os.chdir(path)

carmonaIM = np.load('carmonaIM.npy')
carmonaCentre = np.load('carmonaCentre.npy' )
carmonaDepth = np.load('carmonaDepth.npy')


masterIM = np.load('masterIM.npy')
masterCentre = np.load('masterCentre.npy' )
masterDepth = np.load('masterDepth.npy')

refIM = np.load('refIM.npy')
refCentre = np.load('refCentre.npy' )
refDepth = np.load('refDepth.npy')







path = '//rpclustergw/cluster_temp/cbjorkma/Sesame/Git/Validation'
os.chdir(path)


import matplotlib.colors as colors

#fig = plt.figure()



cooldowns = ['28d', '56d', '84d', '112d', '140d', '181d', '196d', '224d', '254d', '280d', '308d', '336d']
cooldowns = [cooldowns[0], cooldowns[2], cooldowns[5]]

#for i in [0]: #range(len(master)):
i = 0
fig = plt.figure()
#ax = plt.subplot(111)
image = carmonaIM/refIM
vmin = 0.1 #np.min(image[np.nonzero(image)])
vmax = 10
plt.pcolor(X, Y, image,vmin=vmin, vmax=vmax, cmap = 'seismic', norm=colors.LogNorm(vmin=vmin, vmax=vmax))
#plt.pcolor(X, Y, image )

cbar = plt.colorbar()
cbar.set_label(Carmona + '/' + Ref, rotation=90, fontsize = 22)
#cbar.set_label('Error [%]', rotation=90, fontsize = 22)

for j in range(len(Xs)):
    #plt.plot(Xs[i],Ys[i], 'k-',  linewidth=1)
    plt.plot(Ys[j],Xs[j], 'k-',  linewidth=0.5, alpha = 0.5)



plt.xlim(0,maxX )

plt.title('Ratio , '  + Carmona + '/' + Ref + ' . Rebinning factor = ' + str(factor) +', ' + cool, fontsize = 22)
#plt.title('Fluka Errors , Carmona version, ' + cool, fontsize = 26)
plt.xlabel('z [cm from IP]', fontsize = 22)
plt.ylabel('r [cm from IP]', fontsize = 22)
#ax.set_aspect(1/1.618)

xlength = 12

fig.set_size_inches(xlength, xlength/1.618)

plt.show()
#
plt.savefig('CarmonaRefRatio.pdf')









fig = plt.figure()
image = masterIM/refIM
vmin = 0.1 #np.min(image[np.nonzero(image)])
vmax = 10
plt.pcolor(X, Y, image,vmin=vmin, vmax=vmax,cmap = 'seismic', norm=colors.LogNorm(vmin=vmin, vmax=vmax))
#plt.pcolor(X, Y, image )

cbar = plt.colorbar()
cbar.set_label(Master + '/' + Ref, rotation=90, fontsize = 22)
#cbar.set_label('Error', rotation=90, fontsize = 22)

for j in range(len(Xs)):
    #plt.plot(Xs[i],Ys[i], 'k-',  linewidth=1)
    plt.plot(Ys[j],Xs[j], 'k-',  linewidth=0.5, alpha = 0.5)



plt.xlim(0,maxX )

plt.title('Ratio , '+ Master + '/' + Ref +' . Rebinning factor = ' + str(factor) + ', ' + cool, fontsize = 22)
#plt.title('Fluka Errors , Master version, ' + cool, fontsize = 26)
plt.xlabel('z [cm from IP]', fontsize = 22)
plt.ylabel('r [cm from IP]', fontsize = 22)
#ax.set_aspect(1/1.618)

xlength = 12

fig.set_size_inches(xlength, xlength/1.618)

plt.show()
#
plt.savefig('MasterRefRatio.pdf')







width = 0.1

bins= np.arange(0.1 - width/2,3,width)

fig = plt.figure()
image = carmonaIM/refIM
plt.hist(image.flatten(), bins= bins, label = Carmona + '/' + Ref)
image = masterIM/refIM
plt.hist(image.flatten(), bins=bins, label = Master + '/' + Ref , alpha = 0.6 )
#image = refIM
#plt.hist(image.flatten(), bins=bins, label = 'Fluka only, average = ' + str(calc(image)), alpha = 1, histtype='step', color = 'g', linewidth = 2)
#np.histogram(image)
#plt.axvline(x=1, color = 'k')
plt.legend()
plt.title('Histogram comparison of 2D image', fontsize = 22)
plt.ylabel('Bin counts', fontsize = 20)
plt.xlabel('Ratio', fontsize = 20)
plt.grid(linewidth= 0.3)
ax.set_aspect(1/1.618)

xlength = 12

fig.set_size_inches(xlength, xlength/1.618)

plt.show()
#
plt.savefig('ValueHistogram.pdf')



def calc(image):
    return np.sum(image)/image.size


width = 0.5

bins= np.arange(0.0 - width/2,100,width)


fig = plt.figure()
image = carmonaError.cube[0:,int(carmonaError.cube.shape[1]/2),0:]
plt.hist(image.flatten(), bins= bins, label = Carmona + ', average = ' + str(calc(image)))
image = masterError.cube[0:,int(masterError.cube.shape[1]/2),0:]
plt.hist(image.flatten(), bins=bins, label = Master +', average = ' + str(calc(image)) , alpha = 0.6 )
image = refError.cube[0:,int(refError.cube.shape[1]/2),0:]
plt.hist(image.flatten(), bins=bins, label = Ref +  ', average = ' + str(calc(image)), alpha = 1, histtype='step', color = 'g', linewidth = 2)

plt.legend()
plt.title('Histogram Errors comparison of 2D image', fontsize = 22)
plt.ylabel('Bin counts', fontsize = 20)
plt.xlabel('Errors [%]', fontsize = 20)
plt.grid(linewidth= 0.3)
ax.set_aspect(1/1.618)

xlength = 12

fig.set_size_inches(xlength, xlength/1.618)

plt.show()
#
plt.savefig('ErrorsHistogram.pdf')





factor = 1

maxY = int(carmonaError.info['rmax'][0])
widthY = int(carmonaError.info['rwidth'][0])*factor
maxX = int(carmonaError.info['zmax'][0])
widthX = int(carmonaError.info['zwidth'][0])*factor
X, Y = np.meshgrid(range(0,maxX, widthX),range(-maxY,maxY, widthY))


i = 0
fig = plt.figure()
image = carmonaError.cube[0:,int(carmonaError.cube.shape[1]/2),0:]
vmin = 0.1 #np.min(image[np.nonzero(image)])
vmax = 10
plt.pcolor(X, Y, image)
#plt.pcolor(X, Y, image )

cbar = plt.colorbar()
#cbar.set_label('Carmona/Ref', rotation=90, fontsize = 22)
cbar.set_label('Error [%]', rotation=90, fontsize = 22)

for j in range(len(Xs)):
    #plt.plot(Xs[i],Ys[i], 'k-',  linewidth=1)
    plt.plot(Ys[j],Xs[j], 'k-',  linewidth=0.5, alpha = 0.5)



plt.xlim(0,maxX )

#plt.title('Ratio , Carmona/Ref. Rebinning factor = ' + str(factor) +', ' + cool, fontsize = 26)
plt.title('Fluka Errors , ' + Carmona +' version, ' + cool, fontsize = 26)
plt.xlabel('z [cm from IP]', fontsize = 22)
plt.ylabel('r [cm from IP]', fontsize = 22)
ax.set_aspect(1/1.618)

xlength = 12

fig.set_size_inches(xlength, xlength/1.618)

plt.show()
#
plt.savefig('CarmonaErrors.pdf')







fig = plt.figure()
image = masterError.cube[0:,int(masterError.cube.shape[1]/2),0:]
vmin = 0.1 #np.min(image[np.nonzero(image)])
vmax = 10
plt.pcolor(X, Y, image)
#plt.pcolor(X, Y, image )

cbar = plt.colorbar()
#cbar.set_label('Master/Ref', rotation=90, fontsize = 22)
cbar.set_label('Error [%]', rotation=90, fontsize = 22)

for j in range(len(Xs)):
    #plt.plot(Xs[i],Ys[i], 'k-',  linewidth=1)
    plt.plot(Ys[j],Xs[j], 'k-',  linewidth=0.5, alpha = 0.5)



plt.xlim(0,maxX )

#plt.title('Ratio , Carmona/Ref. Rebinning factor = ' + str(factor) +', ' + cool, fontsize = 26)
plt.title('Fluka Errors , ' + Master + ' version, ' + cool, fontsize = 26)
plt.xlabel('z [cm from IP]', fontsize = 22)
plt.ylabel('r [cm from IP]', fontsize = 22)
ax.set_aspect(1/1.618)

xlength = 12

fig.set_size_inches(xlength, xlength/1.618)

plt.show()
#
plt.savefig('MasterErrors.pdf')


















image1 = carmonaIM/refIM

image2 = masterIM/refIM

width = 0.1

bins= np.arange(0.1 - width/2,3,width)



fig = plt.figure()
#image = carmonaIM/refIM
plt.hist(image1.flatten(), bins=bins, label = Carmona +'/' + Ref)
#image = masterIM/refIM
plt.hist(image2.flatten(), bins=bins, label = Master +'/' + Ref , alpha = 0.6 )
#image = refIM
#plt.hist(image.flatten(), bins=bins, label = 'Fluka only, average = ' + str(calc(image)), alpha = 1, histtype='step', color = 'g', linewidth = 2)
#np.histogram(image)
#plt.axvline(x=1, color = 'k')
plt.legend()
plt.title('Histogram comparison of 2D image', fontsize = 22)
plt.ylabel('Bin counts', fontsize = 20)
plt.xlabel('Ratio', fontsize = 20)
plt.grid(linewidth= 0.3)
plt.show()




cool = '28 days'

import matplotlib.cm as cm
import matplotlib.gridspec as gridspec

gs = gridspec.GridSpec(3, 2)

xes = range(0,2500,2500/500)


fig = plt.figure()

#colors = cm.rainbow(np.linspace(0, 1, len(cooldowns)))

#ax = fig.add_subplot(211)
ax = plt.subplot(gs[0:2, 0])

plt.title('Beam axis residual dose rate', fontsize = 16)
#for i in range(0,len(cooldowns),3): #range(len(cooldowns)):
#plt.plot(xes, carmona.centre/ref.centre, label = 'Carmona/Reference', linestyle = '-')
#plt.plot(xes, master.centre/ref.centre, label = 'Master/Reference', linestyle = '-')

plt.plot(xes, carmonaCentre, label = Carmona, linestyle = '-')
plt.plot(xes, masterCentre, label = Master, linestyle = '-')
plt.plot(xes, refCentre, label = Ref , linestyle = '-')
ax.set_yscale('log')
#plt.xlabel('z [cm from IP]', fontsize = 18)
#plt.ylabel('Ratio dose rate' , fontsize = 14)
plt.ylabel('Residual dose rate [uSv/h]' , fontsize = 14)
#plt.title('Max values along z', fontsize = 15)
#plt.axhline(y=1, color='k', linestyle='-')
plt.grid(linewidth = 0.3)
plt.legend()


ax = plt.subplot(gs[-1, 0])



plt.plot(xes, carmonaCentre/refCentre, label = Carmona +'/' + Ref, linestyle = '-')
plt.plot(xes, masterCentre/refCentre, label = Master +'/' + Ref, linestyle = '-')
#plt.plot(xes, refCentre, label = 'FLUKA only', linestyle = '-')
#ax.set_yscale('log')
plt.xlabel('z [cm from IP]', fontsize = 18)
#plt.ylabel('Ratio dose rate' , fontsize = 14)
plt.ylabel('Ratio' , fontsize = 14)
#plt.title('Max values along z', fontsize = 15)
plt.axhline(y=1, color='k', linestyle='-')
plt.grid(linewidth = 0.3)
plt.legend()


#xes = range(0,2500,2500/250)



#colors = cm.rainbow(np.linspace(0, 1, len(cooldowns)))

#ax = fig.add_subplot(212)
ax = plt.subplot(gs[0:2, 1])

plt.title('Integrade residual dose rate', fontsize = 16)
#for i in range(0,len(cooldowns),3): #range(len(cooldowns)):
#plt.plot(xes, carmona.depthdeposition/ref.depthdeposition, label = 'Carmona/Reference', linestyle = '-')
#plt.plot(xes, master.depthdeposition/ref.depthdeposition, label = 'Master/Reference', linestyle = '-')
plt.plot(xes, carmonaDepth,label = Carmona, linestyle = '-')
plt.plot(xes, masterDepth, label = Master, linestyle = '-')

plt.plot(xes, refDepth, label = Ref, linestyle = '-')

ax.set_yscale('log')

#plt.xlabel('z [cm from IP]', fontsize = 18)
#plt.ylabel('Ratio integrated dose rate' , fontsize = 14)
plt.ylabel('Integrated dose rate [uSv/h]' , fontsize = 14)
#plt.title('Max values along z', fontsize = 15)
#plt.axhline(y=1, color='k', linestyle='-')
plt.grid(linewidth = 0.3)
plt.legend()




ax = plt.subplot(gs[-1, 1])



plt.plot(xes, carmonaDepth/refDepth, label = Carmona +'/' + Ref, linestyle = '-')
plt.plot(xes, masterDepth/refDepth, label = Master +'/' + Ref, linestyle = '-')
#plt.plot(xes, refCentre, label = 'FLUKA only', linestyle = '-')
#ax.set_yscale('log')
plt.xlabel('z [cm from IP]', fontsize = 18)
#plt.ylabel('Ratio dose rate' , fontsize = 14)
plt.ylabel('Ratio' , fontsize = 14)
#plt.title('Max values along z', fontsize = 15)
plt.axhline(y=1, color='k', linestyle='-')
plt.grid(linewidth = 0.3)
plt.legend()





plt.suptitle('Sesame version compare. ATLAS geo, cooldown of ' + cool, fontsize = 22)

xlength = 12

fig.set_size_inches(xlength, xlength/1.618)

plt.show()
#
plt.savefig('CarmonaMasterRefCurves.pdf')





print 'Done'