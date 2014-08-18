# Methods for defining a character's stats and skills

import json
from content import Content
import random

game = Content().data
engine = Content().engine

the_stats = ["Evade","PhyDef","PhyAtk","MagAtk","MagDef",
			"Resistance","CarryStrength","Hit","Accuracy",
			"Craft","MaxHP"]

CONSTRUCTS = engine.keys()

def apply_level_mods(charac, rand=False):
	l = game["LISTS"]["Level"]
	mod_types = engine["Progression"]["Level"]["modifiers"]
	mods = []
	levrange = charac["level"]+1
	for lev in range(l[0], levrange):
		levobj = game[str(lev)]
		mods.extend(get_level_mods(levobj, charac))
	# Take in a character object who has a certain level attribute
	# Iterate over level objects from zero to character level
	# Add to a master list of mods at each level, add mods to character
	charac = apply_mods(charac, mods, rand)
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

def apply_mods(charac, mods, rand):
	PLR = 0
	for mod in mods:
		if mod[:3] in engine["Performance"]["Attribute"].keys():
			charac = apply_att_mod(charac, mod)
		elif mod[:3] == "PLR":
			PLR += int(mod[3:])
		else:
			charac = apply_stat_mod(charac, mod)
	if PLR > 0:
		charac = allocate_player_mods(charac, PLR, rand)
	return charac

def allocate_player_mods(charac, PLR, rand):
	if rand:
		random_mods = {"DEX":0,"MGT":0,"ART":0,"DIV":0,"INT":0,"CON":0}
		for num in range(0,PLR):
			key = random.choice(random_mods.keys())
			charac["attributes"][key] += 1
		return charac
	print "Lets allocate points to attributes!\n"
	print "You have %s points to spend" % str(PLR)
	print "Assign desired number of points to attribute, then press 'enter'"
	for key in engine["Performance"]["Attribute"]["list"]:
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
	for stat in engine["Performance"]["Stat"]["list"]:
		if stat in mod:
			if engine["Performance"]["Stat"][stat]["type"] == "int":
				diff = int(mod.replace(stat,""))
				if (diff != None) and (charac["stats"][stat] != None):
					charac["stats"][stat] = charac["stats"][stat] + diff
			else:
				new = mod.replace(stat,"")
				charac["stats"][stat] = new
	return charac

def get_stat_modifier(charac, statname):
	# General method for determining a stat modifier given an attribute va;ie
	key = engine["Performance"]["Stat"][statname]
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
	return engine["Performance"]["Attribute"][att]["Maps"][stat][str(charac["attributes"][att])]

def apply_att_stats(charac):
	# Apply all of the attribute-derived stat modifiers to the character
	for stat in the_stats:
		mod = get_stat_modifier(charac, stat)
		if isinstance(mod,int):
			if stat == "MaxHP":
				charac["stats"][stat] = charac["stats"][stat]+mod
			else:
				charac["stats"][stat] = mod
		else:
			charac["stats"][stat] = mod
	return charac

def get_inventory_from_strings(string_list):
	# Need to think about some things with this method
	inventory = []
	for thing in string_list:
		thing = thing.lower()
		itms = game["LISTS"]["Item"]
		wpns = game["LISTS"]["Weapon"]
		amrs = game["LISTS"]["Armor"]
		things = [wpns, amrs, itms]
		for a in things:
			if thing in a:
				inventory.append(game[thing])
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
		if string == thing["name"]:
			if thing["scheme"] == "Weapon" or thing["scheme"] == "Armor":
				equip(charac, thing)
			else:
				print "I cannot equip this."
				return
		else:
			continue

def meet_requirements(charac, thing):
	# Returns true if charac meets requirements to equip something
	for key, val in thing["requirements"].iteritems():
		if val == "type":
			check = game["TYPES"][thing["scheme"]][thing["type"]][key]
			if check == []:
				return True
			elif charac[key] not in check:
				return False
			else:
				return True
		elif key not in charac.keys():
			print "I don't know what attribute of the character to check"
			return False
		elif charac[key] not in val:
			return False
	return True

def equip(charac, thing):
	print "Equipping %s" % thing["name"]
	if thing.has_key("requirements"):
		if meet_requirements(charac, thing):
			print "Congrats on meeting the requirements, bruh"
			print thing
			charac["equipment"][thing["scheme"]] = thing
			if thing.has_key("spec_mods"):
				charac["equipment"]["eqp_mods"].extend(thing["spec_mods"])
				apply_mods(charac, charac["equipment"]["eqp_mods"], False)
		else:
			print "You do not meet the requirements to equip this"
	else:
		charac["equipment"][thing["scheme"]] = thing
		if thing.has_key("spec_mods"):
			charac["equipment"]["eqp_mods"].extend(thing["spec_mods"])
			apply_mods(charac, charac["equipment"]["eqp_mods"], False)

def get_learnable_skills(charac):
	learnable = []
	# Should consider a separate abstract skill validation method
	for string in game["LISTS"]["Skill"]:
		skill = game[string]
		for req in skill["requirements"].keys():
			if skill["requirements"][req] != []:
				if charac[req] not in skill["requirements"][req]:
					print "Cannot learn skill '%s'" % skill
				else:
					learnable.append(skill)
	return learnable
