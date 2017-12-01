# -*- coding: utf-8 -*-
"""
Created on Fri Jul 21 09:49:49 2017

@author: cbjorkma
"""

#Validated phase space

import numpy as np

points = np.zeros([3,3,3])


#On momentum 400 GeV/c
#p2
points[0,0:,0] = [7.2, 0.000170, 1]

#p5
points[1,0:,0] = [8.0, 0.000180, 1]

#p8
points[2,0:,0] = [8.4, 0.000185, 1]

#Off momentum at 399.4 GeV/c
#p1
points[0,0:,1] =  [7.2 , 0.0002, 1]

#p4
points[1,0:,1] = [8.0,0.000215, 1]

#7
points[2,0:,1] = [8.6,0.00025, 1]


#Off momentum at 400.6 GeV/c
#p3
points[0,0:,2] =  [7.2 , 0.00014, 0]

#p6
points[1,0:,2] = [8,0.000145, 0]

#9
points[2,0:,2] = [8.5,0.00015,0]



nomP = 400


import matplotlib.pyplot as plt

plt.scatter(points[0:,0,0],points[0:,1,0])
plt.show()


newP = (1-0.0015) * 400


