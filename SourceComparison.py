# -*- coding: utf-8 -*-
"""
Created on Wed Mar 28 14:04:13 2018

@author: cbjorkma
"""

#SoruceComparison


import matplotlib.pyplot as plt

plt.close()

plt.close()

import os
from USRBIN import USRBIN

filename = 'Dump12Res_58.bnn.lis'

path = '//rpclustersrv1/cbjorkma/Dump studies'



daniel = USRBIN(filename,path)

jose = USRBIN('TIDVG5-HLLHC_22.bnn.lis', path)

daniel.read()
daniel.calc()

jose.read()
jose.calc()



#daniel.plot()
import numpy as np
from matplotlib.gridspec import GridSpec

fig = plt.figure()

gs = GridSpec(2,2)


ax = fig.add_subplot(gs[0,0])

plt.pcolor(np.rot90(daniel.zcut,3), cmap='jet')
#locs, labels = plt.xticks()
#plt.xticks(locs, np.arange(15, -15.01, -7.5))
#plt.xticks(locs[len(locs):None:-1])


#locs, labels = plt.yticks()
#plt.yticks(locs, np.arange(-12.50, 5.001 , float(17.5)/4))


plt.xlabel('x (reversed)')

ax = fig.add_subplot(gs[0,1])

#plt.hist()


ax = fig.add_subplot(gs[1,0])

plt.pcolor(np.rot90(jose.zcut,3), cmap='jet')
#locs, labels = plt.xticks()
#plt.xticks(locs, np.arange(15, -15.01, -7.5))
#plt.xticks(locs[len(locs):None:-1])


#locs, labels = plt.yticks()
#plt.yticks(locs, np.arange(-12.50, 5.001 , float(17.5)/4))


plt.xlabel('x (reversed)')


plt.show()



daniel.xaverage = sum(np.mean(daniel.cube, axis = 0)) /sum(np.mean(daniel.cube, axis = 0) != 0) *daniel.info['xmax'][0]

jose.xaverage = sum(np.mean(jose.cube, axis = 0)) /sum(np.mean(jose.cube, axis = 0) != 0)  * jose.info['xmax'][0]


print daniel.xaverage

print jose.xaverage



daniel.yaverage = sum(np.mean(daniel.cube != 0, axis = 1)) /sum(np.mean(daniel.cube, axis = 1) != 0) *daniel.info['xmax'][0]

jose.yaverage = sum(np.mean(jose.cube, axis = 1)) /sum(np.mean(jose.cube, axis = 1) != 0)  * jose.info['xmax'][0]


print daniel.yaverage

print jose.yaverage










ydaniel = np.zeros(int(daniel.info['ybin'][0]))
for i in range(int(daniel.info['xbin'][0])):
    for j in range(int(daniel.info['ybin'][0])):
        if daniel.cube[i,j] != 0:
            ydaniel[j] = ydaniel[j]+ daniel.cube[i,j]
            
shift = - 6.52
            

yjose = np.zeros(int(jose.info['ybin'][0]))
for i in range(int(jose.info['xbin'][0])):
    for j in range(int(jose.info['ybin'][0])):
        if jose.cube[i,j] != 0:
            yjose[j] = yjose[j]+ jose.cube[i,j]
            
            
            
     
          

fig = plt.figure()


jose.info['ymax'][0] = jose.info['ymax'][0] + shift

jose.info['ymin'][0] = jose.info['ymin'][0] + shift


plt.plot(np.arange(float(daniel.info['ymin'][0]),float(daniel.info['ymax'][0] ), (abs(float(daniel.info['ymin'][0])) + abs(float(daniel.info['ymax'][0] )))/(float(daniel.info['ybin'][0]))         ),ydaniel/max(ydaniel), label = 'Daniel')
plt.plot(np.arange(float(jose.info['ymin'][0]),float(jose.info['ymax'][0] ), (abs(float(jose.info['ymin'][0])) + float(jose.info['ymax'][0] ))/(float(jose.info['ybin'][0]))       ) ,yjose/max(yjose), label = 'jose')

plt.legend()

plt.xlabel('y [cm]')

danielspectrum = abs(float(daniel.info['ymin'][0])) + abs(float(daniel.info['ymax'][0] ))
daniel2 = np.argmax(ydaniel)/float(daniel.info['ybin'][0])
danielFinal = danielspectrum * daniel2  + float(daniel.info['ymin'][0])


josespectrum = abs(float(jose.info['ymin'][0])) + float(jose.info['ymax'][0] )
jose2 = np.argmax(yjose)/float(jose.info['ybin'][0])
joseFinal = josespectrum * jose2  + float(jose.info['ymin'][0])



plt.title('Daniel peak at ' + str(danielFinal) + '. Jose peak at: ' + str(joseFinal) + '. Difference: ' + str(joseFinal - danielFinal) + ' cm')


plt.suptitle('Source distribution comparison onto the TIDVG5. Jose dist. shifted by ' + str(shift) + ' cm in y')

plt.xlim(-5.5, -3.0)


plt.show()












