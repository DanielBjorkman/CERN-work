# -*- coding: utf-8 -*-
"""
Created on Fri Oct 05 15:23:56 2018

@author: cbjorkma
"""

#LHCIRRADIATIONPROFILE


import os

path = '//rpclustersrv1/cbjorkma/ATLAS'

os.chdir(path)


import numpy as np

ATLASdata = np.loadtxt('ATLASirradiatonprofile2.txt')
CMSdata = np.loadtxt('CMSirradiatonprofile.txt')
LHCdata = np.loadtxt('LHCirradiatonprofile.txt')

ATLAS = np.zeros([ATLASdata.shape[0]+2,3])
CMS = np.zeros([CMSdata.shape[0]+2,3])
LHC = np.zeros([LHCdata.shape[0]+2,3])

ATLAS[1:len(ATLAS)-1,0:2] = ATLASdata
CMS[1:len(CMS)-1,0:2] = CMSdata
LHC[1:len(LHC)-1,0:2] = LHCdata


ATLAS[0:,0] = ATLAS[0:,0]/(60*60*24)
CMS[0:,0] = CMS[0:,0]/(60*60*24)
LHC[0:,0] = LHC[0:,0]/(60*60*24)


import datetime

#protonEnd = datetime.datetime(2017,10,23,06,00,00)
#ionEnd = datetime.datetime(2017,12,18,06,00,00)

LS2 = datetime.datetime(2018,10,23,13,22,00) #t0
newyear2018 = datetime.datetime(2018,12,31,23,59,59)

#instant = datetime.datetime( time[i].year, time[i].month, time[i].day, time[i].hour, time[i].minute, time[i].second)

timedifference = LS2 - newyear2018
newyearsLS2difference = timedifference.total_seconds()/(60*60*24)

print newyearsLS2difference
    




def calcTimeline(experiment):

    lastidx = len(experiment)-3
    
    experiment[len(experiment)-2,2] = - experiment[len(experiment)-2,0]
    for i in range(lastidx,-1,-1):
        #print i
        experiment[i,2] = -experiment[i,0] - abs(experiment[i+1,2])
    return experiment;
        #print ATLAS[i,3] 
        

ATLAS = calcTimeline(ATLAS)
CMS = calcTimeline(CMS)
LHC = calcTimeline(LHC)    
    
###    
#lastidx = len(ATLAS)-3
#
#ATLAS[len(ATLAS)-2,2] = - ATLAS[len(ATLAS)-2,0]
#for i in range(lastidx,-1,-1):
#    #print i
#    ATLAS[i,2] = -ATLAS[i,0] - abs(ATLAS[i+1,2])
#    #print ATLAS[i,3] 
#    
#    
#    
#
#lastidx = len(CMS)-3
#CMS[len(CMS)-2,2] = - CMS[len(CMS)-2,0] 
#for i in range(lastidx,-1,-1):
#    #print i
#    CMS[i,2] = -CMS[i,0] - abs(CMS[i+1,2])
#    #print ATLAS[i,3] 
#    
# 
    
#ATLAS[0,2] = ATLAS[0,0]
#for i in range(1,len(ATLAS)):
#    ATLAS[i,2] = ATLAS[i,0] + ATLAS[i-1,2]    
    
    
    
#CMS[0,2] = CMS[0,0]
#for i in range(1,len(CMS)):
#    CMS[i,2] = CMS[i,0] + CMS[i-1,2]
#    
    
    
import pandas as pd



def readLumi(filename):
    data = pd.read_csv(filename)

    lumi = np.zeros([len(data),3])
        
    if os.path.isfile('datalumi.npy'):
        lumi = np.load('datalumi.npy')
        return lumi

    else:
    
        for i in range(len(data)):
        
            time = data.time
        #    for i in range(int(0*len(thefile)),len(thefile)):
                #year, month
            instant = datetime.datetime( int(time[i].split('-')[0].strip()), int(time[i].split('-')[1].strip()), int(time[i].split('-')[2][0:2]), int(time[i].split('-')[2].split()[1][0:2]), int(time[i].split('-')[2].split()[1].split(':')[1]), int(time[i].split('-')[2].split()[1].split(':')[2][0:2]))
        #                print instant
            timedifference = instant - LS2
            timeindays = timedifference.total_seconds()/(60*60*24)
            lumi[i,0] = timeindays
            lumi[i,1] = data.ATLAS[i]
            lumi[i,2] = data.CMS[i]
        #                print 'file ' + str(j) + '. Seconds ' + str(amountOfSeconds) + '. value ' + str(thefile.Value[i] )
        #        assert dataPMI[1200,1,2] != dataPMI[1200,1,3]
        np.save('dataLumi', lumi)
        return lumi
    #        print dataPMI


