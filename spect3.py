from astropy.io import fits
import numpy as np
import copy
import pylab
import math

class Star(object):
# Define a star object, which is an (empty) dictionary of fields
	def __init__(self):
		self.fields = {}

class DataFile(object):
    def __init__(self, path):
        self.path = path
        datafile = fits.open(path)
        self.column_names = datafile[1].columns.names
  
 # What we should be doing       
     #   data = datafile[1].data # is a rec array
     #   
     #   mask = (data['targname'] == "your name")
     #   data[mask]
        
        
		# Datafile.stars is a list of star objects
        self.stars = [] 
        # Loop through the file, reading each row one at a time, 
        # until reaching the end of the file
        eof = False
        row = 0
#        while eof is False:
# Takes too long to read in. I have to set a limit or it takes like an hour to finish
        while eof == False and row < 10000 :
            try:
                stardata=datafile[1].data[row]
                if goodStar(stardata):
                    s=Star()
                    for column in self.column_names:
                        s.fields[column]=stardata.field(column)
                    self.stars.append(s)
                print row
                row = row+1
            except IndexError:
                eof = True
                print "eof"		 
        stypes=[]
        for i in xrange(0, len(self.stars)):
            stypes.append(self.stars[i].fields["SPECTYPE_HAMMER"])
        self.spectypes=unique_spectral_types(stypes)
      
      
 #   def get_star_obj (self,starname):
 #       
 #       mask = (data['targname'] == "your name")
 #       data[mask]
 #       # create star object
 #       # return
        
       
def goodStar(stardata, badValue=-9999):
    goodvalues=True
    if stardata["LOGG_ADOP"]==badValue or stardata["FEH_ADOP"]==badValue or stardata["TEFF_ADOP"]==badValue:
        goodvalues=False
    return goodvalues

def unique_spectral_types(stypes):
	return list(set(stypes))
 