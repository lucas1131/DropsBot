import time
import heapq
import logging

import DropsBot.utils
import DropsBot.virtual_hardware.Mouse

logger = logging.getLogger(__name__)
logging.basicConfig()
logger.setLevel(logging.INFO)

# TODO: put these in config file
framesToUpdate = 1 # Update bot state after 10 frames - 3 times per second if 30 fps
fps = 30
spf = 1/fps # Seconds per frame
t1 = 0
run = True
paused = False

SETUP_FUNCS = []
UPDATE_FUNCS = []


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

def update_function(order=50):
	"""Register a setup function
	
	Args:
	    order (int): The order priority for this function. The lower the value, 
	    	The higher the priority.
	"""
	def _decorator(func):
		logger.info("Registering function %s", func.__name__)
		heapq.heappush(UPDATE_FUNCS, (order, func))
	return _decorator

def setup_function(order=50):
	"""Register an update function for the game loop
	
	Args:
	    order (int): The order priority for this function. The lower the value, 
	    	The higher the priority.
	"""
	def _decorator(func):
		logger.info("Registering function %s", func.__name__)
		heapq.heappush(SETUP_FUNCS, (order, func))
	return _decorator


def setup():

	# TODO: load config
	# loadConfig()
	
	for _, func in SETUP_FUNCS:
		func()

def startGameLoop():
	
	# Start external command thread
	# controlThread = Thread()
	# controlThread.start()

	logger.info("Starting game loop")
	t1 = time.clock()
	counter = 0
	while run: # Allow for external command/hotkey to stop or pause the bot
		
		logger.info("Uptading")
		if paused: continue

		t2 = time.clock() # Frame's start time
		deltaTime = t2-t1

		# Do things
		for _, func in UPDATE_FUNCS:
			logger.info("Calling func %s", func.__name__)
			func()

		frameTime = time.clock() - t2
		delay(frameTime, spf*framesToUpdate) # Sincronize with game's framerate
		t1 = t2 # Frame's end time
		counter += 1
		if counter > 5000:
			break

def start():
	setup()
	startGameLoop()

if __name__ == "__main__":
	start()
