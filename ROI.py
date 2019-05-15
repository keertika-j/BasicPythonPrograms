import cv2 as cv
import numpy as np 
img=cv.imread('10205887_Aadhaar.jpg',0)
r=cv.selectROI(img)
crop=img[int(r[1]):int(r[1]+r[3]), int(r[0]):int(r[0]+r[2])]
cv.imshow("image",crop)
cv.waitKey(0)