# -*- coding: utf-8 -*-
"""
Created on Wed Jan 09 16:08:47 2019

@author: cbjorkma
"""



import os
import numpy as np







def readProfile(filename):

    ALICEdata = np.loadtxt(filename)
    
    ALICE = np.zeros([ALICEdata.shape[0]+2,3])
    
    ALICE[1:len(ALICE)-1,0:2] = ALICEdata
    
    ALICE[0:,0] = ALICE[0:,0]/(60*60*24)

    return ALICE




def calcTimeline(experiment):

    lastidx = len(experiment)-3
    
    experiment[len(experiment)-2,2] = - experiment[len(experiment)-2,0]
    for i in range(lastidx,-1,-1):
        
        experiment[i,2] = -experiment[i,0] - abs(experiment[i+1,2])
    return experiment;
 
        

#CMS = calcTimeline(CMS)














import pandas as pd



def readLumi(filename,origo):
    data = pd.read_csv(filename)

    lumi = np.zeros([len(data),2])
        

    for i in range(len(data)):
        
            #time = data.time
        time = data['Date Time']
    

        instant = datetime.datetime( int(time[i].split('-')[0].strip()), int(time[i].split('-')[1].strip()), int(time[i].split('-')[2][0:2]), int(time[i].split('-')[2].split()[1][0:2]), int(time[i].split('-')[2].split()[1].split(':')[1]), int(time[i].split('-')[2].split()[1].split(':')[2][0:2]))
    #                print instant
        timedifference = instant - origo
        timeindays = timedifference.total_seconds()/(60*60*24)
        lumi[i,0] = timeindays
        global experiment
        lumi[i,1] = data[experiment][i]
        
    #                print 'file ' + str(j) + '. Seconds ' + str(amountOfSeconds) + '. value ' + str(thefile.Value[i] )
    #        assert dataPMI[1200,1,2] != dataPMI[1200,1,3]
    #np.save('dataLumi', lumi)
    return lumi
    #        print dataPMI













def sinceOrigo(instant):
    return (instant -origo).total_seconds()/(60*60*24)




def setMagnitude(lumi):
    
    ATLAS = np.zeros([1,3])
    
    
    from scipy.interpolate import interp1d
    x = lumi[0:,0]
    yATLAS = lumi[0:,1]
    f = interp1d(x,yATLAS)
    
    
    

    
    
    #2011
    xsec = 72E-3 #mbar
    timediff = (end2011 - start2011).total_seconds() 
    lumidiff = f(sinceOrigo(end2011)) - f(sinceOrigo(start2011)) #picobarn
    collisions = 1e12*lumidiff*xsec
    newrow = [timediff/(60*60*24),collisions/timediff,0]
    ATLAS = np.vstack([ATLAS,newrow])
    ATLAS = np.vstack([ATLAS,[0,0,0]])
    
    

    
    #2012
    xsec = 75E-3 #mbar
    timediff = (end2012 - start2012).total_seconds() 
    lumidiff = f(sinceOrigo(end2012)) - f(sinceOrigo(start2012)) #picobarn
    collisions = 1e12*lumidiff*xsec
    newrow = [timediff/(60*60*24),collisions/timediff,0]
    ATLAS = np.vstack([ATLAS,newrow])
    ATLAS = np.vstack([ATLAS,[0,0,0]])
    
    
    

    xsec = 80E-3 #mbar
    
    #2015
    timediff = (end2015 - start2015).total_seconds() 
    lumidiff = f(sinceOrigo(end2015)) - f(sinceOrigo(start2015)) #picobarn
    collisions = 1e12*lumidiff*xsec
    newrow = [timediff/(60*60*24),collisions/timediff,0]
    ATLAS = np.vstack([ATLAS,newrow])
    ATLAS = np.vstack([ATLAS,[0,0,0]])
    
    
    
    
    #2016
    
    timediff = (end2016 - start2016).total_seconds() 
    lumidiff = f(sinceOrigo(end2016)) - f(sinceOrigo(start2016)) #picobarn
    collisions = 1e12*lumidiff*xsec
    newrow = [timediff/(60*60*24),collisions/timediff,0]
    ATLAS = np.vstack([ATLAS,newrow])
    ATLAS = np.vstack([ATLAS,[0,0,0]])
    
    
    
    #2017
    timediff = (end2017 - start2017).total_seconds() 
    lumidiff = f(sinceOrigo(end2017)) - f(sinceOrigo(start2017)) #picobarn
    collisions = 1e12*lumidiff*xsec
    newrow = [timediff/(60*60*24),collisions/timediff,0]
    ATLAS = np.vstack([ATLAS,newrow])
    ATLAS = np.vstack([ATLAS,[0,0,0]])
    
    
    #collisions2017
    #ATLAS[9,1]*ATLAS[9,0]
    

    
    #2018, devided in T1, T2,T3 and T4
    
    #T1
