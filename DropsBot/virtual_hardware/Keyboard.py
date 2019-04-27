import KeyCodes

class Keyboard:
	
	A = KeyCodes.A
	B = KeyCodes.B
	C = KeyCodes.C
	D = KeyCodes.D
	E = KeyCodes.E
	F = KeyCodes.F
	G = KeyCodes.G
	H = KeyCodes.H
	I = KeyCodes.I
	J = KeyCodes.J
	K = KeyCodes.K
	L = KeyCodes.L
	M = KeyCodes.M
	N = KeyCodes.N
	O = KeyCodes.O
	P = KeyCodes.P
	Q = KeyCodes.Q
	R = KeyCodes.R
	S = KeyCodes.S
	T = KeyCodes.T
	U = KeyCodes.U
	V = KeyCodes.V
	W = KeyCodes.W
	X = KeyCodes.X
	Y = KeyCodes.Y
	Z = KeyCodes.Z

	SPACE = KeyCodes.SPACE
	
	ZERO = KeyCodes.ZERO
	ONE = KeyCodes.ONE
	TWO = KeyCodes.TWO
	THREE = KeyCodes.THREE
	FOUR = KeyCodes.FOUR
	FIVE = KeyCodes.FIVE
	SIX = KeyCodes.SIX
	SEVEN = KeyCodes.SEVEN
	EIGHT = KeyCodes.EIGHT
	NINE = KeyCodes.NINE

	NUM0 = KeyCodes.NUMPAD0
	NUM1 = KeyCodes.NUMPAD1
	NUM2 = KeyCodes.NUMPAD2
	NUM3 = KeyCodes.NUMPAD3
	NUM4 = KeyCodes.NUMPAD4
	NUM5 = KeyCodes.NUMPAD5
	NUM6 = KeyCodes.NUMPAD6
	NUM7 = KeyCodes.NUMPAD7
	NUM8 = KeyCodes.NUMPAD8
	NUM9 = KeyCodes.NUMPAD9

	F0 = KeyCodes.F0
	F1 = KeyCodes.F1
	F2 = KeyCodes.F2
	F3 = KeyCodes.F3
	F4 = KeyCodes.F4
	F5 = KeyCodes.F5
	F6 = KeyCodes.F6
	F7 = KeyCodes.F7
	F8 = KeyCodes.F8
	F9 = KeyCodes.F9
	F10 = KeyCodes.F10
	F11 = KeyCodes.F11
	F12 = KeyCodes.F12

	SCROLL_LOCK = KeyCodes.SCROLL_LOCK
	CAPS_LOCK = KeyCodes.CAPS_LOCK
	NUM_LOCK = KeyCodes.NUM_LOCK

	ESC = KeyCodes.ESC
	TAB = KeyCodes.TAB
	FN = KeyCodes.FN
	PRINT_SCREEN = KeyCodes.PRINT_SCREEN
	PAUSE_BREAK = KeyCodes.PAUSE_BREAK
	BACKSPACE = KeyCodes.BACKSPACE
	ENTER = KeyCodes.ENTER
	DELETE = KeyCodes.DELETE
	HOME = KeyCodes.HOME
	END = KeyCodes.END
	PAGE_UP = KeyCodes.PAGEUP
	PAGE_DOWN = KeyCodes.PAGEDOWN
	INSERT = KeyCodes.INSERT

	LEFT_CTRL = KeyCodes.LEFTCONTROL
	RIGHT_CTRL = KeyCodes.RIGHTCONTROL
	ANY_CTRL = KeyCodes.CONTROL

	LEFT_SHIFT = KeyCodes.LEFTSHIFT
	RIGHT_SHIFT = KeyCodes.RIGHTSHIFT
	ANY_SHIFT = KeyCodes.SHIFT

	LEFT_ALT = KeyCodes.LEFTMENU
	RIGHT_ALT = KeyCodes.RIGHTMENU
	ANY_ALT = KeyCodes.MENU

	LEFT_WIN = KeyCodes.LEFTWIN
	RIGHT_WIN = KeyCodes.RIGHTWIN

	UP_ARROW = KeyCodes.UP
	DOWN_ARROW = KeyCodes.DOWN
	LEFT_ARROW = KeyCodes.LEFT
	RIGHT_ARROW = KeyCodes.RIGHT

	PERIOD = KeyCodes.OEM_PERIOD
	COMMA = KeyCodes.OEM_COMMA
	PLUS = KeyCodes.OEM_PLUS
	MINUS = KeyCodes.OEM_MINUS

	class USPunctuation:
		
		# ` ~
		GRAVE_TILDE = KeyCodes.OEM_3
		
		#  [{ and ]}
		OPEN_SQR_CUR_BRKT = KeyCodes.OEM_4
		CLOSE_SQR_CUR_BRKT = KeyCodes.OEM_6

		# ; :
		COMMA_SEMICOLON = KeyCodes.OEM_1

		# ' "
		SING_DOUB_QUOTES = KeyCodes.OEM_7

		# , < and . > ??? dont know which key code corresponds to this
		# COMMA_OPEN_ANG_BKRT = KeyCodes.OEM_
		# PERIOD_CLOSE_ANG_BKRT = KeyCodes.OEM_

		# / ?
		SLASH_QUESTION = KeyCodes.OEM_2

		# \ |
		BACKSLASH_PIPE = KeyCodes.OEM_5


	def press(button):

		elif button == "":
			pass # self._do_event(...)

		elif button == "A":
			self._do_event(self.A, )
		elif button == "B":
			self._do_event(self.B, )
		elif button == "C":
			self._do_event(self.C, )
		elif button == "D":
			self._do_event(self.D, )
		elif button == "E":
			self._do_event(self.E, )
		elif button == "F":
			self._do_event(self.F, )
		elif button == "G":
			self._do_event(self.G, )
		elif button == "H":
			self._do_event(self.H, )
		elif button == "I":
			self._do_event(self.I, )
		elif button == "J":
			self._do_event(self.J, )
		elif button == "K":
			self._do_event(self.K, )
		elif button == "L":
			self._do_event(self.L, )
		elif button == "M":
			self._do_event(self.M, )
		elif button == "N":
			self._do_event(self.N, )
		elif button == "O":
			self._do_event(self.O, )
		elif button == "P":
			self._do_event(self.P, )
		elif button == "Q":
			self._do_event(self.Q, )
		elif button == "R":
			self._do_event(self.R, )
		elif button == "S":
			self._do_event(self.S, )
		elif button == "T":
			self._do_event(self.T, )
		elif button == "U":
			self._do_event(self.U, )
		elif button == "V":
			self._do_event(self.V, )
		elif button == "W":
			self._do_event(self.W, )
		elif button == "X":
			self._do_event(self.X, )
		elif button == "Y":
			self._do_event(self.Y, )
		elif button == "Z":
			self._do_event(self.Z, )
		elif button == "SPACE":
			self._do_event(self.SPACE, )
		elif button == "ZERO":
			self._do_event(self.ZERO, )
		elif button == "ONE":
			self._do_event(self.ONE, )
		elif button == "TWO":
			self._do_event(self.TWO, )
		elif button == "THREE":
			self._do_event(self.THREE, )
		elif button == "FOUR":
			self._do_event(self.FOUR, )
		elif button == "FIVE":
			self._do_event(self.FIVE, )
		elif button == "SIX":
			self._do_event(self.SIX, )
		elif button == "SEVEN":
			self._do_event(self.SEVEN, )
		elif button == "EIGHT":
			self._do_event(self.EIGHT, )
		elif button == "NINE":
			self._do_event(self.NINE, )
		elif button == "NUM0":
			self._do_event(self.NUM0, )
		elif button == "NUM1":
			self._do_event(self.NUM1, )
		elif button == "NUM2":
			self._do_event(self.NUM2, )
		elif button == "NUM3":
			self._do_event(self.NUM3, )
		elif button == "NUM4":
			self._do_event(self.NUM4, )
		elif button == "NUM5":
			self._do_event(self.NUM5, )
		elif button == "NUM6":
			self._do_event(self.NUM6, )
		elif button == "NUM7":
			self._do_event(self.NUM7, )
		elif button == "NUM8":
			self._do_event(self.NUM8, )
		elif button == "NUM9":
			self._do_event(self.NUM9, )
		elif button == "F0":
			self._do_event(self.F0, )
		elif button == "F1":
			self._do_event(self.F1, )
		elif button == "F2":
			self._do_event(self.F2, )
		elif button == "F3":
			self._do_event(self.F3, )
		elif button == "F4":
			self._do_event(self.F4, )
		elif button == "F5":
			self._do_event(self.F5, )
		elif button == "F6":
			self._do_event(self.F6, )
		elif button == "F7":
			self._do_event(self.F7, )
		elif button == "F8":
			self._do_event(self.F8, )
		elif button == "F9":
			self._do_event(self.F9, )
		elif button == "F10":
			self._do_event(self.F10, )
		elif button == "F11":
			self._do_event(self.F11, )
		elif button == "F12":
			self._do_event(self.F12, )
		elif button == "SCROLL_LOCK":
			self._do_event(self.SCROLL_LOCK, )
		elif button == "CAPS_LOCK":
			self._do_event(self.CAPS_LOCK, )
		elif button == "NUM_LOCK":
			self._do_event(self.NUM_LOCK, )
		elif button == "ESC":
			self._do_event(self.ESC, )
		elif button == "TAB":
			self._do_event(self.TAB, )
		elif button == "FN":
			self._do_event(self.FN, )
		elif button == "PRINT_SCREEN":
			self._do_event(self.PRINT_SCREEN, )
		elif button == "PAUSE_BREAK":
			self._do_event(self.PAUSE_BREAK, )
		elif button == "BACKSPACE":
			self._do_event(self.BACKSPACE, )
		elif button == "ENTER":
			self._do_event(self.ENTER, )
		elif button == "DELETE":
			self._do_event(self.DELETE, )
		elif button == "HOME":
			self._do_event(self.HOME, )
		elif button == "END":
			self._do_event(self.END, )
		elif button == "PAGE_UP":
			self._do_event(self.PAGE_UP, )
		elif button == "PAGE_DOWN":
			self._do_event(self.PAGE_DOWN, )
		elif button == "INSERT":
			self._do_event(self.INSERT, )
		elif button == "LEFT_CTRL":
			self._do_event(self.LEFT_CTRL, )
		elif button == "RIGHT_CTRL":
			self._do_event(self.RIGHT_CTRL, )
		elif button == "ANY_CTRL":
			self._do_event(self.ANY_CTRL, )
		elif button == "LEFT_SHIFT":
			self._do_event(self.LEFT_SHIFT, )
		elif button == "RIGHT_SHIFT":
			self._do_event(self.RIGHT_SHIFT, )
		elif button == "ANY_SHIFT":
			self._do_event(self.ANY_SHIFT, )
		elif button == "LEFT_ALT":
			self._do_event(self.LEFT_ALT, )
		elif button == "RIGHT_ALT":
			self._do_event(self.RIGHT_ALT, )
		elif button == "ANY_ALT":
			self._do_event(self.ANY_ALT, )
		elif button == "LEFT_WIN":
			self._do_event(self.LEFT_WIN, )
		elif button == "RIGHT_WIN":
			self._do_event(self.RIGHT_WIN, )
		elif button == "UP_ARROW":
			self._do_event(self.UP_ARROW, )
		elif button == "DOWN_ARROW":
			self._do_event(self.DOWN_ARROW, )
		elif button == "LEFT_ARROW":
			self._do_event(self.LEFT_ARROW, )
		elif button == "RIGHT_ARROW":
			self._do_event(self.RIGHT_ARROW, )
		elif button == "PERIOD":
			self._do_event(self.PERIOD, )
		elif button == "COMMA":
			self._do_event(self.COMMA, )
		elif button == "PLUS":
			self._do_event(self.PLUS, )
		elif button == "MINUS":
			self._do_event(self.MINUS, )
		elif button == "GRAVE_TILDE":
			self._do_event(self.GRAVE_TILDE, )
		elif button == "OPEN_SQR_CUR_BRKT":
			self._do_event(self.OPEN_SQR_CUR_BRKT, )
		elif button == "CLOSE_SQR_CUR_BRKT":
			self._do_event(self.CLOSE_SQR_CUR_BRKT, )
		elif button == "COMMA_SEMICOLON":
			self._do_event(self.COMMA_SEMICOLON, )
		elif button == "SING_DOUB_QUOTES":
			self._do_event(self.SING_DOUB_QUOTES, )
		elif button == "SLASH_QUESTION":
			self._do_event(self.SLASH_QUESTION, )
		elif button == "BACKSLASH_PIPE":
			self._do_event(self.BACKSLASH_PIPE, )
