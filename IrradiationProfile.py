# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 16:43:06 2018

@author: cbjorkma
"""

#Irradiation Profile
#import matplotlib.pyplot as plt
import numpy as np
import math as math

#plt.close()
#plt.close()
#plt.close()
#

EI = 1.271 * math.pow(10,19)

#FEE = 0.1772837
FEE = 1

Particles = (1/FEE)*EI

days = 175

seconds = days *24*60*60

average = Particles / seconds

#lastdayParticles = average*100

#last day shots of 2017
#shots = [1.54, 1.54, 1.5, 1.53, 1.48, 1.49, 1.54, 1.53, 1.52, 1.53,1.53, 1.52, 1.53, 1.52, 1.52 ,1.53, 1.53, 1.52, 1.52, 1.53, 1.50, 1.51, 1.52, 1.52, 1.52, 1.52]
#shots = [i*math.pow(10,15) for i in shots]




lastdayTime = 24*60*60
lastdayParticles = 1.27249E+17 #<--- From summing 

lastdayParticleRate =  lastdayParticles/lastdayTime







newaverage = (Particles - lastdayParticleRate*lastdayTime)/(seconds -lastdayTime )

#fig = plt.figure()
#
#
##plt.plot(range(seconds),np.ones(seconds)*average, label = 'Average')
##
##plt.plot(range(seconds-1), np.ones(seconds-1)*newaverage, label = 'NewAverage')
##
##plt.plot(seconds,lastday, label = 'Last day')

nowParticles = ((seconds -lastdayTime)*newaverage + lastdayTime*lastdayParticleRate) 

print nowParticles
print nowParticles/Particles

print average * seconds 

print 'Average / lastday average = ' + str(newaverage/lastdayParticleRate)



print 'Irradiation profile:'
print str(seconds -lastdayTime) + ' ' + str(newaverage) + ' ' + str(lastdayTime) + ' ' + str(lastdayParticleRate) 



#plt.legend()
#
#
#plt.show()



