# This script a rough file to test the matching measure
# Check the file location properly.
#

import scipy as sp
from scipy.misc import imread
from scipy.signal.signaltools import correlate2d as c2d
import warnings

folder = "resized/"

def get(image):
	data = imread(image)
	data = sp.inner(data, [299, 587, 114]) / 1000.0
	return (data - data.mean()) / data.std()

im1 = get(folder + 'capture1.jpg')
im2 = get(folder + 'capture2.jpg')

with warnings.catch_warnings():
	warnings.simplefilter("ignore")
	# This is to suppress a warning saying that imaginary part in complex numbers
	# is being discarded
	c11 = c2d(im1, im1, mode="same")
	c22 = c2d(im2, im2, mode="same")
	c12 = c2d(im1, im2, mode="same")
	c21 = c2d(im2, im1, mode="same")

print c11.max(), c22.max(), c12.max(), c21.max()
