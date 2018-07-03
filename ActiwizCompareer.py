# -*- coding: utf-8 -*-
"""
Created on Thu May 31 11:08:36 2018

@author: cbjorkma
"""

#ActiwizCompareer
#
#class Machine:
#
#    def __init__(self, name):
#        self.name = name
#
##    def Name(self):
##        return self.firstname + " " + self.lastname
#
#class ZS(Machine):
#
#    def __init__(self):
#        self.shell = []
#        self.Cath = []
#        self.SeptHolder = []
#        self.wires = []
#        
   
        
#    def GetEmployee(self):
#        return self.Name() + ", " +  self.staffnumber
        
        
        
#ZS1 = ZS()
#


#70 ZShell
#71 Cathode electric
#72 Septholder
#73 Wires     


import numpy as np
import matplotlib.pyplot as plt
import os


#Wires ---------------------------------------------------------------------------------------
fig = plt.figure()

ax = plt.subplot(111)

yes =  [148, 656]
xes = ['W-26Re', 'Graphite']

data = {'W-26Re': 148, 'Graphite': 656 }
names = list(data.keys())
values = np.asarray(list(data.values()))

values = values/ min(values)

plt.bar(names, values)

#ax.set_xticklabels(xes)

plt.ylabel('Relative Hazard', fontsize = 16)

plt.title('ZS septa wires. H*(10) at 1 meter distance. 0 cooling ')



plt.show()


fig = plt.figure()

ax = plt.subplot(111)

path = '//rpclustersrv1/cbjorkma/LSS2/Fluence/ZSa/Out73_dir'

os.chdir(path)

rhe = np.loadtxt('W-26ReaEvolution.txt', skiprows = 4)
rhe[0:,0] = rhe[0:,0]/(60*60*24)
rhe[0:,1] = rhe[0:,1]/(148)

graphite = np.loadtxt('GraphiteEvolution.txt', skiprows = 4)

graphite[0:,0] = graphite[0:,0]/(60*60*24)
graphite[0:,1] = graphite[0:,1]/(148)

#SS = np.loadtxt('SSEvolution.txt', skiprows = 4)
#
#SS[0:,0] = SS[0:,0]/(60*60*24)
#SS[0:,1] = SS[0:,1]/(148)


plt.plot(rhe[0:,0], rhe[0:,1], label = 'Rhenium/Tungsten', linewidth = 3)

plt.plot(graphite[0:,0], graphite[0:,1], label = 'Graphite', linewidth = 3)

#plt.plot(titanium[0:,0], titanium[0:,1], label = 'Titanium', linewidth = 3)

plt.legend()

plt.xlabel('Days after operations', fontsize = 16)

plt.ylabel('Relative hazard', fontsize = 16)

plt.title('ZS wire material. H*(10) at 1 meter distance', fontsize = 16)

plt.grid(linewidth = 0.3)
ax.set_yscale("log", nonposy='clip')

plt.show()













#Zshell ---------------------------------------------------------------------------------------
#fig = plt.figure()
#
#ax = plt.subplot(111)
#
##yes =  [148, 656]
##xes = ['W-26Re', 'Graphite']
#
#data = {'Alu6061': 120, 'Stainless steel 304L': 246, 'Titanium': 126 }
#names = list(data.keys())
#values = np.asarray(list(data.values()))
#
#values = values/ float(max(values))
#
#plt.bar(names, values)
#
##ax.set_xticklabels(xes)
#
#plt.ylabel('Relative Hazard', fontsize = 16)
#
#plt.title('ZS septa wires. H*(10) at 1 meter distance. 0 cooling ')
#
#
#
#plt.show()



fig = plt.figure()

ax = plt.subplot(111)

path = '//rpclustersrv1/cbjorkma/LSS2/Fluence/ZSa/Out70_dir'

os.chdir(path)

alu = np.loadtxt('Alu6061Evolution.txt', skiprows = 4)
alu[0:,0] = alu[0:,0]/(60*60*24)
alu[0:,1] = alu[0:,1]/(246)

titanium = np.loadtxt('TitaniumEvolution.txt', skiprows = 4)

titanium[0:,0] = titanium[0:,0]/(60*60*24)
titanium[0:,1] = titanium[0:,1]/(246)

SS = np.loadtxt('SSEvolution.txt', skiprows = 4)

