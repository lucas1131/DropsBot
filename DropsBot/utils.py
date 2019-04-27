import os
import pyautogui as gui
import pygetwindow

def getRagWindow():
	"""Get the first window containing 'rag' substring"""
	for w in pygetwindow.getAllWindows():
		if "rag" in w.title.lower():
			return w

def getAllRagWindows():
	"""Get all windows containing 'rag' substring"""
	return [ w for w in pygetwindow.getAllWindows() if "rag" in w.title.lower()]

def focusWindow(w):
	if w.isMinimized:
		w.restore()
	w.activate()

def extractChannel(img, channel):
	if os.sys.platform == "win32":
		channels = { "red": 2, "green": 1, "blue": 0 } # Windows is BGR
	else:
		channels = { "red": 0, "green": 1, "blue": 1 }

	return img[:, :, channels[channel]]
	