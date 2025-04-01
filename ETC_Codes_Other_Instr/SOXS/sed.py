# coding=utf-8

from scipy import constants, sqrt, exp
import numpy as np

# BLACK BODY


def get_blackbody(source, temperature):
    # return 8 * constants.pi * constants.h * constants.c ** 2 / ((source / 10 ** 10) ** 5 * (
    # np.exp(constants.h * constants.c / (constants.k * temperature * (source / 10 ** 10))) - 1)) # J/(s * m2 * m) # W / m^2 m

    return 8 * constants.pi * constants.h * constants.c ** 2 / ((source / 10 ** 10) ** 5 * (
        np.exp(constants.h * constants.c / (constants.k * temperature * (source / 10 ** 10))) - 1))  # J/(s * m2 * m) or W / m^2 * m


def get_powerlaw(source, sed_index=0):
    return np.power(source, sed_index)  # J/(s * m2 * m)


def get_linear_interpolation(source, ll, flux):
    return np.interp(source, ll, flux)  # [erg/s/cm2/A]


def get_single_line(source, ll, flux, fwhm):
    lam_sel_vect = np.ones(len(source)) * ll  # [Ang]
    sigma_sel = fwhm / 2.355  # [Ang]
    flux_sel = flux * (10 ** (-16))  # [erg/s/cm2]
    const1 = (flux_sel / (sigma_sel * sqrt(2. * np.pi)))
    const2 = (source - lam_sel_vect) / sigma_sel
    return const1 * exp(-0.5 * ((const2) ** 2.))  # [erg/s/cm2/A]
