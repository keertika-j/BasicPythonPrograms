import os
import requests
import cv2

with open('1.txt') as fp:
	lines = fp.read().split("\n")
	i = 0
	for kk in lines:
		print(kk)
		fl2=kk.split("/")
		print(fl2[5])
		#filepath = "image" +  str(i) + ".jpg"
		filepath=str(fl2[5])+".jpg"
		with open(filepath, 'wb') as handle:
			response = requests.get(kk, stream=True)
			print(response)
			print(filepath)
			i = i + 1
			if not response.ok:
				print(response)
			for block in response.iter_content(1024):
				if not block:
					break
				handle.write(block)
