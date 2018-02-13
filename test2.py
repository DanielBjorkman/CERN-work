



import os
import numpy as np
import pandas as pd
import datetime #, timedelta
import matplotlib.pyplot as plt
import math
#from Flukato3dMatrix import Flukato3dMatrix 
#plt.close()
#plt.close()
#plt.close()
#plt.close()
#plt.close()
#plt.close()

plt.clf()

# Fluka data------------------------------------------------------------------
path = '//rpclustersrv1/cbjorkma/LSS2/ActivationDetectors/USRBINs' 
os.chdir(path)

files = os.listdir(path)
files = sorted(files)
files = filter(lambda x: x[9:-8].isdigit() , files)  

FlukaData = np.zeros([len(files),8])
#row = 10
#indecies = [7,9, 11 ,13 , 15 ,17,19,21]
#for i in range(len(files)):
#    thefile = open(files[i],'r')
#    filecontent = thefile.readlines()
#    line = filecontent[row].split(' ')
#    for j in range(len(indecies)):
#        FlukaData[i,j] = line[indecies[j]]
#
##Converts data to uSv/h
#FlukaData = 0.0036*FlukaData
#
##Normalization
#normFactor = 1 / 0.1772837
#FlukaData = normFactor * FlukaData
#
##Volume compensation
#Volume = math.pi*8*8*21.5
#FlukaData = FlukaData /Volume
#

#----------------------------------------------------------------------------





#Read PMI data---------------------------------------------------------------------
path = '//rpclustersrv1/cbjorkma/LSS2/ActivationDetectors' 

os.chdir(path)

#protonEnd = '2017-11-23 06:00:00.940000'
protonEnd = datetime.datetime(2017,10,23,06,00,00)
ionEnd = datetime.datetime(2017,12,18,06,00,00)

files = os.listdir(path)
files = sorted(files)
files = filter(lambda x: x[4:7].isdigit() , files)  
filenames = files




path = '//rpclustersrv1/cbjorkma/LSS2/ActivationDetectors' 

os.chdir(path)

##protonEnd = '2017-11-23 06:00:00.940000'
#protonEnd = datetime.datetime(2017,10,23,06,00,00)
#ionEnd = datetime.datetime(2017,12,18,06,00,00)
#
#



#Read PMI data---------------------------------------------------------------------
#path = '//rpclustersrv1/cbjorkma/LSS2/ActivationDetectors' 

path = '//cern.ch/dfs/Users/c/cbjorkma/Documents/LSS 2/ActivationDetectors'

os.chdir(path)

#protonEnd = '2017-11-23 06:00:00.940000'
protonEnd = datetime.datetime(2017,10,23,06,00,00)
ionEnd = datetime.datetime(2017,12,18,06,00,00)
end2016 = datetime.datetime(2015,11,16,06,00,00)
end2017 = datetime.datetime(2016,11,14,06,00,00)

#
#files = os.listdir(path)
#files = sorted(files)
#files = filter(lambda x: x[4:7].isdigit() , files)  
#filenames = files
#thefile = pd.read_excel(files[0])
#
#data = np.zeros([len(thefile),2, len(files)])
#for j in range(len(files)):
#    thefile = pd.read_excel(files[j])
#    time = thefile.Timestamp
#    for i in range(len(thefile)):
#        instant = datetime.datetime( time[i].year, time[i].month, time[i].day, time[i].hour, time[i].minute, time[i].second)
#    #    print instant
##        timedifference = instant - protonEnd
#        timedifference = instant - end2016
#        amountOfSeconds = timedifference.total_seconds()/(60*60*24)
#      #  print 'file ' + str(j) + '. Seconds ' + str(amountOfSeconds) + '. value ' + str(thefile.Value[i] )
#        data[i,0,j] = amountOfSeconds
#        data[i,1,j] = thefile.Value[i]   
#assert data[1200,1,2] != data[1200,1,3]
#np.save('data', data)

data = np.load('data.npy')
#-------------------------------------------------------------------------------




data3 = np.load('data.npy')








files = filenames


from scipy import interp
from scipy.interpolate import interp1d
from scipy.optimize import curve_fit

