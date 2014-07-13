# Weapon objects

import json

o = open("data/weapons.json","r").read()
l = json.loads(o)

types = ["sword","bow","staff","glove"]

def get_weapon_type(weapon):
	for weapon_type in types:
		search_list = l[weapon_type]["instances"].keys()
		if weapon in search_list:
			return weapon_type

class Weapon(object):

	def __init__(self):
		self.name = "generic sword"
		self.kind = "generic type"
		self.weight = "1"
		self.base_pwr = "1"
		self.spec_mods = []
		self.durability = "1"
	
	def load(self, weapon):
		weapon_type = get_weapon_type(weapon)
		weapon_data = l[weapon_type]["instances"][weapon]
		self.name = weapon
		self.kind = weapon_type
		self.weight = weapon_data["weight"]
		self.base_pwr = weapon_data["base_pwr"]
		self.spec_mods = weapon_data["spec_mods"]
		self.attack_range = int(l[self.kind]["range"])
