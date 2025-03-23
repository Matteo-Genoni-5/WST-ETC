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
filename_BLU = 'PowerLaw_2__B_7_VV__z0__BLU.txt'
filename_RED = 'PowerLaw_2__B_7_VV__z0__RED.txt'
filename_save = 'PowerLaw_2__B_7_VV__z0.txt'
filename_save_header = 'lam(nm) Flux (erg/s/cm2/Ang)'

# 2 Open files
Tab_BLU = np.loadtxt(filename_BLU, delimiter='\t', skiprows=1, dtype=float)
Tab_RED = np.loadtxt(filename_RED, delimiter='\t', skiprows=1, dtype=float)
#Tab_BLU = Table.read(filename_BLU)
#Tab_BLU = pd.read_table(filename_BLU,delimiter='t', skiprows=1, index_col=0)

# 3 Reverse 
Tab_BLU_1 = np.flipud(Tab_BLU)
Tab_RED_1 = np.flipud(Tab_RED)

# 4 Concatenate
nrows = np.size(Tab_RED_1,0)
Tab_RED_2 = Tab_RED_1[1:nrows,:]
Tab_XSH_1 = np.concatenate((Tab_BLU_1, Tab_RED_2) , axis=0)
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