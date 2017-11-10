# -*- coding: utf-8 -*-
"""
Created on Tue Aug 08 17:06:54 2017

@author: cbjorkma
"""

#Code collector

#--------------------------------------------------------------------------------
path = '//rpclustersrv1/cbjorkma/Dump studies/Uppstream Hole study/Fluence'

Output = 'Test'

fileNumber= 70



import subprocess
#subprocess.check_call(["c:\\fe re\\python.exe", "program", etcetc...])



import os

os.chdir(path)

#os.getcwd()


os.system('ls *fort.' + str(70) +' | wc -l > inpfile')

os.system('ls *fort.' + str(70) +' >> inpfile')

os.system('echo "*" >> inpfile')

os.system('echo "' + Output + '" >> inpfile')

os.system('./exe -s -i inpfile')


#--------------------------------------------------------------------------------