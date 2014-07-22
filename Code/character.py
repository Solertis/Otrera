from attStats import *
from levels import *
from attMappings import *
from content import Content
import json
import sys

e = Content().data

class Character(object):

	def __init__(self):

		self.name = "John Smith"

		self.character_class = "Base"

		self.level = 0

		self.skills = []

		self.equipment = {
				"weapon" : "naked",
				"armor" : "naked",
				"mods" : []
				}

		self.inventory = []

		self.carry_weight = 0

		self.attributes = {
				"DEX":0,"ART":0,"MGT":0,
				"DIV":0,"INT":0,"CON":0
				}

		self.stats = {
				"MaxHP":"1","Evade":"0","Hit":"0",
				"Accuracy":"0","Physical Defense":"0",
				"Physical Attack":"0","Magical Defense":"0",
				"Magical Attack":"0","Resistance":"0",
				"Carry Strength":"0","Casting Speed":"0",
				"Spell Memory":"0","Spell Failure":"0","Craft":"0"
				}

	def set_attribute(self, attribute, value):
		self.attributes[attribute] = int(value)

	def set_stat(self, stat, value):
		self.stats[stat] = str(value)

	def set_name(self, name):
		self.name = name

	def equip_armor(self, armor):
		if armor not in self.inventory:
			return "Armor not in inventory"
		elif self.character_class not in e[armor.kind]["classes"]:
			print "%s class cannot equip %s armor type" % (self.character_class, armor.kind)
		else:
			self.equipment["armor"] = armor

	def equip_weapon(self, weapon):
		if weapon not in self.inventory:
			return "Weapon not in inventory"
		elif self.character_class not in e[weapon.kind]["classes"]:
			print "%s class cannot equip %s weapon type" % (self.character_class, weapon.kind)
		else:
			self.equipment["weapon"] = weapon

	def equip_weapon_from_string(self, weapon_string):
		for item in self.inventory:
			if item.name == weapon_string:
				self.equip_weapon(item)
		return "Weapon not found."

	def equip_armor_from_string(self, armor_string):
		for item in self.inventory:
			if item.name == armor_string:
				self.equip_armor(item)
		return "Armor not found."

	def add_skill(self, skill_obj):
		req = skill_obj.requirements
		if int(req["Level"]) > self.level:
			print "Character level too low to acquire this skill"
			exit()
		elif req["Class"] != []:
			if self.character_class not in req["Class"]:
				print "Character is the wrong class to acquire this skill"
				exit()
		elif req["Attributes"] != []:
			for att in req["Attributes"]:
				if self.attributes[att[:3]] < int(att[3:]):
					print "Character does not meet attribute requirement for skill"
					exit()
		self.skills.append(skill_obj)

	def set_carry_weight(self):
		weight = 0
		for item in self.inventory:
			weight += int(item.weight)
		self.carry_weight = weight

	def adjust_evade(self):
		# Adjust for inventory weight and carry strength
		self.set_carry_weight()
		weight_penalty = self.carry_weight/10
		mgt_adjusted = weight_penalty - int(self.stats["Carry Strength"])
		evade = int(self.stats["Evade"]) - mgt_adjusted
		self.stats["Evade"] = str(evade)

	def get_equipment_mods(self):
		mods = []
		if self.equipment["weapon"].name in e.keys():
			mods.extend(self.equipment["weapon"].spec_mods)
		elif self.equipment["armor"].name in e.keys():
			mods.extend(self.equipment["armor"].spec_mods)
		self.equipment["mods"] = mods
