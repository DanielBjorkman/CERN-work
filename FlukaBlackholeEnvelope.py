# -*- coding: utf-8 -*-
"""
Created on Mon Mar 05 10:21:53 2018

@author: cbjorkma
"""
#FlukaBlackholeEnvelope



directory = '//cern.ch/dfs/Users/c/cbjorkma/Documents'
filename = 'DumpNewCoreResidualRef.inp'

#directory = '//rpclustersrv1/cbjorkma/Dump studies'
#filename = 'DumpResMarbleBack15cmConcrete.inp'




Inverse = 1

if Inverse == 0:
    Envfilename = 'Env' + filename
else:
    Envfilename = 'EnvInv' + filename


import os
os.chdir(directory)


#Reads tags from file
info = {'Geobegin':[],'end1':[],'end2':[], 'BLCKHOLE':[],'BLCKHOLEpos':[]}
row = 0
with open(filename) as file:
     for line in file.readlines():
         line_content = line.split()
         if line.lstrip(' ').partition(' ')[0] == 'GEOBEGIN':
             info['Geobegin'].append(row)
         if line.lstrip(' ').partition(' ')[0] == 'END\n':
             if len(info['end1']) == 0:
                info['end1'].append(row)
             else:
                info['end2'].append(row)
         if line.lstrip(' ').partition(' ')[0] == 'ASSIGNMA' and line_content[1] == 'BLCKHOLE' :
            info['BLCKHOLE'].append(line_content[2])
            info['BLCKHOLEpos'].append(row)
         row = row +1

if Inverse == 0:
    mainString = '+Envelope '
    invString = '-Envelope '
    EnvelopeBody = 'RPP Envelope   -1000.00 1000.00 -1000.00 1000.00 -1000.00 1000.00\n'
else:    
    mainString = '-Envelope '
    invString = '+Envelope '
    EnvelopeBody = 'RPP Envelope   -100.00 100.00 -100.00 100.00 -100.00 100.00\n'

f = open(filename,"r+")
lines = f.readlines()

#Modify all regions
for row in range(0,len(lines)):
    if row > info['end1'][0] +1 and row < info['end2'][0] :
        line_content = lines[row].split(' ')
        newExpression = 0
        if len(lines[row]) >= 15:
            if lines[row][15] == '|' or lines[row][13] == '5':
                newExpression = 1
        changed = 0
        if line_content[0] != '*':


            #Scenario 1: Region containing the black hole
            if Inverse == 0:
                if line_content[0] == info['BLCKHOLE'][0]:
                    lines[row] = lines[row][:15] + invString + '\n'
                    changed = 1
                else:
                    lines[row] = lines[row][:15] + mainString + '\n'
                    changed = 1

            #Scenario 2: Multiple zones on the same line
            idx = []
            for i in range(0,len(lines[row])):
                if int(lines[row][i] == '|'):
                    idx.append(i)  
            if len(idx) > 1 and not changed:
                lines[row]=lines[row][:15] + mainString + lines[row][15:]
                for i in range(0,len(idx)):
                    lines[row]=lines[row][:(idx[i] +2 +(i+1)*10)] + mainString + lines[row][(idx[i] +2 +(i+1)*10):]
                changed = 1

            #Scenario 3: For regions of a single zone, or multiple zones on different lines
            if len(lines[row]) >= 15 and not changed and newExpression:
                if lines[row][15] == '|': 
                     lines[row]=lines[row][:17] + mainString + lines[row][17:]
                else:
                     lines[row]=lines[row][:15] + mainString + lines[row][15:]




#Add Envelope body
lines2 = lines[0:info['Geobegin'][0]+2]
lines2.append(EnvelopeBody)
lines2[info['Geobegin'][0]+3:] = lines[info['Geobegin'][0]+2:]
lines = lines2


#Add Envelope region
lines2 = lines[0:info['end1'][0]+2]
lines2.append('EnvReg       5 +Envelope\n')
lines2[info['end1'][0]+3:] = lines[info['end1'][0]+3:]
lines = lines2

#Assign blackhole to region
lines2 = lines[0:info['end2'][0]+2]
lines2.append('ASSIGNMA    BLCKHOLE    EnvReg\n')
lines2[info['end2'][0]+3:] = lines[info['end2'][0]+3:]



#Write
with open(Envfilename, 'w') as output:
    output.writelines(lines2)

print('New file created called ' + Envfilename)

