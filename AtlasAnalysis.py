# -*- coding: utf-8 -*-
"""
Created on Mon Aug 27 15:03:35 2018

@author: cbjorkma
"""

#Atlas analysis


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



path = '//rpclustersrv1/cbjorkma/ATLAS/Previous'
os.chdir(path)
#
#try:
#    print carmona
#except:
print 'Loading USRBINs...'

filename = 'ATLAS_LS2_Carmona_4m.txt'

carmona = USRBIN(filename, path, normfactor)
carmona.read()
carmona.calc()




path = '//rpclustersrv1/cbjorkma/ATLAS'
os.chdir(path)

#try:
#    print daniel
#except:
print 'Loading USRBINs...'

#filename = 'ATLAS_Daniel_22.bnn.lis'
filename = 'ATLAS_Fluences_Daniel4_JTTPrep_25.bnn.lis'

daniel = USRBIN(filename, path, normfactor)
daniel.read()
daniel.calc()



fig = plt.figure()

#fig.add_subplot(211)
#
xes = range(0,carmona.cube.shape[2]*5,5)
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

plt.plot(xes, carmona.maxalongz, label = 'Carmona, Standard opening scenario', linestyle = '--')
plt.plot(xes, daniel.maxalongz, label = 'Daniel, JTT exchange opening', linestyle = ':')
plt.legend()
plt.xlabel('z [cm from IP]', fontsize = 18)
plt.ylabel('Max dose rate [uSv/h]' , fontsize = 18)
plt.title('Max values along z', fontsize = 15)
plt.yscale("log", nonposy='clip', fontsize = 18)
plt.grid(linewidth = 0.4)

plt.suptitle('Dose rate comparison. 4 months cool down', fontsize = 22)

plt.show()



#filenames = sorted(os.listdir(path))
#try:
#    print normal
#except:
#    print 'Loading USRBINs...'
#    normal = []
#    for i in range(len(filenames)):
#        x = USRBIN(filenames[i], path, normfactor)
#        x.read()
#        x.calc()
#        normal.append(x)