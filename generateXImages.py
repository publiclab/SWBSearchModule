# This script generates X copies of image N
# X = > sys.argv[1] and N => sys.argv[2]
# Usage: python generateXImages.py 5000 capture.jpg

import Image
import sys

number = int(sys.argv[1])

image = sys.argv[2]
name = image.split('.')[0]

new_folder = "generated/" 
ext = ".jpg"
im = Image.open(image)

for i in range(number):
	im.save(new_folder + name + str(i) + ext)
