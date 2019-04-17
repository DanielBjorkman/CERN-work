# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 10:36:23 2019

@author: cbjorkma
"""

import sys
import numpy as np
from math import log10
import pylab 
from matplotlib.colors import LogNorm, Normalize
from itertools import izip
import copy



def load(filename):
	""" Incorporate search for "this is" to detect line above the first line and "error" to detect end of value block
	"""

	data = []
	axesdata = []
	
	dataReached = False

	for (i, line) in enumerate(file(filename)):
		if line.find("error") > 0:
			break
		if dataReached:
			#print line
			dataLine = [ x for x in map(float, line.split())]
			if dataLine != []:
				data.append(dataLine)
		else:
			if line.find("coordinate:") > 0:
				splitted = line.split()            
				AxisData = (splitted[3], splitted[5], splitted[7])
				axesdata.append( (float(splitted[3]), float(splitted[5]), int(splitted[7])) )
				#print "coordinate " + str(AxisData)
			#print line
			if line.find("this is") > 0:
				dataReached = True
	try:
		BinShape = (axesdata[0][2],axesdata[1][2],axesdata[2][2]) # x,y,z
	except:
		BinShape = (axesdata[0][2],axesdata[1][2]) # x,y,z
	ReverseBinShape = list(BinShape)
	ReverseBinShape.reverse()
	usrbin_data = np.reshape(np.array(data),ReverseBinShape).transpose()
	return usrbin_data, axesdata
	
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



def getAxesRange(axisdata):
	start,end,nBins = axisdata
	step = (end-start)/ nBins
	return np.arange(start, end+step/2., step)

def getAxisIndex(axisdata, value):
	start,end,nBins = axisdata
	step = (end-start)/ nBins
	if value < start:
		return -1
	if value > end:
		return nBins
	return int((value-start)/step) 

def plotMatrix(mat, axesdata, UseLog = True, vMinLog = None, vMaxLog = None, aspectRatioEqual = True, geometryData = None, savefilename = None, vMin = None, vMax = None):
	X = getAxesRange(axesdata[0])
	Y = getAxesRange(axesdata[1])
	if UseLog:
		pylab.pcolor(X,Y, mat, norm = LogNorm(vmin=vMinLog, vmax=vMaxLog))
	else:	
		pylab.pcolor(X,Y, mat, norm = Normalize(vmin=vMin, vmax=vMax) )
	pylab.colorbar()
	pylab.xlim(axesdata[0][0], axesdata[0][1])
	pylab.ylim(axesdata[1][0], axesdata[1][1])
	if aspectRatioEqual:
		pylab.axes().set_aspect('equal') #, 'datalim')
	if geometryData != None:
		for x,y in izip(*geometryData):
			pylab.plot(x,y, 'k-',  linewidth=2)
	if savefilename != None:
		pylab.savefig(savefilename)
	#pylab.show()
	return pylab

def plotMatrixShort(data, axesdata, selection, transpose = False, UseLog = True, vMinLog = None, vMaxLog = None, aspectRatioEqual = True, geometryData = None, savefilename = None, vMin = None, vMax = None):
	selecteddata = data[selection]
	selectedaxesdata = [ axesdata[i] for (i,selectionItem) in enumerate(selection) if selectionItem == Ellipsis]
	print selectedaxesdata
	if transpose:
		selecteddata = selecteddata.transpose()
	else:
		selectedaxesdata.reverse()
	return plotMatrix(selecteddata, selectedaxesdata, UseLog, vMinLog, vMaxLog, aspectRatioEqual, geometryData, savefilename, vMin = vMin, vMax = vMax)

def getValue(x,y,z, data, axesdata):
	xIndex = getAxisIndex(axesdata[0], x)

	yIndex = getAxisIndex(axesdata[1], y)
	zIndex = getAxisIndex(axesdata[2], z)
	#print xIndex, yIndex, zIndex
	return data[xIndex, yIndex, zIndex]
#

if __name__ == "__main__":

	import os
	filename = os.environ.get('PYTHONSTARTUP')
	if filename and os.path.isfile(filename):
		execfile(filename)

	from pydoc import help
	from pprint import pprint


	usrbin_data, axesdata = load(sys.argv[1])
	#BinShape = (axesdata[0][2],axesdata[1][2],axesdata[2][2]) # x,y,z

	#ReverseBinShape = list(BinShape)
	#ReverseBinShape.reverse()
	#a = np.array(data)
	#b = np.reshape(a, (150,30, -1))
	#usrbin_data = np.reshape(np.array(data),ReverseBinShape).transpose()

	normalizationFactor = 1E-12*8.34E12*3600*1E6

	
	#plotMatrix(usrbin_data[75,:,:].transpose(), axesdata[1:])
	plotMatrixShort(usrbin_data, axesdata, (Ellipsis,15,Ellipsis), transpose = True, geometryData = loadGeometryFile(sys.argv[2]), savefilename = "plot.pdf")
	#print getAxesRange(axesdata[0])

		

	#print normalizationFactor * getValue(800,0.,44400, usrbin_data, axesdata)

	def myfunc(x):
		if np.isnan(x):
			return 0.
		else:
			return x
	vfunc = np.vectorize(myfunc)

	da = usrbin_data * normalizationFactor / (usrbin_data * normalizationFactor/5.)

	plotMatrixShort(vfunc(da), axesdata, (Ellipsis,15,Ellipsis), transpose = True, vMin = 1e-1, UseLog = False, geometryData = loadGeometryFile(sys.argv[2]))

#
#import os
#
#path = '//rpclustergw/cbjorkma/ATLAS'
#os.chdir(path)

filename = 'ATLAS2_JTTcontours.dat'


#b = load(filename)
#Xs, Ys = loadGeometryFile(filename)