timedifference = protonEnd - end2016


xes2016 = [-691.709,-689, -685,-671.35,-658,-654,-651,-641.056,-629,-618,-609,-605,-590,-579.75,-565.928, -560.055 , -554.317, -553.13  ]
for i in range(len(xes2016)):
    xes2016[i] = xes2016[i] +timedifference.total_seconds()/(60*60*24)


xes2017 = [-314,-310,-308,-303,-300,-297,-288,-295,-283,-280,-237,-224, -214,-207,-201, -198,-192,-190, -185, -180.475 ,  -174.584]
for i in range(len(xes2017)):
    xes2017[i] = xes2017[i] +timedifference.total_seconds()/(60*60*24)


#xes = [-314,-310,-308,-303,-300,-297,-288,-295,-283]


#
#fig = plt.figure()

ax = plt.subplot(111)
i = 0

x = data[0:,0,i]
y = data[0:,1,i]

f = interp1d(x, y, fill_value='extrapolate')

##Log curve
#def func(x, a,b, c):
#     return a * np.log(-b* x) + c
#popt, pcov = curve_fit(lambda x,a,b,c: a*np.log(-b*x) + c,  xes,  f(xes))







#initialguess = [1, 3.31,0.67,979]


#k1 = 3.14
#
#k2 = 0.69

##MAtthew expression 1 curve
#def func(x,a, k1,k2,c):
#   return a*np.exp(-k1*np.power(np.log(x),k2)) + c
#
#def fitting(xes,y,guess):
#    for i in range(100):
#        try:
#            popt, pcov = curve_fit(lambda x,a,k1,k2,c: a*np.exp(-k1*np.power(np.log(x),k2)) + c,  xes,  f(xes),  p0 = guess)
#        except RuntimeError:
#            print 'Fail'
#    #        print a, k1, k2,c 
#    
#    return popt , pcov
#
#Title = "Curve of format a*np.exp(np.power(-b*np.log(x),k)) + c"
#


###Exponential
#def func(x, a,b, c):
#    return a * np.exp(-b* x) + c
#    
#def fitting(xes,y,guess):
#    for i in range(10):
#        try:
#            popt , pcov = curve_fit(lambda x,a,b,c: a*np.exp(-b*x) + c,  xes,  f(xes), p0 = guess)
#        except:
#            print 'Fail'
#    return popt , pcov 
#
#

#
#def extrapolate(xes,initialguess):
#    for i in range(10):
#        print 'Attempt ' +  str(i +1 )
#        guess = initialguess
#        for j in range(len(guess)):
#            guess[j] = initialguess[j]*(2*(np.random.rand() -np.random.rand()) + 1)
#        
#        try:
#
#            popt, pcov = fitting(xes, f(xes),guess)
#            print 'Success!'
#            break
#        except RuntimeError: 
#            print 'Failed'
#
#    return popt


#xes = np.ones([6])
#xes = xes*[3600,86400,604800, 2.592*math.pow(10,6), 5.184*math.pow(10,6), 6.912*math.pow(10,6)]/(60*60*24)
    
sampleX = [0 ,0.041668,0.0833,0.18,0.208315,1.35,3.5, 8.86, 14.2, 42.37, 49.38,56.13,70,80,84.2]
for i in range(len(sampleX)):
    sampleX[i] = sampleX[i] +timedifference.total_seconds()/(60*60*24)

ax = plt.subplot(111)

plt.plot(x, y, label = 'PMI data')
#plt.plot(sampleX , f(sampleX) , color = 'g' , label =  'Interpolation', marker = 'o')
plt.legend()
xmin =-10
xmax = 850

ymin = 0
ymax = 10000

plt.ylim(ymin , ymax)
plt.xlim(xmin, xmax)

#----------------------------------------------------------------------------
##Exponential
#initialguess = [1, 0.02,979]
#popt = extrapolate(xes2017,initialguess)
#plt.plot(x, func(x, *popt), 'r--', label = 'Curve fit 2017')
#
#
#initialguess = [1, 0.0002,500]
#popt = extrapolate(xes2016,initialguess)
#plt.plot(x, func(x, *popt), 'c--', label = 'Curve fit 2016')
##


