# Methods for defining a character's stats and skills

from skills import *
import json
from content import Content
game = Content().data
engine = Content().engine

the_stats = ["Evade","PhyDef","PhyAtk","MagAtk","MagDef",
			"Resistance","CarryStrength","Hit","Accuracy",
			"Craft","MaxHP"]

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
	for key in levelobj.keys():
		if key == "base":
			return levelobj[key]
		elif key in charac.keys():
			needed = charac[key]
			return levelobj[key][needed]

def apply_mods(charac, mods):
	PLR = 0
	for mod in mods:
		if mod[:3] in engine["ATTRIBUTES"]["list"]:
			apply_att_mod(charac, mod)
		elif mod[:3] == "PLR":
			PLR += int(mod[3:])
		else:
			apply_stat_mod(charac, mod)
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
			charac["attributes"][key] = charac["attributes"][key] + val
		PLR -= val
	return charac

def apply_att_mod(charac, mod):
	charac["attributes"][mod[:3]] = charac["attributes"][mod[:3]] + int(mod[3:])

def apply_stat_mod(charac, mod):
	for stat in engine["STATS"]["list"]:
		if stat in mod:
			if engine["STATS"][stat]["type"] == "int":
				diff = int(mod.replace(stat,""))
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
		newmaps = attMaps[1:]
		for att in newmaps:
			vals.append(charac["attributes"][att])
		total = sum(vals)
		return key['calc'][str(total)]
	else:
		for att in attMaps:
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
	pass

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
