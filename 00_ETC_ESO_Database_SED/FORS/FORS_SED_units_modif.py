# -*- coding: utf-8 -*-
"""
Created on Sun Mar 23 10:51:26 2025

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

# 0. Set names and variables
filename_save_header = 'lam(nm) Flux (erg/s/cm2/Ang)'


# 1. get current directory
cwd = os.getcwd()
# print(cwd)

# 2. find all txt files in the current directory and store them in the list
filename_list = []
nfile=0
for file in os.listdir(cwd):
	if file.endswith(".txt"):
		print(file)
		filename_list.append(file)
		nfile = nfile+1
		
# 3. open all files and modify the flux column
m2_to_cm2 = 10000
um_to_A = 10000
J_to_erg = 1e7	
const = 1e-20	 
for j in range(0,(nfile-1)):
	filename_temp = filename_list[j]
	Tab = np.loadtxt(filename_temp, delimiter=' ', skiprows=1, dtype=float)
	Tab_flu = Tab[:,1]*(const*J_to_erg)/(m2_to_cm2*um_to_A)
	Tab1 = Tab
	Tab1[:,1] = Tab_flu
	filename_save = (filename_temp[0:-4] + '__erg_s_cm2_A.txt')
	np.savetxt(filename_save, Tab1, fmt='%1.4e', delimiter=' ', header=filename_save_header)

