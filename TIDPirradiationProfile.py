# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 16:15:12 2018

@author: cbjorkma
"""

#TIDP irradiation profile


# -*- coding: utf-8 -*-
"""
Created on Fri Oct 05 15:23:56 2018

@author: cbjorkma
"""

#LHCIRRADIATIONPROFILE


import os

path = '//cern.ch/dfs/Users/c/cbjorkma/Documents/Scrapers/Profiles'

os.chdir(path)


import numpy as np



def readData(filename):
    data = np.loadtxt(filename)
    out = np.zeros([data.shape[0]+2,3])
    out[1:len(out)-1,0:2] = data
    out[0:,0] = out[0:,0]/(60*60*24)
    return out;
    
    
    
cons = readData('TIDPconservative.txt')
avg = readData('TIDPavg.txt')
old = readData('TIDPold.txt')   
    


def calcTimeline(experiment):

    lastidx = len(experiment)-3
    
    experiment[len(experiment)-2,2] = - experiment[len(experiment)-2,0]
    for i in range(lastidx,-1,-1):
        #print i
        experiment[i,2] = -experiment[i,0] - abs(experiment[i+1,2])
    return experiment;
        #print ATLAS[i,3] 
        

cons = calcTimeline(cons)
avg = calcTimeline(avg)
old = calcTimeline(old)    
    
    
#consData = np.loadtxt('TIDPconservative.txt')
#avgData = np.loadtxt('TIDPavg.txt')
#oldData = np.loadtxt('TIDPold.txt')
#
#ATLAS = np.zeros([ATLASdata.shape[0]+2,3])
#CMS = np.zeros([CMSdata.shape[0]+2,3])
#
#
#
##ATLASdata = np.loadtxt('ATLASirradiatonprofile2.txt')
##CMSdata = np.loadtxt('CMSirradiatonprofile.txt')
#
#ATLAS = np.zeros([ATLASdata.shape[0]+2,3])
#CMS = np.zeros([CMSdata.shape[0]+2,3])
#
#ATLAS[1:len(ATLAS)-1,0:2] = ATLASdata
#CMS[1:len(CMS)-1,0:2] = CMSdata
#
#ATLAS[0:,0] = ATLAS[0:,0]/(60*60*24)
#CMS[0:,0] = CMS[0:,0]/(60*60*24)


#import datetime
#
##protonEnd = datetime.datetime(2017,10,23,06,00,00)
##ionEnd = datetime.datetime(2017,12,18,06,00,00)
#
#LS2 = datetime.datetime(2018,10,27,00,00,00) #t0
#newyear2018 = datetime.datetime(2018,12,31,23,59,59)
#
##instant = datetime.datetime( time[i].year, time[i].month, time[i].day, time[i].hour, time[i].minute, time[i].second)
#
#timedifference = LS2 - newyear2018
#newyearsLS2difference = timedifference.total_seconds()/(60*60*24)
#
#print newyearsLS2difference
#    



    
    
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
#    
#    
#import pandas as pd
#
#
#
#def readLumi(filename):
#    data = pd.read_csv(filename)
#
#    lumi = np.zeros([len(data),3])
#        
#    if os.path.isfile('datalumi.npy'):
#        lumi = np.load('datalumi.npy')
#        return lumi
#
#    else:
#    
#        for i in range(len(data)):
#        
#            time = data.time
#        #    for i in range(int(0*len(thefile)),len(thefile)):
#                #year, month
#            instant = datetime.datetime( int(time[i].split('-')[0].strip()), int(time[i].split('-')[1].strip()), int(time[i].split('-')[2][0:2]), int(time[i].split('-')[2].split()[1][0:2]), int(time[i].split('-')[2].split()[1].split(':')[1]), int(time[i].split('-')[2].split()[1].split(':')[2][0:2]))
#        #                print instant
#            timedifference = instant - LS2
#            timeindays = timedifference.total_seconds()/(60*60*24)
#            lumi[i,0] = timeindays
#            lumi[i,1] = data.ATLAS[i]
#            lumi[i,2] = data.CMS[i]
#        #                print 'file ' + str(j) + '. Seconds ' + str(amountOfSeconds) + '. value ' + str(thefile.Value[i] )
#        #        assert dataPMI[1200,1,2] != dataPMI[1200,1,3]
#        np.save('dataLumi', lumi)
#        return lumi
#    #        print dataPMI
#
#
#filename = 'LHCluminosity.csv'
#lumi = readLumi(filename)
#
#
#
##end2010 = datetime.datetime(2010,10,11,00,00,00)
#end2011 = datetime.datetime(2011,10,30,9,57,00)
#end2012 = datetime.datetime(2012,12,05,20,53,00)
#end2015 = datetime.datetime(2015,11,02,17,20,00)
#end2016 = datetime.datetime(2016,10,26,07,49,00)
#end2017 = datetime.datetime(2017,11,9,12,02,00)
#end2018 = datetime.datetime(2018,10,27,00,00,00)
#end2018a = datetime.datetime(2018,06,11,23,39,22)   
#end2018b = datetime.datetime(2018,07,22,18,22,43) 
#end2018c = datetime.datetime(2018,8,31,03,39,46)
#end2018d = datetime.datetime(2018,9,10,03,18,45)
#
#
#
#
#
#datesAtlas = []
##datesAtlas.append(end2018)
#datesAtlas.append(end2017)
#datesAtlas.append(end2016)
#datesAtlas.append(end2015)
#datesAtlas.append(end2012)
#datesAtlas.append(end2011)
#
#
#datesCMS = []
#datesCMS.append(end2018d)
##datesCMS.append(end2018c)
#datesCMS.append(end2018b)
#datesCMS.append(end2018a)
#datesCMS.append(end2017)
#datesCMS.append(end2016)
#datesCMS.append(end2015)
#datesCMS.append(end2012)
#
#
#
#newATLAS = np.zeros(ATLAS.shape)
#newATLAS[0:,1] = ATLAS[0:,1]
#
#newCMS = np.zeros(CMS.shape)
#newCMS[0:,1] = CMS[0:,1]


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


#def calcnewprofile(experiment,dates,oldDataExperiment):
#    for i in range(len(experiment)-2,0,-1):
#        if experiment[i,1] == 0:
#            instance = dates.pop(0)
#            print instance
#            timediff = (LS2 - instance).total_seconds() - sum(experiment[i:,0])
#            #print str(timediff)
#            
#            #timediff = (LS2 - datesAtlas.pop(0)).total_seconds() - sum(newATLAS[i:,0])
#            experiment[i,0] = timediff
#            
#        else:
#            experiment[i,0] = (60*60*24)*oldDataExperiment[i,0]
#        
#    experiment[0:,0] = experiment[0:,0]/(60*60*24)
#    
#    experiment = calcTimeline(experiment)
#    return experiment
#
#newAtlas = calcnewprofile(newATLAS, datesAtlas, ATLAS)
#newCMS = calcnewprofile(newCMS, datesCMS, CMS)
#
#















import matplotlib.pyplot as plt


dumpedCons = sum(cons[0:,1]*cons[0:,0])
dumpedAvg = sum(avg[0:,1]*avg[0:,0])
dumpedOld = sum(old[0:,1]*old[0:,0])

#collisionsCMS = sum(CMS[0:,1]*CMS[0:,0])

#print 'Conservative/Averaged = ' + str(dumpedCons/dumpedAvg)
#print 'Conservative/Previous profile = ' + str(dumpedCons/dumpedOld)





fig = plt.figure()



ax = fig.add_subplot(111)

ax.step(cons[0:,0], cons[0:,1], label = 'Conservative',where='post', linestyle = '--', linewidth = 2)

ax.step(avg[0:,0], avg[0:,1], label = 'Averaged',where='post', linestyle = '-.')

ax.step(old[0:,0], old[0:,1], label = 'Previous profile',where='post', linestyle = ':')

plt.grid(linewidth = 0.2)

#ax.step(CMS[0:,2], CMS[0:,1], label = 'CMS, #Collisons= ' + str(collisionsCMS),where='post')

         


#plt.axvline(x=-365*1 - newyearsLS2difference, color = 'k', linestyle = '--', label = 'Year shift')
#plt.axvline(x=-365*2 - newyearsLS2difference, color = 'k', linestyle = '--')
#plt.axvline(x=-365*3 - newyearsLS2difference, color = 'k', linestyle = '--')
#plt.axvline(x=-365*4 - newyearsLS2difference, color = 'k', linestyle = '--')
#plt.axvline(x=-365*5 - newyearsLS2difference, color = 'k', linestyle = '--')
#plt.axvline(x=-365*6 - newyearsLS2difference, color = 'k', linestyle = '--')
#plt.axvline(x=-365*7 - newyearsLS2difference, color = 'k', linestyle = '--')
#plt.axvline(x=-365*8 - newyearsLS2difference, color = 'k', linestyle = '--')
#plt.axvline(x=newyearsLS2difference, color = 'r', linestyle = ':', linewidth = 2, label = 'LS2 starts')

plt.legend(loc = 2)


#ax.set_ylim(0,1e9)

plt.xlabel('Time [days]',  fontsize = 16)
ax.set_xscale("log", nonposx='clip')
ax.set_ylabel('Beam intensity [particles/s]',  fontsize = 16)
plt.gca().invert_xaxis()
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
#ax2.set_ylim(0,187000)
#
#
#
#ax2.set_ylabel('Integrated luminocity [pb-1]',  fontsize = 16)
#
#plt.title('Old Profile', fontsize = 20)




#
#
#ax = fig.add_subplot(212)
#
#ax.step(newATLAS[0:,2], newATLAS[0:,1], label = 'ATLAS, #Collisons= ' + str(collisionsAtlas),where='post')
#
#ax.step(newCMS[0:,2], newCMS[0:,1], label = 'CMS, #Collisons= ' + str(collisionsCMS),where='post')
#
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
#ax2.set_ylim(0,187000)
#
#
#
#ax2.set_ylabel('Integrated luminocity [pb-1]',  fontsize = 16)
#
#plt.title('New Profile', fontsize = 20)












plt.suptitle('TIDP irradiation profiles', fontsize = 22)


plt.show()

#print 'Total ATLAS collisions/Total CMS collisions = '
#print str(collisionsAtlas/collisionsCMS)
#print ' '
#print 'Collisions ATLAS/CMS 2018: '
#print ATLAS[-2,1]/sum(CMS[8:,1])
