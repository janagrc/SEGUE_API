
from astropy.io import fits

class Star(object):
    def __init__(self):
        self.fields = {}
    

class Datafile(object):
    def __init__(self, filepath=None):
        hduList = fits.open(filepath)
        
        # get list of column names
        column_names = hduList[1].columns.names
        
        self.stars = []
        # for each row in the table:
            s = Star()
            # for each column in column_names:
                s.fields[column] = ...
    

d= datafile
d.stars
d = Datafile()
d.fields["LOGG_ADOP"]


d.logg

"LOGG_ADOP", "FEH_ADOP", "TEFF_ADOP", "SPECTYPE_HAMMER"