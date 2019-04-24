"""
python .\DropsBot\prepareImage.py -i .\local\basic-info.png
python .\DropsBot\prepareImage.py -i .\local\inventory.png
python .\DropsBot\prepareImage.py -i .\local\inventory_hover.png
"""
import os
import argparse

import cv2
import numpy as np
import pytesseract

from PIL import Image




if __name__ == "__main__":

	ap = argparse.ArgumentParser()
	ap.add_argument("-i", "--image", required=True, help="Path to image")
	ap.add_argument("-t", "--threshold", type=int, default=0, help="Threshold level for Black and White output")
	ap.add_argument("--rescale", type=int, default=1, help="Reescale factor to apply to input image")
	ap.add_argument("--blur", action="store_true", help="Apply median blur to remove noise")
	ap.add_argument("--interactive", action="store_true", help="Interactive mode to test different parameters")
	args = ap.parse_args()

	def interactive(img):

		def options():
			print("Operations:")
			print("  rescale FACTOR")
			print("  grayscale")
			print("  threshold THRESH (BINARY|BINARY_INV|TRUNCATE|TOZERO|TOZERO_INV) [OTSU]")
			print("  blur RADIUS")
			print("  distance (c|l1|l2)")
			print("  invert")
			print("  erode [KERNEL]")
			print("  dilate [KERNEL]")
			print("  open [KERNEL]")
			print("  close [KERNEL]")
			print("  save PATH")
			print("  undo")
			print("  reset")
			print("  help")
			print("  exit")

		thresholds = {
			"binary": cv2.THRESH_BINARY,
			"binary_inv": cv2.THRESH_BINARY_INV,
			"trunc": cv2.THRESH_TRUNC,
			"tozero": cv2.THRESH_TOZERO,
			"tozer_inv": cv2.THRESH_TOZERO_INV,
			"otsu": cv2.THRESH_OTSU
		}

		distances = {
			"c": cv2.DIST_C,
			"l1": cv2.DIST_L1,
			"l2": cv2.DIST_L2,
		}

		defaultKernel = np.array([
			[1, 1, 1, 1, 1],
			[1, 1, 1, 1, 1],
			[1, 1, 1, 1, 1],
			[1, 1, 1, 1, 1],
			[1, 1, 1, 1, 1]
		], np.uint8)

		history = []
		imgHistory = []
		changed = False
		while(True):
			try:
				options()
				args = input("Operation > ").lower().split()
				history.append(" ".join(args))
				imgHistory.append(img)
				op = args[0]

				if op == "rescale":
					factor = float(args[1])
					img = cv2.resize(img, None, fx=factor, fy=factor, interpolation=cv2.INTER_CUBIC)
					changed = True
				
				elif op == "grayscale":
					img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
					changed = True
				
				elif op == "threshold":
					try:
						otsu = thresholds[args[3]]
					except IndexError:
						otsu = 0
					_, img = cv2.threshold(img, int(args[1]), 255, thresholds[args[2]] | otsu)
					changed = True

				elif op == "blur":
					img = cv2.medianBlur(img, int(args[1]))
					changed = True

				elif op == "distance":
					img = cv2.distanceTransform(img, distances[args[1]], 3)
					changed = True

				elif op == "invert":
					img = (255-img)
					changed = True
				
				elif op == "erode":
					try:
						kernel = np.array(eval(args[1]), np.uint8)
					except IndexError:
						kernel = defaultKernel
					img = cv2.erode(img, kernel)
					changed = True
				
				elif op == "dilate":
					try:
						kernel = np.array(eval(args[1]), np.uint8)
					except IndexError:
						kernel = defaultKernel
					img = cv2.dilate(img, kernel)
					changed = True

				elif op == "open":
					try:
						kernel = np.array(eval(args[1]), np.uint8)
					except IndexError:
						kernel = defaultKernel
					img = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
					changed = True
				
				elif op == "close":
					try:
						kernel = np.array(eval(args[1]), np.uint8)
					except IndexError:
						kernel = defaultKernel
					img = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
					changed = True

				elif op == "save":
					cv2.imwrite(args[1], img)
					changed = False
				
				elif op == "undo":
					img = imgHistory[-2]
					del imgHistory[-1] # Remove current image
					del imgHistory[-1] # Remove old image since it will be reinserted next loop
					del history[-1]
					changed = True

				elif op == "reset":
					history = []
					img = imgHistory[0]
					imgHistory = []
					changed = False

				elif op == "help":
					del history[-1]
					del imgHistory[-1]
					options()
					changed = False

				elif op == "exit":
					return history

				else:
					del history[-1]
					del imgHistory[-1]
					print("Invalid operation.")
					changed = False

				if changed:
					changed = False
					cv2.imshow("img", img)
					cv2.waitKey(0)
					cv2.destroyWindow("img")
			
			except (IndexError, KeyError) as e:
				print("Operation arguments invalid -", e)

			except Exception as e:
				print(e)


	img = cv2.imread(args.image)

	if args.interactive:
		print("History: ", "\n".join(interactive(img)))

	else:
		# Reescale to increase DPI
		img = cv2.resize(img, None, fx=args.rescale, fy=args.rescale, interpolation=cv2.INTER_CUBIC)

		# Greyscale
		grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

		if args.blur:
			grayImg = cv2.medianBlur(grayImg, 1)
			

		# Black and white
		# ret, thresholdImg = cv2.threshold(grayImg, args.threshold, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
		# ret, thresholdImg = cv2.threshold(grayImg, 127, 255, cv2.THRESH_BINARY)
		# ret, thresholdImg = cv2.threshold(grayImg, 127, 255, cv2.THRESH_BINARY_INV)
		ret, thresholdImg = cv2.threshold(grayImg, 127, 255, cv2.THRESH_TRUNC | cv2.THRESH_OTSU)

		# thresholdImg = cv2.morphologyEx(thresholdImg, cv2.MORPH_OPEN, np.ones((5, 5), np.uint8))
		thresholdImg = cv2.morphologyEx(thresholdImg, cv2.MORPH_CLOSE, np.array([
			[0, 1, 1, 1, 0],
			[1, 1, 1, 1, 1],
			[1, 1, 1, 1, 1],
			[1, 1, 1, 1, 1],
			[0, 1, 1, 1, 0]
		], np.uint8))

		# thresholdImg = cv2.morphologyEx(thresholdImg, cv2.MORPH_OPEN, np.array([
		# 	[1, 1, 1, 1],
		# 	[1, 1, 1, 1],
		# 	[1, 1, 1, 1],
		# 	[1, 1, 1, 1],
		# ], np.uint8))



		ret, thresholdImg = cv2.threshold(thresholdImg, 126, 255, cv2.THRESH_BINARY)
		# ret, thresholdImg = cv2.threshold(grayImg, 127, 255, cv2.THRESH_TOZERO)
		# ret, thresholdImg = cv2.threshold(grayImg, 127, 255, cv2.THRESH_TOZERO_INV)


		# thresholdImg = 255-thresholdImg
		thresholdImg = cv2.medianBlur(thresholdImg, 3)
		thresholdImg = cv2.GaussianBlur(thresholdImg, (5,5), 0)
		def filenameAffix(file, preffix="", suffix=""):
			path = os.path.dirname(file)
			name, ext = os.path.basename(file).split(".")
			return os.path.join(path, f"{preffix}{name}{suffix}.{ext}")

		cv2.imwrite(filenameAffix(args.image, suffix="_gray"), grayImg)
		cv2.imwrite(filenameAffix(args.image, suffix="_threshold"), thresholdImg)
