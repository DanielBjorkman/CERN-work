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



#path = '//rpclustersrv1/cbjorkma/ATLAS/Previous'
#os.chdir(path)
##
#try:
#    print carmona
#except:
#    print 'Loading USRBINs...'
#    
#    filename = 'ATLAS_LS2_Carmona_1m.txt'
#    
#    carmona = USRBIN(filename, path, normfactor)
#    carmona.read()
#    carmona.calc()
#    #
##
#
#
path = '//rpclustersrv1/cbjorkma/ATLAS'
os.chdir(path)
#
#try:
#    print danielold
#except:
print 'Loading USRBINs...'
#
filename = 'ATLAS_Daniel_22.bnn.lis'

danielold = USRBIN(filename, path, normfactor)
danielold.read()
danielold.calc()

#filename = 'ATLAS_Daniel_23.bnn.lis'
#
#danielold2m = USRBIN(filename, path, normfactor)
#danielold2m.read()
#danielold2m.calc()

##filename = 'ATLAS_Daniel_22.bnn.lis'
#filename = 'ATLAS_Fluences_Daniel4_JTTPrep_25.bnn.lis'
#
#daniel = USRBIN(filename, path, normfactor)
#daniel.read()
#daniel.calc()





path = '//rpclustersrv1/cluster_temp/cbjorkma/2018-11-09_14h38m21s_ATLAS1'
os.chdir(path)
filename = 'ATLAS1_72.bnn.lis'

danielnew = USRBIN(filename, path, normfactor)
danielnew.read()
danielnew.calc()

#filename = 'ATLAS1_73.bnn.lis'
#
#danielnew2m = USRBIN(filename, path, normfactor)
#danielnew2m.read()
#danielnew2m.calc()






fig = plt.figure()

fig.add_subplot(211)
#
xes = range(0,danielold.cube.shape[2]*5,5)
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
plt.plot(xes, danielold.centre, label = 'Old Profile', linestyle = '--')
plt.plot(xes, danielnew.centre, label = 'New Profile', linestyle = '-.')
plt.legend()
#plt.xlabel('z [cm from IP]', fontsize = 18)
plt.ylabel('dose rate [uSv/h]' , fontsize = 18)
plt.title('Sampled along beam axis', fontsize = 15)
plt.yscale("log", nonposy='clip', fontsize = 18)
plt.grid(linewidth = 0.3)

plt.suptitle('ATLAS dose rate comparison. 1 month cool down', fontsize = 22)





fig.add_subplot(212)

plt.title('Ratio comparison', fontsize = 15)
plt.plot(xes, danielnew.centre/danielold.centre, label = 'New profile/old profile', linestyle = '-')

plt.xlabel('z [cm from IP]', fontsize = 18)
plt.ylabel('Ratio dose rate' , fontsize = 18)
#plt.title('Max values along z', fontsize = 15)
plt.axhline(y=1, color='k', linestyle='-')
plt.grid(linewidth = 0.3)
plt.legend()




plt.show()








#
#fig = plt.figure()
#
#fig.add_subplot(211)
##
#xes = range(0,danielold2m.cube.shape[2]*5,5)
##
##plt.plot(xes, carmona.depthdeposition, label = 'Carmona')
##plt.plot(xes, daniel.depthdeposition, label = 'Daniel')
##plt.legend()
###plt.xlabel('z [cm]')
##plt.ylabel('Integrated dose rate [uSv/h]')
##plt.title('Integrated dose rate along z')
##plt.yscale("log", nonposy='clip')
##plt.grid(linewidth = 0.4)
##
##fig.add_subplot(212)
#
##plt.plot(xes, carmona.maxalongz, label = 'Carmona, Standard opening scenario', linestyle = '--')
##plt.plot(xes, daniel.maxalongz, label = 'Daniel, JTT exchange opening', linestyle = ':')
#plt.plot(xes, danielold2m.maxalongz, label = 'Old Profile', linestyle = '--')
#plt.plot(xes, danielnew2m.maxalongz, label = 'New Profile', linestyle = '-.')
#plt.legend()
##plt.xlabel('z [cm from IP]', fontsize = 18)
#plt.ylabel('Max dose rate [uSv/h]' , fontsize = 18)
#plt.title('Max values along z', fontsize = 15)
#plt.yscale("log", nonposy='clip', fontsize = 18)
#plt.grid(linewidth = 0.3)
#
#plt.suptitle('Dose rate comparison. 2 months cool down', fontsize = 22)
#
#
#
#
#
#fig.add_subplot(212)
#
#plt.plot(xes, danielnew2m.maxalongz/danielold2m.maxalongz, label = 'New profile/old profile', linestyle = '-')
#
#plt.xlabel('z [cm from IP]', fontsize = 18)
#plt.ylabel('Ratio Max dose rate' , fontsize = 18)
##plt.title('Max values along z', fontsize = 15)
#plt.axhline(y=1, color='k', linestyle='-')
#plt.grid(linewidth = 0.3)
#plt.legend()
#
#
#
#
#plt.show()

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