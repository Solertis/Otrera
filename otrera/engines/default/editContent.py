#!/usr/bin/env python

import json
from content import Content
from addContent import get_list
path = Content().path
e = Content().data

def get_input(prompt):
	return raw_input(prompt)

def pick_function():
	print "Welcome to the Otrera Content Editor!\n"
	print "Press '1' to edit a specific content item"
	# Will add search / list functions later
	response = get_input("What would you like to do?: ")
	if response == '1':
		content_item = get_input("What piece of content do you want to edit?: ")
		arg = content_item.lower()
		cont = e[arg]
		update = edit_item(cont)
		update_json(update)
	else:
		print "I am twelve years old and what is this"

def print_content(cont):
	for k,v in cont.iteritems():
		if isinstance(v, dict):
			print_content(v)
		else:
			print k + " = " + str(v)

def edit_item(cont):
	print_content(cont)
	key = get_input("What would you like to change? (top level key): ")
	if isinstance(cont[key], dict):
		edit_item(cont[key])
	elif isinstance(cont[key], list):
		new_val = get_list(key)
		cont[key] = new_val
		e.update(cont)
		return e
	else:
		new_val = get_input("What is your desired new value?: ")
		cont[key] = new_val
		e.update(cont)
		return e

def update_json(data):
	with open(path,"w") as f:
		json.dump(data, f, sort_keys=True, indent=4, ensure_ascii=False)

if __name__=="__main__":
	pick_function()
