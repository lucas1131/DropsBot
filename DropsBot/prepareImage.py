import os
import argparse

import cv2
import pytesseract

from PIL import Image

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="path to input image to be OCR'd")
ap.add_argument("-t", "--threshold", type=int, default=0, help="type of preprocessing to be done")
args = ap.parse_args()


img = cv2.imread(args.image)
grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

thresholdImg = cv2.threshold(grayImg, args.threshold, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]


def filenameAffix(file, preffix="", suffix=""):
	path = os.path.dirname(file)
	name, ext = os.path.basename(file).split(".")
	return os.path.join(path, f"{preffix}{name}{suffix}.{ext}")

cv2.imwrite(filenameAffix(args.image, suffix="_gray"), grayImg)
cv2.imwrite(filenameAffix(args.image, suffix="_threshold"), thresholdImg)
