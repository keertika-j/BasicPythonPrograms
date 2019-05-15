# USAGE
# python detect_blur.py --images images

# import the necessary packages
from imutils import paths
import argparse
import cv2
import csv
import time
import os

messi =time.time()
def variance_of_laplacian(image):
	# compute the Laplacian of the image and then return the focus
	# measure, which is simply the variance of the Laplacian
	return cv2.Laplacian(image, cv2.CV_64F).var()

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--images", required=True,
	help="path to input directory of images")
ap.add_argument("-t", "--threshold", type=float, default=250.0,
	help="focus measures that fall below this value will be considered 'blurry'")
args = vars(ap.parse_args())

# loop over the input images
f=open('Blurriness.csv','w')
with f:
	fnames=['ImageName','fake_crop_blurriness']
	writer=csv.DictWriter(f,fieldnames=fnames)
	for imagePath in paths.list_images(args["images"]):
		image = cv2.imread(imagePath)
		s=os.path.basename(imagePath)
		gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
		fm = variance_of_laplacian(gray)
		writer.writerow({'ImageName':s,'fake_crop_blurriness':fm})
		text = "Not Blurry"
		if fm < args["threshold"]:
			text = "Blurry"
cr7=time.time()
RT=cr7-messi
print(RT)
