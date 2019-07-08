# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 10:36:40 2019

@author: cbjorkma
"""

#ATLASbenchmark


import os
import glob
from USRBIN import USRBIN


#ATLAS fluka version


normfactor = 0.0036

idx = 0
cool = '28 days'


#2.3
path = '//rpclustergw/cluster_temp/cbjorkma/2019-02-15_16h44m29s_ATLAS2'
os.chdir(path)

filenames = sorted(glob.glob('*.lis'))

point3 = USRBIN(filenames[0], path, normfactor)
point3.read()
point3.calc()