#    T1end = datetime.datetime(2018,6,11,23,39,11)
#    T1start = datetime.datetime(2018,4,17,11,00,23)
    timediff = (T1end - T1start).total_seconds() 
    lumidiff = f(sinceOrigo(T1end)) - f(sinceOrigo(T1start)) #picobarn
    collisions = 1e12*lumidiff*xsec
    newrow = [timediff/(60*60*24),collisions/timediff,0]
    ATLAS = np.vstack([ATLAS,newrow])
    ATLAS = np.vstack([ATLAS,[0,0,0]])
    
    #T2
#    T2end =  datetime.datetime(2018,7,22,18,22,43)
#    T2start = datetime.datetime(2018,6,26,19,22,10)
    timediff = (T2end - T2start).total_seconds() 
    lumidiff = f(sinceOrigo(T2end)) - f(sinceOrigo(T2start)) #picobarn
    collisions = 1e12*lumidiff*xsec
    newrow = [timediff/(60*60*24),collisions/timediff,0]
    ATLAS = np.vstack([ATLAS,newrow])
    ATLAS = np.vstack([ATLAS,[0,0,0]])
    
    
    
    #T3
#    T3end = datetime.datetime(2018,9,10,03,18,45)
#    T3start = datetime.datetime(2018,8,1,2,8,37)
    timediff = (T3end - T3start).total_seconds() 
    lumidiff = f(sinceOrigo(T3end)) - f(sinceOrigo(T3start)) #picobarn
    collisions = 1e12*lumidiff*xsec
    newrow = [timediff/(60*60*24),collisions/timediff,0]
    ATLAS = np.vstack([ATLAS,newrow])
    ATLAS = np.vstack([ATLAS,[0,0,0]])
   


    
    #T4
    global T4end
    global T4start
#    T4end = LS2
#    T4start = datetime.datetime(2018,9,23,17,55,33)
    timediff = (T4end - T4start).total_seconds() 
    lumidiff = f(sinceOrigo(T4end)) - f(sinceOrigo(T4start)) #picobarn
    collisions = 1e12*lumidiff*xsec
    newrow = [timediff/(60*60*24),collisions/timediff,0]
    ATLAS = np.vstack([ATLAS,newrow])
    ATLAS = np.vstack([ATLAS,[0,0,0]])
    
    
    
    global experiment
    if experiment == 'ALICE':
    
        #Ion run
        xsec = 8. #barn
        protonToIonFactor = 500/float(6)
        
        
        timediff = (ionEnd- ionStart).total_seconds() 
        #lumidiff = f(sinceLS2(T4end)) - f(sinceLS2(T4start)) #picobarn
        lumidiff = 1E9 #barn 
        collisions = lumidiff*xsec
        #newrow = [timediff/(60*60*24),collisions/timediff,0]
        newrow = [timediff/(60*60*24),protonToIonFactor*collisions/timediff,0]
        ATLAS = np.vstack([ATLAS,newrow])
        ATLAS = np.vstack([ATLAS,[0,0,0]])
    
    return ATLAS;








#
def calcTimingNewprofile(dates,experimentMagnitudes, origo):
    experiment = np.zeros(experimentMagnitudes.shape)
    experiment[0:,1] = experimentMagnitudes[0:,1]    
    for i in range(len(experiment)-2,0,-1):
        if experiment[i,1] == 0:
            instance = dates.pop(0)
            #print instance
            timediff = (origo - instance).total_seconds() - sum(experiment[i:,0])
            #print str(timediff)
            
            #timediff = (LS2 - datesAtlas.pop(0)).total_seconds() - sum(newATLAS[i:,0])
            experiment[i,0] = timediff
            
        else:
            
            experiment[i,0] = (60*60*24)*experimentMagnitudes[i,0]
    
    #print experiment[0:,0]/(60*60*24)
    experiment[0:,0] = experiment[0:,0]/(60*60*24)
    
    experiment = calcTimeline(experiment)
    return experiment




def plot(prev, new, origo, title):

    
    import matplotlib.pyplot as plt
    
    
    timedifference = origo - newyear2018
    newyearsLS2difference = timedifference.total_seconds()/(60*60*24)
    
    fig = plt.figure()
    
    
    
    
    
    
    ax = fig.add_subplot(111)
    
    ax.step(ALICE[0:,2], ALICE[0:,1], label = 'Old Profile, #Collisons= ' + str(prevcollisionsALICE) ,where='post') #
    
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
    
    
    ax.set_ylabel('Beam intensity [collisions/s]',  fontsize = 16)
    
    ax2 = ax.twinx()
    
    lumicolor = 'm'
    
    ax2.plot(lumi[0:,0],lumi[0:,1], label = 'Integrated Luminosity', linestyle = '--', color = lumicolor)
    
    
    ax2.tick_params(axis='y', colors=lumicolor)
    
    ax2.set_ylabel('Integrated luminosity [pb-1]',  fontsize = 16)
    
    plt.title(title, fontsize = 20)
    
    
    plt.xlabel('Time [days until ' + str(origo.day) + '/' + str(origo.month) + '/' + str(origo.year) + ']',  fontsize = 16)
    
    plt.show()


