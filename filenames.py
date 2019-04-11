import os
import csv

folder_path="/home/arun/Desktop/data/crop_200"

file=open("file_names.txt", "a")

folder=os.listdir(folder_path)

for filenames in folder:
	file.write(filenames+'\n')

file.close()