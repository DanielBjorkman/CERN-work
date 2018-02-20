# -*- coding: utf-8 -*-
"""
Created on Thu Feb 15 16:10:46 2018

@author: cbjorkma
"""

#Find ifs

import os

path = '//rpclustersrv1/cbjorkma/Scrapers'

os.chdir(path)

filename = 'arc1RP_exp.inp'

f = open(filename, 'r')

lines = f.readlines()

ifs = []
endifs = []
combo = []

for i in range(len(lines)):
    b = 0
    if lines[i][0:3] == '#if':
        ifs.append(i)
        a = i
    if lines[i][0:6] == '#endif':
        endifs.append(i)
        combo.append((a,i))

        

for i in range(len(combo)-1):
    if combo[i][0] == combo[i+1][0]:
        print combo[i][0]
        print combo[i+1][0]
        
        
print len(ifs)
print len(endifs)

print len(ifs) == len(endifs)