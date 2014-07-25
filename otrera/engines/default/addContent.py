#!/usr/bin/env python

import json
from templates import *
from content import Content

path = Content().path

def pick_content_type():
	"""
	Method for getting the user to pick what type of 
	content they wish to make
	Args:
	  None
	Returns:
	  (str) content type
	"""
	types = ["skill","weapon","armor","item","character","class"]
	print "Hi there fella. What sorta content would you like to make?\n"
	content_type = raw_input("Enter 'skill', 'weapon', 'armor', class, character, or 'item': ")
	if content_type not in types:
		#User is making up content types. Mayb re-prompt?
		return "Are you funnin' me son?"
	else:
		return content_type

def get_update(content_type, thing_name):
	"""
	Top level method for actually getting the update
	data to go into everything.json
	
	Args:
	  (str) content_type: The type of content to create
	  (str) thing_name: The content's name (JSON key)
	Returns:
	  (dict) update_data: The update to apply to the JSON
	"""
	template = templates[content_type]
	template[thing_name] = template.pop(template.keys()[0])
	update_data = get_content_info(template, content_type)
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
			get_content_info(v)
		elif isinstance(v, list):
			data_dict[k] = get_list(k)
		else:
			data_dict[k] = raw_input(k+": ")
	return data_dict

def make_content(content_type, thing_name):
	"""
	Method for actually writing to everything.json.
	This method calls all of the other needed
	methods.

	Args:
	  (str) content_type: Informs which template to use
	  (str) thing_name: The new key to create in the JSON
	Returns:
	  None
	"""
	with open(path) as f:
		data = json.load(f)
	update = get_update(content_type, thing_name)
	data.update(update)
	data = update_lists(content_type, data, update, thing_name)
	with open(path,"w") as f:
		json.dump(data, f, sort_keys=True, indent=4, ensure_ascii=False)

def update_lists(content_type, data, update, thing_name):
	"""
	Content types have master lists in everything.json
	This method adds the name to the relevant master
	list as part of the content creation process.

	Args:
	  (str) content_type: Type of content
	  (dict) data: The everything.json data in dict form
	  (dict) update: The new content data in dict form
	  (thing_name): The name to append to the list
	"""
	if content_type == "skill":
		if update[thing_name]["category"] == "class":
			class_key = update[thing_name]["requirements"]["Class"][0]+"_skills"
			data[class_key].append(thing_name)
		elif update[thing_name]["category"] == "attribute":
			req_key = update[thing_name]["requirements"]["Attributes"][0]
			att = req_key[:3]
			req = req_key[3:]
			data[att][req].append(thing_name)
	elif content_type == "character":
		key = "characters"
		data[key].append(thing_name)
	elif content_type == "class":
		key = "classes"
		data[key].append(thing_name)
	else:
		key = update[thing_name]["kind"]
		data[key]["list"].append(thing_name)
	return data

if __name__=="__main__":
	content_type = pick_content_type()
	thing_name = raw_input("Name your %s (lower case only): ")
	make_content(content_type, thing_name)
