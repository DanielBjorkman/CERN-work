# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 15:29:21 2018

@author: cbjorkma
"""

#SetVacum

import os

path = '//rpclustersrv1/cbjorkma/Dump studies/Settovacuum'

os.chdir(path)


#filename = 'Dump18Res.inp'
filename = 'Dump18block1.inp'

fileIn = open(filename,'r').readlines()

fileOut = open(filename[0:-4] + 'Vacuum.inp' ,'w')


for i in range(len(fileIn)):
    if fileIn[i][0:8] == 'ASSIGNMA':
        if fileIn[i][-9:-1] != 'BLCKHOLE' and fileIn[i][-7:-1] != 'VACUUM' :
            line = fileIn[i][0:-1] + '                                  VACUUM' + fileIn[i][-1:]
            #line = fileIn[i][0:-1] + '    VACUUM' + fileIn[i][-1:]
            #line[64:70] = 'VACUUM'
            fileOut.write( line)
        else:
            fileOut.write( fileIn[i])     
    else:
        fileOut.write( fileIn[i])






fileOut.close()

#fileIn.close()



#fileIn[16464][-9:-1]
#fileIn[1448][0:-2]
#
#fileIn[1448][-1:]
