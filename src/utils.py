import pyautogui as gui
import pygetwindow

def get_rag_window():
	"""Get the first window containing 'rag' substring"""
	for w in pygetwindow.getAllWindows():
		if "rag" in w.title.lower():
			return w

def get_all_rag_windows():
	"""Get all windows containing 'rag' substring"""
	return [ w for w in pygetwindow.getAllWindows() if "rag" in w.title.lower()]

def focus_window(w):
	if w.isMinimized:
		w.restore()
	w.activate()
