#! python2.7
#  ________________________________________________________________________________
# |     ____  __  ___   __________________  _   __   ____  __  ___________________ |
# |    / __ \/ / / / | / / ____/ ____/ __ \/ | / /  / __ \/ / / / ____/ ___/_  __/ |
# |   / / / / / / /  |/ / / __/ __/ / / / /  |/ /  / / / / / / / __/  \__ \ / /    |
# |  / /_/ / /_/ / /|  / /_/ / /___/ /_/ / /|  /  / /_/ / /_/ / /___ ___/ // /     |
# | /_____/\____/_/ |_/\____/_____/\____/_/ |_/   \___\_\____/_____//____//_/      |
# |________________________________________________________________________________|
# Andrew Karapostolakis
# 2014-12-08

import sys
import os
import ctypes
# change title bar text
ctypes.windll.kernel32.SetConsoleTitleA("Dungeon Quest")

# Start of game
def start():
	# clear screen
	os.system("cls")
	# make sure inventory, door1, player, and chest are global
	global inventory
	global door1
	global player
	global troll_base
	global chest3
	global troll4
	# empty inventory, restore door in first room, generate player and monster stats, fill chest in third room
	inventory = []
	door1 = True
	player = {'health': 100,
			  'defence': 10,
			  'attack': 10,
			  'gold': 0}
	troll_base = {'health': 70,
				  'defence': 5,
				  'attack': 10}
	chest3 = True
	troll4 = True
	print """
	DUNGEON QUEST
	A Banzai! Production
	Andrew Karapostolakis 2014
	"""
	# this does not matter; anything can be input
	action = raw_input("Press Enter to begin, or type e to exit. ").lower()
	# enter first room
	if action != "e":
		room1()

# First room
def room1():
	# make sure inventory and door1 are global
	global inventory
	global door1
	# no need to say this if user is still in the same room
	if "Torch" in inventory: # if user has torch, they will have burned down the door
		# room intro (no door)
		print "You see an empty room, with the charred frame of the door you burned earlier.\n"
	else:
		# room intro (door)
		print "\nYou wake up in a dark room. \nYou see a flaming torch and a wooden door. \n"
	# ask user for action
	action = raw_input("What do you do? ").lower()
	# loop until player leaves room
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
		action = ""
		# ask user for action again
		action = raw_input("What do you do? ").lower()
	print "You walk through the burnt door frame.\n"
	# next room
	room2()

# Second room
def room2():
	# room intro
	print "You see a burnt door frame, a dark doorway, and a wooden door with a handle.\n"
	# loop until player leaves room
	loop = True
	while loop:
		# ask user for action
		action = raw_input("What do you do? ").lower()
		if action in ('look around', 'look', 'survey', 'look at room'):
				print "You see a burnt door frame, a dark doorway, and a wooden door with a handle.\n"
		elif action in ("door frame", "burnt door", "burnt door frame"):
			loop = False
			# enter first room
			room1()
		elif action in ("wooden door", "door", "door with handle", "wooden door with handle"):
			loop = False
			# enter third room
			room3()
		elif action in ("doorway", "dark doorway"):
			loop = False
			# enter fourth room
			room4()
		else:
			print "You can't do that here.\n"

# Third room
def room3():
	# make sure player and chest are global
	global player
	global chest3
	# initialize action
	action = ""
	# room intro
	print "You enter a room with a treasure chest.\n"
	# loop until user leaves room
	while action not in ("door", "leave", "go through door"):
		# ask user for action
		action = raw_input("What do you do? ").lower()
		if action in ("chest", "open chest", "treasure chest", "take treasure chest", "open treasure chest", "take chest", "look in chest", "look in treasure chest") and chest3 == True:
			print "You found the Leather Armour! You gained 10 defence points.\n"
			inventory.append("Leather Armour")
			# leather armour adds 10 to defence
			player['defence'] += 10
			# chest emptied
			chest3 = False
		elif action in ("chest", "open chest", "treasure chest", "take treasure chest", "open treasure chest", "take chest", "look in chest", "look in treasure chest"):
			print "The chest is empty.\n"
		elif action in ('look around', 'look', 'survey', 'look at room'):
			print "A room containing only a treasure chest.\n"
		elif action not in ("door", "leave", "go through door"):
			print "You can't do that here.\n"
	room2()

# Fourth room
def room4():
	# make sure player and troll4 are global
	global player
	global troll4
	# set up troll stats and initialize action
	action = ""
	troll = troll_base
	# room intro
	if troll4 == True:
		print "You can see a door, but it's blocked by an ornery troll.\n"
	else:
		print "A room with a door and a dark doorway."
	while not (action in ("door", "go through door", "open door") and troll4 == False):
		# ask user for action
		action = raw_input("What do you do? ").lower()
		if action in ("fight troll", "kill troll", "beat up troll", "punch troll in the face", "fight") and troll4 == True:
			while troll4 == True:
				print "The troll has ", troll['health'], " health. You have ", player['health'], " health. What do you do?"
				print "ATTACK   FLEE"
				action = raw_input().lower()
				if action == ("attack"):
					# torch deals 2 damage (only weapon available at this point)
					print "\nYou attack the troll and deal ", ((player['attack'] * 2) / troll['defence']), " damage.\n"
					troll['health'] -= ((player['attack'] * 2) / troll['defence'])
					if troll['health'] < 0:
						troll4 = False
						print "You defeated the troll! You get 100 gold and a wooden club.\n"
						inventory.append("Wooden Club")
						player['gold'] += 100
						troll4 = False
					else:
						# counter-attack (troll attacks with club (5 damage))
						print "The troll counter-attacks and deals ", ((troll['attack'] * 5) / player['defence']), " damage.\n"
						player['health'] -= ((troll['attack'] * 2) / player['defence'])
						if player['health'] < 0:
							print "You have died."
							print "GAME OVER"
							sys.exit()
				elif action == ("flee"):
					break
				else:
					print "Please enter either ATTACK or FLEE\n"
		elif action in ('look around', 'look', 'survey', 'look at room') and troll4 == True:
			print "You can see a door, but it's blocked by an ornery troll.\n"
		elif action in ('look around', 'look', 'survey', 'look at room'):
			print "A room with a door and a dark doorway."
		elif action in ("door", "go through door", "open door") and troll4 == False:
			print "The door is blocked by a troll.\n"
		elif action in ("doorway", "dark doorway"):
			room2()
		else:
			print "You can't do that here.\n"
	room5()
	
# Fifth room
def room5():
	# initialize action
	action = ""
	# room intro
	print "You enter a room with a treasure chest.\n"
	# loop until user leaves room
	while action not in ("chest", "open chest", "treasure chest", "take treasure chest", "open treasure chest", "take chest", "look in chest", "look in treasure chest"):
		# ask user for action
		action = raw_input("What do you do? ").lower()
		if action in ("door", "leave", "go through door"):
			room4()
		elif action in ('look around', 'look', 'survey', 'look at room'):
			print "A room containing only a treasure chest.\n"
		elif action not in ("door", "leave", "go through door"):
			print "You can't do that here.\n"
	print "You found the Golden Chalice!"
	action = raw_input("Thank you for playing Dungeon Quest. To play again, press Enter. To quit, enter Quit.").lower()
	# restart
	if action != "quit":
		start()

# start game
start()
