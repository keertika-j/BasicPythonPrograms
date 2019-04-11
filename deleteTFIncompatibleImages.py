import os
from imutils import paths
import sys
import tensorflow as tf

F="F:/Liveness/FR+FlMaintainance/Oregon"
sess=tf.Session()
for g in paths.list_images(F):
	try:
		# print(g)
		input_name = "file_reader"
		output_name = "normalized"
		file_reader = tf.read_file(g, input_name)
		k=tf.image.decode_jpeg(file_reader, channels=3, name="jpeg_reader")
		image_float = tf.image.convert_image_dtype(k, dtype=tf.float32)
		img, img_float = sess.run([k, image_float])
		# print(img)
		print(k)
	except:
		os.remove(g)
		print(g+"removed")
		continue