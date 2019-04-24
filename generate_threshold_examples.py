import cv2
import numpy as np
import argparse
from matplotlib import pyplot as plt

ap = argparse.ArgumentParser()
ap.add_argument("image", type=str, help="Path to image to generate examples")
args = ap.parse_args()

img = cv2.imread(args.image, 0)
ret, thresh1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
ret, thresh2 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)

ret, thresh3 = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)


ret, thresh4 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
ret, thresh5 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)

titles = ['Original Image', 'BINARY', 'BINARY_INV', 'TRUNC', 'TOZERO', 'TOZERO_INV']
images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]

for i, title in enumerate(titles):
	print(i, title)
	plt.subplot(2, 3, i+1)
	print(images[i])
	plt.imshow(images[i], 'gray')
	plt.title(title)
	plt.xticks([]), plt.yticks([])

plt.show()
