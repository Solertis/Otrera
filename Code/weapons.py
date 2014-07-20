# Weapon objects

import json

o = open("data/everything.json","r").read()
e = json.loads(o)

types = ["sword","bow","staff","glove"]

class Weapon(object):

	def __init__(self, make=None):
		self.name = "generic sword"
		self.kind = "generic type"
		self.weight = "1"
		self.base_pwr = "1"
		self.spec_mods = []
		self.durability = "1"
		if make is not None:
			self.load(make)
	
	def load(self, weapon):
		k = e[weapon]
		self.name = weapon
		self.kind = k["kind"]
		self.weight = k["weight"]
		self.base_pwr = k["base_pwr"]
		self.durability = k["durability"]
		self.spec_mods = k["spec_mods"]
