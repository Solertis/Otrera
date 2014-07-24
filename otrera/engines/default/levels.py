# Functionality for working with levels.json and other character level code

import json
import random
from content import Content
l = Content().data

def get_player_points(character_class, level):
	"""This method should just return an int
	representing the number of player allocatable
	points afforded a character based on their
	level and class"""
	level = int(level)
	player_points = 0
	key = 1
	while level >= key:
		player_points += int(l[character_class][str(key)][-1])
		key+=1
	return player_points

def get_level_mods(character_class, level):
	"""This method should take in a character level
	and class and spit out a dict of mods."""
	Class = character_class.lower().strip()
	if Class not in l.keys():
		return "I know nothing of this class of which you speak."
	class_mods = get_class_mods(character_class, level)
	player_points = get_player_points(character_class, level)
	complete_mods = allocate_player_points(player_points, class_mods)
	return complete_mods

def get_class_mods(character_class, level):
	level = int(level)
	class_dict = l[character_class]
	final = {"DEX":0,"ART":0,"MGT":0,"DIV":0,"INT":0,"CON":0}
	key = 1
	while level >= key:
		# We do this weird split / list thing to account for
		# more complex classes in the future and the fact that
		# the last item will always be a player point (PLR#)
		mod_list = class_dict[str(key)].split()[:-1]
		for mod in mod_list:
			final[mod[:3]] = final[mod[:3]] + int(mod[-1])
		key += 1
	return final

def allocate_player_points(player_points, class_mods):
	"""This method should take in the initial output
	of 'get_level_mods' and then allow the user to
	allocate and 'player' points to attributes of
	their choosing"""
	resp = raw_input("Do you want to allocate points randomly? y/n: ")
	if "y" in resp:
		complete_mods = allocate_randomly(player_points, class_mods)
		return complete_mods
	else:
		final = {"DEX":0,"ART":0,"MGT":0,"DIV":0,"INT":0,"CON":0}
		print "You have %s points available\n" % str(player_points)
		print "Assign desired number of points to attribute, then press 'enter'"
		final["DEX"] = final["DEX"] + int(raw_input("DEX: "))
		final["ART"] = final["ART"] + int(raw_input("ART: "))
		final["MGT"] = final["MGT"] + int(raw_input("MGT: "))
		final["DIV"] = final["DIV"] + int(raw_input("DIV: "))
		final["INT"] = final["INT"] + int(raw_input("INT: "))
		final["CON"] = final["CON"] + int(raw_input("CON: "))	
		if class_mods == {}:
			return final
		else:
			complete_mods = combine_mods(final, class_mods)
			return complete_mods

def allocate_randomly(player_points, class_mods):
	"""Randomly add points to attributes"""
	random_mods = {"DEX":0,"ART":0,"MGT":0,"DIV":0,"CON":0,"INT":0}
	for num in range(0,player_points):
		key = random.choice(random_mods.keys())
		random_mods[key] = random_mods[key] + 1
	if class_mods == {}:
		return random_mods
	else:
		complete_mods = combine_mods(random_mods, class_mods)
		return complete_mods

def combine_mods(mods1, mods2):
	final = {"DEX":0,"ART":0,"MGT":0,"DIV":0,"INT":0,"CON":0}
	for key in final.keys():
		if key in mods1.keys():
			final[key] = final[key] + mods1[key]
		if key in mods2.keys():
			final[key] = final[key] + mods2[key]
	return final
