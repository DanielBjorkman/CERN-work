
#! /usr/bin/env python
import os
path = '//rpclustergw/cbjorkma/ATLAS/LLcalc'
os.chdir(path)

#filename = os.environ.get('PYTHONSTARTUP')

filename = 'JTTin3m_63_tab.lis'


if filename and os.path.isfile(filename):
	execfile(filename)

from pydoc import help
from pprint import pprint
###########################
import sys

import json

LL_values = json.load(file("//rpclustergw/cbjorkma/ATLAS/LLcalc/rp-data/json/CH-LL-2018-isomeresCap.json"))
from jeremy.utils.decaydata import DecayData, ElementsNumber2StringDict, StandardHalfLifeUnitsConversionToSeconds
from jeremy.utils import makeSorter, decorateSortUndecorate
DecayDataFileName = "//rpclustergw/cbjorkma/ATLAS/LLcalc/decaydata.pkl"
dd= DecayData(DecayDataFileName)

import pyfluka.resnucle


def extractMajorComponents(activityDict):
	activityList = [(v[0],k) for k,v in activityDict.iteritems() if dd.halfLifeStr(k)]
	activityList.sort()
	return activityList


##-------------------------------
filename = sys.argv[1]
try:
	primariesPerSecond = eval(sys.argv[2],{},{})
except:
	primariesPerSecond = 1.

primariesPerYear = primariesPerSecond * StandardHalfLifeUnitsConversionToSeconds["y"]

writeFile = open(filename[:-4] + 'Out' + filename[-4:], 'w')
##-------------------------------
string = "Filename = %s" % filename
print string
writeFile.write(string + '\n')

string = "primaries / s  = %g" % (primariesPerSecond)
print string
writeFile.write(string + '\n')

string = "primaries / y  = %g" % (primariesPerYear)
print string
writeFile.write(string + '\n')

string = ' '
print string
writeFile.write(string + '\n')

##-------------------------------
activityDict = pyfluka.resnucle.load(filename)
keys = activityDict.keys()
keys.sort()
for k in keys:
	print k
	acc = []
	for act,isotope in reversed(extractMajorComponents(activityDict[k])[:]):
		activity = primariesPerSecond * act
		if LL_values.has_key(isotope):
			LL = activity/LL_values[isotope]/1e3
		else:   
			LL = 0.
		acc.append( [isotope, activity, LL ] )

	acc = decorateSortUndecorate(acc, makeSorter([2,1]), SortAscending = False)
	for isotope, activity, LL in acc:
		string = "  %s%s%s%s" % (isotope.ljust(10),  dd.halfLifeStr(isotope).ljust(12), ("%.2e Bq/g" % activity).rjust(13), ("%.3g (fraction LL [kg])" % LL).rjust(30))
		print string
		writeFile.write(string + '\n')
	#pprint(extractMajorComponents(activityDict[k])[-4:])
	
	print
	print
writeFile.close()

