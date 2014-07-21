# Armor objects

import json

o = open("data/everything.json","r").read()
e = json.loads(o)

class Armor(object):

	def __init__(self, make=None):
		self.name = "generic armor"
		self.kind = "cloth"
		self.weight = "1"
		self.spec_mods = []
		self.durability = "5"
		self.defense = "1d4"
		if make is not None:
			self.load(make)
	
	def load(self, armor):
		k = e[armor]
		self.name = armor
		self.kind = k["kind"]
		self.weight = k["weight"]
		self.spec_mods = k["spec_mods"]
		self.durability = k["durability"]
		self.defense = e[k["kind"]]["defense"]
