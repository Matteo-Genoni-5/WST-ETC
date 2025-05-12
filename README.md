# WST-ETC

The folder is organized as follow:

(1) 00_ETC_ESO_Database_SED: subfolders with different instrument ETC generated spectra under different conditions (magnitude, filter, system, redshift, ...) as well as some tests done with spextra-based and INAF-SOXS codes (8) to reproduce the input spectra

(2) Band_Filters: folder containing the transmission curves of UBVRIYJHK filters from ESO

(3) GitHub_Test_Subfolders & XSHOOTER: test folders

(4) tested_MF: comparison plots between templates from folder (1) and spectra produced via SPCalib.ipynb

(5) Link_and_References: useful links

(6) Notebook_docs.ipynb: general notebook to highlight and test the pyetc/wst classes and methods

(7) SPcalib.ipynb: class and test for the magnitude calibation 

(8) ETC_Codes_Other_instr/SOXS: SOXS python useful codes for the magnitude calibration

In developement:

_____ pyetc2 _____
evolution of the original pyetc package, below a list of updates:

- SPcalib.ipynb -> Classes in a standalone .py module specalib.py for filter/magnitude spectral calibration and SED generation
- ESO_original_spectra/ -> folder with the ESO SED templates
- Band_Filters/ -> transmission curves with the UBVRI - SDSS ugriz - LSST ugriz
- Modified <get_seeing_fwhm> in order to return both atmospheric+telescope IQ with atmospheric+telescope+instrument IQ  
  Also added (courtesy of Schiappacasse J.) handling of fiber-injection losses from ESPRESSO (Schimdt+24)
  
(9) pyetc2_tests.ipynb -> Test notebook with several new methods and functions that will end up in the main etc.py of the pyetc2 module, mainly:
- 1) definition of a full dictionary for observations - sky - image - spectrum, basically a wrapper for the built-in methods of pyetc
- 2) new functions for spectrum generation given templates, lines, black body and powerlaws
- 3) ESOSkycalc call for dynamical sky cofiguration generations  

- In the main code added a keyword in the obs dictionary -> "skycalc", if this is set to true the sky configuration is computed dinamically, if not is taken locally as usual (using the MOON parameter)

