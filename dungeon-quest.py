#! python2.7
#  ________________________________________________________________________________
# |     ____  __  ___   __________________  _   __   ____  __  ___________________ |
# |    / __ \/ / / / | / / ____/ ____/ __ \/ | / /  / __ \/ / / / ____/ ___/_  __/ |
# |   / / / / / / /  |/ / / __/ __/ / / / /  |/ /  / / / / / / / __/  \__ \ / /    |
# |  / /_/ / /_/ / /|  / /_/ / /___/ /_/ / /|  /  / /_/ / /_/ / /___ ___/ // /     |
# | /_____/\____/_/ |_/\____/_____/\____/_/ |_/   \___\_\____/_____//____//_/      |
# |________________________________________________________________________________|
# Andrew Karapostolakis (pwnzor.ak)
# 2014-12-09

# change title bar text
import ctypes
ctypes.windll.kernel32.SetConsoleTitleA("Dungeon Quest")

# Start of game
def start():
	# clear screen
	import os
	os.system("cls")
	# make sure inventory, input, and door1 are global
	global inventory
	global input
	global door1
	# empty inventory, restore door in first room
	inventory = []
	door1 = True
	print """
	DUNGEON QUEST
	A Banzai! Production
	Andrew Karapostolakis 2014
	"""
	# this does not matter; anything can be input
	action = raw_input("Press Enter to begin, or type e to exit. ").lower()
	# initialize input
	input = False 
	# enter first room
	if action != "e":
		room1()

# First room
def room1():
	# make sure input, inventory, and door1 are global
	global input
	global inventory
	global door1
	# no need to say this if user is still in the same room
	if "Torch" in inventory: # if user has torch, they will have burned down the door
		print "\nAn empty room.\n"
	else:
		print "\nYou wake up in a dark room. \nYou see a flaming torch and a wooden door. \n"
	# ask user for action
	action = raw_input("What do you do? ").lower()
	while action != ("open door", "door", "go through door") and door1 == True:
		if action in ("open door", "door", "break door", "burn door") and "Torch" in inventory and door1 == True:
			print "The old, dry, door catches easily and you stand back as it goes up in flames.\n"
			door1 = False
		elif action in ("open door", "door", "break door",):
			print "The door has no handle, and it is too thick to break down. \nIt does seem to be very dry, though.\n"
		elif action in ("take torch", "torch", "get torch", "pick up torch"):
			print "You picked up the torch.\n"
			# add torch to inventory
			inventory.append("Torch")
		elif action in ("look around", "look", "survey", "look at room"):
			if door1 == False: # if the door is not there
				print "An empty room.\n"
			elif "Torch" in inventory:
				print "You see a wooden door.\n"
			else:
				print "You see a flaming torch and a wooden door.\n"
		else:
			print "You can't do that here.\n"
		# user has input action
		input = True
		# ask user for action again
		action = raw_input("What do you do? ").lower()
	print "You walk through the burnt door frame.\n"
	input = False
	room2()

# Second room
def room2():
	# make sure inventory is global
	global inventory
	# room intro
	print "Second room"
# start game
start()
