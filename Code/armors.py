# Armor objects

import json

o = open("data/armor.json","r").read()
l = json.loads(o)

class Armor(object):

	def __init__(self):
		self.name = "generic armor"
		self.kind = "cloth"
		self.weight = "1"
		self.defense_dice = "1d4"
		self.spec_mods = []
		self.durability = "5"
