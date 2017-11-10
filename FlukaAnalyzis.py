# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 16:31:32 2017

@author: cbjorkma
"""

import os

os.chdir('//cern.ch/dfs/Users/c/cbjorkma/Documents/Visual Studio 2013/Projects/PythonApplication1')

from Flukato3dMatrix import Flukato3dMatrix
import numpy as np

directory = '//rpclustersrv1/cbjorkma/Dump studies'
filename = 'Dump2Res_22.bnn.lis'


cube = Flukato3dMatrix(filename, directory,1)
np.save('cubeRef', cube)
# #np.load('filename.npy')

