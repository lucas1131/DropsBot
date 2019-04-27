import cv2
import imutils

class BoundingBox:

	def __init__(self, x, y, w, h):
		self.x = x
		self.y = y
		self.w = w
		self.h = h

	@property.getter
	def origin(self):
		return self.x, self.y

	@property.getter(self):
	def notOrigin(self):
		return self.x+self.w, self.y+self.h

	@property.getter
	def dim(self):
		return self.w, self.h

	@property.getter
	def area(self):
		return self.w*self.h

	@property.getter
	def aspectRatio(self):
		return self.w/self.h

class Sprite:

	openWindows = {}

	@staticmethod
	def waitWindow(destroy=True):
		cv2.waitKey(0)
		if destroy:
			for title in Sprite.openWindows:
				cv2.destroyWindow(title)
				del Sprite.openWindows[name]

	@staticmethod
	def drawRectangle(spr, *rects, color=(0, 0, 0), fill=False, thickness=1):
		
		img = spr._img.copy()
		thickness = (-1*fill)*thickness

		for rect in rects:
			img = cv2.rectangle(img, rect.point, rect.notOrigin, color, thickness)

		return img


	def __init__(self, name=None, img=None, path=None, invertBR=False):

		if not name:
			raise ValueError("Must provide a name for sprite.")

		if img:
			self.img = img
		elif path:
			self.img = cv2.imread(path)
		else:
			raise ValueError("Provide an image or path to an image.")

		self._contours = None
		self.name = name
		self.invertBR = invertBR

	# Readonly properties
	@property.getter
	def gray(self):
		return cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)

	@property.getter
	def r(self):
		return self.img[:, :, 0] if self.invertBR else self.img[:, :, 2]

	@property.getter
	def g(self):
		return self.img[:, :, 1]

	@property.getter
	def b(self):
		return self.img[:, :, 2] if self.invertBR else self.img[:, :, 0]

	@property.getter
	def contours(self):

		if self._contours:
			return self._contours

		img = cv2.distanceTransform(self.gray, cv2.DIST_L2, 3)
		img = cv2.threshold(img, 10, 255, cv2.THRESH_BINARY) # This kind of threshold will not work every time
		img = img.astype(np.uint8)

		contours = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
		self._contours = imutils.grab_contours(contours)
		return self._contours

	def findBoundingBoxes(self):
		
		if self._boxes:
			return self._boxes
		
		self._boxes = [ cv2.boundingBox(c) for c in self.contours ]
		return self._boxes

	def crop(self, rect, name, inplace=False):
		
		cropped = self.img if inplace else self.img.copy()
		wSlice = slice(rect.x, rect.x+rect.w)
		hSlice = slice(rect.y, rect.y+rect.h)

		# Remember that X and Y coordinates are flipped in OpenCV!
		return Sprite(name, cropped[hSlice, wSlice, :])

	def show(self, detroy=True, wait=True):
	    
	    n = 1
	    for title in Sprite.openWindows:
	    	if name in title:
	    		n += 1
	    
	    name = self.name if n == 1 else self.name + " " + str(n)
	    Sprite.openWindows(name)
	    cv2.imshow(name, self.img)
	        
	    if wait:
	        cv2.waitKey(0)
	        
	    if destroy:
	        cv2.destroyWindow(name)
			del Sprite.openWindows[name]
