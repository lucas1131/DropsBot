import os
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("files", nargs="+", help="Input files")
ap.add_argument("-d", "--directory", default=".", help="Output directory")
args = ap.parse_args()


gimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, timg = cv2.threshold(gimg, 127, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
closedImg = cv2.morphologyEx(timg, cv2.MORPH_CLOSE, np.ones((5, 5)))
contours, _ = cv2.findContours(closedImg, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

for file in args.files:

	filename = os.path.basename(file)
	crop()
	save