filename = 'LHCluminosity.csv'
lumi = readLumi(filename)



##end2010 = datetime.datetime(2010,10,11,00,00,00)
#end2011 = datetime.datetime(2011,10,30,9,57,00)
#end2012 = datetime.datetime(2012,12,05,20,53,00)
#end2015 = datetime.datetime(2015,11,02,17,20,00)
#end2016 = datetime.datetime(2016,10,26,07,49,00)
#end2017 = datetime.datetime(2017,11,9,12,02,00)
#end2018 = LS2 #datetime.datetime(2018,10,27,00,00,00)
#end2018a = datetime.datetime(2018,06,11,23,39,22)   
#end2018b = datetime.datetime(2018,07,22,18,22,43) 
#end2018c = datetime.datetime(2018,8,31,03,39,46)
#end2018d = datetime.datetime(2018,9,10,03,18,45)
#
#



end2011 = datetime.datetime(2011,10,30,9,57,00)
end2012 = datetime.datetime(2012,12,16,11,58,00)
end2015 = datetime.datetime(2015,11,21,19,22,00)
end2016 = datetime.datetime(2016,10,26,07,49,00)
end2017 = datetime.datetime(2017,11,26,00,29,00)
end2018 = LS2 #datetime.datetime(2018,10,27,00,00,00)
end2018a = datetime.datetime(2018,06,11,23,39,22)   
end2018b = datetime.datetime(2018,07,22,18,22,43) 
end2018c = datetime.datetime(2018,8,31,03,39,46)
end2018d = datetime.datetime(2018,9,10,03,18,45)

start2011 = datetime.datetime(2011,3,13,13,35,9)
start2012 = datetime.datetime(2012,4,6,23,15,36)
start2015 = datetime.datetime(2015,6,5,23,17,23)
start2016 = datetime.datetime(2016,4,22,22,38,37)
start2017 = datetime.datetime(2017,5,23,14,45,27)






datesAtlas = []
#datesAtlas.append(end2017)
#datesAtlas.append(end2016)
#datesAtlas.append(end2015)
#datesAtlas.append(end2012)
#datesAtlas.append(end2011)
datesAtlas.append(end2018d)
datesAtlas.append(end2018b)
datesAtlas.append(end2018a)
datesAtlas.append(end2017)
datesAtlas.append(end2016)
datesAtlas.append(end2015)
datesAtlas.append(end2012)
datesAtlas.append(end2011)


datesCMS = []
datesCMS.append(end2018d)
#datesCMS.append(end2018c)
datesCMS.append(end2018b)
datesCMS.append(end2018a)
datesCMS.append(end2017)
datesCMS.append(end2016)
datesCMS.append(end2015)
datesCMS.append(end2012)
datesCMS.append(end2011)


def sinceLS2(instant):
    return (instant -LS2).total_seconds()/(60*60*24)

#------------------------------------------------------------------------------------------------------------

ATLASprev = ATLAS


ATLAS = ATLAS[0:-12,0:]

#for i in range(len(newATLAS)-2,0,-1):
#    if newATLAS[i,1] == 0:
#        instance = datesAtlas.pop(0)
#        timediff = (LS2 - instance).total_seconds() - sum(newATLAS[i:,0])
#        print str(timediff)
#        
#        #timediff = (LS2 - datesAtlas.pop(0)).total_seconds() - sum(newATLAS[i:,0])
#        newATLAS[i,0] = timediff
#        
#    else:
#        newATLAS[i,0] = (60*60*24)*ATLAS[i,0]
#    
#newATLAS[0:,0] = newATLAS[0:,0]/(60*60*24)
#
#newATLAS = calcTimeline(newATLAS)
#


#CMS[0:,0] = CMS[0:,0]/(60*60*24)


from scipy.interpolate import interp1d
x = lumi[0:,0]
yATLAS = lumi[0:,1]
f = interp1d(x,yATLAS)






xsec = 72E-3 #mbar



#2011
#start2011 = datetime.datetime(2011,3,13,13,35,9)
timediff = (end2011 - start2011).total_seconds() 
lumidiff = f(sinceLS2(end2011)) - f(sinceLS2(start2011)) #picobar
collisions = 1e12*lumidiff*xsec
newrow = [timediff/(60*60*24),collisions/timediff,0]
ATLAS = np.vstack([ATLAS,newrow])
ATLAS = np.vstack([ATLAS,[0,0,0]])

lumiCollisions = 1e12*f(-2500)*xsec


xsec = 75E-3 #mbar

