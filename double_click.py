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
m.move((2070, 200))
focusWindow(w)

for _ in range(args.n):
	m.doubleClick()
	m.doubleClick()
	time.sleep(args.delay)
