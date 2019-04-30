import time
import ctypes
user32 = ctypes.windll.user32

from DropsBot.virtual_hardware.KeyCodes import KeyCodes
from DropsBot.utils import microsleep

class Keyboard:
	

	# If specified, the scan code was preceded by a prefix byte having the value
	# 0xE0 (224).
	KEY_EVENTF_EXTENDEDKEY = 0x0001

	# If specified, the key is being released. If not specified, the key is
	# being depressed.
	KEY_EVENTF_KEYUP = 0x0002

	# Leave keys as a dict for easier conditionals
	keyCodes = {
		"A" : KeyCodes.A,
		"B" : KeyCodes.B,
		"C" : KeyCodes.C,
		"D" : KeyCodes.D,
		"E" : KeyCodes.E,
		"F" : KeyCodes.F,
		"G" : KeyCodes.G,
		"H" : KeyCodes.H,
		"I" : KeyCodes.I,
		"J" : KeyCodes.J,
		"K" : KeyCodes.K,
		"L" : KeyCodes.L,
		"M" : KeyCodes.M,
		"N" : KeyCodes.N,
		"O" : KeyCodes.O,
		"P" : KeyCodes.P,
		"Q" : KeyCodes.Q,
		"R" : KeyCodes.R,
		"S" : KeyCodes.S,
		"T" : KeyCodes.T,
		"U" : KeyCodes.U,
		"V" : KeyCodes.V,
		"W" : KeyCodes.W,
		"X" : KeyCodes.X,
		"Y" : KeyCodes.Y,
		"Z" : KeyCodes.Z,

		"SPACE" : KeyCodes.SPACE,
		" " : KeyCodes.SPACE,
		
		"ZERO" : KeyCodes.ZERO,
		"ONE" : KeyCodes.ONE,
		"TWO" : KeyCodes.TWO,
		"THREE" : KeyCodes.THREE,
		"FOUR" : KeyCodes.FOUR,
		"FIVE" : KeyCodes.FIVE,
		"SIX" : KeyCodes.SIX,
		"SEVEN" : KeyCodes.SEVEN,
		"EIGHT" : KeyCodes.EIGHT,
		"NINE" : KeyCodes.NINE,
		# Convenience numbers
		"0" : KeyCodes.ZERO,
		"1" : KeyCodes.ONE,
		"2" : KeyCodes.TWO,
		"3" : KeyCodes.THREE,
		"4" : KeyCodes.FOUR,
		"5" : KeyCodes.FIVE,
		"6" : KeyCodes.SIX,
		"7" : KeyCodes.SEVEN,
		"8" : KeyCodes.EIGHT,
		"9" : KeyCodes.NINE,

		"NUM0" : KeyCodes.NUMPAD0,
		"NUM1" : KeyCodes.NUMPAD1,
		"NUM2" : KeyCodes.NUMPAD2,
		"NUM3" : KeyCodes.NUMPAD3,
		"NUM4" : KeyCodes.NUMPAD4,
		"NUM5" : KeyCodes.NUMPAD5,
		"NUM6" : KeyCodes.NUMPAD6,
		"NUM7" : KeyCodes.NUMPAD7,
		"NUM8" : KeyCodes.NUMPAD8,
		"NUM9" : KeyCodes.NUMPAD9,

		"F1" : KeyCodes.F1,
		"F2" : KeyCodes.F2,
		"F3" : KeyCodes.F3,
		"F4" : KeyCodes.F4,
		"F5" : KeyCodes.F5,
		"F6" : KeyCodes.F6,
		"F7" : KeyCodes.F7,
		"F8" : KeyCodes.F8,
		"F9" : KeyCodes.F9,
		"F10" : KeyCodes.F10,
		"F11" : KeyCodes.F11,
		"F12" : KeyCodes.F12,

		"SCROLL_LOCK" : KeyCodes.SCROLL_LOCK,
		"CAPSLOCK" : KeyCodes.CAPSLOCK,
		"NUMLOCK" : KeyCodes.NUMLOCK,

		"ESC" : KeyCodes.ESCAPE,
		"TAB" : KeyCodes.TAB,
		# "FN" : KeyCodes.FN,

		# These are probably all extended keys - need to check them all
		"PRINT_SCREEN" : KeyCodes.PRINTSCREEN,
		"PAUSE_BREAK" : KeyCodes.PAUSE,
		"BACKSPACE" : KeyCodes.BACKSPACE,
		"ENTER" : KeyCodes.RETURN,
		"DELETE" : KeyCodes.DELETE,
		"HOME" : KeyCodes.HOME,
		"END" : KeyCodes.END,
		"PAGE_UP" : KeyCodes.PAGEUP,
		"PAGE_DOWN" : KeyCodes.PAGEDOWN,
		"INSERT" : KeyCodes.INSERT,

		# These are probably all extended keys - need to check them all
		"LEFT_CTRL" : KeyCodes.LEFTCONTROL,
		"RIGHT_CTRL" : KeyCodes.RIGHTCONTROL,
		"ANY_CTRL" : KeyCodes.CONTROL,

		# These are probably all extended keys - need to check them all
		"LEFT_SHIFT" : KeyCodes.LEFTSHIFT,
		"RIGHT_SHIFT" : KeyCodes.RIGHTSHIFT,
		"ANY_SHIFT" : KeyCodes.SHIFT,

		# These are probably all extended keys - need to check them all
		"LEFT_ALT" : KeyCodes.LEFTMENU,
		"RIGHT_ALT" : KeyCodes.RIGHTMENU,
		"ANY_ALT" : KeyCodes.MENU,

		# These are probably all extended keys - need to check them all
		"LEFT_WIN" : KeyCodes.LEFTWIN,
		"RIGHT_WIN" : KeyCodes.RIGHTWIN,

		"UP_ARROW" : KeyCodes.UP,
		"DOWN_ARROW" : KeyCodes.DOWN,
		"LEFT_ARROW" : KeyCodes.LEFT,
		"RIGHT_ARROW" : KeyCodes.RIGHT,

		"PERIOD" : KeyCodes.OEM_PERIOD,
		"." : KeyCodes.OEM_PERIOD,
		"COMMA" : KeyCodes.OEM_COMMA,
		"," : KeyCodes.OEM_COMMA,
		"PLUS" : KeyCodes.OEM_PLUS,
		"+" : KeyCodes.OEM_PLUS,
		"=" : KeyCodes.OEM_PLUS,
		"MINUS" : KeyCodes.OEM_MINUS,
		"-" : KeyCodes.OEM_MINUS,
	}

	shiftKeys = {
		"~": "`",
		"!": "1",
		"@": "2",
		"#": "3",
		"$": "4",
		"%": "5",
		"^": "6",
		"&": "7",
		"*": "8",
		"(": "9",
		")": "0",
		"_": "-",
		"+": "=",
		"{": "[",
		"}": "]",
		"|": "\\",
		":": ";",
		'"': "'",
		"<": ",",
		">": ".",
		"?": "/"
	}

	extendedKeys = [
		KeyCodes.PRINTSCREEN,
		KeyCodes.PAUSE,
		KeyCodes.BACKSPACE,
		KeyCodes.RETURN,
		KeyCodes.DELETE,
		KeyCodes.HOME,
		KeyCodes.END,
		KeyCodes.PAGEUP,
		KeyCodes.PAGEDOWN,
		KeyCodes.INSERT,
		KeyCodes.LEFTCONTROL,
		KeyCodes.RIGHTCONTROL,
		KeyCodes.CONTROL,
		KeyCodes.LEFTSHIFT,
		KeyCodes.RIGHTSHIFT,
		KeyCodes.SHIFT,
		KeyCodes.LEFTMENU,
		KeyCodes.RIGHTMENU,
		KeyCodes.MENU,
		KeyCodes.LEFTWIN,
		KeyCodes.RIGHTWIN
	]

	class USPunctuation:
		
		keyCodes = {
			# ` ~
			"GRAVE_TILDE" : KeyCodes.OEM_3,
			"`" : KeyCodes.OEM_3,
			
			#  [{ and ]}
			"OPEN_SQR_CUR_BRKT" : KeyCodes.OEM_4,
			"[" : KeyCodes.OEM_4,
			"CLOSE_SQR_CUR_BRKT" : KeyCodes.OEM_6,
			"]" : KeyCodes.OEM_6,

			# ; :
			"COMMA_SEMICOLON" : KeyCodes.OEM_1,
			"," : KeyCodes.OEM_1,

			# ' "
			"SING_DOUB_QUOTES" : KeyCodes.OEM_7,
			"'" : KeyCodes.OEM_7,

			# , < and . > ??? dont know which key code corresponds to this
			# COMMA_OPEN_ANG_BKRT = KeyCodes.OEM_
			# PERIOD_CLOSE_ANG_BKRT = KeyCodes.OEM_

			# / ?
			"SLASH_QUESTION" : KeyCodes.OEM_2,
			"/" : KeyCodes.OEM_2,

			# \ |
			"BACKSLASH_PIPE" : KeyCodes.OEM_5,
			"\\" : KeyCodes.OEM_5,
		}

	def _do_event(self, keycode, scancode, flags, extraInfo):
		"""Generate a keyboard event.

		Args:
			keycode (KeyCode.code): A keyboard key code.
			scancode (int): Unknown
			flags (int): Flags for this keystore, like extended key or keyup event
			extraInfo (int): Extra data for this keystroke

		void keybd_event(
		    BYTE      bVk,
		    BYTE      bScan,
		    DWORD     dwFlags,
		    ULONG_PTR dwExtraInfo
		);
		"""

		return user32.keybd_event(keycode, scancode, flags, extraInfo)

	def press(self, button=None, keycode=None, keyUp=False, flags=0, extraInfo=0):
		"""Generate a keyboard event with the given key.
		Args:
		    button (str): String corresponding to the button key.
		    keycode (KeyCode): KeyCode to press.
		    keyUp (bool, optional): If key is being pressed down or being 
		    	released up.
		"""
		if button:
			button = button.upper()
			try:
				keycode = self.keyCodes[button]
			except KeyError:
				keycode = self.USPunctuation.keyCodes[button]

		release = self.KEY_EVENTF_KEYUP if keyUp else 0
		extended = self.KEY_EVENTF_EXTENDEDKEY if keycode in self.extendedKeys else 0

		self._do_event(keycode, 0x45, release | extended, 0)

	def click(self, button=None, keycode=None, time=0.001, flags=0, extraInfo=0):
		"""Generate a keyboard event with the given key for key down and key up.
		Args:
		    button (str): String corresponding to the button key.
		    keycode (KeyCode): KeyCode to press.
		    time (flaot): Time between key down and key up events. Defaults to 
		    	0.1s
		"""
		self.press(button, keycode)
		microsleep(time)
		self.press(button, keycode, True)

	def clickWithShift(self, callback, *args, **kwargs):
		self.press(keycode=self.keyCodes["ANY_SHIFT"])
		callback(*args, **kwargs)
		self.press(keycode=self.keyCodes["ANY_SHIFT"], keyUp=True)

	def clickWithAlt(self, callback, *args, **kwargs):
		self.press(keycode=self.keyCodes["ANY_ALT"])
		callback(*args, **kwargs)
		self.press(keycode=self.keyCodes["ANY_ALT"], keyUp=True)

	def clickWithCtrl(self, callback, *args, **kwargs):
		self.press(keycode=self.keyCodes["ANY_CTRL"])
		callback(*args, **kwargs)
		self.press(keycode=self.keyCodes["ANY_CTRL"], keyUp=True)

	def clickWithWin(self, callback, *args, **kwargs):
		self.press(keycode=self.keyCodes["LEFT_WIN"])
		callback(*args, **kwargs)
		self.press(keycode=self.keyCodes["LEFT_WIN"], keyUp=True)

	def writeText(self, text):

		print("Writing", text)

		for letter in text:
			if letter.isupper():
				print("Writing uppercase", letter)
				self.clickWithShift(self.click, letter)
			elif letter in self.shiftKeys:
				print("Writing special character", letter)
				print("Associated normal character", self.shiftKeys[letter])
				self.clickWithShift(self.click, self.shiftKeys[letter])
			else:
				print("Normal letter", letter)
				self.click(letter)

