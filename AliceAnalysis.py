# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 11:13:08 2018

@author: cbjorkma
"""

#AliceAnalysis


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
normfactor = 0.0036

import os



#
path = '//rpclustersrv1/cbjorkma/ALICE'
os.chdir(path)
#
#try:
#    print week
#except:
print 'Loading USRBINs...'
#
filename = 'ALICE1_21.bnn.lis'

week = USRBIN(filename, path, normfactor)
week.read()
week.calc()

#try:
#    print month
#except:
print 'Loading USRBINs...'
filename = 'ALICE1_22.bnn.lis'

month = USRBIN(filename, path, normfactor)
month.read()
month.calc()
    
    



fig = plt.figure()

fig.add_subplot(111)
#
xes = week.xcoodinates
#
#plt.plot(xes, carmona.depthdeposition, label = 'Carmona')
#plt.plot(xes, daniel.depthdeposition, label = 'Daniel')
#plt.legend()
##plt.xlabel('z [cm]')
#plt.ylabel('Integrated dose rate [uSv/h]')
#plt.title('Integrated dose rate along z')
#plt.yscale("log", nonposy='clip')
#plt.grid(linewidth = 0.4)
#
#fig.add_subplot(212)

#plt.plot(xes, carmona.maxalongz, label = 'Carmona, Standard opening scenario', linestyle = '--')
#plt.plot(xes, daniel.maxalongz, label = 'Daniel, JTT exchange opening', linestyle = ':')
plt.plot(xes, week.maxalongz, label = '1 week cool down', linestyle = '--')
plt.plot(xes, month.maxalongz, label = '1 month cool down', linestyle = '-.')

plt.xlabel('z [cm from IP]', fontsize = 18)
plt.ylabel('Max dose rate [uSv/h]' , fontsize = 18)
plt.title('PP-run dose rate contribution', fontsize = 15)
#plt.yscale("log", nonposy='clip', fontsize = 18)
plt.grid(linewidth = 0.3)

#plt.suptitle('ATLAS dose rate comparison. 1 month cool down', fontsize = 22)

plt.axhline(y=3, color='g', linestyle='-', label ='Supervised')
plt.axhline(y=10, color='r', linestyle='-', label ='Simple')
plt.legend()

plt.show()










