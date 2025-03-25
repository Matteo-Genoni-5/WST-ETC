#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 24 17:30:30 2025

@author: matteog
"""

# 0. IMPORT MODULES
import numpy as np
import matplotlib.pyplot as plt
import astropy.units as u
import os 
from scipy.interpolate import interp1d
#rom astropy import units as u
from spextra import Spextrum
#from setplot import set_plot_style

#set_plot_style()

# 1. LOAD SED FROM INTERNAL DATABASE AND FROM SPEXTRA DATABASE
#
# 1.1 to read a generic file with two columns
file_path = "/home/matteog/Documents/WST/ETC/" #"specX/av0"
file_name = "Starbust1__R_17_VV__z1__erg_s_cm2_A.txt"
source_str = 'Starbust1 R 17 Vega z1'
file_path_tot = (file_path + file_name)
wave2, flux2 = np.loadtxt(file_path_tot, unpack=True)
# set lam in Ang
wave2*=10
#
# 1.2 load from SPEXTRA database and normalization
sp = Spextrum('kc96/starb1', z=1)
sp2 = sp.scale_to_magnitude(amplitude=17 * u.mag, filter_curve="R")
sp3 = sp2.to_spectrum1d(flux_unit='FLAM')
sp2_wave = sp3.wavelength.value
sp2_flux = sp3.flux.value
# plot 1
sp2.plot(flux_unit="FLAM")
plt.plot(wave2,flux2)
plt.grid()
plt.title(source_str)
figure_save_str_1 = (file_path + source_str + ' - plot1.png')
plt.savefig(figure_save_str_1)
plt.show()

# plot 2
plt.figure()
plt.plot(wave2,flux2,'r',label='from ESO-ETC')
plt.plot(sp2_wave,sp2_flux, label = 'Spextra dabase normalized')
plt.xlabel("Wavelength (Angstrom)")
plt.ylabel("Flux (erg/sec/cm2/Ang)")
plt.axis([3000, 7000, 0, (1.5*(flux2.max()))])
plt.legend()
plt.grid()
plt.title(source_str)
figure_save_str_2 = (file_path + source_str + ' - plot2.png')
plt.savefig(figure_save_str_2)
plt.show()

# 2. Interpolate
sp2_flux2 = np.interp(wave2, sp2_wave, sp2_flux)
# Calculate the relative difference between the fluxes
relative_diff = np.abs(sp2_flux2 - flux2) / sp2_flux2
# Calculate the mean of the relative difference
mean_relative_diff = np.mean(relative_diff)
# plot 3
# Plot the relative difference
plt.plot(wave2, relative_diff, label='Relative Difference', color='blue')
# Plot the mean of the relative difference as a horizontal line
plt.axhline(mean_relative_diff, color='red', linestyle='--', label=f'Mean = {mean_relative_diff*100:.2}%')
# Adding labels and legend
plt.xlabel("Wavelength (Angstrom)")
plt.ylabel("Relative Difference")
plt.legend()
plt.title(source_str)
# Display the plot
plt.grid()
figure_save_str_3 = (file_path + source_str + ' - plot3.png')
plt.savefig(figure_save_str_3)
plt.show()


# 3. ...
'''
# plot 3
plt.figure()
plt.plot(wave2,flux2,'r',label='from ESO-ETC')
plt.plot(sp2_wave,sp2_flux2, label = 'Spextra dabase normalized')
plt.xlabel("Wavelength (Angstrom)")
plt.ylabel("Flux (erg)/sec/cm2/Ang")
plt.axis([3000, 7000, 0, (2*(flux2.max()))])
plt.legend()
plt.grid()
plt.show()
'''