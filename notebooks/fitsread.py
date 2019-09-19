# Import some standard libraries
from astropy.io import fits
import sys
import numpy as np
import matplotlib.pyplot as plt
import scipy as scipy
import scipy.optimize as opt
from scipy.stats import norm as norm

# Set up a filename
filename = 'A000001.fits'

# Read in the data.
# The 1 is because SDFits uses an extension on the normal data (which is in [0] and empty)
hdul = fits.open(filename)
fitsdata = hdul[1].data

# Make empty arrays to put the data in.
entries = len(fitsdata)      

vel  = np.zeros(entries)
freq = np.zeros(entries)
spec = np.zeros(entries)
base = np.zeros(entries)
weight = np.zeros(entries)

# Fill the arrays
for i in range(len(fitsdata)):
    vel[i] = fitsdata[i][0]
    freq[i] = fitsdata[i][1]
    spec[i] = fitsdata[i][2]
    base[i] = fitsdata[i][3]
    weight[i] = fitsdata[i][4]

# Make a basic plot and show it
plt.plot(vel, spec)
plt.xlabel("Velocity (km/s)")
plt.ylabel("Flux (mJy)")
plt.show()

# Print out the FITS header
hdul[1].header
