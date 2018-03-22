# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 09:36:30 2018

@author: cbjorkma
"""

#Camera data evaluation


from Flukato3dMatrix import Flukato3dMatrix
import numpy as np
import os 
import math


path ='//rpclustersrv1/cbjorkma/Dump studies'


os.chdir(path)

filename = 'Dump10ResCamera3Bias2_93.bnn.lis'

cube = Flukato3dMatrix(filename, path,1)

cube = cube * 2*10**18

import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
import matplotlib.gridspec as gridspec
import matplotlib.ticker as ticker





errors = np.genfromtxt(filename, skip_header= 32) #, skip_header= 34, skip_footer= 53
errors = np.reshape(errors ,(errors.size,1))
errors = np.reshape(errors, (5,5,8),order='F')






ax = plt.subplot(121)
image = cube[2,0:,0:]
plt.pcolor(image,norm=LogNorm(), cmap='jet')
cbar = plt.colorbar()
cbar.set_label('Fluence [cm-2]')
plt.title('HEHAD fluence')
plt.xlabel('z [bins]')
plt.ylabel('y [bins]')

ax = plt.subplot(122)
image = errors[2,0:,0:]
plt.pcolor(image, cmap='jet')
cbar = plt.colorbar()
cbar.set_label('Error')
plt.title('HEHAD errors')
plt.xlabel('z [bins]')
plt.ylabel('y [bins]')


plt.show()







