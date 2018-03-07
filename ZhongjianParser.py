
#Zhongjian's Parser

import os
import numpy as np
import matplotlib.pyplot as plt

path = 'C:\Users\cbjorkma'

#Change path
os.chdir(path)


filename = 'plot05.dat'

#Preallocate matrix
data = np.zeros([81,4,3])

#Data 1
filename = 'plot05.dat'
data[0:,0:,0] = np.loadtxt(filename , skiprows = 1)

#Data 2
filename = 'plot05.dat'
data[0:,0:,1] = np.loadtxt(filename , skiprows = 1)

#Data 3
filename = 'plot05.dat'
data[0:,0:,2] = np.loadtxt(filename , skiprows = 1)





#Hack 
data[0:,2,1] = 0.01*data[0:,2,1]
data[0:,2,2] = 0.0001*data[0:,2,2]

labels = ['1 hour' , '1 day', '1 week']



#New figure
fig = plt.figure()




ax = fig.add_subplot(211)

plt.plot(data[0:,0,0], data[0:,2,0], label = labels[0])
plt.plot(data[0:,0,1], data[0:,2,1], label = labels[1])
plt.plot(data[0:,0,2], data[0:,2,2], label = labels[2])
plt.legend()
plt.ylabel('uSv/h')
plt.xlabel('x [cm]')
plt.title('My title')
ax.set_yscale("log", nonposy='clip')




ax = fig.add_subplot(212)


xes = range(data.shape[2])
plt.plot(xes, data[50,2,0:])
plt.title('x = 10 cm')
plt.xlabel('time')
plt.ylabel('uSv/h')
plt.xticks(xes, labels)


plt.show()

