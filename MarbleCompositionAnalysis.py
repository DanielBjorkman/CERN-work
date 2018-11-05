# -*- coding: utf-8 -*-
"""
Created on Tue Sep 04 10:00:08 2018

@author: cbjorkma
"""


#MarbleCompositionAnalysis



import numpy as np


calciumMass = 40.078
carbonMass = 12.0107
oxygenMass = 15.999
MgMass = 24.305
SiMass = 28.0855
aluMass = 26.98153
PMass = 30.973762
SMass = 32.065
KMass = 39.0983
FeMass = 55.845
CuMass = 63.546
SrMass = 87.62
ZrMass = 91.224 #Zirconium
NaMass = 22.989769
LiMass = 6.941

manganeseMass = 54.938




elements = ['Ca', 'C','O', 'Mg','Si','Al', 'P', 'S', 'K', 'Fe', 'Cu', 'Sr', 'Zr', 'Na', 'Li']


masses = np.zeros(len(elements))
masses2 = np.zeros(len(elements))
fluka = np.zeros(len(elements))


#CaCO3
wt = 98.5/100

idx = elements.index('Ca')
masses[idx] = masses[idx] +  wt* calciumMass/(calciumMass + carbonMass + 3*oxygenMass)

idx = elements.index('C')
masses[idx] = masses[idx] +  wt* carbonMass/(calciumMass + carbonMass + 3*oxygenMass)

idx = elements.index('O')
masses[idx] = masses[idx] +  wt* 3*oxygenMass/(calciumMass + carbonMass + 3*oxygenMass)


#CaMg(CO3)2
wt = 0.1/100

idx = elements.index('Ca')
masses[idx] = masses[idx] +  wt* calciumMass/(calciumMass + MgMass + 2*(carbonMass + 3*oxygenMass))

idx = elements.index('Mg')
masses[idx] = masses[idx] +  wt* MgMass/(calciumMass + MgMass + 2*(carbonMass + 3*oxygenMass))

idx = elements.index('C')
masses[idx] = masses[idx] +  wt* 2*carbonMass/(calciumMass + MgMass + 2*(carbonMass + 3*oxygenMass))

idx = elements.index('O')
masses[idx] = masses[idx] +  wt* 6*oxygenMass/(calciumMass + MgMass + 2*(carbonMass + 3*oxygenMass))




#SiO2
wt = 0.426/100

idx = elements.index('Si')
masses[idx] = masses[idx] +  wt* SiMass/(SiMass + 2*oxygenMass)

idx = elements.index('O')
masses[idx] = masses[idx] +  wt* 2*oxygenMass/(SiMass + 2*oxygenMass)


#Al2O3
wt = 0.0961/100

idx = elements.index('Al')
masses[idx] = masses[idx] +  wt* 2*aluMass/(2*aluMass + 3*oxygenMass)

idx = elements.index('O')
masses[idx] = masses[idx] +  wt* 3*oxygenMass/(2*aluMass + 3*oxygenMass)



#P2O5
wt = 0.0841/100

idx = elements.index('P')
masses[idx] = masses[idx] +  wt* 2*PMass/(2*PMass + 5*oxygenMass)

idx = elements.index('O')
masses[idx] = masses[idx] +  wt* 5*oxygenMass/(2*PMass + 5*oxygenMass)


#SO3
wt = 0.0376/100

idx = elements.index('S')
masses[idx] = masses[idx] +  wt* SMass/(SMass + 3*oxygenMass)

idx = elements.index('O')
masses[idx] = masses[idx] +  wt* 3*oxygenMass/(SMass + 3*oxygenMass)



#K2O
wt = 0.0269/100

idx = elements.index('K')
masses[idx] = masses[idx] +  wt* 2*KMass/(2*KMass + oxygenMass)

idx = elements.index('O')
masses[idx] = masses[idx] +  wt* 2*oxygenMass/(2*KMass + oxygenMass)



#Fe2O3
wt = 0.0619/100

idx = elements.index('Fe')
masses[idx] = masses[idx] +  wt* 2*FeMass/(2*FeMass + 3*oxygenMass)

idx = elements.index('O')
masses[idx] = masses[idx] +  wt* 3*oxygenMass/(2*FeMass + 3*oxygenMass)



#CuO
wt = 0.0077/100

idx = elements.index('Cu')
masses[idx] = masses[idx] +  wt* CuMass/(CuMass + oxygenMass)

idx = elements.index('O')
masses[idx] = masses[idx] +  wt* oxygenMass/(CuMass + oxygenMass)




#SrO
wt = 0.0444/100

idx = elements.index('Sr')
masses[idx] = masses[idx] +  wt* SrMass/(SrMass + oxygenMass)

idx = elements.index('O')
masses[idx] = masses[idx] +  wt* oxygenMass/(SrMass + oxygenMass)



