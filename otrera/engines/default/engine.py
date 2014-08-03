# Methods for defining a character's stats and skills

import json
from content import Content
game = Content().data
engine = Content().engine

the_stats = ["Evade","PhyDef","PhyAtk","MagAtk","MagDef",
			"Resistance","CarryStrength","Hit","Accuracy",
			"Craft","MaxHP"]

MAX_LEVEL = game["LEVELS"]["list"][-1]

def apply_level_mods(charac):
	l = game["LEVELS"]
	mod_types = engine["LEVELS"]["modifiers"]
	mods = []
	levrange = charac["level"]+1
	for lev in range(l["list"][0], levrange):
		levobj = l[str(lev)]
		mods.extend(get_level_mods(levobj, charac))
	# Take in a character object who has a certain level attribute
	# Iterate over level objects from zero to character level
	# Add to a master list of mods at each level, add mods to character
	charac = apply_mods(charac, mods)
	return charac

def get_level_mods(levelobj, charac):
	# Going to need a try/catch here for specific key errors
	# This method assumes level objects will not nest values more than 2 layers deep
	mods = []
	for key in levelobj.keys():
		if key == "base":
			mods.extend(levelobj[key])
		elif key in charac.keys():
			needed = charac[key]
			mods.extend(levelobj[key][needed])
	return mods

def apply_mods(charac, mods):
	PLR = 0
	for mod in mods:
		if mod[:3] in engine["ATTRIBUTES"]["list"]:
			charac = apply_att_mod(charac, mod)
		elif mod[:3] == "PLR":
			PLR += int(mod[3:])
		else:
			charac = apply_stat_mod(charac, mod)
	if PLR > 0:
		charac = allocate_player_mods(charac, PLR)
	return charac

def allocate_player_mods(charac, PLR):
	print "Lets allocate points to attributes!\n"
	print "You have %s points to spend" % str(PLR)
	print "Assign desired number of points to attribute, then press 'enter'"
	for key in engine["ATTRIBUTES"]["list"]:
		val = int(raw_input(key+": "))
		if val > PLR:
			print "You don't have that many points"
		else:
			charac = apply_att_int_mod(charac, key, val)
		PLR -= val
	return charac

def apply_att_int_mod(charac, att, val):
	total = charac["attributes"][att] + val
	if total > 25:
		total = 25
		charac["attributes"][att] = 25
		return charac
	else:
		charac["attributes"][att] = total
		return charac

def apply_att_mod(charac, mod):
	if charac["attributes"][mod[:3]] >= 25:
		return charac
	else: 
		charac["attributes"][mod[:3]] = charac["attributes"][mod[:3]] + int(mod[3:])
		return charac

def apply_stat_mod(charac, mod):
	for stat in engine["STATS"]["list"]:
		if stat in mod:
			if engine["STATS"][stat]["type"] == "int":
				diff = int(mod.replace(stat,""))
				if (diff != None) and (charac["stats"][stat] != None):
					charac["stats"][stat] = charac["stats"][stat] + diff
			else:
				new = mod.replace(stat,"")
				charac["stats"][stat] = new
	return charac

def get_stat_modifier(charac, statname):
	# General method for determining a stat modifier given an attribute va;ie
	key = engine["STATS"][statname]
	attMaps = key["attMaps"]
	vals = []
	if len(attMaps) == 1:
		return get_att_modifier(attMaps[0], statname, charac)
	elif "COMB" in attMaps:
		max_key = key["max"]
		newmaps = attMaps[1:]
		for att in newmaps:
			vals.append(charac["attributes"][att])
		total = sum(vals)
		if total > max_key:
			return key['calc'][str(max_key)]
		else:
			return key['calc'][str(total)]
	else:
		for att in attMaps:
			val = get_att_modifier(att, statname, charac)
			if val != None:
				vals.append(get_att_modifier(att, statname, charac))
	return sum(vals)

def get_att_modifier(att, stat, charac):
	# Return the modifier mapped to a given attribute value
	return engine["ATTRIBUTES"][att]["StatMaps"][stat][str(charac["attributes"][att])]

def apply_att_stats(charac):
	# Apply all of the attribute-derived stat modifiers to the character
	for stat in the_stats:
		mod = get_stat_modifier(charac, stat)
		if isinstance(mod,int):
			charac["stats"][stat] = charac["stats"][stat]+mod
		else:
			charac["stats"][stat] = mod
	return charac

def get_inventory_from_strings(string_list):
	# Need to think about some things with this method
	inventory = []
	for thing in string_list:
		thing = thing.lower()
		itm = game["EQUIPMENT"][thing]
		inventory.append(itm)
	return inventory

def adjust_evade(charac):
	weight = 0
	for item in charac["inventory"]:
		weight += item["weight"]
	charac["encumbrance"] = weight
	penalty = charac["encumbrance"]/8
	charac["Evade"] -= penalty
	return charac

def equip_from_string(charac, string):
	for thing in charac["inventory"]:
		if thing["category"] == "WEAPONS" or thing["category"] == "ARMORS":
			equip(charac, thing)

def equip(charac, thing):
	depend = engine["EQUIPMENT"]["DEPENDENCIES"]
	for string in depend:
		b = string.split(",")
		const = b[0]
		char = b[1]
		if thing["type"] not in game[const][charac[char]][thing["category"]]:
			print "You cannot equip this"
		elif thing["category"] == "WEAPONS":
			charac["equipment"]["weapon"] = thing
			charac["equipment"]["eqp_mods"].extend(thing["spec_mods"])
			apply_mods(charac, charac["equipment"]["eqp_mods"])
		elif thing["category"] == "ARMORS":
			charac["equipment"]["armor"] = thing
			charac["equipment"]["defense"] = game["EQUIPMENT"]["ARMOR_DEF"][thing["type"]]
			charac["equipment"]["eqp_mods"].extend(thing["spec_mods"])
		else:
			print "I don't know how to equip this"

def get_learnable_skills(charac):
	learnable = []

def get_class_skills(charac):
	# Find the list of class skills in content.json and 
	# make skill objects out of all of them
	class_skills = e[charac.character_class+"_skills"]
	skill_object_list = []
	for thing in class_skills:
		skill_object = Skill(make=thing)
		skill_object_list.append(skill_object)
	return skill_object_list

def get_attribute_skills(charac):
	# Find the list of skills for each attribute key at each
	# requirement level and make skill objects from them
	skill_names = []
	skill_objects = []
	atts = charac.attributes.keys()
	for att in atts:
		att_dict = e[att]
		for key in att_dict.keys():
			if int(key) <= int(charac.attributes[att]):
				skill_names.extend(att_dict[key])
	for name in skill_names:
		obj = Skill(make=name)
		skill_objects.append(obj)
	return skill_objects
