# Item objects

import json

o = open("data/items.json","r").read()
l = json.loads(o)

a = open("data/weapons.json","r").read()
b = json.loads(a)

x = open("data/armors.json","r").read()
y = json.loads(x)

class Weapon(object):

	def __init__(self)
		self.name = "generic item"
		self.kind = "usable"
		self.weight = "1"
		self.effect = "none"
		self.special = {}
		self.durability = "1"


def get_inventory_from_string_list(string_list):

