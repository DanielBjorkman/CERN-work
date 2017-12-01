# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 10:42:36 2017

@author: cbjorkma
"""

#Loss map


import os
import numpy as np
import matplotlib.pyplot as plt
import math
#import math as math
#directory = "//cern.ch/dfs/Users/c/cbjorkma/Documents/LSS 2"

directory = "//rpclustersrv1/cbjorkma/LSS2"

os.chdir(directory)


septaColor = 'limegreen'

#filename = 'LSS2_exp001_usrmed(3).dat'

#filename = 'usrmed(3).dat'
#
#data = np.loadtxt(filename , skiprows = 1)
#np.save(filename, data)
from os import listdir
from os.path import isfile, join      

def readPhaseDirectory(path):



    onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]           
    files = filter(lambda x: x[-3:] == 'dat' , onlyfiles)             
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





path = "//rpclustersrv1/cbjorkma/LSS2/run09"          
os.chdir(path)        
#data = readPhaseDirectory(path)           
#np.save('run09usermed', data)
#



data = np.load('run09usermed.npy')

#toPlot =normHist( data[0:,5])    

end = math.floor(0.0001* data.shape[0])




fig = plt.figure()
ax1 = fig.add_subplot(111)
#plot = plt.hist(data[0:,5]/1, log = True, bins = 80, normed = True)









import matplotlib.patches as patches



myarray = data[0:end,5]
results, edges = np.histogram(myarray, normed=True, bins = 80)    
binWidth = edges[1] - edges[0]    
plt.bar(edges[:-1], results*binWidth, binWidth)   



plt.xlabel('Z [cm]')
h = plt.ylabel('%')
h.set_rotation(0)
plt.title('LSS2 Lossmap')
plt.yscale('log')
plt.grid()
plt.xlim(0, 10400 )

ax = ax1.twinx()

plt.ylim(0, 35 )

#Quads
plt.axvline(x=0,linestyle = '--' ,label='Quadrupoles', color = 'black')
plt.axvline(x=3199.77,linestyle = '--', color = 'black' )
plt.axvline(x=6399.54,linestyle = '--', color = 'black' )
plt.axvline(x=9599.31,linestyle = '--', color = 'black' )

#ZSs
r1 = patches.Rectangle((355.45,6.8), 313,0.006, angle= -0.0861284, color = septaColor, label = 'septa')
r2 = patches.Rectangle((746.45,6.212), 313,0.006, angle= -0.0861284, color = septaColor)
r3 = patches.Rectangle((1137.45,5.623), 313,0.006, angle= -0.0861284, color = septaColor)
r4 = patches.Rectangle((1528.45,5.035), 313,0.006, angle= -0.0861284, color = septaColor)
r5 = patches.Rectangle((1919.45,4.446), 313,0.006, angle= -0.0861284, color = septaColor)
ax.add_patch(r1)
ax.add_patch(r2)
ax.add_patch(r3)
ax.add_patch(r4)
ax.add_patch(r5)


#TPST
r6 = patches.Rectangle((4685.26,3.94), 214 , 0.46, angle= 0.02838015, color = septaColor)
ax.add_patch(r6)

#MST
r7 = patches.Rectangle((4973.016812,4.079), 214,0.41, angle= 0.028409155, color = septaColor,alpha = 0.75)
r8 = patches.Rectangle((5296.416982,4.240), 214,0.41, angle= 0.028409155, color = septaColor,alpha = 0.75)
r9 = patches.Rectangle((5619.816971,4.401), 214,0.41, angle= 0.028409155, color = septaColor,alpha = 0.75)
ax.add_patch(r7)
ax.add_patch(r8)
ax.add_patch(r9)

#MSE
r10 = patches.Rectangle((6717.6328,4.825), 241.32,1.775, angle= -0.025632321, color = septaColor,alpha = 0.75)
r11 = patches.Rectangle((7041.0248,4.777), 241.32,1.775, angle= 0.047495174, color = septaColor,alpha = 0.75)
r12 = patches.Rectangle((7364.41710,5.142), 241.32,1.775, angle= 0.12062252, color = septaColor,alpha = 0.75)
r13 = patches.Rectangle((7687.809591,5.918), 241.32,1.775, angle= 0.193498169, color = septaColor,alpha = 0.75)
r14 = patches.Rectangle((8011.202246,7.107), 241.32,1.775, angle= 0.266624488, color = septaColor,alpha = 0.75)
ax.add_patch(r10)
ax.add_patch(r11)
ax.add_patch(r12)
ax.add_patch(r13)
ax.add_patch(r14)

#QFA219
r15 = patches.Rectangle((9398.76,18.63940), 401,0.2, angle= 0.399731511, color = 'red')
r16 = patches.Rectangle((9398.76,27.43940), 401,0.2, angle= 0.399731511, color = 'red')
ax.add_patch(r15)
ax.add_patch(r16)

plt.legend(loc = 2)
plt.setp( ax.get_yticklabels(), visible=False)
#--------------------------------------------------

#directory = "//cern.ch/dfs/Users/c/cbjorkma/Documents/LSS 2/LSS2 optics validation"
#os.chdir(directory)
#
#flukaData = []
#
#
#flukaData.append( np.loadtxt('LSS2_exp001_TRAKFILEp1' , skiprows = 1))
#flukaData.append( np.loadtxt('LSS2_exp001_TRAKFILEp2' , skiprows = 1))
#flukaData.append( np.loadtxt('LSS2_exp001_TRAKFILEp3' , skiprows = 1))
#flukaData.append( np.loadtxt('LSS2_exp001_TRAKFILEp4' , skiprows = 1))
#flukaData.append( np.loadtxt('LSS2_exp001_TRAKFILEp5' , skiprows = 1))
##flukaData.append( np.loadtxt('LSS2_exp001_TRAKFILEp6' , skiprows = 1))
#flukaData.append( np.loadtxt('LSS2_exp001_TRAKFILEp7' , skiprows = 1))
#flukaData.append( np.loadtxt('LSS2_exp001_TRAKFILEp8' , skiprows = 1))
#
#flukaData.append( np.loadtxt('LSS2_exp001_TRAKFILEp9' , skiprows = 1))
#flukaData.append( np.loadtxt('LSS2_exp001_TRAKFILEp10' , skiprows = 1))
#flukaData.append( np.loadtxt('LSS2_exp001_TRAKFILEp11' , skiprows = 1))
#
#
#
#for i in range(len(flukaData)):
#    fluka = flukaData.pop(0)
#    plt.plot(fluka[0:,2] , fluka[0:,0], color='k',linestyle='--', alpha=0.2)
#
#
##--------------------------------------------------



#--------------------------------------------------------------------------


#Read fluka output
#filenameFluka = 'LSS2_exp001_TRAKFILEp2'
#fluka = np.loadtxt(filenameFluka , skiprows = 1)




plt.show()


