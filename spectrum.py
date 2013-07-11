# class DataFile(object):
#     def openfile(self,filepath=None):
#         from astropy.io import fits
#         self.datafile = fits.open(self.filepath, memmap=True)

#class Star(object):


def openfile(filename):
    '''to open the fits file and read in the LOGG_ADOP, FEH_ADOP and
    TEFF_ADOP columns'''
    
    from astropy.io import fits
    datafile = fits.open(filename)
    
    logg = datafile[1].data.field("LOGG_ADOP")
    feh = datafile[1].data.field("FEH_ADOP")
    teff = datafile[1].data.field("TEFF_ADOP")

        
    print "The fits file is opened as 'datafile'"


def checkdata(logg,feh,teff):
    '''to check if any of the fields have -9999 value'''
    

    for i in len(logg):
        if logg[i] or feh[i] or teff[i] == -9999:
            logg.pop[i]
            feh.pop[i]
            teff.pop[i]
            
    return


        



 
