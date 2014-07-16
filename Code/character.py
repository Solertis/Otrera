from attStats import *
from levels import *
from attMappings import *
import json

b = open("data/everything.json","r").read()
e = json.loads(b)

class Character(object):

	def __init__(self):

		self.name = "John Smith"

		self.character_class = "Base"

		self.level = 0

		self.skills = {}

		self.spells = {}

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
		else:
			self.equipment["armor"] = armor

	def equip_weapon(self, weapon):
		if weapon not in self.inventory:
			return "Weapon not in inventory"
		else:
			self.equipment["weapon"] = weapon

	def equip_weapon_from_string(self, weapon_string):
		for item in self.inventory:
			if item.name == weapon_string:
				print "Equipping weapon"
				self.equip_weapon(item)
		return "Weapon not found."

	def equip_armor_from_string(self, armor_string):
		for item in self.inventory:
			if item.name == armor_string:
				print "Equipping armor"
				self.equip_armor(item)
		return "Armor not found."

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
