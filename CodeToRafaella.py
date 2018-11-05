# -*- coding: utf-8 -*-
"""
Created on Thu Aug 02 14:02:36 2018

@author: cbjorkma
"""

#Code to Rafaella

self.origo = datetime.datetime(2017,10,23,06,00,00)


thefile = pd.read_excel(files[0])

dataPMI = np.zeros([len(thefile),2, len(files)])
for j in range(len(files)):
    thefile = pd.read_excel(files[j])
    time = thefile.Timestamp
    for i in range(int(0*len(thefile)),len(thefile)):
        instant = datetime.datetime( time[i].year, time[i].month, time[i].day, time[i].hour, time[i].minute, time[i].second)
        timedifference = instant - self.origo
        amountOfSeconds = timedifference.total_seconds()/(60*60*24)

        dataPMI[i,0,j] = amountOfSeconds
        dataPMI[i,1,j] = thefile.Value[i]   
np.save('dataPMI', dataPMI)
