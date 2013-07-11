from astropy.io import fits
import numpy as np
import copy
import pylab
import math

<<<<<<< HEAD
class Star(object):
	def__init__(self):
		self.fields = {}
	
class DataFile(object):
	def __init__(self, path):
		self.path = path
		datafile = fits.open(path)
		column_names = datafile[1].columns.names
		self.stars = [] #list of star objects, each with a dict of fields
		#for row in xrange(0,datafile[0].header['naxis2']
		for row in xrange(0,len(datafile[1].data.field('TEFF_ADOP')+1):
			stardata=datafile[1].data[row]
			s=Star()
			for column in column_names:
				s.fields[column]=stardata.field(column)
					
		# for row in rows
		# read in row
		# check it's good if isgood(star) then 
=======

class DataFile:
	def __init__(self, path, variableList=["LOGG_ADOP", "FEH_ADOP", "TEFF_ADOP", "SPECTYPE_HAMMER"]):
	#Input a check for the path?
		self.path = path
		datafile = fits.open(path)
		self.logg = np.array(datafile[1].data.field("LOGG_ADOP"))
		self.feh = np.array(datafile[1].data.field("FEH_ADOP"))
		self.teff = np.array(datafile[1].data.field("TEFF_ADOP"))
		self.spectypehammer = np.array(datafile[1].data.field("SPECTYPE_HAMMER"))
		self.clean()
>>>>>>> 0b7988c45d9a6eea46f5bb6c221720785194482d
		
		# if good, add star object to stars
			if isgood(s):
				self.stars.append(s)
	def isgood(self):
		self= True
		#if anything is bad set to false
	
	def clean(self):
<<<<<<< HEAD
		self.logg, self.feh, self.teff, self.spectypehammer = cleanData([self.logg, self.feh, self.teff, self.spectypehammer])
		#cleanedDataList = cleanData(self.dataDict.values())			
=======
		self.logg, self.feh, self.teff, self.spectypehammer = cleandata([self.logg, self.feh, self.teff, self.spectypehammer])
>>>>>>> 0b7988c45d9a6eea46f5bb6c221720785194482d
		
	def unique_spectral_types(self):
		return list(set(self.spectypehammer))
		
	def plothist(self):
		fig,axes = pylab.subplots(1, 3)
		axes[0].hist(self.feh, label="[Fe/H]", facecolor="red", alpha=0.5, histtype='stepfilled', bins=20)
		axes[1].hist(self.feh, label="[Fe/H]", facecolor="red", alpha=0.5, histtype='stepfilled')
		axes[2].hist(self.feh, label="[Fe/H]", facecolor="red", alpha=0.5, histtype='stepfilled')
		pylab.show()
	

def cleandata(arrayList, badValue=-9999):
	goodIndices = []
	for i in xrange(len(arrayList[0])):
		foundBadValue = False
		for array in arrayList:
			assert len(arrayList[0]) == len(array)
			if array[i] == badValue: foundBadValue = True
		if not foundBadValue: goodIndices.append(i)
	goodIndices = list(set(goodIndices))
	goodIndices.sort()
	#print "goodIndices", goodIndices
	
	for j in xrange(len(arrayList)):
		arrayList[j] = arrayList[j][goodIndices]
	
	return arrayList

def values_eq(x,y):
	for i in xrange(len(x)):
		for j in xrange(len(x[0])):
			if x[i][j] != y[i][j]: return False
	return True
		
def test_clean():
	a = np.array([1,2,5,4,-9999,4,1,2])
	b = np.array([1,2,9,4,-9999,4,-9999,2])
	c = np.array([2,-9999,5,4,-2,8,1,2])
	d = np.array([1,5,5,4,-2,4,1,6])
	#print "clean([a,b,c,d])",  clean([a,b,c,d])
	assert values_eq(clean([a,b,c,d]), [[1,5,4,4,2], [1,9,4,4,2], [2,5,4,8,2], [1,5,4,4,6]])
		

if __name__ == "__main__":
	df = DataFile("/Users/janagrc/desktop/ssppOut-dr9.fits")
	print "Spectral types: ", df.unique_spectral_types()
	df.plothist()
