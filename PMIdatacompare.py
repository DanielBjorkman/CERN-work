# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 10:29:07 2018

@author: cbjorkma
"""
#PMI data compare
import os
import numpy as np
import pandas as pd
import datetime #, timedelta
import matplotlib.pyplot as plt
import math


path = '//rpclustersrv1/cbjorkma/LSS2/ActivationDetectors' 

os.chdir(path)

#protonEnd = '2017-11-23 06:00:00.940000'
protonEnd = datetime.datetime(2017,10,23,06,00,00)
ionEnd = datetime.datetime(2017,12,18,06,00,00)
end2016 = datetime.datetime(2015,11,16,06,00,00)
end2017 = datetime.datetime(2016,11,14,06,00,00)

#
files = os.listdir(path)
files = sorted(files)
files = filter(lambda x: x[4:7].isdigit() , files)  
files = filter(lambda x: not x[0] == '.' , files)  
filenames = files
thefile = pd.read_excel(files[0])

data = np.zeros([len(thefile),2, len(files)])
for j in range(len(files)):
    thefile = pd.read_excel(files[j])
    time = thefile.Timestamp
    for i in range(len(thefile)):
        instant = datetime.datetime( time[i].year, time[i].month, time[i].day, time[i].hour, time[i].minute, time[i].second)
    #    print instant
#        timedifference = instant - protonEnd
        timedifference = instant - end2016
        amountOfSeconds = timedifference.total_seconds()/(60*60*24)
      #  print 'file ' + str(j) + '. Seconds ' + str(amountOfSeconds) + '. value ' + str(thefile.Value[i] )
        data[i,0,j] = amountOfSeconds
        data[i,1,j] = thefile.Value[i]   
assert data[1200,1,2] != data[1200,1,3]
np.save('data', data)
data = np.load('data.npy')

#path = '//cern.ch/dfs/Users/c/cbjorkma/Documents/LSS 2' 
#
#os.chdir(path)
#
#
#thefile = pd.read_excel('TimberData.xlsx')
#
#timber = np.zeros([len(thefile),2])
#time = thefile.date
#for i in range(len(thefile)):      
#        instant = datetime.datetime( time[i].year, time[i].month, time[i].day, time[i].hour, time[i].minute, time[i].second)
#    #    print instant
##        timedifference = instant - protonEnd
#        timedifference = instant - end2016
#        amountOfSeconds = timedifference.total_seconds()/(60*60*24)
#      #  print 'file ' + str(j) + '. Seconds ' + str(amountOfSeconds) + '. value ' + str(thefile.Value[i] )
#        timber[i,0] = amountOfSeconds
#        timber[i,1] = thefile.val[i]   


path = '//rpclustersrv1/cbjorkma/LSS2/ActivationDetectors' 
os.chdir(path)

#np.save('timber',timber)

#timber = np.load('timber.npy')

fig = plt.figure()

ax = plt.subplot(111)


plt.plot(timber[0:,0],timber[0:,1]*10**6, label = 'Timber')
plt.plot(data[0:,0,1],data[0:,1,1], label = 'Remus/Ergo')

plt.xlabel('Days since end of 2015 operations')
plt.ylabel('uSv/h')
ax.set_yscale("log", nonposy='clip')
plt.ylim(10**3,3000)
plt.xlim(775, 803)
plt.legend()
plt.title('PMIU202 comparison')


plt.show()























