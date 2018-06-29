




class USRBIN():
    """
    Class for reconstructing and handling ASCII formatted Fluka USRBIN outputs
    
    Developed by Daniel Björkman 2018
    daniel.bjorkman@cern.ch
    
    call:
    from USRBIN import USRBIN
    x = USRBIN(filename, path, normfactor)
    x.read()
    x.calc()
    x.plot()
    
    """
    def __init__(self, filename, path, normfactor = 1):
        self.filename = filename
        self.path = path
        self.cube = []
        self.info = []
        self.depthdeposition = []
        self.horizontal = []
        self.vertical = []
        self.max = []
        self.min = []
        self.normfactor = normfactor
        self.binningtype = []
        self.below = [] 
        self.side = []
        self.xcoodinates = []
        self.zcut = []
    
    def read(self):
        import os
        import time
    
        directory = self.path
        filename = self.filename
        
        startTime = time.time()
        os.chdir(directory)
    
        RPZ = 0
        RZ = 0
        CAR = 0
        row = 0
    
        #Predefine information into meta info directory and find starting position
        with open(filename) as file:
            for line in file.readlines():
                line_content = line.split()
                row = row + 1
                if len(line_content) > 5:
                    if line_content[5] == 'A(ir,ip,iz),':
                        info = {'rbin':[],'zbin':[],'pbin':[], 'rmin':[],'rmax':[], 'zmin':[],'zmax':[], 'rwidth':[], 'zwidth':[],'prad':[]}
                        RPZ = 1
                        print('R-Phi-Z binning detected')
                    if line_content[5] == 'A(ix,iy,iz),':
                        info = {'xbin':[], 'ybin':[],'zbin':[], 'xmin':[],'xmax':[], 'ymin':[],'ymax':[], 'zmin':[],'zmax':[], 'xwidth':[], 'ywidth':[], 'zwidth':[]}
                        CAR = 1
                        self.binningtype = 'CAR'
                        print('Cartesian binning detected')
                    if line_content[5] == 'A(ir,iz),':
                        info = {'rbin':[],'zbin':[],'pbin':[], 'rmin':[],'rmax':[], 'zmin':[],'zmax':[], 'rwidth':[], 'zwidth':[],'prad':[]}
                        info['pbin'].append(float(1))
                        RZ = 1
                        print('R-Z binning detected')
                    try:
                        a = float(line_content[0])
                        if isinstance(a, float) and len(line_content) > 1:
                            start = row
                            break
                    except Exception:
                        pass
    
        #Return if file is of wrong format
        if not (RPZ or RZ or CAR):
            print("Unable to read file")
            return
    
        #Extract dimensional information
        if RPZ or RZ:
            with open(filename) as file:
                for line in file.readlines():
                    line_content = line.split()
                    if line.lstrip(' ').partition(' ')[0] == 'R':
                        if line_content[1] != '-':
                            info['rbin'].append(float(line_content[7]))
                            info['rmin'].append(float(line_content[3]))
                            info['rmax'].append(float(line_content[5]))
                            info['rwidth'].append(float(line_content[10]))
                    if line.lstrip(' ').partition(' ')[0] == 'Z':
                        info['zbin'].append(float(line_content[7]))
                        info['zmin'].append(float(line_content[3]))
                        info['zmax'].append(float(line_content[5]))
                        info['zwidth'].append(float(line_content[10]))
                    if line.lstrip(' ').partition(' ')[0] == 'P':
                        info['pbin'].append(float(line_content[7]))
                        info['prad'].append(float(line_content[10]))
        elif CAR:
             with open(filename) as file:
                for line in file.readlines():
                     line_content = line.split()
                     if line.lstrip(' ').partition(' ')[0] == 'X':
                         info['xbin'].append(float(line_content[7]))
                         info['xmin'].append(float(line_content[3]))
                         info['xmax'].append(float(line_content[5]))
                         info['xwidth'].append(float(line_content[10]))
                     if line.lstrip(' ').partition(' ')[0] == 'Y':
                         info['ybin'].append(float(line_content[7]))
                         info['ymin'].append(float(line_content[3]))
                         info['ymax'].append(float(line_content[5]))
                         info['ywidth'].append(float(line_content[10]))
                     if line.lstrip(' ').partition(' ')[0] == 'Z':
                         info['zbin'].append(float(line_content[7]))
                         info['zmin'].append(float(line_content[3]))
                         info['zmax'].append(float(line_content[5]))
                         info['zwidth'].append(float(line_content[10]))
    
        if (RZ or RPZ) and not info['rmin'][0] == 0 :
            print("Function currently not defined for minimum rbins other than 0")
            return;
    
        #Find when to stop reading the input data
        with open(filename) as file:
            row = 0
