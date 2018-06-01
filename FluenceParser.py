# -*- coding: utf-8 -*-
"""
Created on Mon May 28 11:44:46 2018

@author: cbjorkma
"""

#FluenceParser

import os

path = '//rpclustersrv1/cbjorkma/LSS2/Fluence' 

os.chdir(path)


#70 ZShell
#71 Cathode electric
#72 Septholder
#73 Wires

ZSa = []
ZSb = []


allfiles = os.listdir(path)


units = ['70','71','72','73']

allfiles = sorted(filter(lambda x: x[-2:] in units, allfiles))

endings = []
for k in range(len(units)):
    filenames = filter(lambda x: x[-2:] == units[k], allfiles)
    
    
    for i in range(len(filenames)):
        
        thefile  = open(filenames[i], 'r').readlines()
        endings.append(filenames[i][-2:])    
        subfiles = [thefile[0:95], thefile[0:7] + thefile[95:]]
        
        
        def editfile(subfiles):
            for j in range(len(subfiles)): 
                subfile = subfiles[j]
                vec = ['Pro','Pi+','Pi-','Neu']
                vec2 = ['a','b']
                for i in range(len(subfile)):
                    if subfile[i][0] == '1':
                        string = subfile[i+2][:20] + '__' + vec2[j] +  vec.pop(0) + subfile[i+2][26:]
                        subfile[i+2] = string
        
                subfiles[j] = subfile        
            return subfiles       
              
        subfiles = editfile(subfiles)
        
        ZSa.append(subfiles[0])
        ZSb.append(subfiles[1])
        
    

#Write

try:
    os.mkdir(path + '/ZSa')
except:
    pass


os.chdir(path + '/ZSa')
newfilenames = []

for i in range(len(ZSa)):
    filename = 'ZSa' + str(i) +'.'+ endings[i]
    newfilenames.append(filename)
    file = open(filename, 'w')
    for j in range(len(ZSa[i])):
        file.write(ZSa[i][j])
        
    file.close()
#   
for i in range(len(units)):
    
    file = open('inpfile' + units[i], 'w')
    file.write(str(endings.count(units[i])) +'\n')
    names = filter(lambda x: x[-2:] == units[i],newfilenames)
    for j in range(len(names)):
        file.write(names[j]+'\n')
    file.write('*'+'\n')
    file.write('Out' + units[i])
    file.close()
    


try:
    os.mkdir(path + '/ZSb')
except:
    pass




os.chdir(path + '/ZSb')
newfilenames = []

for i in range(len(ZSb)):
    filename = 'ZSb' + str(i) +'.'+ endings[i]
    newfilenames.append(filename)
    file = open(filename, 'w')
    for j in range(len(ZSb[i])):
        file.write(ZSb[i][j])
        
    file.close()
#   
for i in range(len(units)):
    
    file = open('inpfile' + units[i], 'w')
    file.write(str(endings.count(units[i])) +'\n')
    names = filter(lambda x: x[-2:] == units[i],newfilenames)
    for j in range(len(names)):
        file.write(names[j]+'\n')
    file.write('*'+'\n')
    file.write('Out' + units[i])
    file.close()
    




































