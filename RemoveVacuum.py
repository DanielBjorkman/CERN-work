# -*- coding: utf-8 -*-




#Remove Vacuum

import os

path = '//rpclustersrv1/cbjorkma/ALICE/NoVacuum'

os.chdir(path)


#filename = 'Dump18Res.inp'
filename = 'ALICE1.inp'

fileIn = open(filename,'rb').readlines()

fileOut = open(filename[0:-4] + 'RemovedVac.inp' ,'wb')


for i in range(len(fileIn)):
    if fileIn[i][0:8] == 'ASSIGNMA' and fileIn[i][-7:-1] == 'VACUUM':
        line = fileIn[i]
        print line
        line = line[:-8] + '      ' + line[-1:]
        print line
        fileOut.write( line)
        
        
#        if fileIn[i][-9:-1] != 'BLCKHOLE' and fileIn[i][-7:-1] != 'VACUUM' :
#            line = fileIn[i][0:-1] + '                                  VACUUM' + fileIn[i][-1:]
#            #line = fileIn[i][0:-1] + '    VACUUM' + fileIn[i][-1:]
#            #line[64:70] = 'VACUUM'
#            fileOut.write( line)
#        else:
#            fileOut.write( fileIn[i])
            
            
            
            
    else:
        fileOut.write( fileIn[i])






fileOut.close()

#fileIn.close()



#fileIn[16464][-9:-1]
#fileIn[1448][0:-2]
#
#fileIn[1448][-1:]