#2012
#start2012 = datetime.datetime(2012,4,6,23,15,36)
timediff = (end2012 - start2012).total_seconds() 
lumidiff = f(sinceLS2(end2012)) - f(sinceLS2(start2012)) #picobar
collisions = 1e12*lumidiff*xsec
newrow = [timediff/(60*60*24),collisions/timediff,0]
ATLAS = np.vstack([ATLAS,newrow])
ATLAS = np.vstack([ATLAS,[0,0,0]])

lumiCollisions = lumiCollisions + 1e12*(f(-2000) - f(-2500))*xsec

xsec = 80E-3 #mbar

#2015
#start2015 = datetime.datetime(2015,6,5,23,17,23)
timediff = (end2015 - start2015).total_seconds() 
lumidiff = f(sinceLS2(end2015)) - f(sinceLS2(start2015)) #picobar
collisions = 1e12*lumidiff*xsec
newrow = [timediff/(60*60*24),collisions/timediff,0]
ATLAS = np.vstack([ATLAS,newrow])
ATLAS = np.vstack([ATLAS,[0,0,0]])




#2016
#start2016 = datetime.datetime(2016,5,8,12,04,37)
timediff = (end2016 - start2016).total_seconds() 
lumidiff = f(sinceLS2(end2016)) - f(sinceLS2(start2016)) #picobar
collisions = 1e12*lumidiff*xsec
newrow = [timediff/(60*60*24),collisions/timediff,0]
ATLAS = np.vstack([ATLAS,newrow])
ATLAS = np.vstack([ATLAS,[0,0,0]])



#2017
#start2017 = datetime.datetime(2017,5,23,14,45,27)
timediff = (end2017 - start2017).total_seconds() 
lumidiff = f(sinceLS2(end2017)) - f(sinceLS2(start2017)) #picobar
collisions = 1e12*lumidiff*xsec
newrow = [timediff/(60*60*24),collisions/timediff,0]
ATLAS = np.vstack([ATLAS,newrow])
ATLAS = np.vstack([ATLAS,[0,0,0]])


#collisions2017
#ATLAS[9,1]*ATLAS[9,0]





#T1
T1end = datetime.datetime(2018,6,11,23,39,11)
T1start = datetime.datetime(2018,4,17,11,00,23)
timediff = (T1end - T1start).total_seconds() 
lumidiff = f(sinceLS2(T1end)) - f(sinceLS2(T1start)) #picobar
collisions = 1e12*lumidiff*xsec
newrow = [timediff/(60*60*24),collisions/timediff,0]
ATLAS = np.vstack([ATLAS,newrow])
ATLAS = np.vstack([ATLAS,[0,0,0]])

#T2
T2end =  datetime.datetime(2018,7,22,18,22,43)
T2start = datetime.datetime(2018,6,26,19,22,10)
timediff = (T2end - T2start).total_seconds() 
lumidiff = f(sinceLS2(T2end)) - f(sinceLS2(T2start)) #picobar
collisions = 1e12*lumidiff*xsec
newrow = [timediff/(60*60*24),collisions/timediff,0]
ATLAS = np.vstack([ATLAS,newrow])
ATLAS = np.vstack([ATLAS,[0,0,0]])



#T3
T3end = datetime.datetime(2018,9,10,03,18,45)
T3start = datetime.datetime(2018,8,1,2,8,37)
timediff = (T3end - T3start).total_seconds() 
lumidiff = f(sinceLS2(T3end)) - f(sinceLS2(T3start)) #picobar
collisions = 1e12*lumidiff*xsec
newrow = [timediff/(60*60*24),collisions/timediff,0]
ATLAS = np.vstack([ATLAS,newrow])
ATLAS = np.vstack([ATLAS,[0,0,0]])

#T4
T4end = LS2
T4start = datetime.datetime(2018,9,23,17,55,33)
timediff = (T4end - T4start).total_seconds() 
lumidiff = f(sinceLS2(T4end)) - f(sinceLS2(T4start)) #picobar
collisions = 1e12*lumidiff*xsec
newrow = [timediff/(60*60*24),collisions/timediff,0]
ATLAS = np.vstack([ATLAS,newrow])
ATLAS = np.vstack([ATLAS,[0,0,0]])




#lumiCollisions = lumiCollisions + 1e12*(f(0) - f(-2000))*xsec




lumiCollisionsATLAS = lumiCollisions +  1e12*(f(0) - f(-2000))*xsec
#------------------------------------------------------------------------------------------------------------


CMSprev = CMS

CMS = CMS[0:-18,0:]
CMS = np.vstack([CMS,[0,0,0]])
#for i in range(len(newATLAS)-2,0,-1):
#    if newATLAS[i,1] == 0:
#        instance = datesAtlas.pop(0)
#        timediff = (LS2 - instance).total_seconds() - sum(newATLAS[i:,0])
#        print str(timediff)
#        
#        #timediff = (LS2 - datesAtlas.pop(0)).total_seconds() - sum(newATLAS[i:,0])
#        newATLAS[i,0] = timediff
#        
#    else:
#        newATLAS[i,0] = (60*60*24)*ATLAS[i,0]
#    
#newATLAS[0:,0] = newATLAS[0:,0]/(60*60*24)
#
#newATLAS = calcTimeline(newATLAS)
#


