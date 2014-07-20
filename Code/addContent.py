#!/usr/bin/env python

import json
from templates import *

def pick_content_type():
	types = ["skill","weapon","armor","item"]
	print "Hi there fella. What sorta content would you like to make?\n"
	content_type = raw_input("Enter 'skill', 'weapon', 'armor', or 'item': ")
	if content_type not in types:
		return "Are you funnin' me son?"
	else:
		return content_type

def get_update(content_type):
	template = templates[content_type]
	new_name = raw_input("Name your %s (lower case only): " % content_type)
	template[new_name] = template.pop(template.keys()[0])
	update_data = get_content_info(template, content_type)
	return update_data

def get_list(key):
	user_list = raw_input("Give me a comma-separated list (no spaces) for %s: " % key)
	if len(user_list) == 0:
		return []
	else:
		return user_list.split(",")

def get_content_info(data_dict, content_type):
	for k, v in data_dict.iteritems():
		if isinstance(v, dict):
			get_content_info(v, content_type)
		elif isinstance(v, list):
			data_dict[k] = get_list(k)
		else:
			data_dict[k] = raw_input(k+": ")
	return data_dict

def make_content(content_type):
	with open("data/everything.json") as f:
		data = json.load(f)
	update = get_update(content_type)
	data.update(update)
	with open("data/everything.json","w") as f:
		json.dump(data, f, sort_keys=True, indent=4, ensure_ascii=False)

if __name__=="__main__":
	content_type = pick_content_type()
	make_content(content_type)
