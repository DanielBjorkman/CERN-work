# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 09:55:51 2018

@author: cbjorkma
"""

#TIDP activation comparison

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
##
#path = '//rpclustersrv1/cbjorkma/Dump studies/MaskComparison/WithMask'
#os.chdir(path)
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