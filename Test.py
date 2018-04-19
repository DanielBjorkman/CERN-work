#
#





import matplotlib.pyplot as plt
#plt.close()
#plt.close()
#plt.close()
#plt.close()

#from PMIs import PMI
from USRBIN import USRBIN
from PMIs import PMI
import datetime
from scipy.interpolate import interp1d
#filename = 'LSS2_exp_24.bnn.lis'

path = '//rpclustersrv1/cbjorkma/LSS2/FullActivation/USRBINs'
#

#Converts data to uSv/h and normalizes data to the number of exstracted particles
normfactor = 0.0036*1 / 0.1772837

import os
os.chdir(path)
filenames = sorted(os.listdir(path))

#USRBINS = []
#for i in range(len(filenames)):
#    x = USRBIN(filenames[i], path, normfactor)
#    x.read()
#    x.calc()
#    USRBINS.append(x)    



protonEnd = datetime.datetime(2017,10,23,06,00,00)
ionEnd = datetime.datetime(2017,12,18,06,00,00)
end2016 = datetime.datetime(2015,11,16,06,00,00)
end2017 = datetime.datetime(2016,11,14,06,00,00)
manualMeasurement = datetime.datetime(2017,10,24,12,00,00)


path = '//cern.ch/dfs/Users/c/cbjorkma/Documents/LSS 2/ActivationDetectors'

pmi = PMI(path, end2017)

pmi.read()
pathFluka = '//rpclustersrv1/cbjorkma/LSS2/FullActivation/PMIs'
pmi.readFluka(pathFluka, normfactor)
pmi.calc()


#def predictBaseline(pmi,usrbin):
from scipy.optimize import minimize , rosen
from scipy.optimize import curve_fit
import numpy as np



data1 = pmi.targetdoseratepercooldown[0][4:]
data2 = pmi.FlukaData[0,4:]

steps = 10000
lbound = 0.0001
hbound = 3
As = np.zeros(steps)
sums = np.zeros(steps)

for i in range(steps):
    A = np.arange(lbound,hbound,(hbound - lbound)/steps)[i]
    sums[i] = sum(abs(data1 -A*data2))
    As[i] = A
    
#print min(sums)
idx = np.argmin(sums)
A = As[idx]

#popt , pcov = curve_fit(lambda A: sum(abs(data1 - A*data2)),  np.zeros(4), p0 = 0.12)

fig = plt.figure()
#popt , pcov = curve_fit(lambda x,a,k1,k2: a*np.exp(-k1*np.power(np.log(x),k2)),  xes,  f(xes), p0 = guess)

plt.plot(pmi.xpos[4:],pmi.targetdoseratepercooldown[0][4:], label = 'Target')
plt.plot(pmi.xpos[4:],A*pmi.FlukaData[0,4:], label = 'Fluka')

plt.legend()

plt.show()











































#
#
#from matplotlib.colors import LogNorm
#import matplotlib.pyplot as plt
#
#plt.close()
#plt.close()
#plt.close()
#
#from USRBIN import USRBIN
#
#path = '//rpclustersrv1/cbjorkma/LSS2/FullActivation/USRBINs'
##
#
##Converts data to uSv/h and normalizes data to the number of exstracted particles
#normfactor = 1 #0.0036*1 / 0.1772837
#
#import os
#os.chdir(path)
#filenames = sorted(os.listdir(path))
#
#USRBINS = []
#for i in range(1):
#    x = USRBIN(filenames[i], path, normfactor)
#    x.read()
#    x.calc()
#    USRBINS.append(x)    
#
#
#
#
#
#
#
#
#fig = plt.figure()
#
#plt.subplot(111)
#
#cube = USRBINS[0]
##cube2 = data[3]
##cube = data[1]
#
#vmax = 10**8
#vmin = 10**3
#
#image = cube.horizontal[0:,0:300]
#plt.pcolor(image, norm=LogNorm(vmin=vmin, vmax=vmax), cmap='jet')
#cbar = plt.colorbar()
#cbar.set_label('uSv/h')
#plt.xlabel('z [~cm]')
#plt.ylabel('x [bins]')
#
##plt.title('New Fluka verison')
#
#
#plt.show()
#
#
#
#fig = plt.figure()
#
#plt.subplot(121)
#
##cube = USRBINS[1]
##cube2 = data[3]
##cube = data[1]
#
#vmax = 10**8
#vmin = 10**3
#
#image = cube.cube[0:,5,0:]
#plt.pcolor(image, norm=LogNorm(vmin=vmin, vmax=vmax), cmap='jet')
#cbar = plt.colorbar()
#cbar.set_label('uSv/h')
#plt.xlabel('z [~cm]')
#plt.ylabel('x [bins]')
#
##plt.title('New Fluka verison')
#plt.subplot(122)
#
#plt.plot(cube.below)
#plt.xlabel('z [~cm]')
#
#
#plt.show()
#
#


















