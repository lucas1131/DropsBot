import time
from DropsBot.Mouse import Mouse
from DropsBot.utils import getRagWindow, focusWindow

time.sleep(1)

w = getRagWindow()
m = Mouse()
m.move_mouse((2070, 200))
# m.move_mouse((2270, 400))
focusWindow(w)
# m._do_event(m._get_button_value("left", False), 0, 0, 0, 0)

for _ in range(150):
	m.click(button="right", delay=0.1)
	time.sleep(0.4)
