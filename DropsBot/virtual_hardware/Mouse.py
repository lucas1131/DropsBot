import time

import win32api, win32gui, win32con
import ctypes
user32 = ctypes.windll.user32 # load user32 dll

# TODO: mouse wheel rolling up and down event data and extra info

def microsleep(t):
	''''Delays the execution until initial time reaches target time.
	This function has 150 nanoseconds of precision, with 1.3 ns standard deviation.
	Args:
		t (int): Target time, in seconds.
	'''
	t1 = time.clock()
	t0 = 0
	while t0 < t:
		t2 = time.clock()
		t0 += t2 - t1
		t1 = t2

class Mouse:
	"""It simulates the mouse"""

	# These are mouse events and *NOT* mouse key codes!
	MOUSE_EVENTF_MOVE       = 0x0001   # Mouse move flag - Must be set for MOUSE_EVENTF_ABSOLUTE movement to work
	MOUSE_EVENTF_LEFTDOWN   = 0x0002   # Left button down 
	MOUSE_EVENTF_LEFTUP     = 0x0004   # Left button up 
	MOUSE_EVENTF_RIGHTDOWN  = 0x0008   # Right button down 
	MOUSE_EVENTF_RIGHTUP    = 0x0010   # Right button up 
	MOUSE_EVENTF_MIDDLEDOWN = 0x0020   # Middle button down 
	MOUSE_EVENTF_MIDDLEUP   = 0x0040   # Middle button up 
	MOUSE_EVENTF_WHEEL      = 0x0800   # Wheel button rolled - The movement amount must be speficied in extra data argument
	MOUSE_EVENTF_XDOWN      = 0x0080   # X button down - dont know what those X buttons are
	MOUSE_EVENTF_XUP        = 0x0100   # X button up - dont know what those X buttons are
	MOUSE_EVENTF_ABSOLUTE   = 0x8000   # Absolute move 
	MOUSE_EVENTF_HWHEEL     = 0x01000  # Wheel button tilted - dont know

	# NOTE: You cannot specify both MOUSE_EVENTF_WHEEL and either MOUSE_EVENTF_XDOWN or 
	# MOUSE_EVENTF_XUP simultaneously in the dwFlags parameter, because they both 
	# require use of the dwData field.

	# ???
	SM_CXSCREEN = 0 
	SM_CYSCREEN = 1

	def _do_event(self, flags, x_pos, y_pos, data, extra_info):
		"""generate a mouse event"""
		x_calc = 65536 * x_pos / user32.GetSystemMetrics(self.SM_CXSCREEN) + 1
		y_calc = 65536 * y_pos / user32.GetSystemMetrics(self.SM_CYSCREEN) + 1
		x_calc = int(x_calc)
		y_calc = int(y_calc)

		return user32.mouse_event(flags, x_calc, y_calc, data, extra_info)

	def _get_button_value(self, button, button_up=False):
		"""convert the name of the button into the corresponding value"""
		buttons = 0
		if button.find("right") >= 0:
			buttons = self.MOUSE_EVENTF_RIGHTDOWN
		if button.find("left") >= 0:
			buttons = buttons + self.MOUSE_EVENTF_LEFTDOWN
		if button.find("middle") >= 0:
			buttons = buttons + self.MOUSE_EVENTF_MIDDLEDOWN
		if button_up:
			buttons = buttons << 1
		return buttons

	def move_mouse(self, pos):
		"""move the mouse to the specified coordinates"""
		(x, y) = pos
		old_pos = self.get_position()
		x = x if (x != -1) else old_pos[0]
		y = y if (y != -1) else old_pos[1]	
		self._do_event(self.MOUSE_EVENTF_MOVE + self.MOUSE_EVENTF_ABSOLUTE, x, y, 0, 0)

	def press_button(self, pos=(-1, -1), button="left", button_up=False):
		"""push a button of the mouse"""
		self.move_mouse(pos)
		self._do_event(self.get_button_value(button, button_up), 0, 0, 0, 0)

	def click(self, pos=(-1, -1), button="left", delay=0.05):
		"""Click at the specified placed"""
		self.move_mouse(pos)
		self._do_event(self._get_button_value(button, False), 0, 0, 0, 0)
		microsleep(delay)
		self._do_event(self._get_button_value(button, True), 0, 0, 0, 0)

	def double_click (self, pos=(-1, -1), button="left"):
		"""Double click at the specifed placed"""
		self.click(pos, button)
		microsleep(0.001)
		self.click(pos, button)

	def get_position(self):
		"""get mouse position"""
		return win32api.GetCursorPos()
		