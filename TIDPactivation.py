# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 09:55:51 2018

@author: cbjorkma
"""

#TIDP activation comparison

import matplotlib.patches as patches
import matplotlib.pyplot as plt
plt.close()
plt.close()
plt.close()
plt.close()
plt.close()
plt.close()
plt.close()
plt.close()


from USRBIN import USRBIN
import numpy as np

#Converts data to uSv/h and normalizes data to the number of exstracted particles
normfactor = 0.0036*0.896836


import os
#
##
path = '//rpclustersrv1/cbjorkma/Scrapers/TIDPavg'
os.chdir(path)
filenames = sorted(os.listdir(path))
try:
    print avg
except:
    print 'Loading USRBINs...'
    avg = []
    for i in range(len(filenames)):
        x = USRBIN(filenames[i], path, normfactor)
        x.read()
        x.calc()
        avg.append(x)
        
        
        
##
path = '//rpclustersrv1/cbjorkma/Scrapers/TIDPconservative'
os.chdir(path)
filenames = sorted(os.listdir(path))
try:
    print cons
except:
    print 'Loading USRBINs...'
    cons = []
    for i in range(len(filenames)):
        x = USRBIN(filenames[i], path, normfactor)
        x.read()
        x.calc()
        cons.append(x)
        


##
path = '//rpclustersrv1/cbjorkma/Scrapers'
os.chdir(path)

filename = 'RingMeasurement_LSS1.txt'

ring1 = np.loadtxt(filename)

filename = 'RingMeasurement_LSS1_feb.txt'

ring2 = np.loadtxt(filename)
#ring[0:,0] = 1100*ring[0:,0] - 100000 - 14000 +200



quad216 = 3.791*100
quad217 = 35.7887*100
quad218 = 67.7864*100
quad219 = 99.7841*100

ring1[0:,0] = (ring1[0:,0] -216)*(quad217 - quad216) +350000 - 26000 + 1918

ring2[0:,0] = (ring2[0:,0] -216)*(quad217 - quad216) +350000 - 26000 + 1918 + 50


ring = []
ring.append(ring1)
ring.append(ring2)








xes = cons[0].xcoodinates

cooldowns = ['30h','3 months']


fig = plt.figure()

for i in range(2):
    ax = plt.subplot(2,1,i+1)
    
    cube1 = cons[i+1]
    cube2 = avg[i+1]
    ringVal = ring[i] 
    
    from scipy.interpolate import interp1d
    x = ringVal[0:,0]
    y = ringVal[0:,1]
    f = interp1d(x,y)
    
    
#    plt.plot(xes, cube1.TIDP1meter + f(xes), label = 'Conservative + ring', linestyle = '--')
#    plt.plot(xes, cube2.TIDP1meter + f(xes), label = 'Averaged + ring', linestyle = '-.')
#    plt.plot(ringVal[0:,0], ringVal[0:,1], label = 'Ring measurement only')
    
    #plt.plot(ring[0:,0], ring[0:,1], label = 'Ring measuremrnt')    
    
    plt.plot(xes, cube1.TIDP1meter, label = 'Conservative', linestyle = '--')
    plt.plot(xes, cube2.TIDP1meter, label = 'Averaged', linestyle = '-.')
    plt.plot(ringVal[0:,0], ringVal[0:,1], label = 'Ring measurement')
    
 #   plt.axhline(y=1, color='k', linestyle='-')
    
    plt.title(cooldowns.pop(0), fontsize = 12)
    plt.legend(loc = 1)
    if i == 1:
        plt.xlabel('z [cm]', fontsize = 18)
        plt.ylim(0,400)
        #plt.ylim(0,280)
    else:
        plt.ylim(0,1400)
        #plt.ylim(0,800)
    #plt.yscale("log", nonposy='clip')
    #plt.ylim(0,800)
    plt.xlim(-400,1700)
    
    plt.ylabel('Dose rate [uSv/h]', fontsize = 18)
    
    
   # plt.ylabel('Fraction dose rate', fontsize = 12)
    #plt.yscale("log", nonposy='clip')
    #plt.ylim(0,1.2)
   # ax2 = ax.twinx()
#    plotSepta(ax2)
#    ax2.get_yaxis().set_visible(False)
#    plt.ylim([0,30])
#    plt.legend(loc = 2)
#    plt.xlim(-570,2800)
    ax2 = ax.twinx()
    
    r1 = patches.Rectangle((413,0), 430,5, color = 'Green', alpha = 0.3, label = 'TIDP')
    
    ax2.add_patch(r1)
    ax2.get_yaxis().set_visible(False)
    plt.legend(loc = 2)


plt.suptitle('TIDP dose rate contribution. Sampled 1 meter from beam axis', fontsize = 16)
plt.show()



fig = plt.figure()


ax = plt.subplot(111)

cube1 = cons[0]
cube2 = cons[1]
cube3 = cons[2]
#cube2 = avg[0]
#ringVal = ring[0] 

#    from scipy.interpolate import interp1d
#x = ringVal[0:,0]
#y = ringVal[0:,1]
#f = interp1d(x,y)


plt.plot(xes, cube1.TIDP1meter, label = '1h cool down', linestyle = '--')
plt.plot(xes, cube2.TIDP1meter, label = '30h cool down', linestyle = '--')
plt.plot(xes, cube3.TIDP1meter, label = '3 months cool down', linestyle = '--')
#    plt.plot(xes, cube2.TIDP1meter + f(xes), label = 'Averaged + ring', linestyle = '-.')
#    plt.plot(ringVal[0:,0], ringVal[0:,1], label = 'Ring measurement only')

#plt.plot(ring[0:,0], ring[0:,1], label = 'Ring measuremrnt')    

#    plt.plot(xes, cube1.TIDP1meter, label = 'Conservative', linestyle = '--')
#    plt.plot(xes, cube2.TIDP1meter, label = 'Averaged', linestyle = '-.')
#plt.plot(ringVal[0:,0], ringVal[0:,1], label = 'Ring measurement')

 #   plt.axhline(y=1, color='k', linestyle='-')

plt.title('Conservative contribution at 1 meter distance', fontsize = 18)
plt.legend(loc = 1)

plt.xlabel('z [cm]', fontsize = 18)
#plt.ylim(0,400)
#plt.ylim(0,280)

plt.ylim(0,3500)
    #plt.ylim(0,800)
#plt.yscale("log", nonposy='clip')
#plt.ylim(0,800)
plt.xlim(-400,1700)

plt.ylabel('Dose rate [uSv/h]', fontsize = 18)


   # plt.ylabel('Fraction dose rate', fontsize = 12)
#plt.yscale("log", nonposy='clip')
#plt.ylim(0,1.2)
   # ax2 = ax.twinx()
#    plotSepta(ax2)
#    ax2.get_yaxis().set_visible(False)
#    plt.ylim([0,30])
#    plt.legend(loc = 2)
#    plt.xlim(-570,2800)
ax2 = ax.twinx()

r1 = patches.Rectangle((413,0), 430,5, color = 'Green', alpha = 0.3, label = 'TIDP')

ax2.add_patch(r1)
ax2.get_yaxis().set_visible(False)
plt.legend(loc = 2)


#plt.suptitle('Worse case scenario', fontsize = 16)
plt.show()

