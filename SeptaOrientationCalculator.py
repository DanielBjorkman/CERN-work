# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 11:22:25 2017

@author: cbjorkma
"""

#SeptaOrientationCalculator

#Coded by Daniel Björkman 2017
# daniel.bjorkman@cern.ch



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
#
#
#plt.close()


#TPST septum
#fig = plt.figure()

#ax = plt.subplot(111)


MADXoffset = 1665.4231

#Defines the baseline
point1 = [100*(1712.0858 - MADXoffset) , 0.1*37.20618]
point2 = [100*(1714.6058 - MADXoffset), 0.1*38.55173]


LindaAngle = math.atan((point2[1] - point1[1])/ (point2[0] - point1[0]))

#plt.plot([point1[0] , point2[0]] , [point1[1] , point2[1]], label = 'Base line')

#Unmoved TPST center position
TPST = [4792.27, 2.77]

        
        
#TPST septa dimensions        
length = 120 #214
width = 0.46

#Shift required to get from center to corner
Xshift = math.sin(LindaAngle) *length/2
Zshift = math.cos(LindaAngle)*length/2

z = np.zeros(2)
x = np.zeros(2)
z[0] = point1[0]
z[1] = point2[0]
x[0] = point1[1]
x[1] = point2[1]

f = interpolate.interp1d(z, x)

Zcorner = TPST[0] - Zshift
Xcorner = TPST[1] - Xshift

linebuilderX = f(TPST[0]) 

print 'Linebuilder input TPST x = ' + str(linebuilderX - TPST[1]) + ', Angle = ' + str(LindaAngle)
print 'TPST should be observed at Z = ' + str(TPST[0]) + ' and x = ' + str(f(TPST[0])) + ' [cm]'

#r1 = patches.Rectangle((Zcorner ,Xcorner), length,width, angle= math.degrees(LindaAngle), label = 'septa')
#ax.add_patch(r1)
#
#plt.title('TPST septa')
#plt.xlabel('Z [cm]')
#plt.ylabel('X [cm]')
#plt.show()

print ' '   
print ' '
print 'MST-------------------------------------------------------'


#MSTs------------------------------------------------------------------------

Zs = [5093.02,5416.42,5739.82 ]

point1 = []
point2 = []

#Defines the baselines
point1.append( [100*(1715.1633 - MADXoffset) , 0.1*39.41577])
point2.append( [100*(1717.5433 - MADXoffset), 0.1*40.96990])

point1.append(  [100*(1718.3973 - MADXoffset) , 0.1*41.52756])
point2.append( [100*(1720.7773 - MADXoffset), 0.1*43.08169])

point1.append( [100*(1721.6313 - MADXoffset) , 0.1*43.63934])
point2.append( [100*(1724.0113 - MADXoffset), 0.1*45.19347])


for i in range(len(Zs)):

    print ' '
    
    z = np.zeros(2)
    x = np.zeros(2)
    z[0] = point1[i][0]
    z[1] = point2[i][0]
    x[0] = point1[i][1]
    x[1] = point2[i][1]
    
    LindaAngle = -math.atan((x[1] - x[0])/ (z[1] - z[0]))
    
    MST = [Zs[i], 6.14]

    
    f = interpolate.interp1d(z, x)
    
    linebuilderX = f(MST[0]) 
    
    print 'Linebuilder input MST'+str(i +1) +' x = ' + str(MST[1] -linebuilderX) + ', Angle = ' + str(LindaAngle)
    print 'MST'+str(i +1) +' should be observed at Z = ' + str(z[0]) + ' and x = ' + str(x[0]) + ' [cm] and '
    print ' Z = ' + str(z[1]) + ' and x = ' + str(x[1]) + ' [cm] '
    #print 'MST'+str(i +1) +' center should be observed at Z = ' + str(MST[0]) + ' and x = ' + str(f(MST[0])) + ' [cm]'

print ' '   
print ' '
print 'MSE-------------------------------------------------------'


#MSEs------------------------------------------------------------------------

Zs = [6838.29,7161.69,7485.09, 7808.49, 8131.89 ]

point1 = []
point2 = []

#Defines the baselines
point1.append( [100*(1732.616                 - MADXoffset) , 0.1*48.26604])
point2.append( [100*(1734.996                - MADXoffset), 0.1*47.46876])

point1.append(  [100*(1735.85                  - MADXoffset) , 0.1*47.89989])
point2.append( [100*(1738.23                 - MADXoffset), 0.1*50.14024])

point1.append( [100*(1739.084                - MADXoffset) , 0.1*51.30396])
point2.append( [100*(1741.464               - MADXoffset), 0.1*56.57150])

point1.append(  [100*(1742.318                - MADXoffset) , 0.1*59.18803])
point2.append( [100*(1744.698                - MADXoffset), 0.1*67.48276])

point1.append( [100*(1745.552                - MADXoffset) , 0.1*70.83187])
point2.append( [100*(1747.932                - MADXoffset), 0.1*82.16424])

for i in range(len(Zs)):

    print ' '
    
    z = np.zeros(2)
    x = np.zeros(2)
    z[0] = point1[i][0]
    z[1] = point2[i][0]
    x[0] = point1[i][1]
    x[1] = point2[i][1]
    
    LindaAngle = -math.atan((x[1] - x[0])/ (z[1] - z[0]))
    
    MSE = [Zs[i], 6.245]

    
    f = interpolate.interp1d(z, x)
    
    linebuilderX = f(MSE[0]) 
    
    print 'Linebuilder input MST'+str(i +1) +' x = ' + str(MSE[1] - linebuilderX) + ', Angle = ' + str(LindaAngle)
    print 'MST'+str(i +1) +' should be observed at Z = ' + str(z[0]) + ' and x = ' + str(x[0]) + ' [cm] and '
    print ' Z = ' + str(z[1]) + ' and x = ' + str(x[1]) + ' [cm] '
  #  print 'MSE'+str(i +1) +' center should be observed at Z = ' + str(MSE[0]) + ' and x = ' + str(f(MSE[0])) + ' [cm]'
    
