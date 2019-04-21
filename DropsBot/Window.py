from pygetwindow import Window as PyWindow

class Window(PyWindow):
	def focus(self):
		if self.isMinimized:
			self.restore()
		self.activate()


