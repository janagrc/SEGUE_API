from astropy.io import fits
import numpy as np
import copy
import pylab
import math

class DataFile(object):
    def mask(self,required_fields=["LOGG_ADOP","FEH_ADOP","TEFF_ADOP","DIST_ADOP"], badValue=-9999):
        #print self.data.size
        msk=np.ones(self.data.size,dtype=bool)
        for field in required_fields:
            msk &= (self.data[field] != badValue)
        return self.data[msk]
        
    def unique_spectral_types(self):
	    return list(set(self.data["SPECTYPE_HAMMER"]))
	    
    def __init__(self, path):
        self.path = path
        datafile = fits.open(path)
        self.column_names = datafile[1].columns.names
        self.data = datafile[1].data 
        self.gooddata=self.mask()
        self.spectypes=self.unique_spectral_types()

