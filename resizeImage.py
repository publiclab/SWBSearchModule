# This script is to resize a file and store in 'resized/' folder/
# Make sure the width and heights are properly defined as required
# Usage: python resizeImage.py image.jpg

import Image
import sys

image = sys.argv[1]

im = Image.open(image)

width = 5
height = 5

resized = im.resize((width, height), Image.ANTIALIAS)
# Can use 	NEAREST => for nearest neighbour
#		BILINEAR => for linear interpolation in 2x2
#		BICUBIC => for cubic spline interpolation in 4x4

new_folder = "resized/"
resized.save(new_folder + image)

