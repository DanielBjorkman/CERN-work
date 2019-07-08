# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 16:19:52 2018

@author: cbjorkma
"""

#ConcreteAnalysis 2



import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt

plt.close()
plt.close()
plt.close()
plt.close()
plt.close()


path = '//cern.ch/dfs/Users/c/cbjorkma/Documents/Dump TIDGV5'
os.chdir(path)


filename = 'Danielall_weight%.xlsx'

thefile = pd.read_excel(filename)

elements = []
structural = []
structuralError = []
foamed = []
foamedError = []



vec = [13,14,15,16,17]
for i in range(len(thefile.Major)):
    if i not in vec:
        elements.append(thefile.Major[i])
        structural.append(thefile.Structural1[i])
        structuralError.append(thefile.structuralError[i])
        foamed.append(thefile.Foamed1[i])
        foamedError.append(thefile.foamedError[i])
        
    
foamedError[10] = 0



transp = 0.5

fig = plt.figure()
ax = plt.subplot(111)

width = 0.01
x = np.arange(len(elements))

plt.bar(x -width,structural, yerr = structuralError, label = 'Structural')
plt.bar(x +width,foamed, yerr = foamedError, label = 'Foamed', alpha = transp)

plt.xticks(x)
ax.set_xticklabels(elements)

#plt.ylabel('Fraction',fontsize = 20)
plt.yscale("log", nonposy='clip')

plt.legend()

plt.show()



oxygenMass = 15.999



siliconeMass = 28.0855
titaniumMass = 47.867 #Ti
aluMass = 26.98153
ironMass = 55.845
manganeseMass = 54.938 #Mn
magnesiumMass = 24.305 #Mg
calciumMass = 40.078
sodiumMass = 22.989769
potassiumMass = 39.0983
fosfor = 30.973762 #P
chromMass = 51.9961 #Cr
nickelMass = 58.6934 #Ni
Carbon = 12


elements2 = []
structural2 = []
structuralError2 = []
foamed2 = []
foamedError2 = []

#Oxygen
elements2.append('O')
structural2.append(thefile.Structural1[0]*2*oxygenMass/(siliconeMass + 2*oxygenMass) + 
                   thefile.Structural1[1]*2*oxygenMass/(titaniumMass + 2*oxygenMass) + 
                   thefile.Structural1[2]*3*oxygenMass/(2*aluMass + 3*oxygenMass) + 
                   thefile.Structural1[3]*3*oxygenMass/(2*ironMass + 3*oxygenMass) +
                   thefile.Structural1[4]*1*oxygenMass/(1*manganeseMass + 1*oxygenMass) +
                   thefile.Structural1[5]*1*oxygenMass/(1*magnesiumMass + 1*oxygenMass) +
                   thefile.Structural1[6]*1*oxygenMass/(1*calciumMass + 1*oxygenMass) +
                   thefile.Structural1[7]*1*oxygenMass/(2*sodiumMass + 1*oxygenMass) +
                   thefile.Structural1[8]*1*oxygenMass/(2*potassiumMass + 1*oxygenMass) +
                   thefile.Structural1[9]*5*oxygenMass/(2*fosfor + 5*oxygenMass) +
                   thefile.Structural1[10]*2*oxygenMass/(1*Carbon + 2*oxygenMass) +
                   thefile.Structural1[11]*3*oxygenMass/(2*chromMass + 3*oxygenMass) +
                   thefile.Structural1[12]*1*oxygenMass/(1*nickelMass + 1*oxygenMass) 
                   )
foamed2.append(    thefile.Foamed1[0]*2*oxygenMass/(siliconeMass + 2*oxygenMass) + 
                   thefile.Foamed1[1]*2*oxygenMass/(titaniumMass + 2*oxygenMass) + 
                   thefile.Foamed1[2]*3*oxygenMass/(2*aluMass + 3*oxygenMass) + 
                   thefile.Foamed1[3]*3*oxygenMass/(2*ironMass + 3*oxygenMass) +
                   thefile.Foamed1[4]*1*oxygenMass/(1*manganeseMass + 1*oxygenMass) +
                   thefile.Foamed1[5]*1*oxygenMass/(1*magnesiumMass + 1*oxygenMass) +
                   thefile.Foamed1[6]*1*oxygenMass/(1*calciumMass + 1*oxygenMass) +
                   thefile.Foamed1[7]*1*oxygenMass/(2*sodiumMass + 1*oxygenMass) +
                   thefile.Foamed1[8]*1*oxygenMass/(2*potassiumMass + 1*oxygenMass) +
                   thefile.Foamed1[9]*5*oxygenMass/(2*fosfor + 5*oxygenMass) +
                   thefile.Foamed1[10]*2*oxygenMass/(1*Carbon + 2*oxygenMass) +
                   thefile.Foamed1[11]*3*oxygenMass/(2*chromMass + 3*oxygenMass) +
                   thefile.Foamed1[12]*1*oxygenMass/(1*nickelMass + 1*oxygenMass) 
                   )



#Silicone
elements2.append('Si')
structural2.append(thefile.Structural1[0]*siliconeMass/(siliconeMass + 2*oxygenMass))
foamed2.append(thefile.Foamed1[0]*siliconeMass/(siliconeMass + 2*oxygenMass))

#Titanium
elements2.append('Ti')
structural2.append(thefile.Structural1[1]*titaniumMass/(titaniumMass + 2*oxygenMass))
foamed2.append(thefile.Foamed1[1]*titaniumMass/(titaniumMass + 2*oxygenMass))

#Aluminium
elements2.append('Al')
structural2.append(thefile.Structural1[2]*2*aluMass/(2*aluMass + 3*oxygenMass))
foamed2.append(thefile.Foamed1[2]*2*aluMass/(2*aluMass + 3*oxygenMass))


#Iron
elements2.append('Fe')
structural2.append(thefile.Structural1[3]*2*ironMass/(2*ironMass + 3*oxygenMass))
foamed2.append(thefile.Foamed1[3]*2*ironMass/(2*ironMass + 3*oxygenMass))

#Manganese
elements2.append('Mn')
structural2.append(thefile.Structural1[4]*1*manganeseMass/(1*manganeseMass + 1*oxygenMass))
foamed2.append(thefile.Foamed1[4]*1*manganeseMass/(1*manganeseMass + 1*oxygenMass))


#Mangnesium
elements2.append('Mg')
structural2.append(thefile.Structural1[5]*1*magnesiumMass/(1*magnesiumMass + 1*oxygenMass))
foamed2.append(thefile.Foamed1[5]*1*magnesiumMass/(1*magnesiumMass + 1*oxygenMass))


#Calcium
elements2.append('Ca')
structural2.append(thefile.Structural1[6]*1*calciumMass/(1*calciumMass + 1*oxygenMass) )
foamed2.append(thefile.Foamed1[6]*1*calciumMass/(1*calciumMass + 1*oxygenMass) )

#Sodium
elements2.append('Na')
structural2.append(thefile.Structural1[7]*2*sodiumMass/(2*sodiumMass + 1*oxygenMass) )
foamed2.append(thefile.Foamed1[7]*2*sodiumMass/(2*sodiumMass + 1*oxygenMass) )

#Potassium
elements2.append('K')
structural2.append(thefile.Structural1[8]*2*potassiumMass/(2*potassiumMass + 1*oxygenMass) )
foamed2.append(thefile.Foamed1[8]*2*potassiumMass/(2*potassiumMass + 1*oxygenMass) )

#Fosfor
elements2.append('P')
structural2.append(thefile.Structural1[9]*2*fosfor/(2*fosfor + 5*oxygenMass)  )
foamed2.append(thefile.Foamed1[9]*2*fosfor/(2*fosfor + 5*oxygenMass) )

#Carbon
elements2.append('C')
structural2.append(thefile.Structural1[10]*1*Carbon/(1*Carbon + 2*oxygenMass)  )
foamed2.append(thefile.Foamed1[10]*1*Carbon/(1*Carbon + 2*oxygenMass)  )


#Chrom
elements2.append('Cr')
structural2.append(thefile.Structural1[11]*2*chromMass/(2*chromMass + 3*oxygenMass)  )
foamed2.append(thefile.Foamed1[11]*2*chromMass/(2*chromMass + 3*oxygenMass)   )

##Nickle
#elements2.append('Ni')
#structural2.append(thefile.Structural1[12]*1*nickelMass/(1*nickelMass + 1*oxygenMass)  )
#foamed2.append(thefile.Foamed1[12]*1*nickelMass/(1*nickelMass + 1*oxygenMass)   )

idx = elements.index('Ni')
structural[idx] = structural[idx] + thefile.Structural1[12]*1*nickelMass/(1*nickelMass + 1*oxygenMass)
foamed[idx] = foamed[idx] + thefile.Foamed1[12]*1*nickelMass/(1*nickelMass + 1*oxygenMass) 


for i in range(13, len(elements)):
    elements2.append(elements[i])
    print elements[i]
    structural2.append(structural[i])
    foamed2.append(foamed[i])

print 100 - sum(structural2)
elements2.append('H')
elements2.append('S')
elements2.append('Zn')
structural2.append(100 - sum(structural2))
foamed2.append(100 -sum(foamed2))
structural2.append(0)
foamed2.append(0)
structural2.append(0)
foamed2.append(0)







path = '//rpclustergw/cbjorkma/Dump studies/Uppstream Hole study/Fluence'
os.chdir(path)

filename = 'Concrete2ChangedFormat.mat'

file = file_object  = open(filename, 'r')

lines = file.readlines()
lines = lines[2:]

fluka = np.zeros(len(elements2))

for i in range(len(lines)):
    string = lines[i].split('\t')
    fluka[elements2.index(string[0])] = float(string[1][:-1])







struct = np.zeros(len(elements2))
fom = np.zeros(len(elements2))
for i in range(0, len(elements2)):
    struct[i] = structural2[i]/100
    fom[i] = foamed2[i]/100



elements2[elements2.index('H')] = 'H**'


fig = plt.figure()
ax = plt.subplot(111)
transp = 0.70

width = 0.30
x = np.arange(len(elements2))

plt.bar(x -width, struct,width = width, label = 'Structural sample')
plt.bar(x  , fom,width = width, label = 'Foamy sample', alpha = transp, color = 'g') #/sum(foamed)
plt.bar(x + width ,fluka,width = width, label = 'Fluka', alpha = transp, color = 'r')

plt.xticks(x)
ax.set_xticklabels(elements2)

plt.ylabel('Fraction',fontsize = 20)
plt.yscale("log", nonposy='clip')
#plt.title('Structural concrete composition',fontsize = 16)

plt.legend()



plt.title('Concrete composition comparison. Samples extracted from ECX5 abutment',fontsize = 22)


plt.xlabel('*for Co, the estimated mean is a maximal estimate; the true value is lower, because the actually measured signal is a collective signal of 59Co+ and 43Ca16O+, while the sample is depleted in Co and enriched in Ca.\n ** Hydrogen added after best estimate     ')


plt.show()



print 'Fluka: ' + str(sum(fluka))

print 'Structural: ' + str(sum(struct))

print 'Foamed: ' + str(sum(fom))




fig = plt.figure()


ax = plt.subplot(211)
plt.title('Concrete composition comparison. Samples extracted from ECX5 abutment',fontsize = 22)
transp = 0.70

width = 0.30
x = np.arange(len(elements2))

stop = len(x)/2

plt.bar(x[0:stop] -width, struct[0:stop],width = width, label = 'Structural sample')
plt.bar(x[0:stop]  , fom[0:stop],width = width, label = 'Foamy sample', alpha = transp, color = 'g') #/sum(foamed)
#plt.bar(x[0:stop] + width ,fluka[0:stop],width = width, label = 'Fluka', alpha = transp, color = 'r')

plt.xticks(x[0:stop])
ax.set_xticklabels(elements2[0:stop])

plt.ylabel('Fraction',fontsize = 20)
plt.yscale("log", nonposy='clip')
#plt.title('Structural concrete composition',fontsize = 16)

plt.legend()

ax = plt.subplot(212)

plt.title('Continuation',fontsize = 14)

plt.bar(x[stop:] -width, struct[stop:],width = width, label = 'Structural sample')
plt.bar(x[stop:]  , fom[stop:],width = width, label = 'Foamy sample', alpha = transp, color = 'g') #/sum(foamed)
#plt.bar(x[stop:] + width ,fluka[stop:],width = width, label = 'Fluka', alpha = transp, color = 'r')

plt.xticks(x[stop:])
ax.set_xticklabels(elements2[stop:])

plt.ylabel('Fraction',fontsize = 20)
plt.yscale("log", nonposy='clip')




plt.xlabel('*for Co, the estimated mean is a maximal estimate; the true value is lower.\n ** Hydrogen added post-analysis', fontsize = 12)


plt.show()





x = x[0:-2]
struct = struct[0:-2]
fom = fom[0:-2]
elements2 = elements[0:-2]

fig = plt.figure()


ax = plt.subplot(211)
plt.title('Concrete composition comparison. Samples extracted from ECX5 abutment',fontsize = 22)
transp = 0.70

width = 0.30
x = np.arange(len(elements2))

stop = len(x)/2

plt.bar(x[0:stop] -width, struct[0:stop],width = width, label = 'Structural sample')
plt.bar(x[0:stop]  , fom[0:stop],width = width, label = 'Foamy sample', alpha = transp, color = 'g') #/sum(foamed)
#plt.bar(x[0:stop] + width ,fluka[0:stop],width = width, label = 'Fluka', alpha = transp, color = 'r')

plt.xticks(x[0:stop])
ax.set_xticklabels(elements2[0:stop])

plt.ylabel('Fraction',fontsize = 20)
plt.yscale("log", nonposy='clip')
#plt.title('Structural concrete composition',fontsize = 16)

plt.legend()

ax = plt.subplot(212)

plt.title('Continuation',fontsize = 14)

plt.bar(x[stop:] -width, struct[stop:],width = width, label = 'Structural sample')
plt.bar(x[stop:]  , fom[stop:],width = width, label = 'Foamy sample', alpha = transp, color = 'g') #/sum(foamed)
#plt.bar(x[stop:] + width ,fluka[stop:],width = width, label = 'Fluka', alpha = transp, color = 'r')

plt.xticks(x[stop:])
ax.set_xticklabels(elements2[stop:])

plt.ylabel('Fraction',fontsize = 20)
plt.yscale("log", nonposy='clip')




plt.xlabel('*for Co, the estimated mean is a maximal estimate; the true value is lower.\n ** Hydrogen added post-analysis', fontsize = 12)


plt.show()








