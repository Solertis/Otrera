#!/usr/bin/env python

import json
from content import Content

def pick_content_type(game_name=None):
	"""
	Method for getting the user to pick what type of 
	content they wish to make
	Args:
	  None
	Returns:
	  (str) content type
	"""
	c = Content(game=game_name)
	global engine
	global game
	global path
	engine = c.engine
	game = c.data
	path = c.game
	schemes = get_schemes()
	print "Hi there fella. What type of content are we working with?\n"
	for item in schemes:
		print item
	content_type = raw_input("Enter one of the values above: ")
	if content_type not in schemes:
		print "LOL WTF"
		exit(1)
	else:
		return content_type

def get_schemes():
	schemes = []
	for key in engine.keys():
		if len(engine[key]) > 0:
			schemes.extend(engine[key])
	return schemes

def get_scheme(scheme_name):
	for key in engine.keys():
		if len(engine[key]) > 0:
			if scheme_name in engine[key].keys():
				scheme = engine[key][scheme_name]
	return scheme

def get_update(content_type, thing_name):
	"""
	Top level method for actually getting the update
	data to go into content.json
	
	Args:
	  (str) content_type: The type of content to create
	  (str) thing_name: The content's name (JSON key)
	Returns:
	  (dict) update_data: The update to apply to the JSON
	"""
	#CONSTR = engine[content_type]
	#for key in CONSTR.keys():
	#	if key not in content_type:
	#		del CONSTR[key]
	scheme = get_scheme(content_type)
	scheme[thing_name] = scheme.pop(scheme.keys()[0])
	update_data = get_content_info(scheme)
	return update_data

def get_list(key):
	"""
	General method for converting a user-provided list in
	string form into an actual list

	Args:
	  (str) key: The thing for which we are making a list
	Returns:
	  (list) final_list: The list the user meant to give
	"""
	user_list = raw_input("Give me a comma-separated list for %s: " % key)
	if len(user_list) == 0:
		return []
	else:
		selected = user_list.split(",")
		final_list = []
		for item in selected:
			item = item.lstrip()
			final_list.append(item)
		return final_list

def get_content_info(data_dict):
	"""
	Recursive method for getting the user-desired input
	and putting it into the JSON. The recursion applies
	to content items that have dictionary-style
	attributes.

	Args:
	  (dict) data_dict: The template for the content
	Returns:
	  (dict) data_dict: The completed content piece
	"""
	for k, v in data_dict.iteritems():
		if isinstance(v, dict):
			if v == {}:
				data_dict[k] = get_dict(k)
			else:
				get_content_info(v)
		elif isinstance(v, list):
			data_dict[k] = get_list(k)
		else:
			data_dict[k] = raw_input(k+": ")
	return data_dict

def get_dict(name):
	a = {}
	keys = get_list(name)
	for key in keys:
		value = get_list(key)
		a[key] = value
	return a

def make_content(content_type, update, thing_name):
	"""
	Method for actually writing to content.json.
	This method calls all of the other needed
	methods.

	Args:
	  (str) content_type: Used by update_lists
	  (dict) update: The new JSON
	  (str) thing_name: The new key to create in the JSON
	Returns:
	  None
	"""
	with open(path) as f:
		data = json.load(f)
	data.update(update)
	#data = update_lists(content_type, data, update, thing_name)
	with open(path,"w") as f:
		json.dump(data, f, sort_keys=True, indent=4, ensure_ascii=False)