#            stop = len(file.readlines())
            for line in file.readlines():
                line_content = line.split()   
                if row > start and len(line_content) != 10:
                    stop = row -1
                row = row +1
                
    
                
        import math
        import numpy as np
    
        data = np.genfromtxt(filename, skip_header= start -1, skip_footer= stop -9)
        print data.size
        data = np.reshape(data ,(data.size,1))
        
    
    
        #Cube reconstruction from list
        print("Reconstructing 3D cube...")
        if RPZ:
            cube = np.zeros((int(info['rbin'][0]) * 2,int(info['rbin'][0]) * 2,int(info['zbin'][0])))
            phiBinAngle = int(360 / info['pbin'][0])
            checkedVal = np.zeros((int(info['rbin'][0]) * 2,int(info['rbin'][0]) * 2,int(info['zbin'][0])))
            x0 = int(info['rbin'][0]) - 0.5
            y0 = int(info['rbin'][0]) - 0.5
            stepConverter = 100
    
            #Reconstructs the R-Phi-Z binning into cartesian coordinate system
            Rvector = np.zeros((int(info['rbin'][0]),1))
            tracker = 0
            for z in range(0, int(info['zbin'][0])):
                for phi in range(0,int(info['pbin'][0])):     
                    Rvector = data[range(0 +tracker*int(info['rbin'][0]),(tracker +1)*int(info['rbin'][0])),0]   
                    tracker = tracker +1        
                   # Rvector = list[0:int(info['rbin'][0])]
                   # del list[:int(info['rbin'][0])]
                    for r in range(0,int(info['rbin'][0])):
                        val = Rvector[r]
                        steps = int(math.ceil(math.pi * (r + 1) * float(phiBinAngle) / 180))
                        for p in range(0,stepConverter * phiBinAngle, stepConverter * phiBinAngle / steps):
                            angle = p * math.pi / (180 * stepConverter) + phi * phiBinAngle * math.pi / 180
                            x = int(round(x0 + (r + 0.5) * math.cos(angle)))
                            y = int(round(y0 + (r + 0.5) * math.sin(angle)))
                            if checkedVal[x,y,z] == 0:
                                cube[x, y,z] = val
                                checkedVal[x,y,z] = 1
    
            #Interpolating missing values
            print("Interpolating missing values...")
            for z in range(0,cube.shape[2]-1):
                for x in range(0,cube.shape[0] -1):
                    for y in range(0,cube.shape[1] -1):
                        if not checkedVal[x,y,z] and math.sqrt(math.pow(x-x0,2) + math.pow(y-y0,2)) < info['rbin'][0]:
                            sum = 0
                            sumCh = 0
                            for i in range(-1,2):
                                for ii in range(-1,2):
                                    sum = sum + cube[x+i,y+ii,z]
                                    sumCh = sumCh + checkedVal[x+i,y+ii,z]
                            cube[x,y,z] = sum/sumCh
                            checkedVal[x,y,z] = 1
            print("Missing values interpolated")
            cube = np.rot90(cube)
            cube = np.fliplr(cube)
    
        elif RZ:
            cube = np.zeros((int(info['rbin'][0]) * 2,int(info['rbin'][0]) * 2,int(info['zbin'][0])))
            phiBinAngle = int(360 / 4)
            checkedVal = np.zeros((int(info['rbin'][0]) * 2,int(info['rbin'][0]) * 2,int(info['zbin'][0])))
            x0 = int(info['rbin'][0]) - 0.5
            y0 = int(info['rbin'][0]) - 0.5
            stepConverter = 100      
    
            #Reconstructs a quarter of the R-Z binning into cartesian coordinate system
            Rvector = np.zeros((int(info['rbin'][0]),1))
            tracker = 0
            for z in range(0, int(info['zbin'][0])):
                    Rvector = data[range(0 +tracker*int(info['rbin'][0]),(tracker +1)*int(info['rbin'][0])),0]   
                    tracker = tracker +1 
                    for r in range(0,int(info['rbin'][0])):
                        val = Rvector[r]
                        steps = int(math.ceil(math.pi * (r + 1) * float(phiBinAngle) / 180))
                        for p in range(0,stepConverter * phiBinAngle, stepConverter * phiBinAngle / steps):
                            angle = p * math.pi / (180 * stepConverter)
                            x = int(round(x0 + (r + 0.5) * math.cos(angle)))
                            y = int(round(y0 + (r + 0.5) * math.sin(angle)))
                            if checkedVal[x,y,z] == 0:
                                cube[x, y,z] = val
                                checkedVal[x,y,z] = 1
    
            #Interpolating missing values
            print("Interpolating missing values...")
            for z in range(0,cube.shape[2]-1):
                for x in range(int(cube.shape[0]/2),cube.shape[0] -1):
                    for y in range(int(cube.shape[1]/2),cube.shape[1] -1):
                        if not checkedVal[x,y,z] and math.sqrt(math.pow(x-x0,2) + math.pow(y-y0,2)) < info['rbin'][0]:
                            sum = 0
                            sumCh = 0
                            for i in range(-1,2):
                                for ii in range(-1,2):
                                    sum = sum + cube[x+i,y+ii,z]
                                    sumCh = sumCh + checkedVal[x+i,y+ii,z]
                            cube[x,y,z] = sum/sumCh
                            checkedVal[x,y,z] = 1
            print("Missing values interpolated")
    
            #Mirror the constructed quarter to fill the rest of the cube
            tmpCube = np.fliplr(cube)
            cube = cube + tmpCube
            tmpCube = np.flipud(cube)
            cube = cube + tmpCube
    
        else:
            cube = np.reshape(data, (int(info['xbin'][0]),int(info['ybin'][0]),int(info['zbin'][0])),order='F')
    
        end = time.time()
        print("Cube reconstructed in " + str(round(end - startTime,2)) + " seconds")
    
    
        self.cube = cube * self.normfactor
        self.max = np.amax(cube)
        self.min = np.amin(cube)
        self.info = info
    
    def plot(self):
        
        cube = self.cube
        
        import math
        import numpy as np
        import matplotlib.pyplot as plt
        from matplotlib.colors import LogNorm
        import matplotlib.gridspec as gridspec
        import matplotlib.ticker as ticker

        #Determines the indecies of maxiumum value in cube
        i,j,k = np.unravel_index(cube.argmax(), cube.shape)

        #Conditional color scaling     
        vmax = cube.max()
        vmin = np.min(cube[np.nonzero(cube)])
        if int(math.log10(vmax)) - int(math.log10(vmin)) > 14 :
            vmin = vmax * math.pow(10,-14)

        fig = plt.figure()
        
        gs0 = gridspec.GridSpec(1, 3)
        gs00 = gridspec.GridSpecFromSubplotSpec(3, 1, subplot_spec=gs0[0])
        ax = plt.subplot(gs0[1:])
        image = cube[0:,0:,k]
        image = np.rot90(image,3)
        if self.binningtype == 'CAR':
            def y_fmt(x, y):
                return cube.shape[0] - x
            ax.xaxis.set_major_formatter(ticker.FuncFormatter(y_fmt))
        plt.pcolor(image, norm=LogNorm(vmin=vmin, vmax=vmax), cmap='jet')
        cbar = plt.colorbar()
        cbar.set_label('Intensity')
        plt.title('Z plane')
        plt.xlabel('X- axis')
        plt.ylabel('Y- axis')
        

        plt.subplot(gs00[0])
        image = cube[i,0:,0:]
        plt.pcolor(image, norm=LogNorm(vmin=vmin, vmax=vmax), cmap='jet')
        plt.title('X plane')
        plt.xlabel('Z- axis')
        plt.ylabel('Y- axis')


        plt.subplot(gs00[1])
        image = cube[0:,j,0:]
        plt.pcolor(image, norm=LogNorm(vmin=vmin, vmax=vmax), cmap='jet')
        plt.title('Y plane')
        plt.xlabel('Z- axis')
        plt.ylabel('X- axis')


        plt.subplot(gs00[2])
        vector = np.zeros((cube.shape[2]))
        for r in range(0,cube.shape[2]):
            vector[r] = np.sum(cube[0:,0:,r])
        plt.plot(range(0,cube.shape[2]),vector)
        plt.title('Integrated depth deposition')
        plt.xlabel('Z- axis')
        plt.ylabel('Integrated intensity')
        plt.grid()

        plt.show()

    def calc(self):
        
        import numpy as np
        
        cube = self.cube
        self.vertical = cube[int(cube.shape[0]/2),0:,0:]       
        self.horizontal = cube[0:,int(cube.shape[1]/2),0:]  
        self.zcut = cube[0:,0:,int(cube.shape[2]/2)]  
        
        vector = np.zeros((cube.shape[2]))
        vector2 = np.zeros((cube.shape[2]))
        vector3 = np.zeros((cube.shape[2]))
        for r in range(0,cube.shape[2]):
            vector[r] = np.sum(cube[0:,0:,r])
            vector2[r] = cube[int(cube.shape[0]/2), 5,r]
            vector3[r] = cube[14 ,int( cube.shape[1]/2),r]
        self.depthdeposition = vector
        self.below = vector2
        self.side = vector3
        self.xcoodinates = np.arange(int(self.info['zmin'][0]),int(self.info['zmax'][0]),self.info['zwidth'][0]*1.0001)
        
        
        
#import math
#import numpy as np
#import matplotlib.pyplot as plt
#from matplotlib.colors import LogNorm
#import matplotlib.gridspec as gridspec
#import matplotlib.ticker as ticker       
#
#filename = 'LSS2_exp_24.bnn.lis'
#
#path = '//rpclustersrv1/cbjorkma/LSS2'
#    
#x = USRBIN(filename, path)
##
##
#print x.filename
#
#print x.cube
#
#x.read()
#
#print x.cube
#
#print x.max
#
#print x.info['xbin'][0]
#
#
#
#x.plot()
#
#
#x.calc()
#
#fig = plt.figure()
#
#plt.plot(x.depthdeposition)
#plt.yscale("log", nonposy='clip')
#
#plt.show()
#

#
#a = np.arange(int(x.info['zmin'][0]),int(x.info['zmax'][0]),x.info['zwidth'][0]*1.0001)
#
#assert a.shape == x.below.shape
#
###
###
##
#
#















