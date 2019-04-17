# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 16:46:14 2019

@author: cbjorkma
"""

#ATLASmaterials


#Tile calorimeter



import matplotlib.pyplot as plt
import numpy as np


#Now ------------------------------------------------------------------------
#Full period = 18.2573  mm
full = 18.2573 

#iron
lengthFe = (14. + 4. * 22 / 1570) #mm
densityFe = 7.87 #g/cm3
materialLabelsFe = ['Fe']
materialsFe = [1]
#massesFe = 

#scintillator
lengthScintillator = (3. - 3. * 33 / 1570) 
materialLabelsScintillator = ['C', 'H' ]
materialsScintillator = [0.922578013805796, 0.0774219861942044 ]
densityScintillator = 1.032

#Air gap
lengthAirGap = (1. - 1. * 33 / 1570 + 4. * 11 / 1570) 
materialLabelsAir = ['N', 'O','Ar','H']
materialsAir = [0.7732 , 0.2095 , 0.0093 , 0.008]  
densityAir = 0.001214


#Glue
lengthGlue = 0.2573 
densityGlue = 1.7
#materialLabelsGlue = ['Si', 'O','Ag']
#materialsGlue = [0.28046361142918 , 0.31953638857082 , 0.4 ] 
materialLabelsGlue = ['C', 'O']
materialsGlue = [0.922578013805796 , 0.07742198619420404 ] 



class subpart():
    
        def __init__(self, tag, length, density, labels, ratios):
            self.tag = tag
            self.length = length
            self.density = density
            self.labels = labels
            self.ratios = ratios
            self.mass = 0
            
        
        def output(self):
            print(self.tag)
            print(self.length)
            print(self.density)
            print(self.labels)
            print(self.ratios)

iron = subpart('Iron', lengthFe, 7.87, ['Fe'] , [1] )
#iron.output()


scintillator = subpart('Scintillator', lengthScintillator, 1.032, ['C', 'H' ] , [0.922578013805796, 0.0774219861942044 ] )   
#scintillator.output()

air = subpart('Air', lengthAirGap, 0.001214, ['N', 'O','Ar','H'] , [0.7732 , 0.2095 , 0.0093 , 0.008]    )
#air.output()


glue = subpart('Glue', lengthGlue, 1.7, materialLabelsGlue , materialsGlue )
#glue.output



   
def calcDensity(*args):
    
    #volume = args[0]
    #print volume
    
    mass = 0
    totLength = 0
    for i in range(0, len(args)):
        part = args[i]
        #print sum(part.ratios)
        mass = mass + part.length*part.density
        totLength = totLength + part.length
        
    density = mass/totLength
    print str(density) + ' g/cm3'
    return density;
    
       
calcDensity( iron,scintillator, air, glue)


def calcAtom(*args):
    
    import numpy as np
    
    #length = args[0]
    
    atoms = []
    masses = []
    massTot = 0
    totLength = 0
    for i in range(0,len(args)):
        part= args[i]
        massTot = massTot + part.length*0.1*part.density
        totLength = totLength + part.length
        for j in range(len(part.labels)):
            atoms.append(part.labels[j])
            masses.append(part.ratios[j]*part.density *part.length *0.1)
  
    print masses
    print massTot
    
    ratios = np.asarray(masses)/massTot
    
    print atoms
    print ratios
    print 'Ratios= ' + str(sum(ratios))
    print 'Lengths= ' + str(totLength)

    print sum(masses)/massTot

    if len(atoms ) != len(set(atoms )):         
       print 'Note duplicates!!!!!!!!!!!!!!!'    
    
    return atoms, ratios;
    
atoms, ratios = calcAtom( iron,scintillator, air, glue)

import numpy as np

#        
#part = iron
#
#part.length()

#print atoms
#print ratios
#a = ratios





def fixAtoms(atoms, ratios, idx1, idx2):
    print atoms[idx1]
    print atoms[idx2]
    assert atoms[idx1] == atoms[idx2]
    ratios[idx2] = ratios[idx2] + ratios[idx1]
    ratios = np.delete(ratios, idx1)
    atoms.pop(idx1)
    print atoms
    return atoms, ratios


idx1 = -1
idx2 = 4
atoms, ratios = fixAtoms(atoms, ratios, idx1, idx2)


idx1 = -1
idx2 = 1
atoms, ratios = fixAtoms(atoms, ratios, idx1, idx2)


idx1 = -1
idx2 = 2
atoms, ratios = fixAtoms(atoms, ratios, idx1, idx2)



print atoms
print ratios




#Prev
olddensity = 6.5048
materialLabelsPrev = ['H', 'C','Fe']
materialsPrev = [0.0161662, 0.1926338, 6.296]
materialsPrev = np.asarray(materialsPrev)/sum(materialsPrev)


old = np.zeros(len(atoms))

for i in range(len(materialLabelsPrev)):
    idx = atoms.index(materialLabelsPrev[i])
    old[idx] = materialsPrev[i]







import matplotlib.pyplot as plt

import matplotlib.gridspec as gridspec    
gs1 = gridspec.GridSpec(10, 1)

fig = plt.figure()

#ax = plt.subplot(111)
ax = plt.subplot(gs1[0:-2,0])

width = 0.30

plt.bar(np.asarray(range(len(ratios))) - width/2,ratios, width = width, label = 'New composition', log = 1)
plt.bar(np.asarray(range(len(ratios))) + width/2,old,  width = width,label = 'Old composition', log = 1)

x = np.arange(len(atoms))
plt.xticks(x)
ax.set_xticklabels(atoms)
#ax.set_yscale('log')
plt.legend()
plt.ylim(1E-8,2)
plt.ylabel('Mass fraction', fontsize = 22)
plt.title('Tile calorimeter material definition', fontsize = 22)
#ax.set_xticklabels(atoms)

plt.show()


density = 6.20

ax = plt.subplot(gs1[-1,0])
comp = ('Old', 'New')
y_pos = np.arange(len(comp))
ax.barh(y_pos, [olddensity, density], align='center', color = ['C1', 'C0'])
ax.set_yticks(y_pos)
ax.set_yticklabels(comp)
ax.invert_yaxis()  # labels read top-to-bottom
#ax.set_title('Density', fontsize = 16)
ax.set_xlabel('Density [g/cm3]', fontsize = 16)
#ax.set_title('How fast do you want to go today?')

xlength = 12

fig.set_size_inches(xlength, xlength/1.618)
plt.xlim(6.1, 6.6)
plt.show()


print 'Actual density according to Sanya = ' + str(density)
print 'NOTE!!!!!!!!!!!!!!!!!!!!!!!!!!!1'
print 'Adjust for the air around the units accoring to Sanya'
        
        
        
def UniqeAtoms(*args):
    
    atoms = args[0]
    ratios = args[1]
    
    newAtoms = sorted(list(set(atoms)))
    
    try:
        newAtoms = args[2] #order
    except:
        pass;
    
    newRatios = np.zeros(len(newAtoms)) 
    for i in range(len(newAtoms)):
        currAtoms = newAtoms[i]
        for j in range(len(atoms)):
            if currAtoms == atoms[j]:
                newRatios[i] = newRatios[i] + ratios[j]
    
    try:
        diff = list(set(args[2]) - set(newAtoms))
        newAtoms.append(diff)
    except:
        pass;
        
    
    
    print newAtoms
    print newRatios
    return newAtoms,newRatios;        
        
        






class part():
    
        def __init__(self, tag ):
            self.tag = tag
            self.length = []
            self.density = []
            self.atoms = []
            self.ratios = []
            self.mass = 0
            
        def calcDensity(self,*args):
            
            #volume = args[0]
            #print volume
            
            mass = 0
            totLength = 0
            for i in range(0, len(args)):
                part = args[i]
                #print sum(part.ratios)
                mass = mass + part.length*part.density
                totLength = totLength + part.length
                
            density = mass/totLength
            print str(density) + ' g/cm3'
            self.length= totLength;
            self.density = density;
            
               
        
        
        def calcAtom(self, *args):
            
            import numpy as np
            
            #length = args[0]
            
            atoms = []
            masses = []
            massTot = 0
            totLength = 0
            for i in range(0,len(args)):
                part= args[i]
                massTot = massTot + part.length*0.1*part.density
                totLength = totLength + part.length
                for j in range(len(part.labels)):
                    atoms.append(part.labels[j])
                    masses.append(part.ratios[j]*part.density *part.length *0.1)
          
            
            ratios = np.asarray(masses)/massTot
            
        
            print sum(masses)/massTot
        
           # if len(atoms ) != len(set(atoms )):         
            #   print 'Note duplicates!!!!!!!!!!!!!!!'    
            
            self.atoms = atoms
            self.ratios = ratios;
            self.mass = massTot
    
        def UniqeAtoms(self, *args):
            
            atoms = self.atoms
            ratios = self.ratios
            
            print atoms
            
            
            newAtoms = sorted(list(set(atoms)))
            
            try:
                newAtoms = args[0] #order
                diff = list(set(self.atoms) - set(newAtoms))
                print diff
                newAtoms.append(diff[0])
                #print newAtoms
            except:
                pass;
            
            newRatios = np.zeros(len(newAtoms)) 
            for i in range(len(newAtoms)):
                currAtoms = newAtoms[i]
                for j in range(len(atoms)):
                    if currAtoms == atoms[j]:
                        newRatios[i] = newRatios[i] + ratios[j]
            
#            try:
#                diff = list(set(self.atoms) - set(newAtoms))
#                print diff
#                newAtoms.append(diff)
#            except:
#                pass;
                
            
            
            #print newAtoms
            #print newRatios
            
            self.atoms = newAtoms
            self.ratios = newRatios
            #return newAtoms,newRatios;       
        
        def plot(self):
            
            fig = plt.figure()

            ax = plt.subplot(111)
            
            width = 0.30
        
            
            plt.bar(np.asarray(range(len(self.ratios))) ,self.ratios, width = width, label = self.tag, log = 1)
    
            #plt.bar(np.asarray(range(len(tilefinger.ratios))) + width,tilefingerAlu.ratios,  width = width,label = 'With Aluminum', log = 1)
            
            x = np.arange(len(self.atoms))
            plt.xticks(x)
            ax.set_xticklabels(self.atoms)
            #ax.set_yscale('log')
            plt.legend()
            plt.ylim(1E-4,2)
            plt.ylabel('Mass fraction', fontsize = 22)
            plt.title('Tile finger material definition', fontsize = 22)
            #ax.set_xticklabels(atoms)
            
            plt.show()
        
        def output(self):
            print(self.tag)
            print(self.length)
            print(self.density)
            print(self.labels)
            print(self.ratios)


def plotThis(part1,part2):
    maxi = max(len(part1.atoms), len(part2.atoms))
    
    ratios1 = np.zeros(maxi)
    ratios2 = np.zeros(maxi)
    
    ratios1[0:len(part1.ratios)] = part1.ratios
    ratios2[0:len(part2.ratios)] = part2.ratios
    
    fig = plt.figure()
    
    ax = plt.subplot(111)
    
    width = 0.30
    
    plt.bar(np.asarray(range(maxi)) - width/2, ratios1, width = width, label = part1.tag , log = 1)
    plt.bar(np.asarray(range(maxi)) + width/2, ratios2, width = width, label = part2.tag , log = 1)
    plt.legend()
    plt.ylabel('Mass fraction', fontsize = 22)
    
    x = np.arange(maxi)
    plt.xticks(x)
    
    atoms1 = part1.atoms
    atoms2 = part2.atoms
    
    if len(atoms1) < maxi:
        for i in range(maxi- len(atoms1)):
            atoms1.append([])
    if len(atoms2) < maxi:
        for i in range(maxi- len(atoms2)):
            atoms2.append([])        
    
    ax.set_xticklabels(zip(atoms1,atoms2))
    ax.tick_params(axis='x', rotation=90)
    plt.ylim(1E-4,2)
    
    plt.show()





#TileFingerPos    
        
print ' '
print 'Tilefinger:'
print '' 

TileFinger1 = subpart('LArIronBox', 16, 4.5, ['Fe', 'Mn', 'Si', 'C', 'H', 'Cu'] , [0.784 , 0.008, 0.008 , 0.0881623775538845 , 0.0118376224461155, 0.1] )
#iron.output()

TileFinger2 = subpart('Iron', 4*25.5, 7.87, ['Fe'] , [1] )


TileFinger3 = subpart('LArServices', 3*16, 2.5, ['Fe', 'Mn', 'Si', 'Cu', 'C' , 'H', 'N', 'O', 'Ar'] , [0.196, 0.002, 0.002, 0.6, 0.0881623775538845,0.0119176224461155, 0.07494, 0.02369 ,0.00129 ] )


tilefinger = part('tilefinger')
tilefinger.calcDensity( TileFinger1,TileFinger2, TileFinger3)
tilefinger.calcAtom( TileFinger1,TileFinger2, TileFinger3)
#tilefinger.plot()
tilefinger.UniqeAtoms()
#tilefinger.plot()
        
        

   
print ' '
print 'Tilefinger with air:'
print '' 

TileFinger1 = subpart('LArIronBox', 16, 4.5, ['Fe', 'Mn', 'Si', 'C', 'H', 'Cu'] , [0.784 , 0.008, 0.008 , 0.0881623775538845 , 0.0118376224461155, 0.1] )
#iron.output()

TileFinger2 = subpart('Iron', 4*(25.5 - 17), 7.87, ['Fe'] , [1] )


TileFinger3 = subpart('LArServices', 3*16, 2.5, ['Fe', 'Mn', 'Si', 'Cu', 'C' , 'H', 'N', 'O', 'Ar'] , [0.196, 0.002, 0.002, 0.6, 0.0881623775538845,0.0119176224461155, 0.07494, 0.02369 ,0.00129 ] )

air = subpart('Air', 4*17, 0.001214, ['N', 'O','Ar','H'] , [0.7732 , 0.2095 , 0.0093 , 0.008]    )


tilefingerAir = part('tilefingerAir')
tilefingerAir.calcDensity( TileFinger1,TileFinger2, TileFinger3, air)
tilefingerAir.calcAtom( TileFinger1,TileFinger2, TileFinger3, air)
#tilefingerAir.plot()
tilefingerAir.UniqeAtoms()
#tilefingerAir.plot()



    






print ' '
print 'Tilefinger with Aluminum:'
print '' 

TileFinger1 = subpart('LArIronBox', 16, 4.5, ['Fe', 'Mn', 'Si', 'C', 'H', 'Cu'] , [0.784 , 0.008, 0.008 , 0.0881623775538845 , 0.0118376224461155, 0.1] )
#iron.output()

TileFinger2 = subpart('Iron', 4*(25.5 - 17), 7.87, ['Fe'] , [1] )


TileFinger3 = subpart('LArServices', 3*16, 2.5, ['Fe', 'Mn', 'Si', 'Cu', 'C' , 'H', 'N', 'O', 'Ar'] , [0.196, 0.002, 0.002, 0.6, 0.0881623775538845,0.0119176224461155, 0.07494, 0.02369 ,0.00129 ] )

alu = subpart('Aluminium', 4*17, 2.7, ['Al'] , [1]    )


tilefingerAlu = part('tilefingerAlu')
tilefingerAlu.calcDensity( TileFinger1,TileFinger2, TileFinger3, alu)
tilefingerAlu.calcAtom( TileFinger1,TileFinger2, TileFinger3, alu)
#tilefingerAlu.plot()
tilefingerAlu.UniqeAtoms(tilefinger.atoms)
#tilefingerAlu.plot()



#
#plotThis(tilefinger, tilefingerAlu)
#
#




fig = plt.figure()

ax = plt.subplot(111)

width = 0.30
tilefinger.ratios = np.append(tilefinger.ratios, np.zeros(1))
tilefingerAir.ratios = np.append(tilefingerAir.ratios, np.zeros(1))



plt.bar(np.asarray(range(len(tilefinger.ratios))) - width,tilefinger.ratios, width = width, label = 'No air', log = 1)
plt.bar(np.asarray(range(len(tilefinger.ratios))),tilefingerAir.ratios,  width = width,label = 'With air', log = 1)
plt.bar(np.asarray(range(len(tilefinger.ratios))) + width,tilefingerAlu.ratios,  width = width,label = 'With Aluminum', log = 1)

x = np.arange(len(tilefinger.atoms))
plt.xticks(x)
ax.set_xticklabels(tilefinger.atoms)
#ax.set_yscale('log')
plt.legend()
plt.ylim(1E-4,2)
plt.ylabel('Mass fraction', fontsize = 22)
plt.title('Tile finger material definition', fontsize = 22)
#ax.set_xticklabels(atoms)

#plt.grid(linewidth = 0.3)

plt.show()


#print tilefinger.length
#print tilefingerAir.length
#print tilefingerAlu.length
#


#
#
#






print ' '
print 'EM accordion:'
print '' 

accord1 = subpart('Lead', 1.5, 11.34, ['Pb'] , [1] )

accord2 = subpart('Iron', 2*0.2, 7.87, ['Fe'] , [1] )


masses = [1*28.084 , 4*15.999 , 5*12.0107 , 8*1.00794]
gluemass = sum(masses)
accord3 = subpart('Prepreg', 2*0.13, 1.69, ['Si', 'O', 'C', 'H'] , [y / gluemass for y in masses]  )

#<material name="LArElectronics0x44a16a20"
masses = [1*12.0107, 2*1.00794, 1*39,948]
elecmass = sum(masses)

kapton = [0.69113568, 0.0263634, 0.20923132, 0.07326896595 ]
kapton = [y * 0.62 for y in kapton]
elementRatios = [0.38 ]
for i in range(len(kapton)):
    elementRatios.append(kapton.pop(0))

accord4 = subpart('Electrodes', 0.275, 4.32, ['Cu', 'C', 'H', 'O' , 'N'] , elementRatios )

accord5 = subpart('LAr', 2*2.12, 1.3954, [ 'Ar'] , [1]  )


EMaccord = part('EM accordion')
EMaccord.calcDensity( accord1,accord2, accord3, accord4, accord5)
EMaccord.calcAtom( accord1,accord2, accord3, accord4, accord5)
#tilefinger.plot()
EMaccord.UniqeAtoms()


import matplotlib.gridspec as gridspec    
gs1 = gridspec.GridSpec(10, 1)

fig = plt.figure()

#ax = plt.subplot(111)
ax = plt.subplot(gs1[0:-2,0])


width = 0.30

old = [11 , 0 , 3,  22.2 , 0.1 , 0, 3.6 , 57, 1.8, 1.3  ] # Ca
old = [y / sum(old) for y in old]

atoms = EMaccord.atoms
atoms.append('Ca')
#atoms.append('Ca')
ratios = EMaccord.ratios
ratios = np.append(ratios , 0)
#ratios = np.append(ratios , 0)

#plt.bar(np.asarray(range(len(tilefinger.ratios))) - width,tilefinger.ratios, width = width, label = 'No air', log = 1)
plt.bar(np.asarray(range(len(ratios))) - width/2,ratios,  width = width,label = 'New definition', log = 1)
plt.bar(np.asarray(range(len(ratios))) + width/2,old,  width = width,label = 'Old definition', log = 1)
#plt.bar(np.asarray(range(len(tilefinger.ratios))) + width,tilefingerAlu.ratios,  width = width,label = 'With Aluminum', log = 1)

x = np.arange(len(atoms))
plt.xticks(x)
ax.set_xticklabels(atoms)
#ax.set_yscale('log')
plt.legend()
plt.ylim(1E-4,2)
plt.ylabel('Mass fraction', fontsize = 22)
plt.title('EM accordion material definition', fontsize = 22)
#ax.set_xticklabels(atoms)

#plt.grid(linewidth = 0.3)

ax = plt.subplot(gs1[-1,0])
comp = ('Old', 'New')
y_pos = np.arange(len(comp))
ax.barh(y_pos, [3.805, EMaccord.density], align='center', color = ['C1', 'C0'])
ax.set_yticks(y_pos)
ax.set_yticklabels(comp)
ax.invert_yaxis()  # labels read top-to-bottom
#ax.set_title('Density', fontsize = 16)
ax.set_xlabel('Density [g/cm3]', fontsize = 16)
#ax.set_title('How fast do you want to go today?')

xlength = 12

fig.set_size_inches(xlength, xlength/1.618)
plt.xlim(3.7, 4.18)
plt.show()




















