import numpy as np
import copy
import pylab
import math
import matplotlib.pyplot as plt
import plot_commands_stars as pcs
reload(pcs)

#How do you reimport after making changes?
import star
reload(star)
from star import DataFile
x = DataFile("../data/small_ssppOut-dr9.fits")
print len(x.gooddata)


pcs.plothist(x.gooddata["FEH_ADOP"],x.gooddata["RV_ADOP"],x.gooddata["DIST_ADOP"])