#CMS[0:,0] = CMS[0:,0]/(60*60*24)


x = lumi[0:,0]
yCMS = lumi[0:,2]
f = interp1d(x,yCMS)






xsec = 72E-3 #mbar

#2011
timediff = (end2011 - start2011).total_seconds() 
lumidiff = f(sinceLS2(end2011)) - f(sinceLS2(start2011)) #picobar
collisions = 1e12*lumidiff*xsec
newrow = [timediff/(60*60*24),collisions/timediff,0]
CMS = np.vstack([CMS,newrow])
CMS = np.vstack([CMS,[0,0,0]])

lumiCollisions = 1e12*f(-2500)*xsec


xsec = 75E-3 #mbar
#2012
timediff = (end2012 - start2012).total_seconds() 
lumidiff = f(sinceLS2(end2012)) - f(sinceLS2(start2012)) #picobar
collisions = 1e12*lumidiff*xsec
newrow = [timediff/(60*60*24),collisions/timediff,0]
CMS = np.vstack([CMS,newrow])
CMS = np.vstack([CMS,[0,0,0]])

lumiCollisions = lumiCollisions + 1e12*(f(-2000) - f(-2500))*xsec

xsec = 80E-3 #mbar

#2015
timediff = (end2015 - start2015).total_seconds() 
lumidiff = f(sinceLS2(end2015)) - f(sinceLS2(start2015)) #picobar
collisions = 1e12*lumidiff*xsec
newrow = [timediff/(60*60*24),collisions/timediff,0]
CMS = np.vstack([CMS,newrow])
CMS = np.vstack([CMS,[0,0,0]])




#2016
timediff = (end2016 - start2016).total_seconds() 
lumidiff = f(sinceLS2(end2016)) - f(sinceLS2(start2016)) #picobar
collisions = 1e12*lumidiff*xsec
newrow = [timediff/(60*60*24),collisions/timediff,0]
CMS = np.vstack([CMS,newrow])
CMS = np.vstack([CMS,[0,0,0]])



#2017
timediff = (end2017 - start2017).total_seconds() 
lumidiff = f(sinceLS2(end2017)) - f(sinceLS2(start2017)) #picobar
collisions = 1e12*lumidiff*xsec
newrow = [timediff/(60*60*24),collisions/timediff,0]
CMS = np.vstack([CMS,newrow])
CMS = np.vstack([CMS,[0,0,0]])




#T1
timediff = (T1end - T1start).total_seconds() 
lumidiff = f(sinceLS2(T1end)) - f(sinceLS2(T1start)) #picobar
collisions = 1e12*lumidiff*xsec
newrow = [timediff/(60*60*24),collisions/timediff,0]
CMS = np.vstack([CMS,newrow])
CMS = np.vstack([CMS,[0,0,0]])

#T2
timediff = (T2end - T2start).total_seconds() 
lumidiff = f(sinceLS2(T2end)) - f(sinceLS2(T2start)) #picobar
collisions = 1e12*lumidiff*xsec
newrow = [timediff/(60*60*24),collisions/timediff,0]
CMS = np.vstack([CMS,newrow])
CMS = np.vstack([CMS,[0,0,0]])



#T3
timediff = (T3end - T3start).total_seconds() 
lumidiff = f(sinceLS2(T3end)) - f(sinceLS2(T3start)) #picobar
collisions = 1e12*lumidiff*xsec
newrow = [timediff/(60*60*24),collisions/timediff,0]
CMS = np.vstack([CMS,newrow])
CMS = np.vstack([CMS,[0,0,0]])

#T4
timediff = (T4end - T4start).total_seconds() 
lumidiff = f(sinceLS2(T4end)) - f(sinceLS2(T4start)) #picobar
collisions = 1e12*lumidiff*xsec
newrow = [timediff/(60*60*24),collisions/timediff,0]
CMS = np.vstack([CMS,newrow])
CMS = np.vstack([CMS,[0,0,0]])





lumiCollisionsCMS = lumiCollisions +  1e12*(f(0) - f(-2000))*xsec



#------------------------------------------------------------------------------------------------------------





newATLAS = np.zeros(ATLAS.shape)
newATLAS[0:,1] = ATLAS[0:,1]

newCMS = np.zeros(CMS.shape)
newCMS[0:,1] = CMS[0:,1]






