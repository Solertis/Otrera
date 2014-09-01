# Program for building games
# Publishes content to content.json

from content import Content
from engine import *
from character import Character
import json
import os
from addContent import *
from editContent import *

engine = Content().engine

def get_input(prompt):
	return raw_input(prompt)

def create_game_directory_and_file(game_name):
	gamepath = "engines/default/games/"+game_name
	if os.path.exists(gamepath):
		print "A game with this name already exists for this engine!!!"
		exit(1)
	else:
		os.makedirs(gamepath)
		gamefile = open(gamepath+"/content.json","w+")
		print game_name + " has been created!"
		gamefile.close()

def edit_game(gamename):
	gamepath = "engines/default/games/"+gamename+"/content.json"
	if not os.path.exists(gamepath):
		print "This game does not exist."
		exit(1)
	else:
		print "Press '1' to add content to the game"
		print "Press '2' to edit content already in the game"
		choice = get_input("What is your choice?: ")
		if choice == '1':
			print "Calling addContent module..."
			content_type = pick_content_type(game_name=gamename)
			thing_name = get_input("Name your content: ")
			update = get_update(content_type, thing_name)
			make_content(content_type, update, thing_name)
		elif choice == '2':
			print "Calling editContent module..."
			content_type = pick_content_type(game_name=gamename)
			thing = get_content(content_type, gamename)
			complete = edit_item(thing, content_type)
			update_json(complete)
		else:
			print "Come on now, son."
			exit(1)

def make_game(game_name):
	"""
	Top level method in game builder
	module for creating new games
	from scratch.
	"""
	create_game_directory_and_file(game_name)

def interactive():
	print "Welcome to Otrera Game Builder"
	print "Press '1' to create a new game from scratch"
	print "Press '2' to edit an existing game."
	choice = raw_input("What is your choice?: ")
	if choice == "1":
		game_name = get_input("What is the name of your new game?: ")
		make_game(game_name)
	elif choice == "2":
		game_name = get_input("What is the name of the game you wish to edit? ")
		edit_game(game_name)
	else:
		print "WHOOOOOOOOOOOOOAAAA NELLLLY!!!"