SS[0:,0] = SS[0:,0]/(60*60*24)
SS[0:,1] = SS[0:,1]/(246)


plt.plot(SS[0:,0], SS[0:,1], label = 'SS304L', linewidth = 3)

plt.plot(alu[0:,0], alu[0:,1], label = 'Alu6061', linewidth = 3)

plt.plot(titanium[0:,0], titanium[0:,1], label = 'Titanium', linewidth = 3)

plt.legend()

plt.xlabel('Days after operations', fontsize = 16)

plt.ylabel('Relative hazard', fontsize = 16)

plt.title('ZS tank material. H*(10) at 1 meter distance', fontsize = 16)

plt.grid(linewidth = 0.3)


plt.show()






#Wire support ---------------------------------------------------------------------------------------


#fig = plt.figure()
#
#ax = plt.subplot(111)
#
##yes =  [148, 656]
##xes = ['W-26Re', 'Graphite']
#
#data = {'Invar': 789, 'Stainless steel 304L': 676, 'Titanium': 401 }
#names = list(data.keys())
#values = np.asarray(list(data.values()))
#
#values = values/ float(max(values))
#
#plt.bar(names, values)
#
##ax.set_xticklabels(xes)
#
#plt.ylabel('Relative Hazard', fontsize = 16)
#
#plt.title('ZS septa support. H*(10) at 1 meter distance. 0 cooling ')
#
#
#
#plt.show()



fig = plt.figure()

ax = plt.subplot(111)

path = '//rpclustersrv1/cbjorkma/LSS2/Fluence/ZSa/Out72_dir'

os.chdir(path)

invar = np.loadtxt('InvarEvolution.txt', skiprows = 4)
invar[0:,0] = invar[0:,0]/(60*60*24)
invar[0:,1] = invar[0:,1]/(789)

titanium = np.loadtxt('TitaniumEvolution.txt', skiprows = 4)

titanium[0:,0] = titanium[0:,0]/(60*60*24)
titanium[0:,1] = titanium[0:,1]/(789)

SS = np.loadtxt('SSEvolution.txt', skiprows = 4)

SS[0:,0] = SS[0:,0]/(60*60*24)
SS[0:,1] = SS[0:,1]/(789)


plt.plot(SS[0:,0], SS[0:,1], label = 'SS304L', linewidth = 3)

plt.plot(invar[0:,0], invar[0:,1], label = 'Invar', linewidth = 3)

plt.plot(titanium[0:,0], titanium[0:,1], label = 'Titanium', linewidth = 3)

plt.legend()

plt.xlabel('Days after operations', fontsize = 16)

plt.ylabel('Relative hazard', fontsize = 16)

plt.title('ZS septa support material. H*(10) at 1 meter distance', fontsize = 16)

plt.grid(linewidth = 0.3)


plt.show()







# Cathode -------------------------------------------------------------------------------

fig = plt.figure()

ax = plt.subplot(111)

path = '//rpclustersrv1/cbjorkma/LSS2/Fluence/ZSa/Out71_dir'

os.chdir(path)

invar = np.loadtxt('Peraluman300evolution.txt', skiprows = 4)
invar[0:,0] = invar[0:,0]/(60*60*24)
invar[0:,1] = invar[0:,1]/(37.7)

titanium = np.loadtxt('TitaniumEvolution.txt', skiprows = 4)

titanium[0:,0] = titanium[0:,0]/(60*60*24)
titanium[0:,1] = titanium[0:,1]/(37.7)

#SS = np.loadtxt('SSEvolution.txt', skiprows = 4)
#
#SS[0:,0] = SS[0:,0]/(60*60*24)
#SS[0:,1] = SS[0:,1]/(789)

#
#plt.plot(SS[0:,0], SS[0:,1], label = 'SS304L', linewidth = 3)

plt.plot(invar[0:,0], invar[0:,1], label = 'Peraluman 300', linewidth = 3)

plt.plot(titanium[0:,0], titanium[0:,1], label = 'Titanium', linewidth = 3)

plt.legend()

plt.xlabel('Days after operations', fontsize = 16)

plt.ylabel('Relative hazard', fontsize = 16)

plt.title('ZS cathode material. H*(10) at 1 meter distance', fontsize = 16)

plt.grid(linewidth = 0.3)


plt.show()




# All -------------------------------------------------------------------------------

fig = plt.figure()