import datetime



LS2 = datetime.datetime(2018,10,23,13,22,00) #end of proton-proton run
LS2ion = datetime.datetime(2018,12,3,06,00,00) # end of ion run
newyear2018 = datetime.datetime(2018,12,31,23,59,59)










end2011 = datetime.datetime(2011,10,30,9,57,00)
end2012 = datetime.datetime(2012,12,16,11,58,00)
end2015 = datetime.datetime(2015,11,21,19,22,00)
end2016 = datetime.datetime(2016,10,26,07,49,00)
end2017 = datetime.datetime(2017,11,26,00,29,00)
#end2018a = datetime.datetime(2018,06,11,23,39,22)   
#end2018b = datetime.datetime(2018,07,22,18,22,43) 
#end2018d = datetime.datetime(2018,9,10,03,18,45)
#end2018e = LS2



start2011 = datetime.datetime(2011,3,13,13,35,9)
start2012 = datetime.datetime(2012,4,6,23,15,36)
start2015 = datetime.datetime(2015,6,5,23,17,23)
start2016 = datetime.datetime(2016,4,22,22,38,37)
start2017 = datetime.datetime(2017,5,23,14,45,27)




#2018
T1end = datetime.datetime(2018,6,11,23,39,11)
T1start = datetime.datetime(2018,4,17,11,00,23)

T2end =  datetime.datetime(2018,7,22,18,22,43)
T2start = datetime.datetime(2018,6,26,19,22,10)

T3end = datetime.datetime(2018,9,10,03,18,45)
T3start = datetime.datetime(2018,8,1,2,8,37)

T4end =  LS2 #end of proton-proton run
T4start = datetime.datetime(2018,9,23,17,55,33)


# Ion run
ionEnd = LS2ion
ionStart = datetime.datetime(2018,11,8,00,00,00)



datesAtlas = []
datesAtlas.append(T4end)
datesAtlas.append(T3end)
datesAtlas.append(T2end)
datesAtlas.append(T1end)
datesAtlas.append(end2017)
datesAtlas.append(end2016)
datesAtlas.append(end2015)
datesAtlas.append(end2012)
datesAtlas.append(end2011)





path = '//cern.ch/dfs/Users/c/cbjorkma/Documents/Irrprofi'
os.chdir(path)


#
#newATLASfactorless = newATLAS

experiment = 'ALICE'
origo = LS2ion
ALICE = readProfile('LHCirradiatonprofile.txt')
ALICE[0:,1] = ALICE[0:,1]*0.0001
ALICE = calcTimeline(ALICE)
filename = 'lumiData.csv'
lumi = readLumi(filename, origo)
ATLAS = setMagnitude(lumi)
newATLAS = calcTimingNewprofile(datesAtlas, ATLAS, origo)
plot(ALICE, newATLAS, origo, 'ALICE')














#lumiCollisions = lumiCollisions + 1e12*(f(0) - f(-2000))*xsec


#xsec = 80E-3
#lumiCollisions = 1e12*max(lumi[0:,1])*xsec
#
#
#
#PPcollisionsAtlas = sum(newATLAS[:-3,1]*newATLAS[:-3,0])*24*60*60
#
collisionsAtlas = sum(newATLAS[0:,1]*newATLAS[0:,0])*24*60*60
#
prevcollisionsALICE = sum(ALICE[0:,1]*ALICE[0:,0])*24*60*60
#
#




#print '# PP collisions/Lumi collisions = '
#print str(PPcollisionsAtlas/lumiCollisions)
#print ' ' 
#print 'Fraction of #Collisions increased for ALICE = '
#print str(collisionsAtlas/prevcollisionsALICE)
#














#
#
#
#ax = fig.add_subplot(212)
#
#
##
##ax.step(newCMS[0:,2], newCMS[0:,1], label = 'CMS, #Collisons= ' + str(collisionsCMS),where='post')
##
##         
##ax.set_yscale('log')
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
#plt.xlabel('Time [days until end of 2018 ion run]',  fontsize = 16)
#ax.set_ylabel('Beam intensity [collisions/s]',  fontsize = 16)
#
#ax2 = ax.twinx()
#
##ax2 = fig.add_subplot(111)
#
#ax2.plot(lumi[0:,0],lumi[0:,1], label = 'Integrated Luminosity', linestyle = '--', color = 'Orange')
#
##ax2.plot(lumi[0:,0],lumi[0:,2], label = 'CMS', linestyle = '--')
#
##ax2.legend()
#
##ax2.set_ylim(0,194000)
##ax.set_xlim(-240,10)
#
#
#ax2.set_ylabel('Integrated luminosity [pb-1]',  fontsize = 16)
#
##plt.title('New Profile', fontsize = 20)













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

writeProfile(newATLAS, 'AliceProfile.txt')









