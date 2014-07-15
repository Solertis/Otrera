from attStats import *
from levels import *
from attMappings import *

class Character(object):

	def __init__(self):

		self.name = "John Smith"

		self.character_class = "Base"

		self.level = 0

		self.skills = {}

		self.spells = {}

		self.equipment = {
				"RH" : "none",
				"LH" : "none",
				"armor" : "naked"
				"mods" : get_equipment_mods(self.equipment)
				}

		self.inventory = []

		self.carry_weight = set_carry_weight(self)

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
			self.equipment["RH"] = weapon

	def set_carry_weight(self):
		weight = 0
		for item in inventory:
			weight += int(item.weight)
		self.carry_weight = weight

	def get_equipment_mods(eqp):
		mods = []
		if eqp["RH"] is not "none":
			mods.extend(eqp["RH"].spec_mods
