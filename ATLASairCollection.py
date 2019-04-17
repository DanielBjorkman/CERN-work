# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 10:04:56 2019

@author: cbjorkma
"""

#ATLASairCollection


import os

path = '//rpclustergw/cbjorkma/ATLAS/AirActivation'
#path = '//cern.ch/dfs/Users/c/cbjorkma/Documents/ATLAS'
os.chdir(path)


filename = 'ATLAS2JTTtrack.inp'


data = open(filename, 'r').readlines()


regs = []
assignma = []
for i in range(len(data)):
    
    string = 'ASSIGNMA         AIR'
    line = data[i]
    if line[:len(string)] == string:
        regs.append( line.split()[2])
        assignma.append(i)
        if data[i+1][0:6] == 'EMFCUT':
            assignma.append(i +1)
        if data[i+2][0:8] == 'STEPSIZE':
            assignma.append(i +2)
        if data[i+3][0:8] == 'STEPSIZE':
            assignma.append(i +3)     

for i in range(len(data)):
    if data[i][0:6] == 'EMFCUT' and data[i].split()[-1] in regs:
        assignma.append(i) 
    if data[i][0:8] == 'STEPSIZE' and data[i].split()[-1] in regs:
        assignma.append(i) 

zones = []
checkedIdx = []

startString = 'ALLAIR      25 '
contString ='               '



for j in range(len(regs)):
    
    #currReg = 'SOMEAIR'
    currReg = regs[j]
    #currReg = 'AirVJ01'
    #currReg = 'RGN_437'
    
    idx = regs.index(currReg)
    
    
    
    #find lineindex
    for i in range(len(data)):
        line = data[i]
        if line[:len(currReg) +1 ]  == currReg +' ' : 
            lineindex = i
            checkedIdx.append(i)
            break;
            
    line = data[lineindex]
    
    
    try:
        rest = line.split('|')[1]
    except:
        rest = line[15:]
        
    #See if next line belongs to the same zone
    currLine = lineindex + 1
    extraRest = ' '
    while data[currLine].strip()[0] == '-' or data[currLine].strip()[0] == '+':
        
        lineCont = data[currLine].strip()
        extraRest = extraRest + lineCont
        
        checkedIdx.append(currLine)
        currLine = currLine + 1
        
    if extraRest != ' ':
        rest = rest[:-1] + extraRest + rest[-1:]
    
    zones.append(rest)
    #testString = line.split('|')[0]
     
    
    #See if next line is an additional zone
    currLine = lineindex + 1
    if data[currLine][:4] == '    ' and currLine not in checkedIdx:
    
        sameZone = data[currLine].split('|')[0]
        
        
        
        if data[currLine][0] == '*':
            pass
        else:
            while data[currLine][:len(sameZone)] == sameZone:
                
                #print currLine
                step = 1
                line = data[currLine]
    
                try:
                    rest = line.split('|')[1]
                except:
                    rest = line[15:]   
                
                checkNext = False
                extraRest = ' '
                if data[currLine + 1].strip()[0] == '-' or data[currLine + 1].strip()[0] == '+':
                    lineCont = data[currLine +1].strip()
                    extraRest = extraRest + lineCont   + ' '             
                    checkedIdx.append(currLine + 1)
                    #print currLine +1
                    step = 2
                    checkNext = True
                    
                if checkNext:
                    if data[currLine + 2].strip()[0] == '-' or data[currLine + 2].strip()[0] == '+':
                        lineCont = data[currLine +2].strip()
                        extraRest = extraRest + lineCont            
                        checkedIdx.append(currLine + 2)
                        #print currLine +2
                        step = 3                
                
                if extraRest != ' ':
                    rest = rest[:-1] + extraRest + rest[-1:]
                  
                #print rest
                checkedIdx.append(currLine)
                zones.append(rest)
                currLine = currLine + step
                    
                                                
checkedIdx = sorted(checkedIdx)
print 6896 in checkedIdx

#Find new index for new region
for i in range(len(data)):
    string = 'GEOEND'
    if data[i][:len(string)] == string:
        newRegIdx = i -2
        break;

#Find new index for new assignma
for i in range(len(data)):
    string = '* ### SCORING DEFINITION'
    if data[i][:len(string)] == string:
        newAssignmaIdx = i -2
        break;


print 'Region lines commented: ' + str(len(checkedIdx))
print 'Zones extracted: ' + str(len(zones))
print 'Assigma lines commented: ' + str(len(assignma))


writeFile = open(filename[:-4] + 'Out' + filename[-4:], 'w')
for i in range(len(data)):
    line = data[i]
    if i in checkedIdx:
        writeFile.write('*' + line)
    elif i in assignma:
        writeFile.write('*' + line)
    elif i == newRegIdx:
        writeFile.write(startString + '|' + zones.pop(0))
        times = len(zones)
        for j in range(times):
            writeFile.write(contString + '|' + zones.pop(0))
        writeFile.write(line)
    elif i == newAssignmaIdx:
        writeFile.write('ASSIGNMA         AIR    ALLAIR                           0.0\n')
        writeFile.write('EMFCUT         -1E-4      3E-5              ALLAIR  \n')
        writeFile.write('STEPSIZE        -.01       10.    ALLAIR\n')
        writeFile.write(line)
    elif line[0:8] == 'EMF-BIAS' and line.split()[4] in regs:
        writeFile.write('*' + line)
    else:
        writeFile.write(line)

writeFile.close()
# line.split('|')
    
    
    
    
print 'Done'
    
    
    
    
    
    
print 'Add:'
print 'AIBLFSV2'
print 'AIBLFSV3'
    
    
    
    
    
    
    
    
    
    
    