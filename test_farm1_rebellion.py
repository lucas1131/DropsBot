import logging

import DropsBot
from DropsBot.game_loop import setup_function, update_function

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Handlers
kbd = DropsBot.virtual_hardware.Keyboard.Keyboard()
mouse = DropsBot.virtual_hardware.Mouse.Mouse()
gRagWindow = None

# Skills hotkeys
gAttack = None
gWarp = None
gBuff = None

# gUpdateSeq = [buffFunc, warpFunc, moveUpFunc, moveLeftFunc, wait, attackFunc, wait]
gUpdateSeq = []
gCurSequence = 0
gSeqLen = 0

gAlootMsgs = []

# TODO: where to put this? implement RagWindow class?
def ragSendTextMsg(text):
	kbd.click("ENTER") # Open chat window
	kbd.writeText(text)
	kbd.click("ENTER") # Send text
	kbd.click("ENTER") # Close chat window

@setup_function()
def setup_gefenia():

	global gRagWindow
	global gUpdateSeq
	global gCurSequence
	global gSeqLen
	
	gRagWindow = DropsBot.getRagWindow()
	loadHotkeys() # Skills bindings
	# loadConfig() # General configuration
	
	# Behaviour sequence
	# If we properly configure time between updates, we dont need to wait
	gUpdateSeq = [
		buffFunc,
		wait005,
		warpFunc,
		wait1,
		moveUpFunc,
		moveLeftFunc,
		wait005,
		attackFunc,
		wait010
	]
	gCurSequence = 0
	gSeqLen = len(gUpdateSeq)

	DropsBot.microsleep(0.1)
	gRagWindow.activate()

	loadAloot()


@update_function()
def basic_gefenia_logic():
	"""What the bot should do:
	
		Buff - Rich's Coind + Platinum Alter
		Warp - F5
		Move a little - 2 3 cells up
			Try moving up and then left to have a better chance of actually moving
		delay some microseconds
		Round trip - F4
		delay some microseconds
	"""
	global gCurSequence
	global gUpdateSeq

	func = gUpdateSeq[gCurSequence]
	logger.info("Calling update sequence [%d]: %s", gCurSequence, func.__name__)
	func()
	gCurSequence = (gCurSequence+1)%gSeqLen
	# Now wait until next update

def loadHotkeys():
	global gAttack
	global gWarp
	global gBuff
	
	gAttack = "F4" # Round trip
	gWarp = "F5"   # Teleportation
	gBuff = ["F8", "F7"] # Rich's Coin & Platinum Alter

def loadAloot():
	global gAlootMsgs
	gAlootMsgs = [
		"@autoloot 0.5", 
		"@alootid reset", 
		"@alootid +526|+912|+1009|+1039|+13313",
		"@alootid +2613|+2610|+509|+522",
		"@alootid -5072|-1457|-1478|-2318|-5017"
	]

	for autolootMsg in gAlootMsgs:
		ragSendTextMsg(autolootMsg)

def attackFunc():
	global gAttack
	kbd.click(gAttack)

gBuffcounter = 0
def buffFunc():
	global gBuff
	global gBuffcounter
	# 30 frame * 60 seconds = 1800
	if gBuffcounter % 1800 == 0: # Buff each minute
		kbd.click(gBuff[0])
		wait045()
		kbd.click(gBuff[1])
	gBuffcounter += 1

def warpFunc():
	global gWarp
	kbd.click(gWarp)

def moveUpFunc():
	global getRagWindow
	mouse.pressButton((gRagWindow.center.x+50, gRagWindow.center.y-250))

def moveLeftFunc():
	global getRagWindow
	mouse.pressButton((gRagWindow.center.x-250, gRagWindow.center.y))

def wait005(): # General wait time
	DropsBot.microsleep(0.15)

def wait010(): # General wait time
	DropsBot.microsleep(0.10)

def wait015(): # General wait time
	DropsBot.microsleep(0.15)

def wait030(): # Used for buffs
	DropsBot.microsleep(0.30)

def wait045(): # General wait time
	DropsBot.microsleep(0.45)

def wait060():
	DropsBot.microsleep(0.60)

def wait1(): # mainly for teleport
	DropsBot.microsleep(1)

if __name__ == "__main__":
	
	import argparse
	ap = argparse.ArgumentParser()
	ap.add_argument("--config", help="Configuration file for this bot. If not supplied, use hardcoded behaviour.")
	args = ap.parse_args()

	if args.config:
		logger.warning("Importing of configuration file not yet implemented, using hardcoded behaviour.")

	DropsBot.start()
