# This script resizes all the .jpg images in the 'generated/' folder
# The resized images will be stored in 'resized/' folder
# Usage: python resizeAll.py

import Image
import glob
import os

os.chdir("generated")
for image in glob.glob("*.jpg"):
	im = Image.open(image)

	width = 5
	height = 5

	resized = im.resize((width, height), Image.ANTIALIAS)
	# Can use 	NEAREST => for nearest neighbour
	#		BILINEAR => for linear interpolation in 2x2
	#		BICUBIC => for cubic spline interpolation in 4x4

	new_folder = "../resized/"
	resized.save(new_folder + image)

