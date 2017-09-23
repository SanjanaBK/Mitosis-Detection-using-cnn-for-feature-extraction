import cv2
import os
def smooth(src):
	dst = cv2.medianBlur(src,7)
	return dst

def process(path,final_path):
	for image in os.listdir(path):
		print image
		if os.path.isfile(path+image):
			src = cv2.imread(path+image,1)
			dst = smooth(src)
			print dst
			cv2.imwrite(final_path+image,dst)

process("../A06/frames/x40/","../A06/frames/Preprocess/")
				
	
