# Methods for defining a character's stats and skills

from attMappings import *
from skills import *
import json

relevant_attributes = {
	"Evade" : ["DEX","ART"], "Physical Defense" : ["MGT","CON"],
	"MaxHP" : ["CON"], "Magical Defense" : ["DIV","INT"],
	"Resistance" : ["CON"], "Hit" : ["DEX","ART"], "RHIT" : ["DEX"],
	"Magic Attack" : ["DIV"], "Craft" : ["DEX","INT","ART"],
	"Physical Attack" : ["MGT"], "Carry Strength" : ["MGT"],
	"Casting Speed" : ["ART"], "Spell Failure" : ["INT","ART"]
	}

k = open("data/class_skills.json","r").read()
c = json.loads(k)

b = open("data/attribute_skills.json","r").read()
a = json.loads(b)

def get_evade(DEX, ART):
	dex_modifier = dex_to_evade(DEX)
	art_modifier = art_to_evade(ART)
	total_modifier = dex_modifier + art_modifier
	return total_modifier

def get_physical_attack(MGT):
	dice = mgt_to_atk(MGT)
	return dice

def get_physical_defense(MGT, CON):
	dice = mgt_con_to_def(MGT, CON)
	return dice

def get_maxHP(CON):
	bonus = con_to_maxHP(CON)
	HP = 20 + bonus
	return HP

def get_magic_defense(DIV,ART):
	return div_art_to_magic_defense(DIV,ART)

def get_resistance(CON):
	res = con_to_resistance(CON)
	return res

def get_hit(DEX,ART):
	dex_bonus = dex_to_hit(DEX)
	art_bonus = art_to_hit(ART)
	total = dex_bonus + art_bonus
	return total

def get_accuracy(DEX):
	rhit = dex_to_accuracy(DEX)
	return rhit

def get_magic_attack(DIV):
	dice = div_to_magic_attack(DIV)
	return dice

def get_melee_attack(MGT):
	return mgt_to_attack(MGT)

def get_carry_strength(MGT):
	return mgt_to_carry_strength(MGT)

def get_casting_speed(ART):
	return art_to_casting_speed(ART)

def get_spell_failure(INT,ART):
	total = art_to_spell_fail(ART) + int_to_spell_fail(INT)
	return total

def get_craft(INT,ART,DEX):
	int_bonus = int_to_craft(INT)
	dex_art_bonus = dex_art_to_craft(DEX,ART)
	total = int_bonus+dex_art_bonus
	return total

def get_stats(atts):
	stats = {}
	stats["maxHP"] = get_maxHP(atts["CON"])
	stats["Evade"] = get_evade(atts["DEX"],atts["ART"])
	stats["Hit"] = get_hit(atts["DEX"],atts["ART"])
	stats["Accuracy"] = get_accuracy(atts["DEX"])
	stats["Physical Defense"] = get_physical_defense(atts["MGT"],atts["CON"])
	stats["Physical Attack"] = get_physical_attack(atts["MGT"])
	stats["Magical Defense"] = get_magic_defense(atts["DIV"],atts["ART"])
	stats["Magical Attack"] = get_magic_attack(atts["DIV"])
	stats["Resistance"] = get_resistance(atts["CON"])
	stats["Carry Strength"] = get_carry_strength(atts["MGT"])
	stats["Casting Speed"] = get_casting_speed(atts["ART"])
	stats["Spell Failure"] = get_spell_failure(atts["INT"],atts["ART"])
	stats["Craft"] = get_craft(atts["INT"],atts["ART"],atts["DEX"])
	return stats

def get_class_skills(charac):
	class_skills = c[charac.character_class]
	skill_object_list = []
	for thing in class_skills:
		skill_object = Skill(make=thing)
		skill_object_list.append(skill_object)
	return skill_object_list

def get_attribute_skills(charac):
	skill_list = []
	skill_object_list = []
	for k, v in a.iteritems():
		for score in v.keys():
			if int(score) <= charac.attributes[k]:
				skill_list.extend(v[score])
	for thing in skill_list:
		obj = Skill(make=thing)
		skill_object_list.append(obj)
	return skill_object_list
