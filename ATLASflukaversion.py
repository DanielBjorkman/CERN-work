# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 13:59:54 2019

@author: cbjorkma
"""

import os
import glob
from USRBIN import USRBIN


#ATLAS fluka version


normfactor = 0.0036

idx = 0
cool = '28 days'


#2.3
path = '//rpclustergw/cluster_temp/cbjorkma/2019-02-15_16h44m29s_ATLAS2'
os.chdir(path)

filenames = sorted(glob.glob('*.lis'))

point3 = USRBIN(filenames[0], path, normfactor)
point3.read()
point3.calc()


#2.4 ionsplit
path = '//rpclustergw/cluster_temp/cbjorkma/2019-06-21_14h20m44s_ATLAS2ionsplit'
os.chdir(path)

filenames = sorted(glob.glob('*.lis'))

ionsplit4 = USRBIN(filenames[0], path, normfactor)
ionsplit4.read()
ionsplit4.calc()


#2.6 ionsplit
path = '//rpclustergw/cluster_temp/cbjorkma/2019-06-21_14h21m29s_ATLAS2ionsplit'
os.chdir(path)

filenames = sorted(glob.glob('*.lis'))

ionsplit6 = USRBIN(filenames[0], path, normfactor)
ionsplit6.read()
ionsplit6.calc()




cool = '28 days'
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.gridspec as gridspec

gs = gridspec.GridSpec(3, 2)

xes = range(0,2500,2500/500)


fig = plt.figure()

#colors = cm.rainbow(np.linspace(0, 1, len(cooldowns)))

#ax = fig.add_subplot(211)
ax = plt.subplot(gs[0:2, 0])

#plt.title('Beam axis residual dose rate', fontsize = 16)
#for i in range(0,len(cooldowns),3): #range(len(cooldowns)):
#plt.plot(xes, carmona.centre/ref.centre, label = 'Carmona/Reference', linestyle = '-')
#plt.plot(xes, master.centre/ref.centre, label = 'Master/Reference', linestyle = '-')

plt.plot(xes, point3.centre, label = '2x.3', linestyle = '-')
plt.plot(xes, ionsplit4.centre, label = '2x.4 ionsplit', linestyle = '-')
plt.plot(xes, ionsplit6.centre, label = '2x.6 ionsplit' , linestyle = '-')
ax.set_yscale('log')
#plt.xlabel('z [cm from IP]', fontsize = 18)
#plt.ylabel('Ratio dose rate' , fontsize = 14)
plt.ylabel('Residual dose rate [uSv/h]' , fontsize = 14)
plt.title('Beam axis', fontsize = 15)
#plt.axhline(y=1, color='k', linestyle='-')
plt.grid(linewidth = 0.3)
plt.legend()


ax = plt.subplot(gs[-1, 0])



plt.plot(xes, ionsplit4.centre/point3.centre, label = '2x.4 ionsplit/ 2x.3', linestyle = '-')
plt.plot(xes, ionsplit6.centre/point3.centre, label = '2x.6 ionsplit/ 2x.3', linestyle = '-')
#plt.plot(xes, refCentre, label = 'FLUKA only', linestyle = '-')
#ax.set_yscale('log')
plt.xlabel('z [cm from IP]', fontsize = 18)
#plt.ylabel('Ratio dose rate' , fontsize = 14)
plt.ylabel('Ratio' , fontsize = 14)
#plt.title('Max values along z', fontsize = 15)
plt.axhline(y=1, color='k', linestyle='-')
plt.grid(linewidth = 0.3)
plt.legend()


#xes = range(0,2500,2500/250)



#colors = cm.rainbow(np.linspace(0, 1, len(cooldowns)))

#ax = fig.add_subplot(212)
ax = plt.subplot(gs[0:2, 1])

plt.title('Integrade residual dose rate', fontsize = 16)
#for i in range(0,len(cooldowns),3): #range(len(cooldowns)):
#plt.plot(xes, carmona.depthdeposition/ref.depthdeposition, label = 'Carmona/Reference', linestyle = '-')
#plt.plot(xes, master.depthdeposition/ref.depthdeposition, label = 'Master/Reference', linestyle = '-')
plt.plot(xes, point3.depthdeposition, label = '2x.3', linestyle = '-')
plt.plot(xes, ionsplit4.depthdeposition ,label = '2x.4 ionsplit', linestyle = '-')
plt.plot(xes, ionsplit6.depthdeposition, label = '2x.6 ionsplit', linestyle = '-')



ax.set_yscale('log')

#plt.xlabel('z [cm from IP]', fontsize = 18)
#plt.ylabel('Ratio integrated dose rate' , fontsize = 14)
plt.ylabel('Integrated dose rate [uSv/h]' , fontsize = 14)
#plt.title('Max values along z', fontsize = 15)
#plt.axhline(y=1, color='k', linestyle='-')
plt.grid(linewidth = 0.3)
plt.legend()




ax = plt.subplot(gs[-1, 1])



plt.plot(xes, ionsplit4.depthdeposition/point3.depthdeposition, label = '2x.4 ionsplit/ 2x.3', linestyle = '-')
plt.plot(xes, ionsplit6.depthdeposition/point3.depthdeposition, label = '2x.6 ionsplit/ 2x.3', linestyle = '-')
#plt.plot(xes, refCentre, label = 'FLUKA only', linestyle = '-')
#ax.set_yscale('log')
plt.xlabel('z [cm from IP]', fontsize = 18)
#plt.ylabel('Ratio dose rate' , fontsize = 14)
plt.ylabel('Ratio' , fontsize = 14)
#plt.title('Max values along z', fontsize = 15)
plt.axhline(y=1, color='k', linestyle='-')
plt.grid(linewidth = 0.3)
plt.legend()





plt.suptitle('FLUKA version compare. ATLAS geo, cooldown of ' + cool, fontsize = 22)

xlength = 12

fig.set_size_inches(xlength, xlength/1.618)

plt.show()
#
#plt.savefig('CarmonaMasterRefCurves.pdf')