import numpy as np
import copy
import pylab
import math
import matplotlib.pyplot as plt

def plothist(feh,rv,dist):
    fig,axes = pylab.subplots(1, 3)
    axes[0].hist(feh, label="[Fe/H]", facecolor="red", alpha=0.5, histtype='stepfilled', bins=20)
    axes[1].hist(rv, label="RV", facecolor="red", alpha=0.5, histtype='stepfilled')
    axes[2].hist(dist, label="Dist", facecolor="red", alpha=0.5, histtype='stepfilled')
    pylab.show()
