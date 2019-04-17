# -*- coding: utf-8 -*-
"""
Created on Tue Apr 03 10:59:52 2018

@author: cbjorkma
"""

#ShieldingParameterization



from USRBIN import USRBIN

import os

path = '//rpclustergw/cbjorkma/Scrapers/ShieldingParameterization'

os.chdir(path)

#files = files.sort()

norm = 0.0036

files = sorted(os.listdir(path))
files = filter(lambda x: x[-2:] == '25',files)
list = []
for i in range(len(files)):
    file = files[i]
    tmp = USRBIN(file,path,0.0036)
    tmp.read()
    tmp.calc()
    list.append(tmp)
    
files2 = sorted(os.listdir(path))
files2 = filter(lambda x: x[-2:] == '27',files2)
list2 = []
for i in range(len(files)):
    file = files2[i]
    tmp = USRBIN(file,path,0.0036)
    tmp.read()
    tmp.calc()
    list2.append(tmp)
 



import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm

plt.close()
plt.close()
xes = range(0,250-250/15*4,250/15)

fig = plt.figure()

for i in range(len(files)):
        
    plt.subplot(3,2,i +1)
    
    plt.pcolor(list[i].horizontal,norm=LogNorm(), cmap='jet')
    cbar = plt.colorbar()
    plt.title(list[i].filename)
    
plt.show()

lengths = [15,18,20,22.5 , 25]


fig = plt.figure()


ax = plt.subplot(1,2,1)
for i in range(len(files)):

    plt.plot(xes, list[i].cube[11:None:-1, 5:6,0]/2, label = 'Shielding width: ' +str(lengths[i]) + ' cm')
    
plt.legend()
plt.title('1 day cool down', fontsize = 20)
plt.grid(linewidth = 0.25)
plt.ylabel('uSv/h', fontsize = 16)
plt.xlabel('cm from marble shielding', fontsize = 16)
props = dict(boxstyle='round', facecolor='white', alpha=1)

#ax.text(0.25, 0.98, '1 day cool down', transform=ax.transAxes, fontsize=18, verticalalignment='top',bbox=props)     
#plt.show()



plt.subplot(1,2,2)
for i in range(len(files)):
        
    plt.plot(xes, list2[i].cube[11:None:-1, 5:6,0]/2, label = 'Shielding width: ' +str(lengths[i]) + ' cm')
    
plt.legend()
plt.suptitle('Dose rate behind marble shielding', fontsize = 25)
plt.title('1 month cool down', fontsize = 20)
plt.grid(linewidth = 0.3)
plt.ylabel('uSv/h', fontsize = 16)
plt.xlabel('cm from marble shielding', fontsize = 16)
plt.show()






fig = plt.figure()


ax = plt.subplot(1,2,1)
for i in range(len(files)):

    plt.plot(xes, list[i].cube[11:None:-1, 5:6,0]/2, label = 'Shielding width: ' +str(lengths[i]) + ' cm')
    
plt.legend()
plt.title('1 day cool down', fontsize = 20)
plt.grid(linewidth = 0.25)
plt.ylabel('uSv/h', fontsize = 16)
plt.xlabel('cm from marble shielding', fontsize = 16)
props = dict(boxstyle='round', facecolor='white', alpha=1)




















