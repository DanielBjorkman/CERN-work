# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 17:05:58 2017

@author: cbjorkma
"""

#Transversal distribution

import os
import numpy as np
#import math as math
#directory = "//cern.ch/dfs/Users/c/cbjorkma/Documents/LSS 2"

directory = "//rpclustersrv1/cbjorkma/LSS2"

os.chdir(directory)




def readPhase(filename):
    try:
        print "Attempting to load file..."
        out = np.loadtxt(filename , skiprows = 1)
        print "File loaded"
        np.save(filename, out)
        return out
    except ValueError:
        print "Repairing file... "
        f = open(filename,"r+")
        lines = f.readlines()
        for i in range(len(lines)):
            string = lines[i]
            #print 'Before ' + string
            tmp = list(string)
            try:
                tmp[-5] = ' '
                string = "".join(tmp)
                lines[i] = string
            except:
                pass
        f.seek(0)
        f.writelines(lines)
        f.truncate()
        f.close()
        print "Loading file..."
        out = np.loadtxt(filename , skiprows = 1)
        np.save(filename, out)
        print "File loaded"
        return out        
                   
from os import listdir
from os.path import isfile, join         
        
def readPhaseDirectory(path, identifier):



    onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]           
    files = filter(lambda x: x[-3:] == identifier , onlyfiles)             
    files = sorted(files)      
    
    print 'Found ' + str(len(files)) + ' files'
    
    data = []
    print "Attempting to load files..."    
    for i in range(len(files)): #
      
        filename = files[i]

        try:
            data.append( np.loadtxt(filename , skiprows = 1))
        except ValueError:
            print "Repairing " + filename
            f = open(filename,"r+")
            lines = f.readlines()
            for i in range(len(lines)):
                string = lines[i]
                #print 'Before ' + string
                tmp = list(string)
                try:
                    tmp[-5] = ' '
                    string = "".join(tmp)
                    lines[i] = string
                except:
                    pass
            f.seek(0)
            f.writelines(lines)
            f.truncate()
            f.close()
            data.append( np.loadtxt(filename , skiprows = 1))     
    
    out = data[0]
    for i in range(1,len(data)):
        out = np.concatenate( (out, data[i]), axis = 0)    
    print 'Data loaded'
    return out
        
        
    
#filename = 'LSS2_exp001_fortLarge.90' 
##fluka1 = readPhase(filename)    
#fluka1 = np.load(filename + '.npy')
#np.save(filename, fluka1)
#
#
#filename = 'LSS2_exp001_fortLarge.91' 
#fluka2 = readPhase(filename)   
##fluka2 = np.load(filename + '.npy')  
#


#fluka1 = np.load('LSS2_exp001_fortLarge.90.npy')
#
#fluka2 = np.load('LSS2_exp001_fortLarge.91.npy')
#


path = "//rpclustersrv1/cbjorkma/LSS2/Run Inelastic"          
os.chdir(path)        
#fluka1 = readPhaseDirectory(path, '.90')           
#np.save('90', fluka1)
fluka1 = np.load('90.npy')

path = "//rpclustersrv1/cbjorkma/LSS2/Run Inelastic"          
os.chdir(path)        
#fluka2 = readPhaseDirectory(path, '.91')           
#np.save('91', fluka2)
fluka2 = np.load('91.npy')





import matplotlib as mpl
import matplotlib.pylab as plt
import numpy as np
#
#import math

end = int(0.1*fluka1.shape[0])




fig = plt.figure()


plt.subplot(121)
x = fluka1[0:end,1]
y = fluka1[0:end,2]

plt.hist2d(x, y, bins=100, norm=mpl.colors.LogNorm(),cmap="viridis")




#H, xedges, yedges = np.histogram2d(x, y, bins=50, normed = True)
#
#plt.imshow(H)

#H2, _, _ = np.histogram2d(x,y, bins=50)
#extent = [0,1, xedges[-1], xedges[0]]
#plt.imshow(H/H2)
#plt.colorbar()



plt.xlabel('x [cm]', fontsize = 12)
plt.ylabel('y [cm]', fontsize = 12)
plt.title('Before TPST')
cbar = plt.colorbar()
#cbar.ax.set_xticklabels(0.10,100)
#cbar.set_label('%', rotation = 'horizontal')

cbar.set_label('Intensity')

plt.xlim(-2.7, 9 )




plt.subplot(122)
x = fluka2[0:end,1]
y = fluka2[0:end,2]

plt.hist2d(x, y, bins=100, norm=mpl.colors.LogNorm(),cmap="viridis")

plt.xlabel('x [cm]', fontsize = 12)
plt.ylabel('y [cm]', fontsize = 12)
plt.title('After TPST')
cbar = plt.colorbar()
#cbar.ax.set_xticklabels(0.10,100)
#cbar.set_label('%', rotation = 'horizontal')
cbar.set_label('Intensity')


plt.xlim(-2.7, 9 )




plt.show()


