#ZrO2
wt = 0.00215/100

idx = elements.index('Zr')
masses[idx] = masses[idx] +  wt* ZrMass/(ZrMass + 2*oxygenMass)

idx = elements.index('O')
masses[idx] = masses[idx] +  wt* oxygenMass/(ZrMass + 2*oxygenMass)

#Na
wt = 0.011/100
idx = elements.index('Na')
masses[idx] = masses[idx] +  wt



print 'Strictly wt%:'
print sum(masses)
print ' '





idx = elements.index('Sr')
masses[idx] = masses[idx] +  376/1000000


idx = elements.index('Li')
masses[idx] = masses[idx] +  2.75/1000000


print 'wt% + ppm:'
print sum(masses)
print ' '


#MgO
fraction = 0.0095/100


massfraction = 0.0095*0.01*40.3044/(0.0095*0.01*40.3044 + masses[elements.index('O')]*oxygenMass + masses[elements.index('Ca')]*calciumMass + masses[elements.index('C')]*carbonMass)

wt = massfraction

idx = elements.index('Mg')
masses[idx] = masses[idx] +  wt* MgMass/(MgMass + oxygenMass)

idx = elements.index('O')
masses[idx] = masses[idx] +  wt* oxygenMass/(MgMass + oxygenMass)



print 'wt% + ppm + mol%:'
print sum(masses)
print ' '


#------------------------------------------------------------------------------------------------------------

#
#
#CaCO3
wt = 1

idx = elements.index('Ca')
masses2[idx] = masses2[idx] +  wt* calciumMass/(calciumMass + carbonMass + 3*oxygenMass)

idx = elements.index('C')
masses2[idx] = masses2[idx] +  wt* carbonMass/(calciumMass + carbonMass + 3*oxygenMass)

idx = elements.index('O')
masses2[idx] = masses2[idx] +  wt* 3*oxygenMass/(calciumMass + carbonMass + 3*oxygenMass)
#
#
#
##CaMg(CO3)2
#wt = 1.76/100
#
#idx = elements.index('Ca')
#masses2[idx] = masses2[idx] +  wt* calciumMass/(calciumMass + MgMass + 2*(carbonMass + 3*oxygenMass))
#
#idx = elements.index('Mg')
#masses2[idx] = masses2[idx] +  wt* MgMass/(calciumMass + MgMass + 2*(carbonMass + 3*oxygenMass))
#
#idx = elements.index('C')
#masses2[idx] = masses2[idx] +  wt* 2*carbonMass/(calciumMass + MgMass + 2*(carbonMass + 3*oxygenMass))
#
#idx = elements.index('O')
#masses2[idx] = masses2[idx] +  wt* 6*oxygenMass/(calciumMass + MgMass + 2*(carbonMass + 3*oxygenMass))
#
#
##SiO2
#wt = 0.71/100
#
#idx = elements.index('Si')
#masses2[idx] = masses2[idx] +  wt* SiMass/(SiMass + 2*oxygenMass)
#
#idx = elements.index('O')
#masses2[idx] = masses2[idx] +  wt* 2*oxygenMass/(SiMass + 2*oxygenMass)
#


#------------------------------------------------------------------------------------------------------------


idx = elements.index('S')
fluka[idx] = fluka[idx] +  SMass/(SMass + carbonMass + 3*oxygenMass)

idx = elements.index('C')
fluka[idx] = fluka[idx] +  carbonMass/(SMass + carbonMass + 3*oxygenMass)

idx = elements.index('O')
fluka[idx] = fluka[idx] +  3*oxygenMass/(SMass + carbonMass + 3*oxygenMass)



idx = elements.index('Mg')
elements[idx] = 'Mg*'


import matplotlib.pyplot as plt

fig = plt.figure()
ax = plt.subplot(111)
transp = 0.70

width = 0.30
x = np.arange(len(elements))

plt.bar(x - width/2, masses, width = width , label = 'Caliza Alba marble')
plt.bar(x + width/2, masses2, width = width , label = 'Idealized marble')
#plt.bar(x - width, fluka, width = width, label = 'Fluka composition')
#plt.bar(x, structural,yerr= structuralErrors,width = width, label = 'Structural sample')
#plt.bar(x -width , foamed,width = width,yerr=foamedErrors, label = 'Foamy sample', alpha = transp, color = 'g') #/sum(foamed)
#plt.bar(x + width ,fluka,width = width, label = 'Fluka', alpha = transp, color = 'r')

plt.xticks(x)
ax.set_xticklabels(elements)

plt.ylabel('Fraction',fontsize = 20)
plt.yscale("log", nonposy='clip')
plt.title('Marble composition comparison',fontsize = 16)
plt.xlabel('*Mg after best estimate')
plt.legend()

plt.show()


































