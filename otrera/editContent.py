#!/usr/bin/env python

import json
from content import Content
from addContent import get_list, pick_content_type
from content import Content

def print_content(cont):
	for k,v in cont.iteritems():
		if isinstance(v, dict):
			print_content(v)
		else:
			print k + " = " + str(v)

def get_content(content_type, game_name):
	global game
	global path
	c = Content(game=game_name)
	game = c.data
	path = c.game
	LIST = game[content_type]
	print "Here is list of the content of that type"
	for item in LIST.keys():
		print item
	selected = raw_input("Which would you like to edit? ")
	final = LIST[selected]
	return final

def edit_item(cont, content_type):
	print_content(cont)
	key = raw_input("What would you like to change? (top level key): ")
	if isinstance(cont[key], dict):
		edit_item(cont[key])
	elif isinstance(cont[key], list):
		new_val = get_list(key)
		cont[key] = new_val
		return game
	else:
		new_val = raw_input("What is your desired new value?: ")
		cont[key] = new_val
		game[content_type].update(cont)
		return game

def update_json(data):
	with open(path,"w") as f:
		json.dump(data, f, sort_keys=True, indent=4, ensure_ascii=False)