def calcnewprofile(experiment,dates,oldDataExperiment):
    for i in range(len(experiment)-2,0,-1):
        if experiment[i,1] == 0:
            instance = dates.pop(0)
            #print instance
            timediff = (LS2 - instance).total_seconds() - sum(experiment[i:,0])
            #print str(timediff)
            
            #timediff = (LS2 - datesAtlas.pop(0)).total_seconds() - sum(newATLAS[i:,0])
            experiment[i,0] = timediff
            
        else:
            
            experiment[i,0] = (60*60*24)*oldDataExperiment[i,0]
    
    #print experiment[0:,0]/(60*60*24)
    experiment[0:,0] = experiment[0:,0]/(60*60*24)
    
    experiment = calcTimeline(experiment)
    return experiment




newAtlas = calcnewprofile(newATLAS, datesAtlas, ATLAS)
newCMS = calcnewprofile(newCMS, datesCMS, CMS)




## 2017
#lumistart = 
#T4end = LS2
#T4start = datetime.datetime(2018,9,23,17,55,33)
#timediff = (T4end - T4start).total_seconds() 
#lumidiff = f(sinceLS2(T4end)) - f(sinceLS2(T4start)) #picobar
#collisions = 10e9*lumidiff*xsec/timediff






import matplotlib.pyplot as plt


collisionsAtlas = sum(ATLAS[0:,1]*ATLAS[0:,0])*24*60*60

collisionsCMS = sum(CMS[0:,1]*CMS[0:,0])*24*60*60


prevcollisionsAtlas = sum(ATLASprev[0:,1]*ATLASprev[0:,0])*24*60*60


prevcollisionsCMS = sum(CMSprev[0:,1]*CMSprev[0:,0])*24*60*60




fig = plt.figure()



ax = fig.add_subplot(211)

ax.step(ATLASprev[0:,2], ATLASprev[0:,1], label = 'ATLAS, #Collisons= ' + str(prevcollisionsAtlas),where='post')

ax.step(CMSprev[0:,2], CMSprev[0:,1], label = 'CMS, #Collisons= ' + str(prevcollisionsCMS),where='post')

         


plt.axvline(x=-365*1 - newyearsLS2difference, color = 'k', linestyle = '--', label = 'Year shift')
plt.axvline(x=-365*2 - newyearsLS2difference, color = 'k', linestyle = '--')
plt.axvline(x=-365*3 - newyearsLS2difference, color = 'k', linestyle = '--')
plt.axvline(x=-365*4 - newyearsLS2difference, color = 'k', linestyle = '--')
plt.axvline(x=-365*5 - newyearsLS2difference, color = 'k', linestyle = '--')
plt.axvline(x=-365*6 - newyearsLS2difference, color = 'k', linestyle = '--')
plt.axvline(x=-365*7 - newyearsLS2difference, color = 'k', linestyle = '--')
plt.axvline(x=-365*8 - newyearsLS2difference, color = 'k', linestyle = '--')
#plt.axvline(x=newyearsLS2difference, color = 'r', linestyle = ':', linewidth = 2, label = 'LS2 starts')

plt.legend(loc = 2)


#ax.set_ylim(0,1e9)

#plt.xlabel('Time [days until LS2]',  fontsize = 16)
ax.set_ylabel('Beam intensity [collisions/s]',  fontsize = 16)

ax2 = ax.twinx()

#ax2 = fig.add_subplot(111)

ax2.plot(lumi[0:,0],lumi[0:,1], label = 'ATLAS', linestyle = '--')

ax2.plot(lumi[0:,0],lumi[0:,2], label = 'CMS', linestyle = '--')

#ax2.legend()

ax2.set_ylim(0,194000)
#ax2.set_xlim(-240,10)



ax2.set_ylabel('Integrated luminosity [pb-1]',  fontsize = 16)

plt.title('Old Profile', fontsize = 20)






ax = fig.add_subplot(212)

ax.step(newATLAS[0:,2], newATLAS[0:,1], label = 'ATLAS, #Collisons= ' + str(collisionsAtlas),where='post')

ax.step(newCMS[0:,2], newCMS[0:,1], label = 'CMS, #Collisons= ' + str(collisionsCMS),where='post')

         


plt.axvline(x=-365*1 - newyearsLS2difference, color = 'k', linestyle = '--', label = 'Year shift')
plt.axvline(x=-365*2 - newyearsLS2difference, color = 'k', linestyle = '--')
plt.axvline(x=-365*3 - newyearsLS2difference, color = 'k', linestyle = '--')
plt.axvline(x=-365*4 - newyearsLS2difference, color = 'k', linestyle = '--')
plt.axvline(x=-365*5 - newyearsLS2difference, color = 'k', linestyle = '--')
plt.axvline(x=-365*6 - newyearsLS2difference, color = 'k', linestyle = '--')
plt.axvline(x=-365*7 - newyearsLS2difference, color = 'k', linestyle = '--')
plt.axvline(x=-365*8 - newyearsLS2difference, color = 'k', linestyle = '--')
#plt.axvline(x=newyearsLS2difference, color = 'r', linestyle = ':', linewidth = 2, label = 'LS2 starts')

