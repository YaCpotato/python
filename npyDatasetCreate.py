import os
import cv2
import numpy as np

if __name__ =='__main__':
	dirPath = '/Users/shoichi/Desktop/python/pokemonProject/pokemon'
	fileList = os.listdir(dirPath)
	
		
	for file in fileList:
		filename = dirPath + '/' +file
		a=cv2.imread(filename)
		np.save('pokemon.npy',a)
