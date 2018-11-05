# -*- coding: utf-8 -*-
"""
Created on Wed Aug 01 10:49:50 2018

@author: cbjorkma
"""

#Dump deposition comparison




import matplotlib.pyplot as plt
plt.close()
plt.close()
plt.close()
plt.close()
plt.close()
plt.close()
plt.close()
plt.close()

#from scipy import interp
#import math
import matplotlib.patches as patches
from USRBIN import USRBIN

normfactor = 0.0036

import os


path = '//rpclustersrv1/cbjorkma/Dump studies'
os.chdir(path)

filename = 'Dump15_1h'

try:
    print Dump15
except:
    Dump15 = USRBIN(filename, path, normfactor)
    Dump15.read()
Dump15.calc()


filename = 'DumpOld_21.bnn.lis'

#try:
#    print Dump8
#except:
Dump8 = USRBIN(filename, path, normfactor)
Dump8.read()
Dump8.calc()


fig = plt.figure()

ax =plt.subplot(111)

plt.plot(Dump8.xcoodinates, Dump8.depthdeposition, label = 'Original Dump Design')
plt.plot(Dump15.xcoodinates, Dump15.depthdeposition, label = 'Current Dump Design')
plt.yscale("log", nonposy='clip')
plt.legend()
plt.ylabel('Integrated dose rate [uSv/h]', fontsize = 16)
plt.xlabel('z [cm]', fontsize = 16)
plt.grid(linewidth = 0.4)
plt.title('Fluka dump model version compare. 1h cool down', fontsize = 20)

ax2 = ax.twinx()

r1 = patches.Rectangle((-925,0), 860,5, color = 'Brown', alpha = 0.3)

ax2.add_patch(r1)
ax2.get_yaxis().set_visible(False)


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
