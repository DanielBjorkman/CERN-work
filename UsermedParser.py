# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 16:42:58 2018

@author: cbjorkma
"""

import pandas as pd
import glob

def parse_usrmed(fname):
    df = pd.read_csv(fname, sep='\s+', skiprows=1,
                     names=['NCASE','PID','PTOT','X','Y','Z','COSX','COSY','COSZ','WEIGHT','LTRACK','ISAMPLE',
                           'REG'])    
    return df

def loop_usrmed(basedir, pattern):

    pattern = basedir + pattern
    
    frames = []
    for fname in glob.iglob(pattern):
        d = parse_usrmed(fname)
        frames.append(d)

    print("Files processed %d"%(len(frames)))
    assert len(frames) != 0, "no file processes"

    df = pd.concat(frames)
    
    return df

basedir = '/Volumes/clueet_scratch/luillo/LSS2/2018-01-10_200umRibbonZS_full_abd_z2232cm_ZSrho/'

interacted = loop_usrmed(basedir, pattern='/*/LSS2_exp001_fort.99'  )
loss       = loop_usrmed(basedir, pattern='/*/LSS2_exp001_usrmed.dat')
