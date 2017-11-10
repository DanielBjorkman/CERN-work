# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 14:46:26 2017

@author: cbjorkma
"""



import os
import numpy as np
import math as math
directory = "//cern.ch/dfs/Users/c/cbjorkma/Documents/LSS 2"
os.chdir(directory)


#Read fluka output
filenameFluka = 'LSS2_exp001_TRAKFILEp1'
fluka = np.loadtxt(filenameFluka , skiprows = 1)

#--------------------------------------------------------------------------
#Read Twiss
def readTwiss(filename):

    #filename = 'b0_p1.tfs'
    
    f = open(filename,"r+")
    lines = f.readlines()
    
    num_lines = len(lines)
    
    cont = []
    #cont.append('NAME')
    
    for i in range(0,num_lines):
        if lines[i][0:6] == '* NAME':
            start = i
            for ii in range(10,len(lines[i])):
                if lines[i][ii] != ' ' and lines[i][ii -1] == ' ':
                    cont.append(lines[i][ii])
            break   
    cont.pop()
    
    matrix = np.zeros((num_lines - (start +2), len(cont) ))
    
    lines = lines[start+2:]
    #tmp = lines[0].split()[5].split('e')
    #Px = float(tmp[0])*math.pow(10,float(tmp[1]))
    #shift = float(lines[0].split()[1])
    for i in range(0,len(lines)):
        line_content = lines[i].split()
        matrix[i,0] = float(line_content[1])# - shift
        matrix[i,1] = line_content[2]
        matrix[i,2] = line_content[3]
        matrix[i,3] = line_content[4]
        matrix[i,4] = line_content[5]
    return matrix
#--------------------------------------------------------------------------
matrix = readTwiss('b0_p1.tfs')

# Read all twiss trajectories--------------------------------------------
#filenames = []
#
#filenames.append('b0_p1.tfs')
#filenames.append('b0_p2.tfs')
#filenames.append('b0_p3.tfs')
#filenames.append('b0_p4.tfs')
#filenames.append('b0_p5.tfs')
#filenames.append('b0_p6.tfs')
#filenames.append('b0_p7.tfs')
#filenames.append('b0_p8.tfs')
#filenames.append('b0_p9.tfs')
#
#matrixDefined = False
#
#for k in range(len(filenames)):
#    filename = filenames.pop(0)
#    f = open(filename,"r+")
#    lines = f.readlines()
#    num_lines = len(lines)
#    cont = []
#
#
#    for i in range(0,num_lines):
#        if lines[i][0:6] == '* NAME':
#            start = i
#            for ii in range(10,len(lines[i])):
#                if lines[i][ii] != ' ' and lines[i][ii -1] == ' ':
#                    cont.append(lines[i][ii])
#            break   
#    cont.pop()
#
#    if matrixDefined == 0:
#        matrix = np.zeros((num_lines - (start +2), len(cont),len(filenames) +1 ))
#        matrixDefined = 1
#        
#    lines = lines[start+2:]
#    #tmp = lines[0].split()[5].split('e')
#   # Px = float(tmp[0])*math.pow(10,float(tmp[1]))
#    #shift = float(lines[0].split()[1])
#    for i in range(0,len(lines)):
#        line_content = lines[i].split()
#        matrix[i,0,k] = float(line_content[1]) #- shift
#        matrix[i,1,k] = line_content[2]
#        matrix[i,2,k] = line_content[3]
#        matrix[i,3,k] = line_content[4]
#        matrix[i,4,k] = line_content[5]
#------------------------------------------------------------------------------




#Total momentum
#P = 400 #GeV
#Px = -0.001961832134
#Ptot = math.sqrt( math.pow(P,2) + math.pow(P*Px,2))
#print('Total energy = ' + str(Ptot))

#cosx = Px * P / Ptot
#print('Cosx = ' + str(cosx))


import matplotlib.pyplot as plt
import matplotlib.patches as patches
#import matplotlib as mpl

plt.close()
#plt.subplot(2,1,1)
fig = plt.figure()
ax = fig.add_subplot(211)
plt.plot(fluka[0:,2] , fluka[0:,0], label='FLUKA', color='r',linestyle = ':',linewidth=3.0, marker='x') #, marker='x'
plt.plot(matrix[0:,0]*100 , matrix[0:,1]*100, label='MADX', color='k') #
#for k in range(len(matrix[0,0,0:])):
#    plt.plot(matrix[0:,0,k]*100 , matrix[0:,1,k]*100, color='k') #, label='MADX'
#ax.set_xlim([5212, 5296])

#Quads
plt.axvline(x=0,linestyle = '--' ,label='Quadrupoles')
plt.axvline(x=3199.77,linestyle = '--' )
plt.axvline(x=6399.54,linestyle = '--' )
plt.axvline(x=9599.31,linestyle = '--' )

#ZSs
r1 = patches.Rectangle((355.45,6.8), 313,0.006, angle= -0.0861284)
r2 = patches.Rectangle((746.45,6.212), 313,0.006, angle= -0.0861284)
r3 = patches.Rectangle((1137.45,5.623), 313,0.006, angle= -0.0861284)
r4 = patches.Rectangle((1528.45,5.035), 313,0.006, angle= -0.0861284)
r5 = patches.Rectangle((1919.45,4.446), 313,0.006, angle= -0.0861284)
ax.add_patch(r1)
ax.add_patch(r2)
ax.add_patch(r3)
ax.add_patch(r4)
ax.add_patch(r5)

#TPST
r6 = patches.Rectangle((4685.26,3.94), 214 , 0.46, angle= 0.02838015)
ax.add_patch(r6)

#MST
r7 = patches.Rectangle((4973.016812,4.079), 214,0.41, angle= 0.028409155)
r8 = patches.Rectangle((5296.416982,4.240), 214,0.41, angle= 0.028409155)
r9 = patches.Rectangle((5619.816971,4.401), 214,0.41, angle= 0.028409155)
ax.add_patch(r7)
ax.add_patch(r8)
ax.add_patch(r9)

#MSE
r10 = patches.Rectangle((6717.6328,4.825), 241.32,1.775, angle= -0.025632321)
r11 = patches.Rectangle((7041.0248,4.777), 241.32,1.775, angle= 0.047495174)
r12 = patches.Rectangle((7364.41710,5.142), 241.32,1.775, angle= 0.12062252)
r13 = patches.Rectangle((7687.809591,5.918), 241.32,1.775, angle= 0.193498169)
r14 = patches.Rectangle((8011.202246,7.107), 241.32,1.775, angle= 0.266624488)
ax.add_patch(r10)
ax.add_patch(r11)
ax.add_patch(r12)
ax.add_patch(r13)
ax.add_patch(r14)

#QFA219
r15 = patches.Rectangle((9398.76,18.63940), 401,0.2, angle= 0.399731511)
r16 = patches.Rectangle((9398.76,27.43940), 401,0.2, angle= 0.399731511)
ax.add_patch(r15)
ax.add_patch(r16)

#ax.set_ylim([np.amin(matrix[0:,3]), 31])
plt.title('Particle trajectory',fontweight='bold', fontsize = 15)
plt.ylabel('x [cm]' ,fontsize = 14)
#plt.xlabel('S [cm]',fontsize = 14)
plt.grid()
plt.legend(loc=2)

from scipy import interpolate
x = matrix[0:,0]*100
y = matrix[0:,1]*100
f = interpolate.interp1d(x, y)

MADXnew = f(fluka[:-1,2])


ax = fig.add_subplot(212)
#plt.plot(fluka[0:,2] , fluka[0:,0], label='FLUKA', color='r',linestyle = ':',linewidth=3.0) #, marker='x'
#plt.plot(matrix[0:,0]*100 , matrix[0:,1]*100, label='MADX', color='k') #
plt.plot(fluka[:-1,2] , MADXnew -fluka[:-1,0], label='MADXnew', color='k') #
plt.title('Position difference',fontweight='bold', fontsize = 15)
plt.axvline(x=0,linestyle = '--' )
plt.axvline(x=3199.77,linestyle = '--' )
plt.axvline(x=6399.54,linestyle = '--' )
plt.axvline(x=9599.31,linestyle = '--' )
plt.ylabel('MADX - FLUKA [cm]', fontsize = 14)
#plt.xlabel('S [cm]', fontsize = 14)
#ax.set_xlim([5212, 5296])
plt.grid()
plt.legend(loc=2)


plt.show()

#ax = plt.gca()
#r = patches.Rectangle((.5, .5), .25, .1, fill=False)
#ax.add_artist(r)
