# -*- coding: utf-8 -*-
"""
Created on Thu Jul 20 10:44:35 2017

@author: cbjorkma
"""


P0 = 400 #GeV/c

#PT = dP/(P0 *dP)

PT = 0.0015 #alternativly -0.0015

dP = P0 * PT

P = dP/PT - dP # = P0 - dP
print P




import math as math

L = 2.237/2

B = 0.337034863
gamma = 426.3167458
m = 1.6726219*math.pow(10,-27)

q = 1.60217662*math.pow(10,-19)

c = 299792000

v = c * math.sqrt(1 - 1/(math.pow(gamma,2)))

t = L/v

p0 = 0.89555918723 * math.pow(10,-3)

S = q*v*B/(2*gamma*m) * t*t 
S1 = p0/m * t

#print S*100

#print S1

fluka = 0.50649934061*math.pow(10,1)- 0.49499737285 * math.pow(10,1)

#print fluka

E = 11000000

B = E/v

print B