#
#import os
#import numpy as np
#import pandas as pd
#import datetime #, timedelta
#import matplotlib.pyplot as plt
#import math
##from Flukato3dMatrix import Flukato3dMatrix 
##plt.close()
##plt.close()
##plt.close()
##plt.close()
##plt.close()
##plt.close()
#
#plt.clf()
#
## Fluka data------------------------------------------------------------------
#path = '//rpclustersrv1/cbjorkma/LSS2/ActivationDetectors/USRBINs' 
#os.chdir(path)
#
#files = os.listdir(path)
#files = sorted(files)
#files = filter(lambda x: x[9:-8].isdigit() , files)  
#
#FlukaData = np.zeros([len(files),8])
##row = 10
##indecies = [7,9, 11 ,13 , 15 ,17,19,21]
##for i in range(len(files)):
##    thefile = open(files[i],'r')
##    filecontent = thefile.readlines()
##    line = filecontent[row].split(' ')
##    for j in range(len(indecies)):
##        FlukaData[i,j] = line[indecies[j]]
##
###Converts data to uSv/h
##FlukaData = 0.0036*FlukaData
##
###Normalization
##normFactor = 1 / 0.1772837
##FlukaData = normFactor * FlukaData
##
###Volume compensation
##Volume = math.pi*8*8*21.5
##FlukaData = FlukaData /Volume
##
#
##----------------------------------------------------------------------------
#
#
#
#
#
##Read PMI data---------------------------------------------------------------------
#path = '//rpclustersrv1/cbjorkma/LSS2/ActivationDetectors' 
#
#os.chdir(path)
#
##protonEnd = '2017-11-23 06:00:00.940000'
#protonEnd = datetime.datetime(2017,10,23,06,00,00)
#ionEnd = datetime.datetime(2017,12,18,06,00,00)
#
#files = os.listdir(path)
#files = sorted(files)
#files = filter(lambda x: x[4:7].isdigit() , files)  
#filenames = files
#
#
#
#
#path = '//rpclustersrv1/cbjorkma/LSS2/ActivationDetectors' 
#
#os.chdir(path)
#
###protonEnd = '2017-11-23 06:00:00.940000'
##protonEnd = datetime.datetime(2017,10,23,06,00,00)
##ionEnd = datetime.datetime(2017,12,18,06,00,00)
##
##
#
#
#
##Read PMI data---------------------------------------------------------------------
##path = '//rpclustersrv1/cbjorkma/LSS2/ActivationDetectors' 
#
#path = '//cern.ch/dfs/Users/c/cbjorkma/Documents/LSS 2/ActivationDetectors'
#
#os.chdir(path)
#
##protonEnd = '2017-11-23 06:00:00.940000'
#protonEnd = datetime.datetime(2017,10,23,06,00,00)
#ionEnd = datetime.datetime(2017,12,18,06,00,00)
#end2016 = datetime.datetime(2015,11,16,06,00,00)
#end2017 = datetime.datetime(2016,11,14,06,00,00)
#
##
##files = os.listdir(path)
##files = sorted(files)
##files = filter(lambda x: x[4:7].isdigit() , files)  
##filenames = files
##thefile = pd.read_excel(files[0])
##
##data = np.zeros([len(thefile),2, len(files)])
##for j in range(len(files)):
##    thefile = pd.read_excel(files[j])
##    time = thefile.Timestamp
##    for i in range(len(thefile)):
##        instant = datetime.datetime( time[i].year, time[i].month, time[i].day, time[i].hour, time[i].minute, time[i].second)
##    #    print instant
###        timedifference = instant - protonEnd
##        timedifference = instant - end2016
##        amountOfSeconds = timedifference.total_seconds()/(60*60*24)
##      #  print 'file ' + str(j) + '. Seconds ' + str(amountOfSeconds) + '. value ' + str(thefile.Value[i] )
##        data[i,0,j] = amountOfSeconds
##        data[i,1,j] = thefile.Value[i]   
##assert data[1200,1,2] != data[1200,1,3]
##np.save('data', data)
#
#data = np.load('data.npy')
##-------------------------------------------------------------------------------
#
#
#
#
#data3 = np.load('data.npy')
#
#
#
#
#
#
#
#
#files = filenames
#
#
#from scipy import interp
#from scipy.interpolate import interp1d
#from scipy.optimize import curve_fit
#
#timedifference = protonEnd - end2016
#
#
#xes2016 = [-691.709,-689, -685,-671.35,-658,-654,-651,-641.056,-629,-618,-609,-605,-590,-579.75,-565.928, -560.055 , -554.317, -553.13  ]
#for i in range(len(xes2016)):
#    xes2016[i] = xes2016[i] +timedifference.total_seconds()/(60*60*24)
#
#
#xes2017 = [-314,-310,-308,-303,-300,-297,-288,-295,-283,-280,-237,-224, -214,-207,-201, -198,-192,-190, -185, -180.475 ,  -174.584]
#for i in range(len(xes2017)):
#    xes2017[i] = xes2017[i] +timedifference.total_seconds()/(60*60*24)
#
#
##xes = [-314,-310,-308,-303,-300,-297,-288,-295,-283]
#
#
#
##fig = plt.figure()
#
#ax = plt.subplot(111)
#i = 0
#
#x = data3[0:,0,i]
#y = data3[0:,1,i]
#
#f = interp1d(x, y, fill_value='extrapolate')
#
###Log curve
##def func(x, a,b, c):
##     return a * np.log(-b* x) + c
##popt, pcov = curve_fit(lambda x,a,b,c: a*np.log(-b*x) + c,  xes,  f(xes))
#
#
#
#
#
#
#
##initialguess = [1, 3.31,0.67,979]
#
#
##k1 = 3.14
##
##k2 = 0.69
#
###MAtthew expression 1 curve
##def func(x,a, k1,k2,c):
##   return a*np.exp(-k1*np.power(np.log(x),k2)) + c
##
##def fitting(xes,y,guess):
##    for i in range(100):
##        try:
##            popt, pcov = curve_fit(lambda x,a,k1,k2,c: a*np.exp(-k1*np.power(np.log(x),k2)) + c,  xes,  f(xes),  p0 = guess)
##        except RuntimeError:
##            print 'Fail'
##    #        print a, k1, k2,c 
##    
##    return popt , pcov
##
##Title = "Curve of format a*np.exp(np.power(-b*np.log(x),k)) + c"
##
#
#
####Exponential
##def func(x, a,b, c):
##    return a * np.exp(-b* x) + c
##    
##def fitting(xes,y,guess):
##    for i in range(10):
##        try:
##            popt , pcov = curve_fit(lambda x,a,b,c: a*np.exp(-b*x) + c,  xes,  f(xes), p0 = guess)
##        except:
##            print 'Fail'
##    return popt , pcov 
##
##
##
##
##
##
##
##def extrapolate(xes,initialguess):
##    for i in range(10):
##        print 'Attempt ' +  str(i +1 )
##        guess = initialguess
##        for j in range(len(guess)):
##            guess[j] = initialguess[j]*(2*(np.random.rand() -np.random.rand()) + 1)
##        
##        try:
##
##            popt, pcov = fitting(xes, f(xes),guess)
##            print 'Success!'
##            break
##        except RuntimeError: 
##            print 'Failed'
##
##    return popt
#
#
##xes = np.ones([6])
##xes = xes*[3600,86400,604800, 2.592*math.pow(10,6), 5.184*math.pow(10,6), 6.912*math.pow(10,6)]/(60*60*24)
#    
#sampleX = [0 ,0.041668,0.0833,0.18,0.208315,1.35,3.5, 8.86, 14.2, 42.37, 49.38,56.13,70,80,84.2]
#for i in range(len(sampleX)):
#    sampleX[i] = sampleX[i] +timedifference.total_seconds()/(60*60*24)
#
#ax = plt.subplot(111)
#
#plt.plot(x, y, label = 'PMI data')
##plt.plot(sampleX , f(sampleX) , color = 'g' , label =  'Interpolation', marker = 'o')
#
##ymin = 0
##ymax = 2000
##
##xmin =350
##xmax = 600
#
#
#ymin = 000
#ymax = 6000
#
#xmin =-10
#xmax = 800
#
#
#
#plt.ylim(ymin , ymax)
#plt.xlim(xmin, xmax)
##----------------------------------------------------------------------------
###Exponential
##initialguess = [1, 0.02,979]
##popt = extrapolate(xes2017,initialguess)
##plt.plot(x, func(x, *popt), 'r--', label = 'Curve fit 2017')
##
##
##initialguess = [1, 0.0002,500]
##popt = extrapolate(xes2016,initialguess)
##plt.plot(x, func(x, *popt), 'c--', label = 'Curve fit 2016')
###
#
#
###Exponential, logged exponent
##initialguess = [1, 3.14,0.69,979]
##popt = extrapolate(xes2017,initialguess)
##plt.plot(x, func(x, *popt), 'r--', label = 'Curve fit 2017')
#
#
##initialguess = [1, 0.0002,500]
##popt = extrapolate(xes2016,initialguess)
##plt.plot(x, func(x, *popt), 'c--', label = 'Curve fit 2016')
##----------------------------------------------------------------------------
#
##Exponential, logged exponent
##initialguess = [1, 3.14,0.69,300,318]
##popt = extrapolate(xes2017,initialguess)
#
##x = 0
##i = 318
##k2 = 0.69
#
##def func(x):
##   return 1*np.exp(-1*np.power(np.log(0.001*(10 - x)),0.1)) + 800
#
##def func(x):
##    a = 1500
##    k1 = 1
##    k2 = 0.1
##    dt = 1000**-1 #difference from start
##    i = 1500 #start
##    try:
##        return a*np.exp(-k1*np.power(np.log(dt*(i - x)),k2)) + 800
##    except RuntimeWarning:
##        print np.power(np.log(dt*(i - x)))
##        print dt
##        print x
##        print i
#ax2 = ax.twinx()
#
#
#
#
#timedifference = end2017 - end2016
#
#start = timedifference.total_seconds()/(60*60*24)
#print start
## Very good first approximation of the slope
##start = 370 #start
#def func(x):
##    a = 1000
##    k1 = 0.00019*3.5
##    k2 = 5.25*1.0
##    c = 2000/2
#    a = 1800
#    k1 = 0.00019*3.0
#    k2 = 5.25*0.82
#    try:
#        val =  a*np.exp(-k1*np.power(np.log(x - start),k2))
#    except RuntimeWarning:
##        print np.power(np.log(dt*(i - x)))
##        print dt
#        print x
#        print i
#    return val
##--------------------------------------------------------
#
#
## Very good first approximation of the slope
#start2 = 0 #start
#def func2(x):
##    a = 3500
##    k1 = 0.00019*3.5
##    k2 = 5.25*1.0
##    c = 1200
##    
#    a = 3900
#    k1 = 0.00019*2.8
#    k2 = 5.25*0.90
#    try:
#        val =  a*np.exp(-k1*np.power(np.log(x - start2),k2)) 
#    except RuntimeWarning:
#       # print np.power(np.log(dt*(i - x)))
#     #   print dt
#        print x
#        print i
#    return val
##--------------------------------------------------------
#
#
##a = 1000
##k1 = 0.00019*3
##k2 = 5.25
##c = 2000/2
##
##initialguess = [a, k1 ,k2,c] 
#
#
#
#
#
#
#
#
#
#
#x = np.arange(start,800)
#d = func(x)
#
##plt.ylim(ymin = 1, ymax = 4000)
#
#plt.plot(x[1:], func(x[1:]), 'r--', label = 'Curve fit 2017')
#
#x = np.arange(start2,800)
#d = func(x)
#
##plt.ylim(ymin = 1, ymax = 4000)
#
#plt.plot(x[1:], func2(x[1:]), 'c--', label = 'Curve fit 2016')
#
#
#
#
##for i in range(len(xes2017)):
##    plt.axvline(x= xes2017[i] ,linestyle = '--', color = 'k')
###    
##for i in range(len(xes2016)):
##    plt.axvline(x= xes2016[i] ,linestyle = '--', color = 'k')    
#
##plt.plot(xes, np.polyfit(xes,np.log(f(xes)),1) , 'r--', label = 'Fitted curve')
#plt.title( "Curve fit of format a*np.exp(-k1*np.power(np.log(x - start2),k2))")
#plt.ylim(ymin , ymax)
#plt.xlim(xmin, xmax)
#plt.legend()
#plt.xlabel('time[days]')
#plt.ylabel('uSv/h')
##ax.set_yscale("log", nonposy='clip')
#plt.show()
#
#
#
#
#
#
#
#
###exp curve 1
##def func(x, a,b, c):
##     return a * np.exp(-b* x) + c
##popt, pcov = curve_fit(lambda x,a,b,c: a*np.exp(-b*x) + c,  xes,  f(xes), p0 = guess)
#
#
#
###Taylor expansion of exponential
##def func(x, a,b, c):
##     return a +c - a*b*x + 0.5*a*b*b*x*x# - (1/6)*x*x*x*(a*b*b*b)# + (1/24)*a*b*b*b*b*x*x*x*x
###popt, pcov = curve_fit(func, xes, f(xes))
##popt, pcov = curve_fit(lambda x,a,b,c:a +c - a*b*x + 0.5*a*b*b*x*x - (1/6)*x*x*x*(a*b*b*b),  xes,  f(xes), bounds = (xes[0],200))
###Title = 'Taylor expansion of exponential
##
#
##guess = [1, 0.02,979,0.5,3]
##
###exp curve 2
##def func(x, a,b, c,d,e):
##     return a * np.exp(-b* x) + c + d * np.exp(-e* x)
###popt, pcov = curve_fit(func, xes, f(xes))
##popt, pcov = curve_fit(lambda x,a,b,c,d,e: a * np.exp(-b* x) + c + d * np.exp(-e* x),  xes,  f(xes), p0 = guess)
##
#
##
#
#
#
##
###Polynomial curve
##def func(x, a,b, c):
##     return a *x*x + b*x +c
###popt, pcov = curve_fit(func, xes, f(xes))c
##popt, pcov = curve_fit(lambda x,a,b,c: a *x*x + b*x +c ,  xes,  f(xes))
##Title = 'Second degree polynomial'
#
#
##
###MAtthew expression 1 curve
##def func(x, a,b,c):
##     return np.exp(np.power(-a*np.log(x),b)) + c
###popt, pcov = curve_fit(func, xes, f(xes))
##popt, pcov = curve_fit(lambda x,a,b,c: np.exp(np.power(-a*np.log(x),b)) + c,  xes,  f(xes))
#
#
###MAtthew expression 2 curve
##def func(x,k, a,b,c):
##     return k*np.exp(-a*np.log(x) -b*np.power(np.log(x),2)) + c
###popt, pcov = curve_fit(func, xes, f(xes))
##popt, pcov = curve_fit(lambda x,a,b,c,k: k*np.exp(-a*np.log(x) -b*np.power(np.log(x),2)) + c,  xes,  f(xes))
##
#
##linear
##def func(x, k,m):
##     return k*x + m
###popt, pcov = curve_fit(func, xes, f(xes))
##popt, pcov = curve_fit(lambda x,k,m: k*x +m,  xes,  f(xes))
##Title = 'Linear'
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
### -*- coding: utf-8 -*-
##"""
##Created on Wed Jul 12 14:51:42 2017
##
##@author: cbjorkma
##"""
##
##
##
##
##import os
###import numpy as np
###import math
###from matplotlib.colors import LogNorm
###from matplotlib.gridspec import GridSpec
###import matplotlib.pyplot as plt
###import matplotlib.ticker as tk
###import matplotlib.patches as patches
####plt.close()
##
##
##import pandas as pd
##import glob
##
##
##
##
##path = '/scratch/cbjorkma/LSS2'
##
##basedir = '/Volumes/clueet_scratch/luillo/LSS2/2018-01-10_200umRibbonZS_full_abd_z2232cm_ZSrho/'
##
##os.chdir(basedir)
##
##
##
##
##
##
##
##
##
##
##
##
####path = "//rpclustersrv1/cbjorkma/LSS2/run09"      
###path = "//rpclustersrv1/cbjorkma/LSS2/PyCollimateStudy/UsingPC"    
###os.chdir(path)        
####fluka1 = readPhaseDirectory(path)           
####np.save('run09', fluka1)
####  
###
###plt.clf()
###  
####filename = 'LSS2_exp001_fort.90' 
#####filename = 'fort.90' 
#####fluka1 = readPhase(filename)    
###
###print 'Start'
###
###
###x = np.random.rand(1600000)
###y = np.random.rand(16000)
###y = np.random.normal(0.5,2,10000)
###fluka = np.load('run09.npy')
###fluka = np.load('PCgreaterthan3.716.npy')
###x = fluka[0:,1]
###y = fluka[0:,3]
###primaries = fluka.shape[0]*0.01
###condition = x >= 5
###x = np.extract(condition,x)
###primaries = len(x)
###condition = fluka[0:,1] >= 3.5
###subsetFluka = np.zeros([np.sum(condition),fluka.shape[1]])
###for i in range(fluka.shape[1]):
###    subsetFluka[0:,i] = np.extract(condition, fluka[0:,i])
###print 'Subset Created'
###
##
##
##
##
###import subprocess
###import sys
###
###HOST="cbjorkma@clueet.ch"
#### Ports are handled in ~/.ssh/config since we use OpenSSH
###COMMAND="ls"
###
###ssh = subprocess.Popen(["ssh", "%s" % HOST, COMMAND],
###                       shell=False,
###                       stdout=subprocess.PIPE,
###                       stderr=subprocess.PIPE)
###result = ssh.stdout.readlines()
####if result == []:
####    error = ssh.stderr.readlines()
####    print >>sys.stderr, "ERROR: %s" % error
####else:
####    print result
###
###
###
###
##
##
##
##
##
##
##
##
##
##
##
##
###x = fluka[0:,1]
###y = fluka[0:,3]
##
###newvec = x/y
##
###plt.subplot(211)
###
###histx1, xbins1, patches1 = plt.hist(y, bins = 10,fc=(1, 0, 0, 0.8))
###histx2, xbins2, patches2 = plt.hist(x, bins = xbins1,fc=(0, 1, 0, 0.8))
###
###plt.subplot(212)
###
###newvec = histx1/histx2
###
###binwidth = xbins1[1] - xbins1[0]
###
###plt.bar( xbins1[:-1], newvec,binwidth ,fc=(0, 0, 1, 0.8))
##
###out = plt.hist2d(x,y, bins=300,normed = True,cmap="viridis")
###
###ax1 = plt.subplot(111)
###
####x = fluka[0:,5]
###weights = 100* np.ones_like(x)/float(len(x))
###histx, xbins, Placeholder = plt.hist(x,weights = weights, bins = 100,fc=(1, 0, 0, 0.8), label = 'Fluka')
###
####y = fluka[0:,5]
###weights = 100* np.ones_like(y)/float(len(y))
###histx, xbins, Placeholder = plt.hist(y,weights = weights, bins = 100,fc=(0, 0, 1, 0.8), label = 'MADX')
###
###plt.legend()
####plt.yscale('log')
###ax1.set_yscale("log", nonposy='clip')
###
###
###
###
###
###
###
###ax = ax1.twinx()
###
###ax.plot(range(10),3*np.ones(len(range(10))),  'r.')
###
###r1 = patches.Rectangle((2,6.8), 313, 5, angle= -0.0861284, color = 'g')
###ax.add_patch(r1)
###
###plt.show()
##
##
##
##
##
##
###
###weights = np.transpose(100* np.ones_like([x,y])/float(primaries))
####H, xedges, yedges = np.histogram2d(x, y, bins=[300,300],weights = weights) #, weights = weights) #,cmap="viridis"
####myextent  =[xedges[0],xedges[-1],yedges[0],yedges[-1]]
###out = plt.hist2d(x,y, bins= 300,weights = weights, cmap="viridis")
##
##
##
##
###new = np.zeros([len(x),fluka.shape[1]])
###vec = np.zeros([1,fluka.shape[1]])
###for i in range(fluka.shape[1]):
###    vec[0,0:] = fluka[i,0:]
###    if vec[0,1] >= 3.5:
###        new = np.concatenate( (new, vec), axis = 0) 
##
##
###x = np.extract(fluka[0:,1]>3.7, fluka)
###
###new = np.zeros([len(x),fluka.shape[1]])
###idx = 0
###for i in range(len(x)):
###    if fluka[i,1] >= 3.5:
###        new[idx,0:] = fluka[i,0:]
###        idx = idx +1
##
##        
##        
##        
##        
##        
###normfactor = 1
###
###fig = plt.figure()
###
###plt.clf()
###
###plt.subplot(121)
###
###plt.hist2d(fluka[0:1], fluka[0:3], bins=300, norm=LogNorm(),cmap="viridis")
###
###plt.subplot(122)
###plt.hist2d(new[0:1], new[0:3], bins=300, norm=LogNorm(),cmap="viridis")
##
##
###weights = 100* np.ones_like(y)/float(len(y))
###n, bins, patches =plt.hist(y,weights = weights, bins = 10, fc = (1,0,0, 0.5))
###
###weights = 100* np.ones_like(x)/float(len(x))
###plt.hist(x, weights = weights, bins = 100)
##
##
##
###histx[1][1] - histx[1][0]
##
###print sum(a[0])
###plt.yscale('log')
###results, edges = np.histogram(x, bins = 100, weights = weights)  
###results = results*100
## 
## 
###print sum(results)
###plt.yscale('log')
###binWidth = edges[1] - edges[0]
###plt.bar(edges[:-1], results*binWidth, binWidth, fc=(0, 0, 1, 0.8), label = 'MADX')
##
##plt.show()
##
##
##
##
###import os as os
###
###dir = '//rpclustersrv1/cbjorkma/Dump studies/Uppstream Hole study/Fluence/Halloutput_dir'
###
###filename = 'HallAirproduction.nuc'
###
###os.chdir(dir)
###
###import numpy as np
###
###print np.loadtxt(filename, skiprows = 12, usecols = (1,2))
###
###import math
###septaColor = 'green'
###import matplotlib.pyplot as plt
####from ActiwizFluence import ActiwizFluence
####from ActiwizFluence import ActiwizFluencePlot
####import math
###import numpy as np
###
###plt.close()
###
###fig = plt.figure()
###ax1 = fig.add_subplot(1,1,1)
###
###x = np.random.rand(1000000)*1000
###
###results, edges = np.histogram(x, normed=True, bins = 40)    
###binWidth = edges[1] - edges[0]    
###
###x,y = results*binWidth, edges[:-1]
###
###x = edges[:-1]
###y = results*binWidth
###plt.bar(x, y, binWidth)   
###
###
####ax = fig.add_subplot(1,2,2)
###
####plt.barh(x, y, binWidth)   
####
###ax2 = ax1.twinx()
###
###import matplotlib.patches as patches
###
###
####Quads
###plt.axvline(x=0,linestyle = '--' ,label='Quadrupoles', color = 'black')
###plt.axvline(x=3199.77,linestyle = '--', color = 'black' )
###plt.axvline(x=6399.54,linestyle = '--', color = 'black' )
###plt.axvline(x=9599.31,linestyle = '--', color = 'black' )
###
####ZSs
###r1 = patches.Rectangle((355.45,6.8), 313,0.006, angle= -0.0861284)
###r2 = patches.Rectangle((746.45,6.212), 313,0.006, angle= -0.0861284)
###r3 = patches.Rectangle((1137.45,5.623), 313,0.006, angle= -0.0861284)
###r4 = patches.Rectangle((1528.45,5.035), 313,0.006, angle= -0.0861284)
###r5 = patches.Rectangle((1919.45,4.446), 313,0.006, angle= -0.0861284)
###ax2.add_patch(r1)
###ax2.add_patch(r2)
###ax2.add_patch(r3)
###ax2.add_patch(r4)
###ax2.add_patch(r5)
###
###
###
###
###plt.ylim(0,10)
###
###
###plt.show()
##
###path = '//rpclustersrv1/cbjorkma/Dump studies/Uppstream Hole study/Fluence/AirTunnel_dir'
###
###
####fig = plt.figure()
####ax = fig.add_subplot(211)
####path = '//rpclustersrv1/cbjorkma/Dump studies/Uppstream Hole study/Fluence/Deepscore1_dir'
###data = ActiwizFluence(path, 15912)
###
###prim = 1
###fig = plt.figure()
###ax = plt.subplot(211)
###ActiwizFluencePlot(data, ax, prim)
###plt.title('Downstream tunnel fluence, with first downstream mask', fontsize = 20)
###plt.ylim([math.pow(10,-9), math.pow(10,-1)])
###
###path = '//rpclustersrv1/cbjorkma/Dump studies/Uppstream Hole study/Fluence/AirTunnelNoMASK_dir'
###data = ActiwizFluence(path, 15912)
###ax = plt.subplot(212)
###ActiwizFluencePlot(data, ax, prim)
###plt.title('Downstream tunnel fluence, WITHOUT first downstream mask', fontsize = 20)
###plt.ylim([math.pow(10,-9), math.pow(10,-1)])
###plt.show()
###
####
###ax = fig.add_subplot(212)
###path = '//rpclustersrv1/cbjorkma/Dump studies/Uppstream Hole study/Fluence/Deepscore2_dir'
###obj = ActiwizFluence(path)
##
##
###plt.show()
###
###tunnelVolume = 2.8*math.pow(10,8)
###cavernVolume = 6.82*math.pow(10,9)
###
####With first mask
###path = '//rpclustersrv1/cbjorkma/Dump studies/Uppstream Hole study/Fluence/Cavern_dir'
###data1 = ActiwizFluence(path, cavernVolume)
###
###path = '//rpclustersrv1/cbjorkma/Dump studies/Uppstream Hole study/Fluence/AirTunnel_dir'
###data2 = ActiwizFluence(path, tunnelVolume)
###
###Mask = []
###for i in range(len(data1)-1):
###    tmp = data1[i]
###    tmp[0:,2] = data1[i][0:,2] + data2[i][0:,2]
###    tmp[0:,3] = map(lambda x, y: math.sqrt( math.pow(x,2) + math.pow(y,2)), data1[i][0:,3], data2[i][0:,3])
###    Mask.append( tmp )
###Mask.append( data1[4])
###
###
####Without first mask
###path = '//rpclustersrv1/cbjorkma/Dump studies/Uppstream Hole study/Fluence/CavernNoMASK_dir'
###data1 = ActiwizFluence(path, cavernVolume)
###
###path = '//rpclustersrv1/cbjorkma/Dump studies/Uppstream Hole study/Fluence/AirTunnelNoMASK_dir'
###data2 = ActiwizFluence(path, tunnelVolume)
###
###NoMask = []
###for i in range(len(data1)-1):
###    tmp = data1[i]
###    tmp[0:,2] = data1[i][0:,2] + data2[i][0:,2]
###    tmp[0:,3] = map(lambda x, y: math.sqrt( math.pow(x,2) + math.pow(y,2)), data1[i][0:,3], data2[i][0:,3])
###    NoMask.append( tmp )
###NoMask.append( data1[4])
###
###
###
###
###
###
###
###prim = 2 *math.pow(10,18)
###
###fig = plt.figure()
###ax = plt.subplot(211)
###ActiwizFluencePlot(Mask, ax, prim)
###plt.title('With first mask', fontsize = 20)
####plt.ylim([math.pow(10,-9), 2*math.pow(10,-6)])
###
###
###ax = plt.subplot(212)
###ActiwizFluencePlot(NoMask, ax, prim)
###plt.title('Without first mask', fontsize = 20)
####plt.ylim([math.pow(10,-9), 2*math.pow(10,-6)])
###
###plt.show()
###
####Combination
###combo = []
###for i in range(len(Mask)-1):
###    tmp = Mask[i]
###    tmp[0:,2] = NoMask[i][0:,2] - Mask[i][0:,2] 
###    tmp[0:,3] = map(lambda x, y: math.sqrt( math.pow(x,2) + math.pow(y,2)), Mask[i][0:,3], NoMask[i][0:,3])
###    combo.append( tmp )
###combo.append( Mask[4])
###
###fig = plt.figure()
###ax = plt.subplot(111)
###ActiwizFluencePlot(Mask, ax, prim)
###plt.title('Difference plot / Additional hadrons to activate the ECX5 air volume when first mask is absent', fontsize = 20)
###plt.ylabel('Without Mask - With mask [cm-2]')
####plt.ylim([math.pow(10,-11), math.pow(10,-6)])
###
###
###
###plt.show()
###
###
###
###print 'Zsa1 = ' + str((680 + 342)/2 )
###print 'BLM1 = ' + str((680 + 342)/2 + 51)
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
