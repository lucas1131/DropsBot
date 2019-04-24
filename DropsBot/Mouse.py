import time
import win32gui, win32api, win32con, ctypes

# TODO: mouse wheel rolling up and down event data and extra info

class Mouse:
	"""It simulates the mouse"""
	MOUSEEVENTF_MOVE = 0x0001 # mouse move 
	MOUSEEVENTF_LEFTDOWN = 0x0002 # left button down 
	MOUSEEVENTF_LEFTUP = 0x0004 # left button up 
	MOUSEEVENTF_RIGHTDOWN = 0x0008 # right button down 
	MOUSEEVENTF_RIGHTUP = 0x0010 # right button up 
	MOUSEEVENTF_MIDDLEDOWN = 0x0020 # middle button down 
	MOUSEEVENTF_MIDDLEUP = 0x0040 # middle button up 
	MOUSEEVENTF_WHEEL = 0x0800 # wheel button rolled 
	MOUSEEVENTF_ABSOLUTE = 0x8000 # absolute move 
	SM_CXSCREEN = 0
	SM_CYSCREEN = 1

	def _do_event(self, flags, x_pos, y_pos, data, extra_info):
		"""generate a mouse event"""
		x_calc = 65536 * x_pos / ctypes.windll.user32.GetSystemMetrics(self.SM_CXSCREEN) + 1
		y_calc = 65536 * y_pos / ctypes.windll.user32.GetSystemMetrics(self.SM_CYSCREEN) + 1
		x_calc = int(x_calc)
		y_calc = int(y_calc)

		return ctypes.windll.user32.mouse_event(flags, x_calc, y_calc, data, extra_info)

	def _get_button_value(self, button, button_up=False):
		"""convert the name of the button into the corresponding value"""
		buttons = 0
		if button.find("right") >= 0:
			buttons = self.MOUSEEVENTF_RIGHTDOWN
		if button.find("left") >= 0:
			buttons = buttons + self.MOUSEEVENTF_LEFTDOWN
		if button.find("middle") >= 0:
			buttons = buttons + self.MOUSEEVENTF_MIDDLEDOWN
		if button_up:
			buttons = buttons << 1
		return buttons

	def move_mouse(self, pos):
		"""move the mouse to the specified coordinates"""
		(x, y) = pos
		old_pos = self.get_position()
		x = x if (x != -1) else old_pos[0]
		y = y if (y != -1) else old_pos[1]	
		self._do_event(self.MOUSEEVENTF_MOVE + self.MOUSEEVENTF_ABSOLUTE, x, y, 0, 0)

	def press_button(self, pos=(-1, -1), button="left", button_up=False):
		"""push a button of the mouse"""
		self.move_mouse(pos)
		self._do_event(self.get_button_value(button, button_up), 0, 0, 0, 0)

	def click(self, pos=(-1, -1), button="left", delay=0.01):
		"""Click at the specified placed"""
		self.move_mouse(pos)
		self._do_event(self._get_button_value(button, False), 0, 0, 0, 0)
		time.sleep(delay)
		self._do_event(self._get_button_value(button, True), 0, 0, 0, 0)

	def double_click (self, pos=(-1, -1), button="left"):
		"""Double click at the specifed placed"""
		self.click(pos, button)
		self.click(pos, button)

	def get_position(self):
		"""get mouse position"""
		return win32api.GetCursorPos()
		