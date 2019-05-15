import os
from imutils import paths
import sys
import argparse
import dlib
import cv2

ap=argparse.ArgumentParser()
ap.add_argument("-i","--F",required=True,help="path to  directory ")
args = vars(ap.parse_args())
a=os.listdir(args["F"])
for g in a:
	print("g",g)
	dir_src=os.path.join(args["F"],g)
	print(dir_src)
	img_name=os.listdir(dir_src)
	for x in img_name:

		fin_img=os.path.join(dir_src,x)
		fin_img2=fin_img.split(".")[0]
		image=cv2.imread(fin_img)
		face_detector = dlib.get_frontal_face_detector()
		try:
			if len(image)>0:
				gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
				detected_faces = face_detector(gray, 0)
				height = image.shape[0]
				width = image.shape[1]
				height2 = image.shape[0]
				face_rect = detected_faces[0]
				a = face_rect.left()
				b = face_rect.top()
				c = face_rect.right()
				d = face_rect.bottom()
				if(face_rect.left() < 0):
					a = 0
				if(face_rect.top() < 0):
					b = 0
				if(face_rect.right() > width):
					c = width-1
				if(face_rect.bottom() > height):
					d = height-1
				face = image[b:d , a:c]
				cv2.imwrite(fin_img2+"cropped.jpg" ,face)
				print("done")
		except:
			# os.remove(image)
			print("not cropped so deleted",fin_img)
			continue

		
	    