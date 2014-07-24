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

def get_update(content_type, thing_name):
	template = templates[content_type]
	template[thing_name] = template.pop(template.keys()[0])
	update_data = get_content_info(template, content_type)
	return update_data

def get_list(key):
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

def get_content_info(data_dict, content_type):
	for k, v in data_dict.iteritems():
		if isinstance(v, dict):
			get_content_info(v, content_type)
		elif isinstance(v, list):
			data_dict[k] = get_list(k)
		else:
			data_dict[k] = raw_input(k+": ")
	return data_dict

def make_content(content_type, thing_name):
	with open("data/everything.json") as f:
		data = json.load(f)
	update = get_update(content_type, thing_name)
	data.update(update)
	data = update_lists(content_type, data, update, thing_name)
	with open("data/everything.json","w") as f:
		json.dump(data, f, sort_keys=True, indent=4, ensure_ascii=False)

def update_lists(content_type, data, update, thing_name):
	if content_type == "skill":
		if update[thing_name]["category"] == "class":
			class_key = update[thing_name]["requirements"]["Class"][0]+"_skills"
			data[class_key].append(thing_name)
		elif update[thing_name]["category"] == "attribute":
			req_key = update[thing_name]["requirements"]["Attributes"][0]
			att = req_key[:3]
			req = req_key[3:]
			data[att][req].append(thing_name)
	else:
		key = update[thing_name]["kind"]
		data[key]["list"].append(thing_name)
	return data

if __name__=="__main__":
	content_type = pick_content_type()
	thing_name = raw_input("Name your %s (lower case only): ")
	make_content(content_type, thing_name)
