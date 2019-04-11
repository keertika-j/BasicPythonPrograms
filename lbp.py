import cv2
import os
from skimage.feature import local_binary_pattern
from imutils import paths
import scipy.misc
from PIL import Image
 
for image_path in paths.list_images('PrintFake'):
	im = cv2.imread(image_path)
	s1=os.path.basename(image_path)
	s=os.path.splitext(s1)[0]
	print(s)
	im_gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
	radius = 3
	no_points = 8 * radius
	lbp = local_binary_pattern(im_gray, no_points, radius, method='uniform')
	print("done")
	scipy.misc.imsave('PrintFake/'+s+'LBP.jpg', lbp)