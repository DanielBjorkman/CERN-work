# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 10:24:29 2018

@author: cbjorkma
"""

#ActivationMonitors

#Fluka run ends on 23rd of October 2017

import os
import numpy as np
import pandas as pd
import datetime #, timedelta
import matplotlib.pyplot as plt
import math
#from Flukato3dMatrix import Flukato3dMatrix 
plt.close()
plt.close()
plt.close()
plt.close()
plt.close()
plt.close()

#plt.clf()
#plt.clf()
#plt.clf()



# Fluka data------------------------------------------------------------------
#path = '//rpclustersrv1/cbjorkma/LSS2/ActivationDetectors/USRBINs' 

path = '//cern.ch/dfs/Users/c/cbjorkma/Documents/LSS 2/ActivationDetectors'
os.chdir(path)

files = os.listdir(path)
files = sorted(files)
#files = filter(lambda x: x[9:-8].isdigit() , files)  
files = filter(lambda x: x[0:5] == 'Fluka' , files) 


FlukaData = np.zeros([len(files),8])
FlukaSD = np.zeros([len(files),8])
row = 10
row2 = 14
indecies = [7,9, 11 ,13 , 15 ,17,19,21]
for i in range(len(files)):
    thefile = open(files[i],'r')
    filecontent = thefile.readlines()
    line = filecontent[row].split(' ')
    line2 = filecontent[row2].split(' ')
    for j in range(len(indecies)):
        FlukaData[i,j] = line[indecies[j]]
        FlukaSD[i,j] =  line2[indecies[j]]

#Converts data to uSv/h
FlukaData = 0.0036*FlukaData

#Normalization
normFactor = 1 / 0.1772837
FlukaData = normFactor * FlukaData

#Volume compensation
Volume = math.pi*8*8*21.5
FlukaData = FlukaData /Volume


#----------------------------------------------------------------------------





#Read PMI data---------------------------------------------------------------------
#path = '//rpclustersrv1/cbjorkma/LSS2/ActivationDetectors' 

path = '//cern.ch/dfs/Users/c/cbjorkma/Documents/LSS 2/ActivationDetectors'

os.chdir(path)

#protonEnd = '2017-11-23 06:00:00.940000'
protonEnd = datetime.datetime(2017,10,23,06,00,00)
ionEnd = datetime.datetime(2017,12,18,06,00,00)
end2016 = datetime.datetime(2015,11,16,06,00,00)
end2017 = datetime.datetime(2016,11,14,06,00,00)


#files = os.listdir(path)
#files = sorted(files)
#files = filter(lambda x: x[4:7].isdigit() , files)  
#files = filter(lambda x: not x[0] == '.' , files)  
#filenames = files
#thefile = pd.read_excel(files[0])
#
#data = np.zeros([len(thefile),2, len(files)])
#for j in range(len(files)):
#    thefile = pd.read_excel(files[j])
#    time = thefile.Timestamp
#    for i in range(len(thefile)):
#        instant = datetime.datetime( time[i].year, time[i].month, time[i].day, time[i].hour, time[i].minute, time[i].second)
#    #    print instant
#        timedifference = instant - protonEnd
#        amountOfSeconds = timedifference.total_seconds()/(60*60*24)
#      #  print 'file ' + str(j) + '. Seconds ' + str(amountOfSeconds) + '. value ' + str(thefile.Value[i] )
#        data[i,0,j] = amountOfSeconds
#        data[i,1,j] = thefile.Value[i]   
#assert data[1200,1,2] != data[1200,1,3]
#np.save('data', data)

data = np.load('data.npy')
#-------------------------------------------------------------------------------

def func(x,a,k1,k2):
    return a*np.exp(-k1*np.power(np.log(x - start),k2))

#def fitting(xes,y,guess):
#    for i in range(10):
#        try:
#            popt , pcov = curve_fit(lambda x,a,k1,k2,c: a*np.exp(-k1*np.power(np.log(x - start),k2)) +c,  xes,  f(xes), p0 = guess)
#        except:
#            print 'Fail'
#    return popt , pcov 
#

def extrapolate(xes,initialguess):
    for i in range(100):
        print 'Attempt ' +  str(i +1 )
        guess = initialguess
#        for j in range(len(guess)):
#            guess[j] = initialguess[j]*(2*(np.random.rand() -np.random.rand()) + 1)
        guess[0] = guess[0] +100*(2*np.random.rand() -1)
        guess[1] = guess[1] +0.0005*(2*np.random.rand() -1)
        guess[2] = guess[2] +0.0005*(2*np.random.rand() -1)      
        try:
#            popt, pcov = fitting(xes, f(xes),guess)
            popt , pcov = curve_fit(lambda x,a,k1,k2: a*np.exp(-k1*np.power(np.log(x - start),k2)),  xes,  f(xes), p0 = guess)
            print 'Success!'
            print [x/y for x, y in zip(guess, initialguess)]
            break
        except RuntimeError: 
            print 'Failed'

    return popt






files = filenames


#from scipy import interp
from scipy.interpolate import interp1d
from scipy.optimize import curve_fit

xes = [-314,-310,-308,-303,-300,-288,-295,-283,-280,-237,-224, -214,-207,-201, -198,-192,-190, -185]





#xesEx = [-314,-310,-308,-303,-300,-288,-295,-283,-280,-237,-224, -214,-207,-201, -198,-192,-190, -185]



#data = np.load('data3.npy')


#Time markers. 1 hour - 1 day - 1 week - 1 month - 2 month - 80 days
xes = np.ones([6])
cooldowns = ['1 hour' , '1 day' , '1 week' , '1 month' , '2 month' , '80 days']
xes = xes*[3600,86400,604800, 2.592*math.pow(10,6), 5.184*math.pow(10,6), 6.912*math.pow(10,6)]/(60*60*24)




sampleX = [0 ,0.041668,0.0833,0.18,0.208315,1.35,3.5, 8.86, 14.2, 42.37, 49.38,56.13,70,80,84.2]
alldiffs = np.zeros([8,6])
alldiffsInterpolated = np.zeros([8,6])

fig = plt.figure()

yminimum = 10000000


for i in range(data.shape[2]):
    ax = plt.subplot(4,2,i +1 )
    
    #Interpolate 1
    x = data[0:,0,i]
    y = data[0:,1,i]
    f = interp1d(x, y)

    diffs = f(xes) - FlukaData[0:,i]
#    alldiffs[i,0:] = diffs
    diffsRatios = f(xes) / FlukaData[0:,i]
    alldiffs[i,0:] = diffsRatios

    #Interpolation 2
    x = sampleX
    y = f(sampleX)    
    g = interp1d(x,y)
    
 
    diffsRatios = g(xes) / FlukaData[0:,i]
    alldiffsInterpolated[i,0:] = diffsRatios
    
 
    plt.plot(data[0:,0,i], data[0:,1,i], label = 'PMI data')
#    plt.scatter(xes,FlukaData[0:,i], color = 'r', label = 'Fluka')
    
    plt.plot(sampleX , f(sampleX) , color = 'g' , label =  'Interpolation', marker = 'o')   
#    plt.plot(data[0:,0,i], func(data[0:,0,i], *popt), 'r--', label = 'Fitted curve')
    plt.errorbar(xes,FlukaData[0:,i],FlukaData[0:,i]*FlukaSD[0:,i], linestyle='None', fmt='o', color = 'r', label = 'Fluka')
    plt.title(files[i][:-5], y = 0.85)
    plt.ylabel('uSv/h')

    ax.set_yscale("log", nonposy='clip')
    NoBeam = ionEnd - protonEnd
    plt.axvline(x= NoBeam.total_seconds()/(60*60*24) ,linestyle = '--', color = 'black', label = 'Ion run ends' )
#    plt.axvline(x= protonEnd.total_seconds() ,linestyle = '--', color = 'red', label = 'Proton run ends' )
    plt.legend()
#    
    ymin = 0.85*min(min(FlukaData[0:,i]))
    ymax = min(g(xes))
    xmin = -410
    xmax = 90
    
    
    plt.xlim(xmin,xmax)
    plt.ylim(ymin, ymax)

    if i%2 == 0:
        plt.xlabel('time [days]', x = 1.10, y = -1)



    ax2 = ax.twinx()
    a = 1800
    k1 = 0.00019*3.0
    k2 = 5.25*0.82
    timedifference = protonEnd - end2017
    start = timedifference.total_seconds()/(60*60*24)
    initialguess = [a,k1 ,k2] 
    
    
    
    
    
    plt.xlim(xmin,xmax)
    plt.ylim(ymin, ymax)    
    


     
plt.suptitle('Dose rate evolution per PMI unit', fontsize = 22)        
plt.show()









xcoord = np.arange(FlukaData.shape[0])




fig = plt.figure()

width = 0.27

for i in range(data.shape[2]):

    ax = plt.subplot(4,2,i +1 )
    
#    plt.bar(xcoord, alldiffs[i,0:], width, label = files[i][:-5] )
#    plt.bar(xcoord + width, alldiffsInterpolated[i,0:], width, label = 'interpolated' )
    plt.bar(xcoord, alldiffsInterpolated[i,0:], label = files[i][:-5] )
    
    #plt.plot(xcoord, np.ones(len(xcoord)), color = 'k')
    plt.axhline(y=1, color='k', linestyle='-')
    
    
    plt.ylabel('PMI / Fluka [uSv/h]')
    plt.xticks(xcoord, cooldowns)
    plt.legend()


plt.suptitle('Dose rates difference per PMI unit', fontsize = 22)
plt.show()








for i in range(len(files)):
    files[i] = files[i][:-5]



xcoord = np.arange(len(alldiffs))
#
fig = plt.figure()

for i in range(len(xes)):

#i = 0
    ax = plt.subplot(3,2,i +1 )
    
        
#    plt.bar(xcoord, alldiffs[0:,i], width, label = 'Measured data' )
#    plt.bar(xcoord + width, alldiffsInterpolated[0:,i], width, label = 'Interpolated' )
    
    plt.bar(xcoord, alldiffsInterpolated[0:,i] )
    plt.axhline(y=1, color='k', linestyle='-')    
    
    plt.title(cooldowns[i] + ' cool down')    
    plt.ylabel('PMI / Fluka [uSv/h]')
    plt.xticks(xcoord, files[0:], rotation = 0)
    plt.legend()
    
plt.suptitle('Dose rates difference per cooling time', fontsize = 22)

plt.show()





#---------------------------------------------------------------------------------------------------











#(fluka,info) =  Flukato3dMatrix('LSS2_exp_24.bnn.lis', path,1, (1/0.1772837)*0.0036)

#np.save('1hour',fluka)



#fluka = np.rot90(fluka,3)
#from matplotlib.colors import LogNorm
#
#fluka = np.load('1hour.npy')
##
##
#xmid = int(info['xbin'][0])/2 # = 0
#z = (600-int(info['zmin'][0]))/int(info['zwidth'][0])
#x = int(info['xbin'][0])/2 # = 0
#y = (-70-int(info['ymin'][0]))/int(info['ywidth'][0])
##fluka[xmid,y,z] = fluka[xmid,y,z]*1000
#image = fluka[0:,y,0:(4000-int(info['zmin'][0]))/int(info['zwidth'][0])]
#vmin=math.pow(10,-7)
#vmax=math.pow(10,7)
#plt.pcolor(image, cmap='jet',norm=LogNorm(vmin=vmin, vmax=vmax) )
#plt.colorbar()
#plt.show()

#def sumSurrounding(cube, x,y,z):
#    sum = 0
#    counts = 0
#    for i in range(-1,2):
#        for j in range(-1,2):
#                val = cube[x + i, y + j, z ]
#                print val
#                sum = sum + val
#                counts = counts + 1
#    return sum/counts
#
#
#
#out = sumSurrounding(fluka, xmid, y, z)
#print '    ' 
#print out


# PMI201 (x,y,z) = (0,-80,600)

#y = 60/int(info['ywidth'][0])
#y = (0-int(info['ymin'][0]))/int(info['ywidth'][0])
#z = (600-int(info['zmin'][0]))/int(info['zwidth'][0])

#x, y ,z = 0,0,1100/int(info['zwidth'][0])

#y = 5
#x,y = 26, 13
#print fluka[x, y,z]







#
##from datetime import datetime, timedelta
#d1 = datetime(2017,11,23,06,00,00)
#d2 = datetime(2017,11,24,06,00,00)
#d3 = d2- d1
#print d3.total_seconds()
#
#






#
#
#
#fig = plt.figure()
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
##exp curve 1
#def func(x, a,b, c):
#     return a * np.exp(-b* x) + c
##popt, pcov = curve_fit(func, xes, f(xes))
#popt, pcov = curve_fit(lambda x,a,b,c: a*np.exp(-b*x) + c,  xes,  f(xes), bounds = (xes[0],xes[len(xes)-1]))
#
#
###Taylor expansion of exponential
##def func(x, a,b, c):
##     return a +c - a*b*x + 0.5*a*b*b*x*x# - (1/6)*x*x*x*(a*b*b*b)# + (1/24)*a*b*b*b*b*x*x*x*x
###popt, pcov = curve_fit(func, xes, f(xes))
##popt, pcov = curve_fit(lambda x,a,b,c:a +c - a*b*x + 0.5*a*b*b*x*x - (1/6)*x*x*x*(a*b*b*b),  xes,  f(xes), bounds = (xes[0],200))
###Title = 'Taylor expansion of exponential
##
##
#
#
###exp curve 2
##def func(x, a,b, c,d,e):
##     return a * np.exp(-b* x) + c + d * np.exp(-e* x)
###popt, pcov = curve_fit(func, xes, f(xes))
##popt, pcov = curve_fit(lambda x,a,b,c,d,e: a * np.exp(-b* x) + c + d * np.exp(-e* x),  xes,  f(xes), bounds = (xes[0],200))
##
##
##
#
#
#
##
###Polynomial curve
##def func(x, a,b, c):
##     return a *x*x + b*x +c
###popt, pcov = curve_fit(func, xes, f(xes))
##popt, pcov = curve_fit(lambda x,a,b,c: a *x*x + b*x +c ,  xes,  f(xes))
##Title = 'Second degree polynomial'
#
#
#
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
#plt.plot(x, y, label = 'PMI data')
#plt.plot(xes , f(xes) , color = 'g' , label =  'Interpolation', marker = 'o') 
#plt.plot(x, func(x, *popt), 'r--', label = 'Fitted curve')
##plt.plot(xes, np.polyfit(xes,np.log(f(xes)),1) , 'r--', label = 'Fitted curve')
##plt.title(Title)
#plt.ylim(ymin = -1000, ymax = 10000)
#plt.legend()
#
##ax.set_yscale("log", nonposy='clip')
#plt.show()
#
#



#Read data to determine previous dose rates of the geometri

#path = '//rpclustersrv1/cbjorkma/LSS2/ActivationDetectors/PrevActivation' 
#
#os.chdir(path)
#
#files = os.listdir(path)
#files = sorted(files)
#files = filter(lambda x: x[6:9].isdigit() , files) 
#
#thefile = pd.read_excel(files[0])
#data2 = np.zeros([len(thefile),2, len(files)])
#for j in range(len(files)):
#    thefile = pd.read_excel(files[j])
#    time = thefile.Timestamp
#    for i in range(len(thefile)-1):
#        instant = datetime.datetime( time[i].year, time[i].month, time[i].day, time[i].hour, time[i].minute, time[i].second)
#    #    print instant
#        timedifference = instant - protonEnd
#        amountOfSeconds = timedifference.total_seconds()/(60*60*24)
#      #  print 'file ' + str(j) + '. Seconds ' + str(amountOfSeconds) + '. value ' + str(thefile.Value[i] )
#        data2[i,0,j] = amountOfSeconds
#        data2[i,1,j] = thefile.Value[i]   
#assert data2[1200,1,2] != data2[1200,1,3]
#
#path = '//rpclustersrv1/cbjorkma/LSS2/ActivationDetectors' 
#
#os.chdir(path)
#np.save('data2', data2)
#data2 = np.load('data2.npy')



##Read data to determine previous dose rates of the geometri
#
#path = '//rpclustersrv1/cbjorkma/LSS2/ActivationDetectors/Full' 
#
#os.chdir(path)
#
#files = os.listdir(path)
#files = sorted(files)
#files = filter(lambda x: x[4:7].isdigit() , files) 
#
#thefile = pd.read_excel(files[0])
#data2 = np.zeros([len(thefile),2, len(files)])
#for j in range(len(files)):
#    thefile = pd.read_excel(files[j])
#    time = thefile.Timestamp
#    for i in range(len(thefile)-1):
#        instant = datetime.datetime( time[i].year, time[i].month, time[i].day, time[i].hour, time[i].minute, time[i].second)
#    #    print instant
#        timedifference = instant - protonEnd
#        amountOfSeconds = timedifference.total_seconds()/(60*60*24)
#      #  print 'file ' + str(j) + '. Seconds ' + str(amountOfSeconds) + '. value ' + str(thefile.Value[i] )
#        data2[i,0,j] = amountOfSeconds
#        data2[i,1,j] = thefile.Value[i]   
#assert data2[1200,1,2] != data2[1200,1,3]
#
#path = '//rpclustersrv1/cbjorkma/LSS2/ActivationDetectors' 
#
#os.chdir(path)
#np.save('data3', data2)



#data3 = np.load('data3.npy')



