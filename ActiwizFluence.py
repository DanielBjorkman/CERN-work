#
#Actiwiz Fluence and Actiwiz fluence plot
#
# Code for parsing and plotting particle fluence data
#
#Call:
#fig = plt.figure()
#data = ActiwizFluence(path, volume)
#ax = plt.subplot(111)
#ActiwizFluencePlot(data, ax, prim)
#
#prim is optional, as it is set to 1 by default
#
#
# Required python libraries: Numpy, Matplotlib
#
# Developed by Daniel Bjorkman at CERN 2017
# daniel.bjorkman@cern.ch

def ActiwizFluence(path,volume = 1):
    
    import os
    os.chdir(path)
    
    
    import numpy as np
    
    from os import listdir
    from os.path import isfile, join
    
    onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]           
    files = filter(lambda x: x[-4:] == '.txt' , onlyfiles)             
    files = filter(lambda x: x[-8:-4] == 'NEUT'or x[-8:-4] == 'PROT' or x[-8:-4] == '_PI+' or x[-8:-4] == '_PI-', files)
    files = sorted(files)      
                   
         
    Out = []
    particles = []
   
    
    for i in range(len(files)):
    
        filename = files[i]
        
        f = open(filename,'r') 
        lines = f.readlines()
        
        particles.append( lines[0].split(' ')[4][:-1])
        
        
        data = np.loadtxt(filename, skiprows = 2, dtype='float')
        
        data[0:,2] = data[0:,2]/volume
        Out.append(data)

  
    Out.append(particles)
    return Out
 
def ActiwizFluencePlot(In ,ax, prim =1):

    import matplotlib.pyplot as plt
    
    for i in range(len(In) -1):
        #print 
        data = In[i]
        particle = In[len(In)-1][i]        

        #plt.loglog((data[0:,0] +  data[0:,1])/2, data[0:,2],label= particle)
        xes = (data[0:,0] +  data[0:,1])/2
        plt.errorbar(xes, xes*prim*data[0:,2], yerr = xes*data[0:,3]*data[0:,2], label= particle)
        ax.set_xscale("log", nonposx='clip')
        ax.set_yscale("log", nonposy='clip')
        plt.xlabel('E [GeV]', fontsize = 13)
        plt.ylabel('E * Fluence [cm-2]', fontsize = 16)
        plt.grid(True)
        plt.legend()