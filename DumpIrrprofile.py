# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 15:45:46 2018

@author: cbjorkma
"""

#DUMPirrprofile


import numpy as np

dump = np.zeros([3,3])

dump[0,0:2] = [6.307E8, 6.34216E10]
dump[1,0:2] = [86400, 5.0E12]

dump[0:,0] = dump[0:,0]/(60*60*24)

lastidx = len(dump)-3

dump[len(dump)-2,2] = - dump[len(dump)-2,0]
for i in range(lastidx,-1,-1):
    #print i
    dump[i,2] = -dump[i,0] - abs(dump[i+1,2])
    #print ATLAS[i,3] 


fig = plt.figure()

ax = fig.add_subplot(111)

ax.step(dump[0:,2], dump[0:,1],where='post')

#ax.step(CMS[0:,2], CMS[0:,1], label = 'CMS, #Collisons= ' + str(collisionsCMS),where='post')

         


#plt.axvline(x=-365*1, color = 'k', linestyle = '--', label = 'Year shift')
#plt.axvline(x=-365*2, color = 'k', linestyle = '--')
#plt.axvline(x=-365*3, color = 'k', linestyle = '--')
#plt.axvline(x=-365*4, color = 'k', linestyle = '--')
#plt.axvline(x=-365*5, color = 'k', linestyle = '--')
#plt.axvline(x=-365*6 , color = 'k', linestyle = '--')
#plt.axvline(x=-365*7, color = 'k', linestyle = '--')
#plt.axvline(x=newyearsLS2difference, color = 'r', linestyle = ':', linewidth = 2, label = 'LS2 starts')

plt.legend()


#ax.set_ylim(0,1e9)

plt.xlabel('Time [days]',  fontsize = 16)
ax.set_ylabel('Beam intensity [particles/s]',  fontsize = 16)
plt.xlim(-5,0.1)

plt.ylim(1E6,1E15)
plt.grid(linewidth = 0.1)
ax.set_yscale("log", nonposy='clip')
#ax2.set_ylabel('Integrated luminocity [pb-1]',  fontsize = 16)

#plt.title('ATLAS/CMS irradiation profiles', fontsize = 20)

plt.show()