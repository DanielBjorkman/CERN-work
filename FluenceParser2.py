# -*- coding: utf-8 -*-
"""
Created on Tue Jul 03 09:57:03 2018

@author: cbjorkma
"""

# -*- coding: utf-8 -*-
"""
Created on Mon May 28 11:44:46 2018

@author: cbjorkma
"""

#FluenceParser

import os

path = '//rpclustersrv1/cbjorkma/LSS2/Fluence/Lead blocks' 

os.chdir(path)



block1 = []
block2 = []
block3 = []
block4 = []

blocks = (block1,block2,block3,block4)


allfiles = os.listdir(path)


units = ['74','75','76','77']

try:
    os.mkdir(path + '/NewFormat')
except:
    pass


allfiles = sorted(filter(lambda x: x[-2:] in units, allfiles))

def editfile(thefile):
   # for j in range(len(subfiles)): 
        #subfile = subfiles[j]
        vec = ['Pro','Pi+','Pi-','Neu']
        #vec2 = ['a','b']
        for i in range(len(thefile)):
            if thefile[i][0] == '1':
                string = thefile[i+2][:20] + thefile[i+2][22] +thefile[i+2][25] + '_' +  vec.pop(0) + thefile[i+2][26:]
                thefile[i+2] = string

        #subfiles[j] = subfile        
        return thefile       

for k in range(len(units)):

    filenames = filter(lambda x: x[-2:] == units[k], allfiles)

    for i in range(len(filenames)):
        os.chdir(path)
        thefile  = open(filenames[i], 'r').readlines()
        newfile = editfile(thefile)
        
        os.chdir(path + '/NewFormat')
        file = open(filenames[i][:-3] + 'edit' + filenames[i][-3:] , 'w')
        for j in range(len(newfile)):
            file.write(newfile[j])
        file.close()
    #blocks[k].append(thefile)    


