##Exponential, logged exponent
#initialguess = [1, 3.14,0.69,979]
#popt = extrapolate(xes2017,initialguess)
#plt.plot(x, func(x, *popt), 'r--', label = 'Curve fit 2017')


#initialguess = [1, 0.0002,500]
#popt = extrapolate(xes2016,initialguess)
#plt.plot(x, func(x, *popt), 'c--', label = 'Curve fit 2016')
#----------------------------------------------------------------------------

#Exponential, logged exponent
#initialguess = [1, 3.14,0.69,300,318]
#popt = extrapolate(xes2017,initialguess)

#x = 0
#i = 318
#k2 = 0.69

#def func(x):
#   return 1*np.exp(-1*np.power(np.log(0.001*(10 - x)),0.1)) + 800

#def func(x):
#    a = 1500
#    k1 = 1
#    k2 = 0.1
#    dt = 1000**-1 #difference from start
#    i = 1500 #start
#    try:
#        return a*np.exp(-k1*np.power(np.log(dt*(i - x)),k2)) + 800
#    except RuntimeWarning:
#        print np.power(np.log(dt*(i - x)))
#        print dt
#        print x
#        print i
ax2 = ax.twinx()





#
## Very good first approximation of the slope
##--------------------------------------------------------
#start = 370 #start
#def func(x):
#    a = 1000
#    k1 = 0.00019*3
#    k2 = 5.25
#    dt = 1 #difference from start
#    c = 2000/2
#    try:
#        val =  a*np.exp(-k1*np.power(np.log(dt*(x - start)),k2)) +c
#    except RuntimeWarning:
#        print np.power(np.log(dt*(i - x)))
#        print dt
#        print x
#        print i
#    return val
##--------------------------------------------------------



a = 1800
k1 = 0.00019*3.0
k2 = 5.25*0.82
timedifference = end2017 - end2016
start = timedifference.total_seconds()/(60*60*24)
initialguess = [a,k1 ,k2] 


def func(x,a,k1,k2):
    return a*np.exp(-k1*np.power(np.log(x - start),k2))

#def fitting(xes,y,guess):
#    for i in range(10):
#        try:
#            popt , pcov = curve_fit(lambda x,a,k1,k2,c: a*np.exp(-k1*np.power(np.log(x - start),k2)) +c,  xes,  f(xes), p0 = guess)
#        except:
#            print 'Fail'
#    return popt , pcov 
#

def extrapolate(xes,initialguess):
    for i in range(100):
        print 'Attempt ' +  str(i +1 )
        guess = initialguess
#        for j in range(len(guess)):
#            guess[j] = initialguess[j]*(2*(np.random.rand() -np.random.rand()) + 1)
        guess[0] = guess[0] +100*(2*np.random.rand() -1)
        guess[1] = guess[1] +0.0005*(2*np.random.rand() -1)
        guess[2] = guess[2] +0.0005*(2*np.random.rand() -1)      
        try:
#            popt, pcov = fitting(xes, f(xes),guess)
            popt , pcov = curve_fit(lambda x,a,k1,k2: a*np.exp(-k1*np.power(np.log(x - start),k2)),  xes,  f(xes), p0 = guess)
            print 'Success!'
            print [x/y for x, y in zip(guess, initialguess)]
            break
        except RuntimeError: 
            print 'Failed'

    return popt




end = 12786
x = np.arange(start,800)
#d = func(x)

#plt.ylim(ymin = 1, ymax = 4000)

#plt.plot(x[1:], func(x[1:]), 'r--', label = 'Curve fit 2017')


for i in range(len(xes2017)):
    if i == 0:
        plt.axvline(x= xes2017[i] ,linestyle = '--', color = 'k', linewidth = 0.3, label = 'Sampling points')
    else:
        plt.axvline(x= xes2017[i] ,linestyle = '--', color = 'k', linewidth = 0.3)
#    
for i in range(len(xes2016)):
    plt.axvline(x= xes2016[i] ,linestyle = '--', color = 'k', linewidth = 0.3)

i = 0

x = data[0:,0,i]
y = data[0:,1,i]

