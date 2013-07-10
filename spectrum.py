# class DataFile(object):
#     def openfile(self,filepath=None):
#         from astropy.io import fits
#         self.datafile = fits.open(self.filepath, memmap=True)

class Star(object):


def openfile(filename):
    
    from astropy.io import fits
    data = fits.open("filename")

    return "The fits file is opened as 'data'"




 
