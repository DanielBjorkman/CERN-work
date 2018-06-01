# -*- coding: utf-8 -*-
"""
Created on Tue May 22 13:25:52 2018

@author: cbjorkma
"""

#ZSlosses


import os
import numpy as np

import matplotlib.pyplot as plt
print 'Reading Fluka'
directory = "//rpclustersrv1/cbjorkma/LSS2/LSS2_diffuser2018-04-12_200umRibbonZS_ZSint_full_2011_abd"
os.chdir(directory)

#filename = 'FlukaDiffuserZSinteractionFull'


import pickle
with open('LSS2_exp001_fort.99.pkl', 'rb') as f:
    data1 = pickle.load(f)

with open('LSS2_exp001_usrmed.dat.pkl', 'rb') as f:
    data2 = pickle.load(f)


ZSnew = []

ZSnew.append(  data2[data2['Z'].between(3,7)])

ZSnew.append(  data2[data2['Z'].between(7,11)])

ZSnew.append(  data2[data2['Z'].between(11,15)])

ZSnew.append(  data2[data2['Z'].between(15,19)])

ZSnew.append(  data2[data2['Z'].between(19,23)])

#set(ZSnew[4].REG)



normNew = 160000000









path = '//rpclustersrv1/cbjorkma/LSS2'

os.chdir(path)

#filename = 'FlukaDiffuserZSinteractionFull'


import pickle
with open('LSS2_exp001_fort.99.pkl', 'rb') as f:
    data1 = pickle.load(f)

with open('LSS2_exp001_usrmed.pkl', 'rb') as f:
    data2 = pickle.load(f)


ZSold = []

ZSold.append(  data2[data2['Z'].between(3,7)])

ZSold.append(  data2[data2['Z'].between(7,11)])

ZSold.append(  data2[data2['Z'].between(11,15)])

ZSold.append(  data2[data2['Z'].between(15,19)])

ZSold.append(  data2[data2['Z'].between(19,23)])



normOld = 20000000








fig = plt.figure()

for i in range(1,5):

    #new
    ZS = ZSnew[i]
    xes = sorted(ZS.REG.unique())
    yes = np.zeros(len(xes))
    for j in range(len(xes)):
        yes[j] = sum(ZS.REG == xes[j])
    
    yes = yes/ normNew
    
    #old
    ZS = ZSold[i]
    xesold = sorted(ZS.REG.unique())
    #assert xes == xesold
    yesold = np.zeros(len(xes))
    for j in range(len(xes)):
        try:
            yesold[j] = sum(ZS.REG == xesold[j])
        except:
            yesold[j] = 0
    yesold = yesold / normOld

    
    ax = fig.add_subplot(2,2,i)
    
    plt.bar(np.arange(len(xes)), yes, label = 'New')
    try:
        plt.bar(np.arange(len(xes)), yesold, label = 'Old', alpha = 0.5)
    except:
        pass
    
    if i == 1:
#        #array([273, 269, 274, 268], dtype=int64)
#        newticks = ('IonTraps','SeptHold','ShellOp','CathEle')
        #[268, 269, 273, 274]
        newticks = ('CathEle','SeptHold','IonTraps','ShellOp')
    elif i == 2:
        #array([302, 297, 296, 301], dtype=int64)
        #newticks = ('ShellOpb','SeptHldb','CathEleb','IonTrapb')
        #[296, 297, 301, 302]
        newticks = ('CathEleb','SeptHldb','IonTrapb','ShellOpb')
    elif i == 3:   
        #array([282, 283, 288, 287], dtype=int64)
        #newticks = ('CathElec','SeptHldc','ShellOpc','IonTrapc')
        #[282, 283, 287, 288]
        newticks = ('CathElec','SeptHldc','IonTrapc','ShellOpc')
    elif i == 4:
        #array([282, 283, 288, 287], dtype=int64)
        #newticks = ('CathElec','SeptHldc','ShellOpc','IonTrapc')
        #[282, 283, 287, 288]
        newticks = ('CathElec','SeptHldc','IonTrapc','ShellOpc')
    plt.xticks(np.arange(len(xes)), newticks)
    plt.title('ZS element ' + str(i+1))
    plt.legend()
    plt.ylabel('Hits per primary particle')
    
plt.suptitle('Hits in the non-septa ZS aperture', fontsize = 22)
plt.show()

for i in range(1,5):

    #ZS = ZSnew[i]
    print sorted(ZSnew[i].REG.unique())
    print sorted(ZSold[i].REG.unique())
    print ' '
    print ' '






#    if i == 1:
#        #array([273, 269, 274, 268], dtype=int64)
#        newticks = ('IonTraps','SeptHold','ShellOp','CathEle')
#    elif i == 2:
#        #array([302, 297, 296, 301], dtype=int64)
#        newticks = ('ShellOpb','SeptHldb','CathEleb','IonTrapb')
#    elif i == 3:   
#        #array([282, 283, 288, 287], dtype=int64)
#        newticks = ('CathElec','SeptHldc','ShellOpc','IonTrapc')
#    elif i == 4:
#        #array([282, 283, 288, 287], dtype=int64)
#        newticks = ('CathElec','SeptHldc','ShellOpc','IonTrapc')






#try:
#    fluka = np.load(filename + '.npy')
#except:
#    
#    import pickle
#    with open('LSS2_exp001_fort.99.pkl', 'rb') as f:
#        data = pickle.load(f)
#    
#    #madxListed = data.values()
#    
#    keys = data.keys()
#    print 'First...'
#    print keys
#    fluka1 = np.zeros([data.shape[0],3])
#    
#    for i in range(data.shape[0]):
#        fluka1[0:,0] = data.X*100
#        fluka1[0:,1] = data.Y*100
#        fluka1[0:,2] = data.Z*100
#    
#    with open('LSS2_exp001_usrmed.dat.pkl', 'rb') as f:
#        data = pickle.load(f)
#    
#    #madxListed = data.values()
#    
#    keys = data.keys()
#    print 'Second...'
#    print keys
#    fluka2 = np.zeros([data.shape[0],3])
#    
#    for i in range(data.shape[0]):
#        fluka2[0:,0] = data.X*100
#        fluka2[0:,1] = data.Y*100
#        fluka2[0:,2] = data.Z*100
#    
#    fluka = np.concatenate((fluka1,fluka2), axis = 0)
#    
#    np.save(filename,fluka )
print 'Fluka loaded'