plt.legend(loc = 2)


#ax.set_ylim(0,1e9)

plt.xlabel('Time [days until LS2]',  fontsize = 16)
ax.set_ylabel('Beam intensity [collisions/s]',  fontsize = 16)

ax2 = ax.twinx()

#ax2 = fig.add_subplot(111)

ax2.plot(lumi[0:,0],lumi[0:,1], label = 'ATLAS', linestyle = '--')

ax2.plot(lumi[0:,0],lumi[0:,2], label = 'CMS', linestyle = '--')

#ax2.legend()

ax2.set_ylim(0,194000)
#ax.set_xlim(-240,10)


ax2.set_ylabel('Integrated luminosity [pb-1]',  fontsize = 16)

plt.title('New Profile', fontsize = 20)




#atlasLumi = lumi





plt.suptitle('ATLAS/CMS irradiation profiles', fontsize = 22)


plt.show()












print 'ATLAS #Collisions/Lumi collisions = '
print str(collisionsAtlas/lumiCollisionsATLAS)
print ' ' 
print 'CMS #Collisions/Lumi collisions = '
print str(collisionsCMS/lumiCollisionsCMS)
print ' ' 


print 'Total ATLAS collisions/Total CMS collisions = '
print str(collisionsAtlas/collisionsCMS)
print ' '
print ' '
print '2018 collisions ATLAS new/ATLAS old: '
print sum(newATLAS[-8:,1]*newATLAS[-8:,0]*(60*60*24))/(ATLASprev[11,1]*ATLASprev[11,0]*(60*60*24))
print ' '
print '2017 collisions ATLAS new/ATLAS old: '
print (newATLAS[-10,1]*newATLAS[-10,0]*(60*60*24))/(ATLASprev[9,1]*ATLASprev[9,0]*(60*60*24))
print ' '
print '2016 collisions ATLAS new/ATLAS old: '
print (newATLAS[-12,1]*newATLAS[-12,0]*(60*60*24))/(ATLASprev[7,1]*ATLASprev[7,0]*(60*60*24))
#print ' '
#print 'Collisions ATLAS/CMS 2017: '
#print (newATLAS[9,1]*newATLAS[9,0])/(newCMS[7,1]*newCMS[7,0])
#print ' '
#print 'Collisions ATLAS/CMS 2016: '
#print (newATLAS[7,1]*newATLAS[7,0])/(newCMS[5,1]*newCMS[5,0])
#








#write

def writeProfile(experiment, outname):

    f = open(outname, 'wb')
    f.write('* ..+....1....+....2....+....3....+....4....+....5....+....6....+....7....+....8\n')
    now = datetime.datetime.now()
    f.write('* Profile written by irradiation profile script on '+str(now) + '\n')
    for i in range(len(experiment)):
        if experiment[i,0] == 0:
            pass
        else:
            string = 'IRRPROFI  '
            val1 = int(round(experiment[i,0]*24*60*60))
            for j in range(10 - len(str(val1))):
                string = string + ' ' 
            string = string + str(val1)
            val2 = int(round(experiment[i,1]))
            
            for j in range(10 - len(str(val2))):
                string = string + ' '   
            string = string + str(val2)
            f.write(string + '\n')
                
                

            #f.write(str(int(round(experiment[i,0]*24*60*60))) + ' ' + str(int(round(experiment[i,1]))) + '\n')
            
    f.close()


#writeProfile(newAtlas, 'AtlasProfile.inp')
#writeProfile(newCMS, 'CMSprofile.inp')






fig = plt.figure()



ax = fig.add_subplot(111)

ax.step(ATLASprev[0:,2], ATLASprev[0:,1], label = 'Old profile, #Collisons= ' + str(prevcollisionsAtlas),where='post')

#ax.step(CMSprev[0:,2], CMSprev[0:,1], label = 'CMS, #Collisons= ' + str(prevcollisionsCMS),where='post')

ax.step(newATLAS[0:,2], newATLAS[0:,1], label = 'New Profile, #Collisons= ' + str(collisionsAtlas),where='post')    


