# -*- coding: utf-8 -*-
"""
Created on Wed Jul 03 14:37:28 2019

@author: cbjorkma
"""

#Dice

import random

min = 1
max = 6

tries = 100000000

list = []
count = 0
for i in range(1000):
    val1 = random.randint(min,max)
    val2 = random.randint(min,max)
    list.append(val1 + val2 )
    if (val1 != val2 and val1 + val2 == 6):
        count = count +1
    
    
print float(count) / float(tries)
    
import matplotlib.pyplot as plt

figure = plt.figure()

plt.hist(list, normed = tries)

plt.show()

