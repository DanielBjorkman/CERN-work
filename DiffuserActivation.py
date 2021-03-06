# -*- coding: utf-8 -*-
"""
Created on Thu Jul 12 17:11:35 2018

@author: cbjorkma
"""

#DiffuserActivation
plt.close()
plt.close()
from USRBIN import USRBIN

import os

path = '//rpclustersrv1/cbjorkma/diffuser/USRBINSs'
os.chdir(path)




#x = USRBIN(filenames[i], path, normfactor)
#
#
#




norm = 0.0036

files = sorted(os.listdir(path))

list = []
for i in range(len(files)):
    file = files[i]
    tmp = USRBIN(file,path,norm)
    tmp.read()
    tmp.calc()
    list.append(tmp)
    
    
    
    
    
    
    
    
    


import matplotlib.pyplot as plt
#from matplotlib.colors import LogNorm


#xes = range(0,250-250/15*4,250/15)
#
#fig = plt.figure()
#
#for i in range(len(files)):
#        
#    plt.subplot(3,2,i +1)
#    
#    plt.pcolor(list[i].horizontal,norm=LogNorm(), cmap='jet')
#    cbar = plt.colorbar()
#    plt.title(list[i].filename)
#    
#plt.show()

#lengths = [15,18,20,22.5 , 25]
#

labels = ['1h', '12h', '30h', '1m','4m']

fig = plt.figure()

i = 0
ax = plt.subplot(111)
for i in range(len(files)):
    cube  = list[i]
    
    #info = cube.info
    
    xes = range(0,100,2)
    
    
    plt.plot(xes,cube.cube[0:,2,2], label = labels[i])

plt.legend()
plt.title('Dose rate evolution for diffuser contribution ', fontsize = 20)
plt.grid(linewidth = 0.25)
plt.ylabel('uSv/h', fontsize = 16)
plt.xlabel('cm outside beampipe, laterally from diffuser', fontsize = 16)
ax.set_yscale("log", nonposy='clip')

plt.show()



#
#
#
#
#
#ax = plt.subplot(1,2,1)
#for i in range(len(files)):
#
#    plt.plot(xes, list[i].cube[11:None:-1, 5:6,0]/2, label = 'Shielding width: ' +str(lengths[i]) + ' cm')
#    
#plt.legend()
#plt.title('1 day cool down', fontsize = 20)
#plt.grid(linewidth = 0.25)
#plt.ylabel('uSv/h', fontsize = 16)
#plt.xlabel('cm from marble shielding', fontsize = 16)
#props = dict(boxstyle='round', facecolor='white', alpha=1)
#
##ax.text(0.25, 0.98, '1 day cool down', transform=ax.transAxes, fontsize=18, verticalalignment='top',bbox=props)     
##plt.show()
#
#
#
#plt.subplot(1,2,2)
#for i in range(len(files)):
#        
#    plt.plot(xes, list2[i].cube[11:None:-1, 5:6,0]/2, label = 'Shielding width: ' +str(lengths[i]) + ' cm')
#    
#plt.legend()
#plt.suptitle('Dose rate behind marble shielding', fontsize = 25)
#plt.title('1 month cool down', fontsize = 20)
#plt.grid(linewidth = 0.3)
#plt.ylabel('uSv/h', fontsize = 16)
#plt.xlabel('cm from marble shielding', fontsize = 16)
#plt.show()
#


