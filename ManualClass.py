# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 16:39:42 2018

@author: cbjorkma
"""

#ManualClass


class ManualClass():
    
    
    def __init__(self,filename, path, normfactor = 1):
        self.path = path
        self.filename = filename
        self.data = []
        self.normfactor = normfactor
        self.xes = []
        
    def read(self):
        
        
        import os
        import numpy as np
        import pandas as pd
#        import datetime #, timedelta
#        import matplotlib.pyplot as plt

        path = self.path #'//rpclustersrv1/cbjorkma/LSS2/'
        
        os.chdir(path)
        
        #filename = 'ManualMeasurent.xlsx'
    
        thefile = pd.read_excel(self.filename)
        
        data = np.zeros(thefile.shape)
        
        quad216 = 3.791*100
        quad217 = 35.7887*100
        quad218 = 67.7864*100
        quad219 = 99.7841*100
        
        data[0:,0] = (thefile.position -216)*(quad217 - quad216) -480
        data[0:,1] = thefile.doserate
        data[0:,2] = (thefile.position1m30h -216)*(quad217 - quad216) -630
        data[0:,3] = thefile.doserate1m30h
        
        self.data = data
        
    def readFluka(self, path):
        
        import os
        import numpy as np
        
        self.xes  = np.arange(-500,10100,(10100+500)/float(1000))
        
        os.chdir(path)
        
        def openFluka(filename,shift = 0):
            data = []
            fp = open(filename)
            lines = fp.readlines()
            for i in range(len(lines)):
                if i > 8 +shift and i < 109+shift:
            #        datalines.append(lines[i])
                    for j in range(len(lines[i].split())):
                        data.append(lines[i].split()[j])
            fp.close()
            
            dataout = np.zeros(len(data))
            for i in range(len(data)):
                dataout[i] = float(data[i])
            
            return dataout
        
        def openFlukaErrors(filename,shift = 0):
            errors = []
            fp = open(filename)
            lines = fp.readlines()
            for i in range(len(lines)):
                if i > 111 +shift and i < 212 +shift:
            #        datalines.append(lines[i])
                    for j in range(len(lines[i].split())):
                        errors.append(lines[i].split()[j])
            fp.close()
            dataout = np.zeros(len(errors))
            for i in range(len(errors)):
                dataout[i] = float(errors[i])
            
            return dataout
        
        files = sorted(os.listdir(path))
        #print files
        
        #filename = '30h'
        data1 = openFluka(files[0])
        #errors1 = openFlukaErrors(filename1)
        data2 = openFluka(files[1])
        
        self.fluka1 = data1*self.normfactor
        self.errors1 = openFlukaErrors(files[0])
        self.fluka2 = data2*self.normfactor
        self.errors2 = openFlukaErrors(files[1])
#        #Converts data to uSv/h
#        data1 = 0.0036*data1
#        
#        #Normalization
#        normFactor = 1 / 0.1772837
#        data1 = normFactor * data1
#        
#        #Volume compensation
#        #Volume = 20*20*(500+10100)/float(1000)
#        #data1 = data1 /Volume
#        
#        
#        
#        #filename = '1m30h'
#        data2 = openFluka(filename2, -15)
#        errors2 = openFlukaErrors(filename2, -15)
#        
#        
#        #Converts data to uSv/h
#        data2 = 0.0036*data2
#        
#        #Normalization
#        normFactor = 1 / 0.1772837
#        data2 = normFactor * data2        
#        
#        
        
#        
##        
#filename = 'ManualMeasurent.xlsx'
#path = '//rpclustersrv1/cbjorkma/LSS2/'
#
#x = ManualClass(filename, path)
#        
#x.read()
#path = '//rpclustersrv1/cbjorkma/LSS2/FullActivation/Manual'
#x.readFluka(path)
##x.readFluka('30h','1m30h')
#
#print x.fluka1[0]
#
#print x.fluka1[-1]
#
#print x.errors1[0]
#
#print x.errors1[-1]
#

        
        
        
        
        
        