import matplotlib.pyplot as plt
import numpy as np
from scipy import interpolate
from astropy.io import fits



class Spectrum(object):
    
    def __init__(self, path):
        self.specfile = fits.open(path)
        
        
    def intpol(self):
        '''to interpolate the spectum file (loglam converted back
        to Ä)'''
        self.flux = np.array(self.specfile[1].data.field("flux"))
        self.log = np.array(self.specfile[1].data.field("loglam"))
        self.wavelen = 10**self.log
        #plt.plot(self.wavelen, self.flux)

        self.interpolated = interpolate.interp1d(self.wavelen,
        self.flux, bounds_error=False)  
        interpolated = self.interpolated
        
        return interpolated


    def plot_intpol(self, newgrid): #method not necessary
        '''to plot the interpolated function using 'newgrid' eg.
        np.arange(3000, 10000, 0.5) to mimic original spectrum'''
        plt.plot(newgrid, self.interpolated(newgrid))
        plt.show()


# to test the script(data from http://data.sdss3.org/bulkSpectra):
# info on spec files: http://data.sdss3.org/datamodel/files/BOSS_SPECTRO_REDUX/RUN2D/spectra/PLATE4/spec.html        
# a = Spectrum("spec-0266-51602-0001.fits")
# a.intpol()
# a.plot_intpol(np.arange(3000,10000, 0.5))
# plt.show()
# print "done"


# to proceed:

speclist = [] # list of spec file names



def coadd_spectra(speclist, newgrid):
    '''
    coadd_spectra(speclist, newgrid) 
    To coadd and plot spectra files specified in speclist. The grid
    for interpolation is given by newgrid (a numpy array).
    '''  

    try:
        assert type(speclist) == list 
    except AssertionError:
        print "First argument must be a list of specfile names"
       
    try:
        assert type(newgrid) == numpy.ndarray #could be anything
    except AssertionError:
        print "Second argument must be a numpy array"
        
    flux_coadd = np.zeros(newgrid.size) 
 
    for name in l:
        
        specobj = Spectrum(name)
        specobj.intpol()
        
        flux_coadd += interpolated(newgrid)

        
    plt.plot(newgrid, flux_coadd)

    plt.xlabel("Wavelength (Ä)", fontsize=16)
    plt.ylabel("Flux (1e-17 ergs/s/cm^2/Ä)", fontsize=16)
    plt.title("Coadded spectra", fontsize=20)

    plt.show()


