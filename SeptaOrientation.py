# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 11:22:25 2017

@author: cbjorkma
"""

#SeptaOrientation



import matplotlib.pyplot as plt
import matplotlib.patches as patches
import math
import numpy as np
from scipy import interpolate
#import matplotlib as mpl

plt.close()
#plt.subplot(2,1,1)
fig = plt.figure()
for i in range(6):
    for k in range(2):
        ax = fig.add_subplot(3,4,2*i +1 +k)
        
        point1 = [100*3.5545 , 100*0.06795]
        point2 = [100*22.3245 , 100*0.04140]
        
        LindaAngle = math.atan((point2[1] - point1[1])/ (point2[0] - point1[0])) #radians
    
        #print 'Linda angle ' + str(LindaAngle)
        
        plt.plot([point1[0] , point2[0]] , [point1[1] , point2[1]], label = 'Base line')
        
        #Convert to zero offset
        point1[1] = point1[1] + 0.01  
        point2[1] = point2[1] + 0.01  
    
        plt.plot([point1[0] , point2[0]] , [point1[1] , point2[1]], label = 'Zero offset line', linewidth = 3)
        
        x = np.zeros(2)
        if i == 0:
            x = np.zeros(2)
            y = np.zeros(2)
            x[0] = point1[0]
            x[1] = point2[0]
            y[0] = point1[1]
            y[1] = point2[1]
            f = interpolate.interp1d(x, y)
            positions = [511.95, 902.95, 1293.95, 1684.95 ,2075.95]
            newX = np.zeros(5)
            for j in range(5):
                newX[j] = f(positions[j])
                if j <2:
                    print 'Linebuilder ZS' + str(j+1) +  ' input = ' + str(newX[j] - 3.652)
                else:
                    print 'Linebuilder ZS' + str(j+1) +  ' input = ' + str(newX[j] - 3.65)
        #ZS1
        #point1 = [0 , 6.806]
        #point2 = [310 , 6.340]
        
        #print math.atan((point2[1] - point1[1])/ (point2[0] - point1[0]))
        
        
        #overall
        point1 = [0 , 6.806]
        point2 = [1874 , 3.99]
        
        #print 'Overall angle ' +str( math.atan((point2[1] - point1[1])/ (point2[0] - point1[0])))
        
        
        
        point1[0] = point1[0] + 100*3.5545
        point2[0] = point2[0] + 100*3.5545
        
        #print 'Overall angle, adjusted ' +str( math.atan((point2[1] - point1[1])/ (point2[0] - point1[0])))
        
        #plt.plot([point1[0] , point2[0]] , [point1[1] , point2[1]], label = 'Base line, Excel sheet')
        
        Xshift = math.sin(LindaAngle) *312/2
        Yshift = math.cos(LindaAngle)*312/2
    
        #ZSs
        r1 = patches.Rectangle((positions[0] - Yshift,newX[0] -Xshift -0.003), 312,0.006, angle= math.degrees(LindaAngle), label = 'septa')
        r2 = patches.Rectangle((positions[1] - Yshift,newX[1] -Xshift -0.003), 312,0.006, angle= math.degrees(LindaAngle))
        r3 = patches.Rectangle((positions[2] - Yshift,newX[2]-Xshift -0.005), 312,0.010, angle= math.degrees(LindaAngle))
        r4 = patches.Rectangle((positions[3] - Yshift,newX[3]-Xshift -0.005), 312,0.010, angle= math.degrees(LindaAngle))
        r5 = patches.Rectangle((positions[4] - Yshift,newX[4]-Xshift -0.005), 312,0.010, angle= math.degrees(LindaAngle))
        ax.add_patch(r1)
        ax.add_patch(r2)
        ax.add_patch(r3)
        ax.add_patch(r4)
        ax.add_patch(r5)
        
        if i == 0:
            plt.xlim(327, 673)
            plt.ylim(6.27 ,6.85 )
        elif i ==1:
            plt.xlim(737, 1070)
            plt.ylim(5.7 ,6.3 )        
        elif i ==2:
            plt.xlim(1129, 1465)
            plt.ylim(5.1 ,5.75 )        
        elif i ==3:
            plt.xlim(1522, 1857)
            plt.ylim(4.5 ,5.19 )    
        elif i ==4:
            plt.xlim(1910, 2244)
            plt.ylim(3.9 ,4.61 )
            
    
        if i == 5:
            plt.setp( ax.get_xticklabels(), visible=False)
            plt.setp( ax.get_yticklabels(), visible=False)
            if k ==1:
                plt.legend(prop={'size':55}, loc = 7)
        else:
            plt.xlabel('Z [cm]')
            plt.ylabel('X [cm]')
            if k ==1:
                plt.title('ZS ' + str(i+1),x=-0.1,y=1, fontsize = 18)
            plt.grid()
            
plt.suptitle('ZS septa position validation', fontsize = 25 ,fontweight='bold')
plt.show()




#import matplotlib.gridspec as gridspec
#
#fig = plt.figure()
#outer = gridspec.GridSpec(3, 2, wspace=0.2, hspace=0.2)
#
#for i in range(6):
#    inner = gridspec.GridSpecFromSubplotSpec(1, 2,
#                    subplot_spec=outer[i], wspace=0.1, hspace=0.1)
#
#    for y in range(2):
#        ax = plt.Subplot(fig, inner[y])
#        point1 = [100*3.5545 , 100*0.06795]
#        point2 = [100*22.3245 , 100*0.04140]
#        
#        LindaAngle = math.atan((point2[1] - point1[1])/ (point2[0] - point1[0])) #radians
#    
#        #print 'Linda angle ' + str(LindaAngle)
#        
#        plt.plot([point1[0] , point2[0]] , [point1[1] , point2[1]], label = 'Base line, Linda')
#        
#        #Convert to zero offset
#        point1[1] = point1[1] + 0.01  
#        point2[1] = point2[1] + 0.01  
#    
#        plt.plot([point1[0] , point2[0]] , [point1[1] , point2[1]], label = 'Zero offset line', linewidth = 3)
#        
#        print 1
#        
#        x = np.zeros(2)
#        if i == 0 and y == 0:
#            x = np.zeros(2)
#            y = np.zeros(2)
#            x[0] = point1[0]
#            x[1] = point2[0]
#            y[0] = point1[1]
#            y[1] = point2[1]
#            f = interpolate.interp1d(x, y)
#            positions = [511.95, 902.95, 1293.95, 1684.95 ,2075.95]
#            newX = np.zeros(5)
#            for j in range(5):
#                newX[j] = f(positions[j])
#                if j <2:
#                    print 'Linebuilder ZS' + str(j+1) +  ' input = ' + str(newX[j] - 3.652)
#                else:
#                    print 'Linebuilder ZS' + str(j+1) +  ' input = ' + str(newX[j] - 3.65)
#
#       # ax.set_xticks([])
#        #ax.set_yticks([])
#        fig.add_subplot(ax)
#
#fig.show()
##
#import matplotlib.gridspec as gridspec
#
#
#fig = plt.figure(figsize=(10, 8))
#outer = gridspec.GridSpec(2, 2, wspace=0.2, hspace=0.2)
#
#for i in range(4):
#    inner = gridspec.GridSpecFromSubplotSpec(2, 1,
#                    subplot_spec=outer[i], wspace=0.1, hspace=0.1)
#
#    for j in range(2):
#        ax = plt.Subplot(fig, inner[j])
#        plt.plot([1,2] , [3,4])
#        fig.add_subplot(ax)
#
#fig.show()
#
#
#