#----------------------------------------------------------------------
a = 1800
k1 = 0.00019*3.0
k2 = 5.25*0.82
timedifference = end2017 - end2016
start = timedifference.total_seconds()/(60*60*24)
initialguess = [a,k1 ,k2] 
popt = extrapolate(xes2017,initialguess)
#popt , pcov = curve_fit(lambda x,a,k1,k2,c: a*np.exp(-k1*np.power(np.log(x - start),k2)) +c,  xes2017,  f(xes2017), p0 = initialguess)
plt.plot(x[1:], func(x[1:], *popt), 'r--', label = 'Curve fit 2017')
#----------------------------------------------------------------------

#----------------------------------------------------------------------
a = 3900
k1 = 0.00019*2.8
k2 = 5.25*0.90
start = 0
initialguess = [a,k1 ,k2] 
popt = extrapolate(xes2016,initialguess)
plt.plot(x[1:], func(x[1:], *popt), 'c--', label = 'Curve fit 2016')

#----------------------------------------------------------------------


#plt.plot(xes, np.polyfit(xes,np.log(f(xes)),1) , 'r--', label = 'Fitted curve')
plt.title( "Curve fit of format a*exp[-k1*(ln(x - x0)^k2)]")
plt.ylim(ymin , ymax)
plt.xlim(xmin, xmax)
plt.legend()
plt.xlabel('time[days]')
plt.ylabel('uSv/h')
#ax.set_yscale("log", nonposy='clip')
plt.show()








##exp curve 1
#def func(x, a,b, c):
#     return a * np.exp(-b* x) + c
#popt, pcov = curve_fit(lambda x,a,b,c: a*np.exp(-b*x) + c,  xes,  f(xes), p0 = guess)



##Taylor expansion of exponential
#def func(x, a,b, c):
#     return a +c - a*b*x + 0.5*a*b*b*x*x# - (1/6)*x*x*x*(a*b*b*b)# + (1/24)*a*b*b*b*b*x*x*x*x
##popt, pcov = curve_fit(func, xes, f(xes))
#popt, pcov = curve_fit(lambda x,a,b,c:a +c - a*b*x + 0.5*a*b*b*x*x - (1/6)*x*x*x*(a*b*b*b),  xes,  f(xes), bounds = (xes[0],200))
##Title = 'Taylor expansion of exponential
#

#guess = [1, 0.02,979,0.5,3]
#
##exp curve 2
#def func(x, a,b, c,d,e):
#     return a * np.exp(-b* x) + c + d * np.exp(-e* x)
##popt, pcov = curve_fit(func, xes, f(xes))
#popt, pcov = curve_fit(lambda x,a,b,c,d,e: a * np.exp(-b* x) + c + d * np.exp(-e* x),  xes,  f(xes), p0 = guess)
#

#



#
##Polynomial curve
#def func(x, a,b, c):
#     return a *x*x + b*x +c
##popt, pcov = curve_fit(func, xes, f(xes))c
#popt, pcov = curve_fit(lambda x,a,b,c: a *x*x + b*x +c ,  xes,  f(xes))
#Title = 'Second degree polynomial'


#
##MAtthew expression 1 curve
#def func(x, a,b,c):
#     return np.exp(np.power(-a*np.log(x),b)) + c
##popt, pcov = curve_fit(func, xes, f(xes))
#popt, pcov = curve_fit(lambda x,a,b,c: np.exp(np.power(-a*np.log(x),b)) + c,  xes,  f(xes))


##MAtthew expression 2 curve
#def func(x,k, a,b,c):
#     return k*np.exp(-a*np.log(x) -b*np.power(np.log(x),2)) + c
##popt, pcov = curve_fit(func, xes, f(xes))
#popt, pcov = curve_fit(lambda x,a,b,c,k: k*np.exp(-a*np.log(x) -b*np.power(np.log(x),2)) + c,  xes,  f(xes))
#

#linear
#def func(x, k,m):
#     return k*x + m
##popt, pcov = curve_fit(func, xes, f(xes))
#popt, pcov = curve_fit(lambda x,k,m: k*x +m,  xes,  f(xes))
#Title = 'Linear'






