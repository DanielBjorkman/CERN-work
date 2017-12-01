# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 14:12:04 2017

@author: cbjorkma
"""

#Phase space plot


import os
import numpy as np
import math as math
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
        
def readPhaseDirectory(path):



    onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]           
    files = filter(lambda x: x[-3:] == '.90' , onlyfiles)             
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


          
  

#
path = "//rpclustersrv1/cbjorkma/LSS2/run11"          
os.chdir(path)        
fluka1 = readPhaseDirectory(path)           
np.save('run11', fluka1)
#  


  
#filename = 'LSS2_exp001_fort.90' 
##filename = 'fort.90' 
##fluka1 = readPhase(filename)    
#fluka1 = np.load('run11.npy')
    
end = int(1*fluka1.shape[0])

print 'Plotting ' + str(end) + ' primaries'




import matplotlib.pyplot as plt
import matplotlib.ticker as tk
#from matplotlib.ticker import FuncFormatter

#        
#plt.close()
#plt.close()



#
#
#Position according to energy-------------------------------------------



x = fluka1[0:end,1]
y = fluka1[0:end,3]
z = fluka1[0:end,5]
print 'Maximum momenta ' + str(max(z))


def my_func(x, pos):
    return str(x)

fmt1 = tk.FuncFormatter(my_func)


fig , ax = plt.subplots(1, 1)
plt.suptitle('Momentum distribution, Phase space X')
plot = ax.scatter(x, y, s=5, c=z, cmap="viridis", edgecolors="none")
ymin, ymax = 0.0003 ,0.0028
xmin, xmax = 0.036*100, 0.1*100
plt.ylim(ymin, ymax)
plt.xlim(xmin, xmax )
cbar = fig.colorbar(plot ,format=fmt1)
cbar.set_label('GeV/c', rotation = 'horizontal', labelpad=15)
#h.set_rotation(0)



plt.xlabel('x [cm]', fontsize = 12)
h = plt.ylabel("$x^p$", fontsize=18)
h.set_rotation(0)
plt.grid()
#
#
plt.show()
#
##





from matplotlib.colors import LogNorm
from matplotlib.gridspec import GridSpec


#Starting plotting-----------------------------------------------------------------



fig = plt.figure()


plt.suptitle('Phase space Y')

x = fluka1[0:end,2]
y = fluka1[0:end,4]


gs = GridSpec(4,4)

ax_joint = fig.add_subplot(gs[1:4,0:3])


plt.hist2d(x, y, bins=100, norm=LogNorm())
ymin, ymax = -0.00065 ,0.0006
xmin, xmax = -2,2
plt.ylim(ymin, ymax)
plt.xlim(xmin, xmax )


plt.xlabel('y [cm]', fontsize = 12)
h = plt.ylabel("$y^p$", fontsize=18)
h.set_rotation(0)
#plt.grid()
#plt.colorbar()



ax_marg_x = fig.add_subplot(gs[0,0:3])

#np.histogram(x, bins = 40, density = True)
#plt.setp(ax_marg_x.get_xticklabels(), visible=False)
#plt.xlim(xmin, xmax)
##plt.set_yscale('log')
#plt.grid()
##plt.set_ylabel('Intensity')

results, edges = np.histogram(x, normed=True, bins = 40)    
binWidth = edges[1] - edges[0]    
plt.bar(edges[:-1], results*binWidth, binWidth)   
plt.xlim(xmin, xmax )
plt.yscale('log')
plt.tick_params(
    axis='x',          # changes apply to the x-axis
    bottom='off',      # ticks along the bottom edge are off
    labelbottom='off') # labels along the bottom edge are off
h = plt.ylabel('%')
h.set_rotation(0)
plt.grid()          
                



ax = fig.add_subplot(gs[1:4,3])
#


results, edges = np.histogram(y, normed=True, bins = 40)    
binWidth = edges[1] - edges[0]    
plt.barh(edges[:-1], results*binWidth , binWidth)   
plt.ylim(ymin, ymax )
plt.xscale('log')
plt.xlabel('%')

plt.grid()

plt.setp( ax.get_yticklabels(), visible=False)






plt.show()

#
##
##
#
#
#
##Figure 2--------------------------------------------------------------
fig = plt.figure()


plt.suptitle('Phase space X')

x = fluka1[0:end,1]
y = fluka1[0:end,3]


gs = GridSpec(4,4)

fig.add_subplot(gs[1:4,0:3])

plt.hist2d(x, y, bins=200, norm=LogNorm())
ymin, ymax = 0.0003 ,0.0028
xmin, xmax = 0.036*100, 0.1*100
plt.ylim(ymin, ymax)
plt.xlim(xmin, xmax)

plt.xlabel('x [cm]', fontsize=12)
h = plt.ylabel("$x^p$", fontsize=18)
h.set_rotation(0)
#plt.grid()
#plt.colorbar()



ax_marg_x = fig.add_subplot(gs[0,0:3])

#np.histogram(x, bins = 40, density = True)
#plt.setp(ax_marg_x.get_xticklabels(), visible=False)
#plt.xlim(xmin, xmax)
##plt.set_yscale('log')
#plt.grid()
##plt.set_ylabel('Intensity')

results, edges = np.histogram(x, normed=True, bins = 40)    
binWidth = edges[1] - edges[0]    
plt.bar(edges[:-1], results*binWidth, binWidth)   
plt.xlim(xmin, xmax )
plt.yscale('log')

plt.tick_params(
    axis='x',          # changes apply to the x-axis
    bottom='off',      # ticks along the bottom edge are off
    labelbottom='off') # labels along the bottom edge are off
h = plt.ylabel('%')
h.set_rotation(0)

plt.grid()

#ax_marg_x.hist(x, bins = 80)
#plt.setp(ax_marg_x.get_xticklabels(), visible=False)
#ax_marg_x.set_xlim(xmin, xmax)
#ax_marg_x.set_yscale('log')
#ax_marg_x.grid()
#ax_marg_x.set_ylabel('intensity')
#


ax = fig.add_subplot(gs[1:4,3])
#

#ax_marg_y.hist(y,orientation="horizontal",  bins= 80)
#
#plt.setp(ax_marg_y.get_yticklabels(), visible=False)
#ax_marg_y.set_ylim(ymin, ymax)
#ax_marg_y.set_xscale('log')
#ax_marg_y.grid()
#ax_marg_y.set_xlabel('Intensity')

results, edges = np.histogram(y, normed=True, bins = 40)    
binWidth = edges[1] - edges[0]    
plt.barh(edges[:-1], results*binWidth , binWidth)   
plt.ylim(ymin, ymax )
plt.xscale('log')
plt.xlabel('%')

plt.grid()

plt.setp( ax.get_yticklabels(), visible=False)





plt.show()



#
#
#