plt.axvline(x=-365*1 - newyearsLS2difference, color = 'k', linestyle = '--', label = 'Year shift')
plt.axvline(x=-365*2 - newyearsLS2difference, color = 'k', linestyle = '--')
plt.axvline(x=-365*3 - newyearsLS2difference, color = 'k', linestyle = '--')
plt.axvline(x=-365*4 - newyearsLS2difference, color = 'k', linestyle = '--')
plt.axvline(x=-365*5 - newyearsLS2difference, color = 'k', linestyle = '--')
plt.axvline(x=-365*6 - newyearsLS2difference, color = 'k', linestyle = '--')
plt.axvline(x=-365*7 - newyearsLS2difference, color = 'k', linestyle = '--')
plt.axvline(x=-365*8 - newyearsLS2difference, color = 'k', linestyle = '--')
#plt.axvline(x=newyearsLS2difference, color = 'r', linestyle = ':', linewidth = 2, label = 'LS2 starts')

plt.legend(loc = 2)

plt.xlabel('Time [days until LS2]',  fontsize = 16)
        
#ax.set_ylim(0,1e9)

#plt.xlabel('Time [days until LS2]',  fontsize = 16)
ax.set_ylabel('Beam intensity [collisions/s]',  fontsize = 16)

ax2 = ax.twinx()

#ax2 = fig.add_subplot(111)

lumicolor = 'm'

ax2.plot(lumi[0:,0],lumi[0:,1], label = 'ATLAS', linestyle = '--', color = lumicolor)

#ax2.plot(lumi[0:,0],lumi[0:,2], label = 'CMS', linestyle = '--')

#ax2.legend()

ax2.set_ylim(0,194000)
#ax2.set_xlim(-240,10)



ax2.set_ylabel('Integrated luminosity [pb-1]',  fontsize = 16)

#plt.title('Old Profile', fontsize = 20)



ax2.tick_params(axis='y', colors=lumicolor)


#ax = fig.add_subplot(212)

plt.title('ATLAS irradiation profiles comparison',  fontsize = 22)


#ax.step(newCMS[0:,2], newCMS[0:,1], label = 'CMS, #Collisons= ' + str(collisionsCMS),where='post')

plt.show()        






fig = plt.figure()



ax = fig.add_subplot(111)

ax.step(ATLASprev[0:,2], ATLASprev[0:,1], label = 'Old profile, #Collisons= ' + str(prevcollisionsAtlas),where='post')

#ax.step(CMSprev[0:,2], CMSprev[0:,1], label = 'CMS, #Collisons= ' + str(prevcollisionsCMS),where='post')

ax.step(newATLAS[0:,2], newATLAS[0:,1], label = 'New Profile, #Collisons= ' + str(collisionsAtlas),where='post')    


#plt.axvline(x=-365*1 - newyearsLS2difference, color = 'k', linestyle = '--', label = 'Year shift')
plt.axvline(x=-365*2 - newyearsLS2difference, color = 'k', linestyle = '--')
plt.axvline(x=-365*3 - newyearsLS2difference, color = 'k', linestyle = '--')
plt.axvline(x=-365*4 - newyearsLS2difference, color = 'k', linestyle = '--')
plt.axvline(x=-365*5 - newyearsLS2difference, color = 'k', linestyle = '--')
plt.axvline(x=-365*6 - newyearsLS2difference, color = 'k', linestyle = '--')
plt.axvline(x=-365*7 - newyearsLS2difference, color = 'k', linestyle = '--')
plt.axvline(x=-365*8 - newyearsLS2difference, color = 'k', linestyle = '--')
#plt.axvline(x=newyearsLS2difference, color = 'r', linestyle = ':', linewidth = 2, label = 'LS2 starts')

plt.legend(loc = 2, prop={'size': 16})

plt.xlabel('Time [days until LS2]',  fontsize = 16)

ax.set_xlim(-200,0)

#plt.xlabel('Time [days until LS2]',  fontsize = 16)
ax.set_ylabel('Beam intensity [collisions/s]',  fontsize = 16)

ax2 = ax.twinx()

#ax2 = fig.add_subplot(111)

lumicolor = 'm'

ax2.plot(lumi[0:,0],lumi[0:,1], label = 'ATLAS', linestyle = '--', color = lumicolor)

#ax2.plot(lumi[0:,0],lumi[0:,2], label = 'CMS', linestyle = '--')

#ax2.legend()

ax2.set_ylim(0,194000)
#ax2.set_xlim(-240,10)



ax2.set_ylabel('Integrated luminosity [pb-1]',  fontsize = 16)

#plt.title('Old Profile', fontsize = 20)



ax2.tick_params(axis='y', colors=lumicolor)


#ax = fig.add_subplot(212)

plt.title('ATLAS irradiation profiles, Last year',  fontsize = 26)


#ax.step(newCMS[0:,2], newCMS[0:,1], label = 'CMS, #Collisons= ' + str(collisionsCMS),where='post')

plt.show()        


