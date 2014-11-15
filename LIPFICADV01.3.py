from math import *
import pylab as pl
import numpy as np

x = np.linspace(-10., 10., 1000)
pl.plot(x, np.sin(x))
pl.show()