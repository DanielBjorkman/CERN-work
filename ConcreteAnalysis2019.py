# -*- coding: utf-8 -*-
"""
Created on Tue Jun 04 11:38:38 2019

@author: cbjorkma
"""

#ConcreteAnalysis2019 




import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt

#plt.close()
#plt.close()
#plt.close()
#plt.close()
#plt.close()


path = '//rpclustergw/cbjorkma/Dump studies'
os.chdir(path)


filename = 'ConcreteAnalysis2019.xlsx'

thefile = pd.read_excel(filename)


elements = []
for col in thefile.columns:
    elements.append(str(col))

data = []
for i in elements:
    data.append(( i , thefile.iloc[0][i], thefile.iloc[1][i]))




stop = int(len(elements)/2)

fig = plt.figure()
ax = plt.subplot(211)

width = 0.30
x = np.arange(len(elements[0:stop]))

plt.bar(x[0:stop] -width/2, thefile.iloc[0][0:stop]/100 , label = 'Sample 1', width = width)
plt.bar(x[0:stop] +width/2,thefile.iloc[1][0:stop]/100, label = 'Sample 2', width = width)

plt.xticks(x)
ax.set_xticklabels(elements[0:stop])

plt.ylabel('Mass Fraction',fontsize = 20)
plt.yscale("log", nonposy='clip')

#for i in range(stop):
#    plt.text(x = x - width  , y = thefile.iloc[0][i] , s = round(thefile.iloc[0][i],3), size = 12)
#    plt.text(x = x   , y = thefile.iloc[1][i] , s = round(thefile.iloc[1][i],3), size = 12)
#


plt.legend()




ax = plt.subplot(212)

width = 0.30
x = np.arange(len(elements[stop:]))

plt.bar(x -width/2, thefile.iloc[0][stop:]/100 , label = 'Sample 1', width = width)
plt.bar(x +width/2,thefile.iloc[1][stop:]/100, label = 'Sample 2', width = width)

plt.xticks(x)
ax.set_xticklabels(elements[stop:])

plt.ylabel('Mass Fraction',fontsize = 20)
plt.yscale("log", nonposy='clip')

plt.legend()



plt.show()





















#print elements