# This script is for searching all the resized images for similarity
# This performs a one-one comparision and returns the similarity metrics
# Usage: python searchAll.py new_image.jpg

import scipy as sp
from scipy.misc import imread
from scipy.signal.signaltools import correlate2d as c2d
import warnings
import glob
import os
import sys
import time

folder = "resized/"
images = {}
scores = {}
os.chdir(folder)

def get(image):
	data = imread(image)
	data = sp.inner(data, [299, 587, 114]) / 1000.0
	return (data - data.mean()) / data.std()
start = time.clock()
search = get(sys.argv[1])

for image in glob.glob("*.jpg"):
	images[image] = get(image)

with warnings.catch_warnings():
	warnings.simplefilter("ignore")
	# This is to ignore a warning saying that imaginary part in complex numbers
	# is being discarded
	for image in images:
		scores[image] = c2d(search, images[image], mode = "same").max()
stop = time.clock()

print "done"
for score in scores:
	print score, scores[score]

print stop-start
