# Item objects

import json

o = open("data/items.json","r").read()
l = json.loads(o)

class Weapon(object):

	def __init__(self):
		self.name = "generic item"
		self.kind = "usable"
		self.weight = "1"
		self.effect = "none"
		self.special = {}
		self.durability = "1"
