import matplotlib.pyplot as plt
import numpy as np
from scipy import interpolate
from astropy.io import fits



class Spectrum(object):
    
    def __init__(self, path):
        self.specfile = fits.open(path)
        
        
    def intpol(self):
        '''to interpolate the spectum file (x axis is converted back
        to Ä)'''
        self.flux = self.specfile[1].data.field("flux")
        self.log = np.array(self.specfile[1].data.field("loglam"))
        self.wavelen = 10**self.log
        #plt.plot(self.wavelen, self.flux)

        self.interpolated = interpolate.interp1d(self.wavelen,
        self.flux, bounds_error=False)  

    def plot_intpol(self, newgrid):
        '''to plot the interpolated function using 'newgrid' eg.
        np.arange(3000, 10000, 0.5) to mimic original spectrum'''
        plt.plot(newgrid, self.interpolated(newgrid))
        plt.show()



#to test the script:
        
# a = Spectrum("spec-0266-51602-0001.fits")

# a.intpol()
# a.plot_intpol(np.arange(3000,10000, 0.5))
# plt.show()
# print "done"

