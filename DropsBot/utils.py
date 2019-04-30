import os
import time
import logging

import pyautogui as gui
import pygetwindow

logger = logging.getLogger(__name__)

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
	
def microsleep(t):
	''''Delays the execution until initial time reaches target time.
	This function has 150 nanoseconds of precision, with 1.3 ns standard deviation.
	Args:
		t (int): Target time, in seconds.
	'''
	t0 = 0
	t1 = time.clock()
	while t0 < t:
		t2 = time.clock()
		t0 += t2 - t1
		t1 = t2