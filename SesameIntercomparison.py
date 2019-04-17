# -*- coding: utf-8 -*-
"""
Created on Thu Feb 07 13:52:49 2019

@author: cbjorkma
"""

#SesameIntercomparison



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
import glob

# Master
path = '//rpclustergw/cluster_temp/cbjorkma/OpeningScenarios/DECAY/Master/2019-02-06_14h21m55s_ATLAS2_JTTPrep'
os.chdir(path)
#



#try:
#    print danielold
#except:
print 'Loading USRBINs...'


filenames = sorted(glob.glob('*.lis'))

#filenames.append('ATLAS1_28.bnn.lis')

masterCentre = []
masterIntegrated = []

for i in range(len(filenames)):
    filename = filenames.pop(0)
    
    x = USRBIN(filename, path, normfactor)
    x.read()
    x.calc()
    masterCentre.append(x.centre)
    masterIntegrated.append(x.depthdeposition)




# Carmona
path = '//rpclustergw/cluster_temp/cbjorkma/OpeningScenarios/DECAY/Carmona/2019-02-07_11h02m53s_ATLAS2_JTTPrep'
os.chdir(path)


filenames = sorted(glob.glob('*.lis'))


carmonaCentre = []
carmonaIntegrated = []

for i in range(len(filenames)):
    filename = filenames.pop(0)
    
    x = USRBIN(filename, path, normfactor)
    x.read()
    x.calc()
    carmonaCentre.append(x.centre)
    carmonaIntegrated.append(x.depthdeposition)





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





##path = '//rpclustersrv1/cluster_temp/cbjorkma/2018-11-09_14h38m21s_ATLAS1'
#os.chdir(path)
#filename = 'ATLAS1_72.bnn.lis'
#
#danielnew = USRBIN(filename, path, normfactor)
#danielnew.read()
#danielnew.calc()

#filename = 'ATLAS1_73.bnn.lis'
#
#danielnew2m = USRBIN(filename, path, normfactor)
#danielnew2m.read()
#danielnew2m.calc()




xes = range(0,2500,2500/500)

#fig = plt.figure()


cooldowns = ['28d', '56d', '84d', '112d', '140d', '181d', '196d', '224d', '254d', '280d', '308d', '336d']

#for i in range(len(cooldowns)):
#
#    ax =plt.subplot(3,1,i +1)
#    
#    
#    
#    
#    xes = range(0,new[0].cube.shape[2]*5,5)
#    
#    
#    #plt.plot(xes, carmona.depthdeposition, label = 'Carmona')
#    #plt.plot(xes, daniel.depthdeposition, label = 'Daniel')
#    #plt.legend()
#    ##plt.xlabel('z [cm]')
#    #plt.ylabel('Integrated dose rate [uSv/h]')
#    #plt.title('Integrated dose rate along z')
#    #plt.yscale("log", nonposy='clip')
#    #plt.grid(linewidth = 0.4)
#    #
#    #fig.add_subplot(212)
#    
#    #plt.plot(xes, carmona.maxalongz, label = 'Carmona, Standard opening scenario', linestyle = '--')
#    #plt.plot(xes, daniel.maxalongz, label = 'Daniel, JTT exchange opening', linestyle = ':')
#    
#    
#    plt.plot(xes, old[i].centre, label = 'Old Profile ' , linestyle = '--')
#    plt.plot(xes, new[i].centre, label = 'New Profile ' , linestyle = '-.')
#    plt.legend()
#    if i == 2:
#        plt.xlabel('z [cm from IP]', fontsize = 18)
#    plt.ylabel('dose rate [uSv/h]' , fontsize = 18)
#    plt.title(cooldowns[i], fontsize = 15)
#    plt.yscale("log", nonposy='clip', fontsize = 18)
#    plt.grid(linewidth = 0.3)
#        
#    plt.suptitle('ATLAS dose rate comparison of centre bin', fontsize = 22)
#
#plt.show()
import matplotlib.cm as cm

#xes = range(0,2500,2500/250)


fig = plt.figure()

colors = cm.rainbow(np.linspace(0, 1, len(cooldowns)))

fig.add_subplot(211)

plt.title('Beam axis residual dose rate, Carmona/Master version', fontsize = 16)
for i in range(0,len(cooldowns),3): #range(len(cooldowns)):
    plt.plot(xes, carmonaCentre[i]/masterCentre[i], label = cooldowns[i], linestyle = '-', color = colors[len(cooldowns) - i -1 ])

#plt.xlabel('z [cm from IP]', fontsize = 18)
plt.ylabel('Ratio dose rate' , fontsize = 14)
#plt.title('Max values along z', fontsize = 15)
plt.axhline(y=1, color='k', linestyle='-')
plt.grid(linewidth = 0.3)
plt.legend()




plt.show()


import matplotlib.cm as cm

#xes = range(0,2500,2500/250)


#fig = plt.figure()

colors = cm.rainbow(np.linspace(0, 1, len(cooldowns)))

fig.add_subplot(212)

plt.title('Integrade residual dose rate, Carmona/Master version', fontsize = 16)
for i in range(0,len(cooldowns),3): #range(len(cooldowns)):
    plt.plot(xes, carmonaIntegrated[i]/masterIntegrated[i], label = cooldowns[i], linestyle = '-', color = colors[len(cooldowns) - i -1 ])

plt.xlabel('z [cm from IP]', fontsize = 18)
plt.ylabel('Ratio integrated dose rate' , fontsize = 14)
#plt.title('Max values along z', fontsize = 15)
plt.axhline(y=1, color='k', linestyle='-')
plt.grid(linewidth = 0.3)
plt.legend()


plt.suptitle('Sesame version compare. ATLAS geo, Carmona's vs Master version', fontsize = 22)

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