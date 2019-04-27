import time
import argparse
from DropsBot.virtual_hardware.Mouse import Mouse
from DropsBot.utils import getRagWindow, focusWindow

ap = argparse.ArgumentParser()
ap.add_argument("-n", type=int, default=135, help="Number of times to click")
ap.add_argument("-d", "--delay", type=float, default=0.4, help="Delay in milliseconds between each click")
args = ap.parse_args()

time.sleep(1.5)

w = getRagWindow()
m = Mouse()
m.move_mouse((2070, 200))
# m.move_mouse((2270, 400))
focusWindow(w)
# m._do_event(m._get_button_value("left", False), 0, 0, 0, 0)

for _ in range(args.n):
	m.click(button="right", delay=0.1)
	time.sleep(args.delay)
