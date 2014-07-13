# Weapon objects

import json

o = open("weapons.json","r").read()
l = json.loads(o)

class Weapon(object):

	def __init__(self):
		self.name = "generic sword"
		self.kind = "sword"
		self.weight = "1"
		self.base_pwr = "1"
		self.spec_mods = []
		self.durability = "1"
		self.attack_range = int(l[self.kind]["range"])
