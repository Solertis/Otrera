#!/usr/bin/env python

import json
from content import Content
from addContent import get_list, pick_content_type
e = Content().data
engine = Content().engine

def print_content(cont):
	for k,v in cont.iteritems():
		if isinstance(v, dict):
			print_content(v)
		else:
			print k + " = " + str(v)

def get_content(content_type):
	LIST = e[content_type]
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
		e[content_type].update(cont)
		return e
	else:
		new_val = raw_input("What is your desired new value?: ")
		cont[key] = new_val
		e[content_type].update(cont)
		return e

def update_json(data):
	with open(path,"w") as f:
		json.dump(data, f, sort_keys=True, indent=4, ensure_ascii=False)

if __name__=="__main__":
	content_type = pick_content_type()
	thing = get_content(content_type)
	complete = edit_item(thing, content_type)
	update_json(complete)
