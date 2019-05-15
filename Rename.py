import os
from imutils import paths
import sys
import argparse

ap=argparse.ArgumentParser()
ap.add_argument("-i","--F",required=True,help="path to  directory ")
args = vars(ap.parse_args())
i=1
# F="/Users/keertika/Projects/DataPreProcessing/AadharWithFaceImages"
for g in os.listdir(args["F"]):
	# print(i)
	src=args["F"]+g
	print(str(i))
	os.rename(src,str(i))
	i+=1