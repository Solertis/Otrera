#Class objects

import json
from content import Content

e = Content().data

class Class(object):

	def __init__(self, make=None):
		self.name = ""
		self.level_atts = {}
		if make is not None:
			self.load(make)

	def load(self, clas):
		k = e[clas]
		self.name = clas
		self.level_atts = k