lines = ['-', '--',':','-.']


ax = plt.subplot(111)

path = '//rpclustersrv1/cbjorkma/LSS2/Fluence/ZSa/Out71_dir'
os.chdir(path)

cathode = np.loadtxt('Peraluman300evolution.txt', skiprows = 4)
cathode[0:,0] = cathode[0:,0]/(60*60*24)
cathode[0:,1] = cathode[0:,1]/(4784)


path = '//rpclustersrv1/cbjorkma/LSS2/Fluence/ZSa/Out72_dir'
os.chdir(path)

support = np.loadtxt('InvarEvolution.txt', skiprows = 4)
support[0:,0] = support[0:,0]/(60*60*24)
support[0:,1] = support[0:,1]/(29584)


path = '//rpclustersrv1/cbjorkma/LSS2/Fluence/ZSa/Out70_dir'
os.chdir(path)

tank = np.loadtxt('SSEvolution.txt', skiprows = 4)

tank[0:,0] = tank[0:,0]/(60*60*24)
tank[0:,1] = tank[0:,1]/(35368)


path = '//rpclustersrv1/cbjorkma/LSS2/Fluence/ZSa/Out73_dir'
os.chdir(path)

rhe = np.loadtxt('W-26ReaEvolution.txt', skiprows = 4)
rhe[0:,0] = rhe[0:,0]/(60*60*24)
rhe[0:,1] = rhe[0:,1]/(26.208)

path = '//rpclustersrv1/cbjorkma/LSS2/Fluence/Lead blocks/NewFormat/Block1_dir' 
os.chdir(path)

block1 = np.loadtxt('Block1Evolution.txt', skiprows = 4)
block1[0:,0] = block1[0:,0]/(60*60*24)
block1[0:,1] = block1[0:,1]/(5280*2)

path = '//rpclustersrv1/cbjorkma/LSS2/Fluence/Lead blocks/NewFormat/Block2_dir' 
os.chdir(path)

block2 = np.loadtxt('Block2Evolution.txt', skiprows = 4)
block2[0:,0] = block2[0:,0]/(60*60*24)
block2[0:,1] = block2[0:,1]/(5280*2)

path = '//rpclustersrv1/cbjorkma/LSS2/Fluence/Lead blocks/NewFormat/Block3_dir' 
os.chdir(path)

block3 = np.loadtxt('Block3Evolution.txt', skiprows = 4)
block3[0:,0] = block3[0:,0]/(60*60*24)
block3[0:,1] = block3[0:,1]/(5280*2)

path = '//rpclustersrv1/cbjorkma/LSS2/Fluence/Lead blocks/NewFormat/Block4_dir' 
os.chdir(path)

block4 = np.loadtxt('Block4Evolution.txt', skiprows = 4)
block4[0:,0] = block4[0:,0]/(60*60*24)
block4[0:,1] = block4[0:,1]/(5280*2)

norm = max(rhe[0:,1])

plt.plot(cathode[0:,0], cathode[0:,1]/norm, label = 'Cathode', linewidth = 3)

plt.plot(support[0:,0], support[0:,1]/norm, label = 'Wire support', linewidth = 3)

plt.plot(tank[0:,0], tank[0:,1]/norm, label = 'Tank', linewidth = 3)

plt.plot(rhe[0:,0], rhe[0:,1]/norm, label = 'Wire septa', linewidth = 3)

plt.plot(block1[0:,0], block1[0:,1]/norm, label = 'Lead block 1', linewidth = 2, color = 'k', linestyle = lines.pop(0))

plt.plot(block2[0:,0], block2[0:,1]/norm, label = 'Lead block 2', linewidth = 2, color = 'k', linestyle = lines.pop(0))

plt.plot(block3[0:,0], block3[0:,1]/norm, label = 'Lead block 3', linewidth = 2, color = 'k', linestyle = lines.pop(0))

plt.plot(block4[0:,0], block4[0:,1]/norm, label = 'Lead block 4', linewidth = 2, color = 'k', linestyle = lines.pop(0))

plt.legend()

plt.xlabel('Days after operations', fontsize = 16)

plt.ylabel('Relative hazard', fontsize = 16)

plt.title('ZS components, relative hazards. H*(10) at 1 meter distance', fontsize = 16)

plt.grid(linewidth = 0.3)
ax.set_yscale("log", nonposy='clip')

plt.show()














