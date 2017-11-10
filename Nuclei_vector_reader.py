


import time as time
start = time.time()

path = '//rpclustersrv1/cbjorkma/Sesame'

filenames = ['ATLAS_ID3_Fixgeom_prompt_40001_tsresnuc_prompt_nuclides','ATLAS_ID3_Fixgeom_prompt_59001_tsresnuc_prompt_nuclides', 'ATLAS_ID3_Fixgeom_prompt_62001_tsresnuc_prompt_nuclides']

outName = 'tmpName'

import os


os.chdir(path)

MasterDict = {}


for i in range(len(filenames)):
    filename = filenames[i]
    f = open(filename,"r+")
    lines = f.readlines()
    f.close()

    for j in range(len(lines)):
        line_cont = lines[j].split(' ')
        key = (line_cont[1] ,line_cont[2], line_cont[3], line_cont[4])
        
        val = float(line_cont[6])
        if MasterDict.has_key(key):
            MasterDict[key] = (MasterDict[key][0] + val ,MasterDict[key][1] + val*val, MasterDict[key][2] ,MasterDict[key][3])
        else:      
            MasterDict[key] = (val, val*val,line_cont[7], line_cont[9])


keys = MasterDict.keys()
values = MasterDict.values()
sortedVal = sorted(zip(keys,values))

import math
N = float(len(filenames)) #Cannot be int

def calcError(vals, sqrdvals):
    squareofmean = math.pow(vals/N,2)
    meanofsquares = sqrdvals/N
    try:
        return math.sqrt((1/(N -1))*(meanofsquares - squareofmean))
    except:
        return 0

    
out = []
for i in range(len(sortedVal)):
    line = sortedVal[i]
    key = ' '.join(map(str, (sortedVal[i][0])))
    mean = str(round(line[1][0]/N,8))
    error = str(round(calcError(line[1][0],line[1][1]),8)) 
    
    out.append(key + ' ' + mean +' ' + error + ' ' + line[1][2] + ' ' + line[1][3])

f = open(outName, 'w')
f.writelines(out)
f.close()


stop = time.time()
print 'Took ' + str(stop - start) + ' seconds'





#Code for testing validity of script---------------------
test = [1, 2, 3] #<--- add three values from different runs for any nuclei here and see if their mean and SD is equivalent in the out file

vals = sum(test)

sqrdtest = []
for i in range(len(test)):
    sqrdtest.append(test[i]*test[i])
sqrdvals = sum(sqrdtest)

print 'mean = ' + str(vals/N)
print 'error = ' + str(calcError(vals, sqrdvals))
#---------------------------------------------------------



     
        



            
            
            
            
            
            
            
            
            
            
            
            
            
            