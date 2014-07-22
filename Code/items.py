# Item objects

import json
from weapons import Weapon as w
from armors import Armor as a
from content import Content

e = Content().data

weapon_types = ["sword","bow","glove","staff"]
armor_types = ["leather","cloth","robes","metal"]
item_types = ["usable","gear"]

class Item(object):

	def __init__(self, make=None):
		self.name = "generic item"
		self.kind = "usable"
		self.weight = "1"
		self.effect = "none"
		self.special = {}
		self.durability = "1"
		if make is not None:
			self.load(make)

	def load(self, item):
		k = e[item]
		self.name = item
		self.kind = k["kind"]
		self.weight = k["weight"]
		self.effect = k["effect"]
		self.special = k["special"]
		self.durability = k["durability"]

def get_inventory_from_string_list(string_list):
	inventory = []
	string_list = string_list
	for thing in string_list:
		thing = thing.strip()
		thing_type = e[thing]["kind"]
		if thing_type in weapon_types:
			weap = w(make=thing)
			inventory.append(weap)
		elif thing_type in armor_types:
			arm = a(make=thing)
			inventory.append(arm)
		elif thing_type in item_types:
			itm = Item(make=thing)
			inventory.append(itm)
		else:
			print "I am twelve years old and what is this"
			return
	return inventory