#
#
#
#
#fig = plt.figure()
#
#
#
#ax = fig.add_subplot(211)
#
#ax.step(ATLASprev[0:,2], ATLASprev[0:,1], label = 'ATLAS, #Collisons= ' + str(prevcollisionsAtlas),where='post')
#
#ax.step(CMSprev[0:,2], CMSprev[0:,1], label = 'CMS, #Collisons= ' + str(prevcollisionsCMS),where='post')
#
#ax.step(LHC[0:,2], LHC[0:,1], label = 'LHC',where='post')       
#
#
#plt.axvline(x=-365*1 - newyearsLS2difference, color = 'k', linestyle = '--', label = 'Year shift')
#plt.axvline(x=-365*2 - newyearsLS2difference, color = 'k', linestyle = '--')
#plt.axvline(x=-365*3 - newyearsLS2difference, color = 'k', linestyle = '--')
#plt.axvline(x=-365*4 - newyearsLS2difference, color = 'k', linestyle = '--')
#plt.axvline(x=-365*5 - newyearsLS2difference, color = 'k', linestyle = '--')
#plt.axvline(x=-365*6 - newyearsLS2difference, color = 'k', linestyle = '--')
#plt.axvline(x=-365*7 - newyearsLS2difference, color = 'k', linestyle = '--')
#plt.axvline(x=-365*8 - newyearsLS2difference, color = 'k', linestyle = '--')
##plt.axvline(x=newyearsLS2difference, color = 'r', linestyle = ':', linewidth = 2, label = 'LS2 starts')
#
#plt.legend(loc = 2)
#
#
##ax.set_ylim(0,1e9)
#
##plt.xlabel('Time [days until LS2]',  fontsize = 16)
#ax.set_ylabel('Beam intensity [collisions/s]',  fontsize = 16)
#
#ax2 = ax.twinx()
#
##ax2 = fig.add_subplot(111)
#
#ax2.plot(lumi[0:,0],lumi[0:,1], label = 'ATLAS', linestyle = '--')
#
#ax2.plot(lumi[0:,0],lumi[0:,2], label = 'CMS', linestyle = '--')
#
##ax2.legend()
#
#ax2.set_ylim(0,194000)
##ax2.set_xlim(-240,10)
#
#
#
#ax2.set_ylabel('Integrated luminosity [pb-1]',  fontsize = 16)
#
#plt.title('Old Profile', fontsize = 20)
#
#
#
#
#
#
#ax = fig.add_subplot(212)
#
#ax.step(newATLAS[0:,2], newATLAS[0:,1], label = 'ATLAS, #Collisons= ' + str(collisionsAtlas),where='post')
#
#ax.step(newCMS[0:,2], newCMS[0:,1], label = 'CMS, #Collisons= ' + str(collisionsCMS),where='post')
#ax.step(LHC[0:,2], LHC[0:,1], label = 'LHC',where='post')       
#         
#
#
#plt.axvline(x=-365*1 - newyearsLS2difference, color = 'k', linestyle = '--', label = 'Year shift')
#plt.axvline(x=-365*2 - newyearsLS2difference, color = 'k', linestyle = '--')
#plt.axvline(x=-365*3 - newyearsLS2difference, color = 'k', linestyle = '--')
#plt.axvline(x=-365*4 - newyearsLS2difference, color = 'k', linestyle = '--')
#plt.axvline(x=-365*5 - newyearsLS2difference, color = 'k', linestyle = '--')
#plt.axvline(x=-365*6 - newyearsLS2difference, color = 'k', linestyle = '--')
#plt.axvline(x=-365*7 - newyearsLS2difference, color = 'k', linestyle = '--')
#plt.axvline(x=-365*8 - newyearsLS2difference, color = 'k', linestyle = '--')
##plt.axvline(x=newyearsLS2difference, color = 'r', linestyle = ':', linewidth = 2, label = 'LS2 starts')
#
#plt.legend(loc = 2)
#
#
##ax.set_ylim(0,1e9)
#
#plt.xlabel('Time [days until LS2]',  fontsize = 16)
#ax.set_ylabel('Beam intensity [collisions/s]',  fontsize = 16)
#
#ax2 = ax.twinx()
#
##ax2 = fig.add_subplot(111)
#
#ax2.plot(lumi[0:,0],lumi[0:,1], label = 'ATLAS', linestyle = '--')
#
#ax2.plot(lumi[0:,0],lumi[0:,2], label = 'CMS', linestyle = '--')
#
##ax2.legend()
#
#ax2.set_ylim(0,194000)
##ax.set_xlim(-240,10)
#
#
#ax2.set_ylabel('Integrated luminosity [pb-1]',  fontsize = 16)
#
#plt.title('New Profile', fontsize = 20)
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
#plt.suptitle('ATLAS/CMS irradiation profiles', fontsize = 22)
#
#
#plt.show()
#
#
#







