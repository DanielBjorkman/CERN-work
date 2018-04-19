# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 10:29:22 2018

@author: cbjorkma
"""

#FlukaVersionCompare

import matplotlib.pyplot as plt

from USRBIN import USRBIN
plt.close()
plt.close()
plt.close()

import os


path = '//rpclustersrv1/cbjorkma/LSS2/FlukaversionCompare' 

os.chdir(path)


filenames = os.listdir(path)

#data = []
#
#for i in range(len(filenames)):
#    x = USRBIN(filenames[i],path, 0.0036)
#    x.read()
#    x.calc()
#    data.append(x)
#    
#    



fig = plt.figure()

plt.subplot(221)

cube = data[1]
plt.plot(cube.xcoodinates, cube.depthdeposition, label = 'New Fluka version')

cube = data[3]
plt.plot(cube.xcoodinates, cube.depthdeposition, label = 'Old Fluka version')

plt.xlabel('z [~cm]')
plt.ylabel('Integrated dose rate [uSv/h]')

plt.grid(linewidth = 0.4)

plt.title('1 hour cool down')
plt.legend()

plt.subplot(222)

cube = data[0]
plt.plot(cube.xcoodinates, cube.depthdeposition, label = 'New Fluka version')

cube = data[2]
plt.plot(cube.xcoodinates, cube.depthdeposition, label = 'Old Fluka version')

plt.xlabel('z [~cm]')
plt.ylabel('Integrated dose rate [uSv/h]')

plt.grid(linewidth = 0.4)

plt.title('1 week cool down')


plt.suptitle('Integrated dose rate comparison', fontsize = 20)


plt.legend()


plt.subplot(223)

cube1 = data[1]
#plt.plot(cube.xcoodinates, cube.depthdeposition, label = 'New Fluka version')

cube2 = data[3]
plt.plot(cube.xcoodinates, cube2.depthdeposition/cube1.depthdeposition, label = 'Old/New Fluka version')


plt.xlabel('z [~cm]')
plt.ylabel('Ratio')
plt.axhline(y=1, color='k', linestyle='-')
plt.grid(linewidth = 0.4)

plt.title('1 hour cool down')
plt.legend()


plt.subplot(224)

cube1 = data[0]
#plt.plot(cube.xcoodinates, cube.depthdeposition, label = 'New Fluka version')

cube2 = data[2]
plt.plot(cube.xcoodinates, cube2.depthdeposition/cube1.depthdeposition, label = 'Old/New Fluka version')


plt.xlabel('z [~cm]')
plt.ylabel('Ratio')
plt.axhline(y=1, color='k', linestyle='-')
plt.grid(linewidth = 0.4)

plt.title('1 week cool down')
plt.legend()







plt.show()



from matplotlib.colors import LogNorm

fig = plt.figure()

plt.subplot(221)

cube1 = data[1]
cube2 = data[3]
#cube = data[1]

vmax = 10**4
vmin = 10**-1

image = cube1.horizontal
plt.pcolor(image, norm=LogNorm(vmin=vmin, vmax=vmax), cmap='jet')
cbar = plt.colorbar()
cbar.set_label('uSv/h')
plt.xlabel('z [~cm]')
plt.ylabel('x [bins]')

plt.title('New Fluka verison')

plt.subplot(222)
#cube = data[3]
image = cube2.horizontal
plt.pcolor(image, norm=LogNorm(vmin=vmin, vmax=vmax), cmap='jet')
cbar = plt.colorbar()
cbar.set_label('uSv/h')
plt.title('Old Fluka verison')

plt.xlabel('z [~cm]')
plt.ylabel('x [bins]')



plt.subplot(223)

image = cube2.horizontal - cube1.horizontal
plt.pcolor(image, cmap='jet')
cbar = plt.colorbar()
cbar.set_label('Old - New [uSv/h]')
plt.title('Old Fluka - New Fluka')

plt.xlabel('z [~cm]')
plt.ylabel('x [bins]')




plt.suptitle('Horizontal sampling at beam height. Dose rate comparison. 1 h cool down', fontsize = 20)

plt.show()



#----------------------------------------------------------------------------


fig = plt.figure()

plt.subplot(221)

cube1 = data[0]
cube2 = data[2]
#cube = data[1]

vmax = 3*10**3
vmin = 10**-1

image = cube1.horizontal
plt.pcolor(image, norm=LogNorm(vmin=vmin, vmax=vmax), cmap='jet')
cbar = plt.colorbar()
cbar.set_label('uSv/h')
plt.xlabel('z [~cm]')
plt.ylabel('x [bins]')

plt.title('New Fluka verison')

plt.subplot(222)
#cube = data[3]
image = cube2.horizontal
plt.pcolor(image, norm=LogNorm(vmin=vmin, vmax=vmax), cmap='jet')
cbar = plt.colorbar()
cbar.set_label('uSv/h')
plt.title('Old Fluka verison')

plt.xlabel('z [~cm]')
plt.ylabel('x [bins]')



plt.subplot(223)

image = cube2.horizontal - cube1.horizontal
plt.pcolor(image, cmap='jet')
cbar = plt.colorbar()
cbar.set_label('Old - New [uSv/h]')
plt.title('Old Fluka - New Fluka')

plt.xlabel('z [~cm]')
plt.ylabel('x [bins]')




plt.suptitle('Horizontal sampling at beam height. Dose rate comparison. 1 week cool down', fontsize = 20)

plt.show()































