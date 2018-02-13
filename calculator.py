# -*- coding: utf-8 -*-
"""
Created on Fri Feb 02 15:36:18 2018

@author: cbjorkma
"""

#calculator


point1 = [0,1.77]

point2 = [500,2.06]


import math
import numpy as np


print math.degrees(np.arctan((point2[1] - point1[1]) /500)) + math.degrees(np.arctan((0.02) /500))