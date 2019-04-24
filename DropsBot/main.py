import time
import Mouse
import utils


fps = 30
spf = 1/fps # Seconds per frame
t1 = 0

def delay(t0, target):
	''''Delays the execution until initial time reaches target time.
	This function has 150 nanoseconds of precision, with 1.3 ns standard deviation.
	Args:
		t0 (int): Initial time, in seconds.
		target (int): Target time, in seconds.
	'''
	t1 = time.clock()
	while t0 < target:
		t2 = time.clock()
		t0 += t2 - t1
		t1 = t2

def setup():
	pass

def gameLoop():
	
	t1 = time.clock()
	while True:
		t2 = time.clock() # Frame's start time
		deltaTime = t2-t1

		# Do things
		print(deltaTime)

		frameTime = time.clock() - t2
		delay(frameTime, spf) # Sincronize with game's framerate
		t1 = t2 # Frame's end time

if __name__ == "__main__":
	setup()
	gameLoop()