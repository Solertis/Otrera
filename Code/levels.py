# Functionality for working with levels.json and other character level code

import json

o = open("levels.json","r").read()
l = json.loads(o)

def get_player_points(character_class, level):
	"""This method should just return an int
	representing the number of player allocatable
	points afforded a character based on their
	level and class"""
	if level >= 3:
		player_points = 8
	else:
		player_points = 0
	key = 1
	while level >= key:
		player_points += int(l[character_class][str(key)][-1])
		key+=1
	return player_points

def get_level_mods(character_class, level):
	"""This method should take in a character level
	and class and spit out a dict of mods."""
	points = get_player_points(character_class, level)
	complete_mods = allocate_player_points(points, mods)
	return complete_mods

def allocate_player_points(points, mods):
	"""This method should take in the initial output
	of 'get_level_mods' and then allow the user to
	allocate and 'player' points to attributes of
	their choosing"""
	resp = raw_input("Do you want to allocate points randomly? y/n: ")
	if "y" in resp:
		complete_mods = allocate_randomly(points, mods)
		return complete_mods
	else:
		# Use points to manually allocate mods
		return complete_mods

def allocate_randomly(points, mods):
	"""Randomly add points to attributes"""
	return complete_mods
