# -*- coding: utf-8 -*-
"""
Created on Fri Mar 21 23:36:24 2025

@author: MatteoGenoni
"""

import math #ok
import numpy as np #ok
from numpy import exp, cos, linspace #ok
import matplotlib.pyplot as plt #ok
import os, time, glob
import scipy.special as sp
from ftplib import FTP
import gzip
from scipy import interpolate, constants, sqrt, exp
from astropy.io import fits
from os import listdir # CANCELLARE
from os.path import isfile, join
from operator import truediv
from glob import glob
from astropy.table import Table
import pandas as pd


# 1. Set the SED txt filename
filename_UVB = 'Pickles_AOV__J_17_VV__z0__UVB.txt'
filename_VIS = 'Pickles_AOV__J_17_VV__z0__VIS.txt'
filename_NIR = 'Pickles_AOV__J_17_VV__z0__NIR.txt'
filename_save = 'Pickles_AOV__J_17_VV__z0.txt'
filename_save_header = 'lam(nm) Flux (erg/s/cm2/Ang)'

# 2 Open files
Tab_UVB = np.loadtxt(filename_UVB, delimiter='\t', skiprows=1, dtype=float)
Tab_VIS = np.loadtxt(filename_VIS, delimiter='\t', skiprows=1, dtype=float)
Tab_NIR = np.loadtxt(filename_NIR, delimiter='\t', skiprows=1, dtype=float)
#Tab_UVB = Table.read(filename_UVB)
#Tab_UVB = pd.read_table(filename_UVB,delimiter='t', skiprows=1, index_col=0)

# 3 Reverse 
Tab_UVB_1 = np.flipud(Tab_UVB)
Tab_VIS_1 = np.flipud(Tab_VIS)
Tab_NIR_1 = np.flipud(Tab_NIR)

# 4 Concatenate
Tab_XSH_1 = np.concatenate((Tab_UVB_1, Tab_VIS_1, Tab_NIR_1) , axis=0)
Tab_XSH_1_lam = Tab_XSH_1[:,0]
Tab_XSH_1_flu = Tab_XSH_1[:,1]

# 5 plot
plt.figure()
plt.plot(Tab_XSH_1_lam, Tab_XSH_1_flu, 'b')
plt.axis([Tab_XSH_1_lam[0], Tab_XSH_1_lam[-1], 0, Tab_XSH_1_flu.max()])
plt.title('SED ')
plt.show()

# 6 save txt
np.savetxt(filename_save, Tab_XSH_1, fmt='%1.4e', delimiter=' ', header=filename_save_header)

# 7 Test reopening
Tab_XSH_2 = np.loadtxt(filename_save, delimiter=' ', skiprows=1, dtype=float)
Tab_XSH_2_lam = Tab_XSH_2[:,0]
Tab_XSH_2_flu = Tab_XSH_2[:,1]
#
plt.figure()
plt.plot(Tab_XSH_2_lam, Tab_XSH_2_flu, 'b')
plt.axis([Tab_XSH_2_lam[0], Tab_XSH_2_lam[-1], 0, Tab_XSH_2_flu.max()])
plt.title('SED Test')
plt.show()