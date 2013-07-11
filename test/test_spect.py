from astropy.io import fits
import numpy as np
import copy
import pylab
import math

from ..spect import DataFile

def test_clean():
	a = np.array([1,2,5,4,-9999,4,1,2])
	b = np.array([1,2,9,4,-9999,4,-9999,2])
	c = np.array([2,-9999,5,4,-2,8,1,2])
	d = np.array([1,5,5,4,-2,4,1,6])
	#print "clean([a,b,c,d])",  clean([a,b,c,d])
	assert values_eq(clean([a,b,c,d]), [[1,5,4,4,2], [1,9,4,4,2], [2,5,4,8,2], [1,5,4,4,6]])
