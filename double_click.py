import time
import argparse
from DropsBot.virtual_hardware.Mouse import Mouse
from DropsBot.utils import getRagWindow, focusWindow

ap = argparse.ArgumentParser()
ap.add_argument("-n", type=int, default=135, help="Number of times to click")
ap.add_argument("-d", "--delay", type=float, default=0.3, help="Delay in milliseconds between each click")
args = ap.parse_args()

time.sleep(1.5)

w = getRagWindow()
m = Mouse()
m.move_mouse((2070, 200))
# m.move_mouse((2270, 400))
focusWindow(w)
# m._do_event(m._get_button_value("left", False), 0, 0, 0, 0)

for _ in range(args.n):
	m.double_click()
	m.double_click()
	time.sleep(args.delay)
