# -*- coding: utf-8 -*-
"""
Created on Fri Sep 14 10:52:59 2018

@author: cbjorkma
"""

#AtlasfieldParser

import os

path = '//rpclustersrv1/cluster_temp/cbjorkma/OpeningScenarios/PROMPT/2018-12-05_15h36m13s_ATLAS2'

os.chdir(path)



subs = [x[0] for x in os.walk(path)]

subs.pop(0)


filename = 'magfld.txt'
magfldpath = '//rpclustersrv1/cluster_temp/cbjorkma/OpeningScenarios'
os.chdir(magfldpath)
filecontent = open(filename,"r+").readlines()
os.chdir(path)

#filename2 = 'Atlas.geo'
#
#filecontent2 = open(filename2,"r+").readlines()
#


for i in range(len(subs)):
#i = 0
    os.chdir(subs[i])
    f = open(filename,"w+")
#    f2 = open(filename2,"w+")
    for j in range(len(filecontent)):
        try:
            f.write(filecontent[j])
        except:
            pass
#        try:
#            f2.write(filecontent2[j])
#        except:
#            pass
    f.close()
#    f2.close()

    
    
    
    
    
    
print 'Done'

