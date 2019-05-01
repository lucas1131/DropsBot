import os
import argparse

import cv2
import numpy as np

ap = argparse.ArgumentParser()
ap.add_argument("files", nargs="+", help="Input files")
ap.add_argument("-d", "--directory", default=".", help="Output directory")
ap.add_argument("--minimum-area", type=int, default=2500, help="Minimum area to consider for a valid sprite box. Defaults to 2500")
ap.add_argument("--kernel-size", type=int, default=5, help="Kernel size to use (will always be a square kernel). Defaults to 5")
ap.add_argument("--bounding-box-padding", type=int, dest="padding", default=0, help="Number of pixels to add as padding when calculating bounding boxes. Defaults to 0")
ap.add_argument("--outlier-cutoff", type=float, dest="cutoff", default=3.5, help="Outlier cutoff value for Median Absolute Deviation. Defaults to 3.5")
args = ap.parse_args()

def removeFileExt(file):
	
	# This file has no extension!
	if "." not in os.path.basename(file): 
		return file 

	# Keep relative paths if they were given
	if file.startswith(".."):
		s = ".." # Parent directory
	elif file[0] == ".":
		s = "." # Current directory
	else:
		s = "" # No relative path

	return s.join((file.split(".")[:-1]))

def getFileParts(file):

	ext = file.split(".")[-1]
	filename = os.path.basename(file)[:-(len(ext)+1)] # Remove extension
	path = os.path.dirname(file)
	return path, filename, ext

def createDirectory(path):
	path = removeFileExt(path)
	os.makedirs(path, exist_ok=True)
	return path

def medianAbsoluteDeviation(arr, median=None):
			
	if median is None:
		median = arr[int(arr.size/2)]

	mad = np.zeros(arr.size, np.int32)
	for i, item in enumerate(arr):
		mad[i] = abs(median-item)
	mad.sort()
	return mad[int(mad.size/2)]

def addPadding(x, y, w, h, padding):
	
	# Calculate width and height first for correct padding since they depend on
	# X and Y values. Also, if they overflow everything still works, so no need
	# to do any checks here.
	w += padding
	h += padding

	# But dont let X nor Y be negative
	x -= padding
	if x < 0: 
		x = 0

	y -= padding
	if y < 0: 
		y = 0

	return x, y, w, h


def imshow(img, title="img"):
	cv2.imshow("img", img)
	cv2.waitKey(0)
	cv2.destroyWindow(title)

if __name__ == "__main__":

	minArea = args.minimum_area
	kerSize = args.kernel_size
	padding = args.padding
	cutoff  = args.cutoff

	os.makedirs("trash", exist_ok=True)

	for file in args.files:

		print("\nProcessing file", file)
		directory, filename, ext = getFileParts(file)
		createDirectory(os.path.join(args.directory, filename))
		img = cv2.imread(file)
		
		# Convert to grayscale to process image
		gimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

		# Apply threshold but inverse so we get blobs of white
		# Maybe we need to adjust to parametize threshold values?
		_, timg = cv2.threshold(gimg, 127, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)

		# Apply closing operation to remove separation lines and text noise
		closedImg = cv2.morphologyEx(timg, cv2.MORPH_CLOSE, np.ones((kerSize, kerSize)))

		# Get blobs contours
		contours, _ = cv2.findContours(closedImg, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

		# Copy original image to apply contours
		contourImg = img.copy()

		# Debug
		# cv2.drawContours(contourImg, contours, -1, (0, 0, 255), 5)

		bboxes = []
		areas = []
		for c in contours:
			
			# Get bounding rect of this contour
			box = cv2.boundingRect(c)
			x, y, w, h = box
			x, y, w, h = addPadding(x, y, w, h, padding)
			# Calculate sprite area to validade this box
			area = w*h
			
			bboxes.append((x, y, w, h)) # Add bbox with padding
			areas.append(area)

		areas = np.array(areas, np.int32)
		areas.sort()
		median = areas[int(areas.size/2)]

		# Here we use the Median Absolute Deviation as an outlier detection method
		mad = medianAbsoluteDeviation(areas, median)

		i = 0
		ti = 0
		for x, y, w, h in bboxes:
			
			area = w*h
			pointWeight = abs(area-median)/mad
			
			# I tried checking sprites aspect ratio but they are way too
			# inconsistent, we would probably have a lot of false positives,
			# its not worth it.
			#
			# This 3 is a statistical known value, go research yourself
			if pointWeight < cutoff or area < minArea: 
				# This is not a valid sprite
				sprite = img[y:(y+h), x:(x+w), :]
				d = createDirectory(os.path.join("trash/", filename))
				cv2.imwrite(d+"/{file}_{ti}.png".format(file=filename, ti=ti), sprite)
				ti += 1
				# imshow(sprite, "INVALID IMAGE")
				continue

			# Crop original image region containing this single sprite
			# REMEMBER that opencv Y and X are reversed!! The last one is depth
			sprite = img[y:(y+h), x:(x+w), :]
			# imshow(sprite, "VALID IMAGE")

			# Save file - note that 'args.directory' is output dir when 
			# 'directory' is the path component of this file name
			# filename appears two times to create a directory with the same
			# base name as this sprite, later, for each individual sprite, we 
			# add a suffix and file extension
			path = os.path.join(args.directory, filename, filename)
			path = "{path}_{i}.{ext}".format(path=path, i=i, ext=ext)
			print("  Saving sprite as", path)
			cv2.imwrite(path, sprite)
			i += 1
