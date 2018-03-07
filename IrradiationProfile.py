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


print "-----------------------------------------------------------------------------------"

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

for i in range(6):
    print ' '
    
    
print 'Scraper Geometry'

yearlyloss = 200 * 120 * 7.4*10**13*0.2

oneyear = 365*24*60*60

print str(oneyear) +'     ' + str(yearlyloss/oneyear)
print 'One year of operations at 20% lossrate'
for i in range(2):
    print ' '

print str(oneyear*20) +'     ' + str(yearlyloss/oneyear)
print '20 years of operations at 20% lossrate'



for i in range(6):
    print ' '
    
    
print 'LSS2'

protons = np.array([8.8,6.2 ,11.2,2.9 ,5.5 ,8.7 , 5.7 , 4.9 , 2.2 , 10.3,8.99])*10**18
import datetime #, timedelta
#start 09 05 2004
end2016 = datetime.datetime(2016,11,14,06,00,00)
end2017 = datetime.datetime(2017,10,26,06,00,00)

start2004 = datetime.datetime(2004,05,9,17,00,00)
start2017 = datetime.datetime(2017,05,02,11,41,00)


timedifference = end2016 - start2004
amountOfSeconds = timedifference.total_seconds()

print 'Long run '
print str(amountOfSeconds) +' ' + str(sum(protons)/amountOfSeconds)

print ' '
print ' '


timedifference = start2017 - end2016
amountOfSeconds = timedifference.total_seconds()
print '2017 cool down: '
print str(amountOfSeconds) + ' 0'



#plt.legend()
#
#
#plt.show()



