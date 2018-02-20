# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 12:12:55 2018

@author: cbjorkma
"""

#USRBIN parser

directory ='//rpclustersrv1/cbjorkma/Dump studies/backup'


import os
import shutil
#from pathlib2 import Path

os.chdir(directory)

Numbers = [25,29,92]


dirs = sorted([name for name in os.listdir(".") if os.path.isdir(name)])


movedFiles = []
count = 0
for j in range(len(dirs)):
    newpath = directory + '/' + dirs[j]
    os.chdir(newpath)
    files = os.listdir(newpath)
    files = filter(lambda x: x[-2:].isdigit() , files)   
    for i in range(len(files)):
        #my_file = Path(directory + '/' + files[i])
        if os.path.isfile('../' + files[i]):
            print files[i]
            new_name =  files[i][:-8] +'_' + str(count) + files[i][-8:]
            thefile = open(files[i], 'r')
            lines = thefile.readlines() 
            thefile.close()
            os.chdir(directory)
            newfile = open(new_name, 'w')
            newfile.writelines(lines)
            newfile.close()
            movedFiles.append(files[i])
            count = count +1
        else:    
            if int(files[i][-2:]) in Numbers:
                try:
                    shutil.copy(files[i],directory)
                except Exception as e:
                    print e + 'Moving file anyway'
                    new_name =  files[i][:-8] +'_' + str(count) + files[i][-8:]
                    thefile = open(files[i], 'r')
                    lines = thefile.readlines() 
                    thefile.close()
                    os.chdir(directory)
                    newfile = open(new_name, 'w')
                    newfile.writelines(lines)
                    newfile.close()
                    movedFiles.append(files[i])
                    count = count +1                    
                movedFiles.append(files[i])
                count = count +1
    

print str(count) + ' files copied over to parent directory:'
print movedFiles



#
#
##USRBIN parser
#
#directory ='/scratch/cbjorkma/LSS2/activation8/'
#
##destination = directory
#
##/scratch/luillo/LSS2/2018-01-10_200umRibbonZS_full_abd_z2232cm_ZSrho/
##/scratch/cbjorkma/LSS2/ac/tivation4/ /scratch/cbjorkma/LSS2/activation8/
#import os
#import shutil
##from pathlib2 import Path
#
#os.chdir(directory)
#
##Numbers = [23,24,25,26,27,28, 30,90,91,92]
#Numbers = [29]
#
#dirs = sorted([name for name in os.listdir(".") if os.path.isdir(name)])
#
#
#movedFiles = []
#count = 0
#for j in range(len(dirs)):
#    newpath = directory + '/' + dirs[j]
#    os.chdir(newpath)
#    files = os.listdir(newpath)
#    files = filter(lambda x: x[-2:].isdigit() , files)   
#    for i in range(len(files)):
#        #my_file = Path(directory + '/' + files[i])
#        if os.path.isfile('../' + files[i]):
##        if os.path.isfile(destination + files[i]):
#            #print files[i]
#            new_name =  files[i][:-8] +'_' + str(count) + files[i][-8:]
#            thefile = open(files[i], 'r')
#            lines = thefile.readlines() 
#            thefile.close()
#            os.chdir(directory)
#            newfile = open(new_name, 'w')
#            newfile.writelines(lines)
#            newfile.close()
#            movedFiles.append(files[i])
#            count = count +1
#        else:    
#            if int(files[i][-2:]) in Numbers:
#                try:
#                    shutil.copy(files[i],directory)
#                except Exception as e:
##                    print e
##		    print 'Moving file anyway'
#                    new_name =  files[i][:-8] +'_' + str(count) + files[i][-8:]
#		    try:
#                    	thefile = open(files[i], 'r')
#                    	lines = thefile.readlines() 
#                    	thefile.close()
#                    	os.chdir(directory)
#                    	newfile = open(new_name, 'w')
#                    	newfile.writelines(lines)
#                    	newfile.close()
#                    	movedFiles.append(files[i])
#                    	count = count +1
#		    except:
#			print 'Unable to move ' + files[i]                    
#                movedFiles.append(files[i])
#                count = count +1
#    
#
#print str(count) + ' files copied over to parent directory:'
#print movedFiles
