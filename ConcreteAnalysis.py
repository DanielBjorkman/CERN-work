# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 10:24:57 2018

@author: cbjorkma
"""

#ConcreteAnalysis


import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt

plt.close()
plt.close()
plt.close()
plt.close()
plt.close()


path = '//rpclustersrv1/cbjorkma/Dump studies'
os.chdir(path)


filename = 'CERN_Structural_Foamed.xlsx'

thefile = pd.read_excel(filename)

elements = list(thefile)
elements = elements[4:]

#file_object  = open('ElementMasses.txt', 'r+')
#
#for i in range(len(elements)):
#    file_object.write(elements[i] + '\n')
#file.close()
#

print len(elements)

oxygenMass = 15.999
aluMass = 26.98153
calciumMass = 40.078
manganeseMass = 54.938



newelements = ['H','C','O', 'Al', 'Ca', 'Mn','Fe', 'Mg', 'P','K', 'Si', 'Na', 'S', 'Zn']
elements = newelements + elements





masses = {}







foamed = np.zeros(len(elements))
foamedErrors = np.zeros(len(elements))
structural = np.zeros(len(elements))
structuralErrors = np.zeros(len(elements))
mass = np.zeros(len(elements))
fluka = np.zeros(len(elements))


for i in range(len(newelements), len(elements)):
    
    values = thefile[elements[i]]
    
    mass[i] = values[0]
    structural[i] = values[7]/10**6
    structuralErrors[i] = values[8]/10**6
    foamed[i] = values[16]/10**6
    foamedErrors[i] = values[17]/10**6
    
    
    
    
    
#Aluminium
i =3 
structural[i] = thefile['Al2O3'][7] * 2*aluMass/(2*aluMass + 3*oxygenMass)/100
foamed[i] = thefile['Al2O3'][16] * 2*aluMass/(2*aluMass + 3*oxygenMass)/100

#Oxygen
i = 2
structural[i] = (thefile['Al2O3'][7] * 3*oxygenMass/(2*aluMass + 3*oxygenMass) + thefile['CaO'][7]*oxygenMass/(oxygenMass + calciumMass) + thefile['MnO'][7]* oxygenMass/(oxygenMass + manganeseMass))/100
foamed[i] = (thefile['Al2O3'][16] * 3*oxygenMass/(2*aluMass + 3*oxygenMass) + thefile['CaO'][16]*oxygenMass/(oxygenMass + calciumMass) + thefile['MnO'][16]* oxygenMass/(oxygenMass + manganeseMass))/100


#Calcium
i = 4
structural[i] = thefile['CaO'][7] *calciumMass/(oxygenMass + calciumMass)/100
foamed[i] = thefile['CaO'][16] * calciumMass/(oxygenMass + calciumMass) /100


#Manganese
i = 5
structural[i] = thefile['MnO'][7] *manganeseMass/(oxygenMass + manganeseMass)/100
foamed[i] = thefile['MnO'][16] * manganeseMass/(oxygenMass + calciumMass) /100




#sum(structural[0:])


path = '//rpclustersrv1/cbjorkma/Dump studies/Uppstream Hole study/Fluence'

os.chdir(path)

filename = 'Concrete2ChangedFormat.mat'

file = file_object  = open(filename, 'r')

lines = file.readlines()
lines = lines[2:]

for i in range(len(lines)):
    string = lines[i].split('\t')
    fluka[elements.index(string[0])] = float(string[1][:-1])




fig = plt.figure()

transp = 0.70

ax = plt.subplot(211)

plt.bar(elements, structural,yerr=structuralErrors, label = 'Sample analysis')

plt.bar(elements,fluka/sum(fluka), label = 'Fluka', alpha = transp, color = 'r')

plt.ylabel('%',fontsize = 16)
plt.yscale("log", nonposy='clip')
plt.title('Structural concrete composition',fontsize = 16)

plt.legend()

ax = plt.subplot(212)

plt.bar(elements, foamed ,yerr=foamedErrors, label = 'Sample analysis') #/sum(foamed)

plt.bar(elements,fluka/sum(fluka), label = 'Fluka', alpha = transp, color = 'r')

plt.ylabel('%',fontsize = 20)
plt.yscale("log", nonposy='clip')
plt.title('Foamed concrete composition',fontsize = 16)

plt.legend()

plt.xlabel('*for Co, the estimated mean is a maximal estimate; the true value is lower, because the actually measured signal is a collective signal of 59Co+ and 43Ca16O+, while the sample is depleted in Co and enriched in Ca    ')




plt.suptitle('Concrete composition comparison',fontsize = 22)

plt.show()




fig = plt.figure()
ax = plt.subplot(111)
transp = 0.70

width = 0.30
x = np.arange(len(elements))

plt.bar(x, structural,yerr= structuralErrors,width = width, label = 'Structural sample')
plt.bar(x -width , foamed,width = width,yerr=foamedErrors, label = 'Foamy sample', alpha = transp, color = 'g') #/sum(foamed)
plt.bar(x + width ,fluka,width = width, label = 'Fluka', alpha = transp, color = 'r')

plt.xticks(x)
ax.set_xticklabels(elements)

plt.ylabel('Fraction',fontsize = 20)
plt.yscale("log", nonposy='clip')
#plt.title('Structural concrete composition',fontsize = 16)

plt.legend()



plt.title('Concrete composition comparison',fontsize = 22)


plt.xlabel('*for Co, the estimated mean is a maximal estimate; the true value is lower, because the actually measured signal is a collective signal of 59Co+ and 43Ca16O+, while the sample is depleted in Co and enriched in Ca    ')


plt.show()



print 'Fluka: ' + str(sum(fluka))

print 'Structural: ' + str(sum(structural))

print 'Foamed: ' + str(sum(foamed))














