import numpy as np
import copy
import pylab
import math
import matplotlib.pyplot as plt
#How do you reimport after making changes?
import spect3
reload(spect3)
from spect3 import DataFile


x = DataFile("../data/ssppOut-dr9.fits")
# Print out unique spectral types. Note: I had to loop through stars to get this...
print x.spectypes

# Either I'm missing something or I really don't see the benefit of putting each star
# in its own object. Now I have to loop through stars to get out a single column
feh=[]
rv=[]
dist=[]
for i in xrange(0, len(x.stars)):
    feh.append(x.stars[i].fields["FEH_ADOP"])
    rv.append(x.stars[i].fields["RV_ADOP"])
    dist.append(x.stars[i].fields["DIST_ADOP"])
    
# I can't plot anything!
def plothist(feh,rv,dist):
    fig,axes = pylab.subplots(1, 3)
    axes[0].hist(feh, label="[Fe/H]", facecolor="red", alpha=0.5, histtype='stepfilled', bins=20)
    axes[1].hist(rv, label="RV", facecolor="red", alpha=0.5, histtype='stepfilled')
    axes[2].hist(dist, label="Dist", facecolor="red", alpha=0.5, histtype='stepfilled')
    pylab.show()

plothist(feh,rv,dist)

# Need Function to accept galactic longitude, latitude and heliocentric distance and convert to Galactic X, Y, Z
# plothist(feh,rv,galdist)
# Add column to stars that has Galactocentric distance?

# Select stars where [Fe/H]<-1
# plothist...