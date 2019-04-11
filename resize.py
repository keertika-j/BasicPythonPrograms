import os
import argparse
import dlib
import cv2
import imutils

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default="",
	help="path to input image file")
args = vars(ap.parse_args())


images = args["image"]	


for fl in os.listdir(images):
	#print(fl)
	if fl == ".DS_Store" or fl == "_DS_Store":
		#print(fl)
		print("stupid files")

	else:
		images2 = os.path.join(images,fl)	
		frame = cv2.imread(images2)
		# detector = dlib.get_frontal_face_detector()
		# try:			
		fl2 = fl.split(".")[0]
		# cv2.imwrite( "cropped" + ".jpg",face)
		cv_interpolation = cv2.INTER_LANCZOS4
		# cropped = cv2.resize(frame,(224,224))
		cropped = cv2.resize(frame, dsize=(300, 300), interpolation=cv_interpolation)
		# cv2.imwrite( str(fl) + ".jpg",cropped)
		cv2.imwrite( str(images) + "/" + str(fl2) + ".jpg",cropped)

				# ratio = height*width/((c-a)*(d-b))
				# print(ratio)

				# a1 = int(a*width/450)
				# b1 = int(b*height/height2)
				# c1 = int(c*width/450)
				# d1 = int(d*height/height2)

				# face2 = frame[b1:d1 , a1:c1]
				# cv2.imwrite( "cropped1" + ".jpg",face2)
		# except:
		# 	print("gip")
		# 	continue




			

		
