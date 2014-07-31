# Character objects
# This class covers player characters, NPC's, and enemies as well
# The different types of characters can be denoted with the 'tag' attribute

from attStats import *
from levels import *
from content import Content
import json
import sys

e = Content().data

class Character(object):

	def __init__(self, make=None):

		self.name = "John Smith"

		self.character_class = "Base"

		self.tag = ""

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
				"MaxHP":10,"Evade":0,"Hit":0,
				"Accuracy":0,"PhyDef":"",
				"PhyAtk":"","MagDef":0,
				"MagAtk":0,"Resistance":0,
				"CarryStrength":0,"Craft":0
				}

		if make is not None:
			self.load(make)

	def load(self, charac):
		k = e[charac]
		self.name = charac
		self.character_class = k["character_class"]
		self.tag = k["tag"]
		self.level = int(k["level"])
		self.skills = k["skills"]
		self.equipment = k["equipment"]
		self.inventory = k["inventory"]
		self.carry_weight = int(k["carry_weight"])
		self.attributes = k["attributes"]
		self.stats = k["stats"]

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
		# Equips a weapon object. Performs some validation to ensure weapon is equipable
		if weapon not in self.inventory:
			return "Weapon not in inventory"
		elif self.character_class not in e[weapon.kind]["classes"]:
			print "%s class cannot equip %s weapon type" % (self.character_class, weapon.kind)
		else:
			self.equipment["weapon"] = weapon

	def equip_weapon_from_string(self, weapon_string):
		# Sometimes you want to equip a weapon knowing only the string name.
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
		# Add skill to skill list. Perform validation to make sure character can use it.
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
		mgt_adjusted = weight_penalty - int(self.stats["CarryStrength"])
		evade = int(self.stats["Evade"]) - mgt_adjusted
		self.stats["Evade"] = str(evade)

	def get_equipment_mods(self):
		mods = []
		if self.equipment["weapon"].name in e.keys():
			mods.extend(self.equipment["weapon"].spec_mods)
		elif self.equipment["armor"].name in e.keys():
			mods.extend(self.equipment["armor"].spec_mods)
		self.equipment["mods"] = mods
