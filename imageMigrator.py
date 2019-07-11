from PIL import Image
import sys
import os
import re

input_path = './pokemon/'
output_path = './data/pokemon/'
files = os.listdir(input_path)
count = 1

for file in files:
		print(file)
		if file[-4:] == ".png":
				input_im = Image.open(input_path + str(file[0:3]) + ".png")
				rgb_im = input_im.convert('RGB')
				rgb_im.save(output_path + str(file[0:3]) + ".jpg",quality=30)
				count = count + 1
				print("transaction finished" + str(count))
