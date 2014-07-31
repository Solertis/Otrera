# Methods for defining a character's stats and skills

from skills import *
import json
from content import Content

e = Content().data
a = open("engine.json","r").read()
b = json.loads(a)

the_stats = ["Evade","PhyDef","PhyAtk","MagAtk","MagDef",
			"Resistance","CarryStrength","Hit","Accuracy",
			"Craft","MaxHP"]

def get_stat_modifier(charac, statname):
	# General method for determining a stat modifier given an attribute va;ie
	key = b[statname]
	attMaps = key["attMaps"]
	if len(attMaps) == 1:
		return get_att_modifier(attMaps[0], statname, charac)
	else:
		vals = []
		if "COMB" in attMaps:
			attMaps.remove("COMB")
			for att in attMaps:
				vals.append(charac["attributes"][att])
			total = sum(vals)
			return key['calc'][str(total)]
		else:
			for att in attMaps:
				vals.append(get_att_modifier(att, statname, charac))
		return sum(vals)

def get_att_modifier(att, stat, charac):
	# Return the modifier mapped to a given attribute value
	return b[att]["StatMaps"][stat][str(charac["attributes"][att])]

def apply_att_stats(charac):
	# Apply all of the attribute-derived stat modifiers to the character
	for stat in the_stats:
		mod = get_stat_modifier(charac, stat)
		if isinstance(mod,int):
			charac["stats"][stat] = charac["stats"][stat]+mod
		else:
			charac["stats"][stat] = mod
	return charac

def get_class_skills(charac):
	# Find the list of class skills in everything.json and 
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
