# -*- coding: utf-8 -*-
"""
Created on Fri Feb 08 11:23:32 2019

@author: cbjorkma
"""

#DumpAirActivation

import os
import numpy as np


path = '//rpclustergw/cbjorkma/Dump studies' 

os.chdir(path)


filename = 'CavernNoLeakage.txt'
cavern = np.loadtxt(filename)

filename = 'CavernLeakage.txt'
cavernLeakage = np.loadtxt(filename)

filename = 'normalOPleakage.txt'
cavernNormOPleakage = np.loadtxt(filename)


filename = 'CoreEvolution.txt'
coreEvo = np.loadtxt(filename)


filename = 'BotEvolution.txt'
botEvo = np.loadtxt(filename)



# Max diameter found 1980 cm
factor = 0.1



import matplotlib.pyplot as plt


fig = plt.figure()

ax = plt.subplot(111)

plt.plot(cavern[0,0:], factor*cavern[1,0:], label = 'High intensity, No Leakage')
plt.plot(cavernLeakage[0,0:], factor*cavernLeakage[1,0:], label = 'High intensity, Dump leakage of 0.1 $m^3/h$')
plt.plot(cavernNormOPleakage[0,0:], factor*cavernNormOPleakage[1,0:], label = 'Normal Operations, dump leakage of 0.1 $m^3/h$')
extraticks = [18.8]
plt.xticks(list(plt.xticks()[0]) + extraticks)
plt.xlabel('Time [min]', fontsize = 22)
plt.ylabel('uSv/h', fontsize = 22)
ax.set_yscale('log')
plt.grid(linewidth = 0.3)
plt.axhline(y = 1, linewidth=1, color='k', label = 'Safety threshold')
plt.legend()
plt.title('ECX5 Cavern air activation, External factors', fontsize = 22)
plt.xlim(0,230)
plt.show()



fig = plt.figure()

ax = plt.subplot(111)

plt.plot(coreEvo[0,0:], coreEvo[1,0:], label = 'Air pocket within beam dump')
plt.plot(botEvo[0,0:], botEvo[1,0:], label = 'Air pocket below beam dump')
#extraticks = [18.8]
#plt.xticks(list(plt.xticks()[0]) + extraticks)
plt.xlabel('Time [min]', fontsize = 22)
plt.ylabel('uSv/h', fontsize = 22)
ax.set_yscale('log')
plt.grid(linewidth = 0.3)
plt.axhline(y = 1, linewidth=1, color='k', label = 'Safety threshold')
plt.legend()
plt.title('Air pockets within dump, Internal factors', fontsize = 22)
plt.xlim(0,14)
plt.ylim(5e-3, 1e3)
plt.show()




















