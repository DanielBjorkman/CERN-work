# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 13:15:17 2019

@author: cbjorkma
"""

#JTT_resnuc



import os


path = '//rpclustergw/cbjorkma/ATLAS/ResNuc_JTT'
os.chdir(path)


#filenames = sorted(os.listdir(path))

filenames = []
filenames.append('JTTin3m_63_tab.lis')
filenames.append('JTTOUT3m_74_tab.lis')


resnucs = []

#mass = 1.42E7 #[g]
mass = 1



nuc = []



import numpy as np




for i in range(len(filenames)):

    data = np.loadtxt(filenames[i], skiprows = 2)
    data[0:,2] = data[0:,2]/mass
    
    
    if i == 0:
        nuc = zip(data[0:,0], data[0:,1])
        vals = np.zeros((len(nuc),len(filenames)))
        vals[0:,0] = data[0:,2]
        errors = np.zeros((len(nuc),len(filenames)))
        errors[0:,0] = data[0:,3]
        impNuc = zip(nuc,data[0:,2])
        impNuc.sort(key = lambda x: x[1])
    else:
        tempNuc = zip(data[0:,0], data[0:,1])
        for j in range(len(tempNuc)):
            idx = nuc.index(tempNuc[j])
            vals[idx,i] = data[j,2]
            errors[idx,i] = data[j,3]
    

cooldowns = ['3m', '4m' , '5m' , '6m', '1y']


import matplotlib.pyplot as plt

fig = plt.figure()

ax = plt.subplot(111)

xes = np.linspace(0,len(filenames)-1, len(filenames))


ignoreBottom = int(len(impNuc)*0.92)

for i in range(len(impNuc)-1,-1 + ignoreBottom,-1):
    idx = nuc.index(impNuc[i][0])
    if sum(vals[idx,0:]) == 0:
        pass;
    else:
        plt.errorbar(xes , vals[idx,0:], yerr = vals[idx,0:]*errors[idx,0:]/100 , label = nuc[idx])






#for i in range(len(vals[0:,0])):
#    if sum(vals[i,0:]) == 0:
#        pass;
#    else:
#        plt.plot(xes , vals[i,0:], label = nuc[i])






plt.legend()

ax.set_yscale("log", nonposy='clip')

plt.ylim(10**-10,10**3)

plt.ylabel('Bq/g', fontsize = 22)
plt.xlabel('Cooldown time', fontsize = 22)

plt.title('Residual nuclei within the JTT', fontsize = 26)

plt.xticks(np.arange(5), cooldowns)

plt.grid(linewidth = 0.3 )

plt.show()













import matplotlib.gridspec as gridspec

#tags = ['a', 'b', 'c' , 'd' , 'e', 'f', 'h' , 'a', 'a', 'a']

tags = ['Fe-55', 'Mn-54' , 'V-49' , 'Cr-51' , 'H-3', 'Sc-46' , 'Be-7' , 'Fe-59' , 'Co-56' , 'V-48' , 'S-35']

import matplotlib.pyplot as plt

fig = plt.figure()


gs = gridspec.GridSpec(3, 3)

ax1 = plt.subplot(gs[0:2, 0:])

#xes = np.linspace(0,len(filenames)-1, len(filenames))


#ignoreBottom = int(len(impNuc)*0.92)

top = 11

xes = range(0,top)
vec1 = np.zeros(top )
vec2 = np.zeros(top )
tags1 = []
tags2 = []
counter = 0
for i in range(len(impNuc)-1,len(impNuc)-top -1,-1):
    idx = nuc.index(impNuc[i][0])
    print impNuc[i][0]
    vec1[counter] = vals[idx,0]
    vec2[counter] = vals[idx,1]
    counter = counter +1
    tags1.append(nuc[idx])
    

m1 = 2.185e6
m2 = 1.191 * 10**7.

vec1 = vec1/m1
vec2 = vec2/m2


plt.bar(xes , vec1,width = 0.8, label = 'Inner JTT')
plt.bar(xes , vec2,width = 0.8, label = 'Outer JTT')
plt.legend()
    
ax1.set_yscale("log", nonposy='clip')

plt.ylabel('Bq/g', fontsize = 20)

plt.xticks(xes, tags)
plt.legend()


ax2 = plt.subplot(gs[2, 0:])

#temp = np.zeros(top+1)
#temp2 = np.zeros(top+1)
#temp3 = np.zeros(top+1)
#
#vec1temp = vec1
#vec2temp = vec2
#vec1 = temp2
#vec2 = temp3
#
#
#vec1[0:-1] = vec1temp
#vec2[0:-1] = vec2temp



plt.bar(xes , vec1/vec2, width = 0.8, label = 'Inner / Outer')


plt.ylabel('Ratio', fontsize = 20)
plt.xticks(xes, tags)
plt.legend()

plt.suptitle('JTT residual nuclei after 3m cool down', fontsize = 26)



plt.show()





#i = 1
#
#data = np.loadtxt(filenames[i], skiprows = 2)
#data[0:,2] = data[0:,2]/mass
#
#nuc2 = zip(data[0:,0], data[0:,1])
#
#i = 2
#
#data = np.loadtxt(filenames[i], skiprows = 2)
#data[0:,2] = data[0:,2]/mass
#
#nuc3 = zip(data[0:,0], data[0:,1])
#
#
#
#i = 3
#
#data = np.loadtxt(filenames[i], skiprows = 2)
#data[0:,2] = data[0:,2]/mass
#
#nuc4 = zip(data[0:,0], data[0:,1])
#




#path = '//rpclustergw/cbjorkma/ATLAS/LLcalc'
#os.chdir(path)
#
#import pandas as pd
#
#
#data = pd.read_pickle("decaydata.pkl")
#
#










#out = open('out' , 'w')
#
#for i in range(len(file)): 
#    out.write(str(file[i].split()[1]) + '\n')
#out.close()




