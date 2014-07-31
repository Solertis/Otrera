from attStats import *
import json
from content import Content
e = Content().data

class Skill(object):

	def __init__(self, make=None):

		self.name = ""

		self.category = "" # There are attribute skills and class skills

		self.flavor = "" # This is just a descriptive tag to further categorize skills

		self.requirements = {
				"Class" : [], #Empty set means any class can learn
				"Attributes" : ["DEX10","DIV5"], #Minimum attribute scores needed
				"Level" : "1" #Minimum character level
				}

		self.restrictions = {
				"Equipment" : [], # Types of weapons or armor or even specific things
				"Status" : [], # Status ailments that prevent use of skill
				"Stats" : [] # HP > 10 for example
				}

		self.effect = { 
				"Description" : "Text description of skill",
				"Power" : "1d6", # May be fixed int, dice roll, 'scaling', or some combination
				"Element" : "",
				"Inflicts" : "", #Status ailment, skill check against d20 to inflict
				"AOE" : "", #Shape / size of area affected by skill
				"Range" : "1", #How far from the user can I set the skill
				"Time" : "0" #How long does skill take to occur. Most are 0, magic will be more
				}
		self.uses = 1 # The number of times a skill can be used in battle

		if make is not None:
			self.load(make)

	def load(self, skill):
		skill = skill.lower()
		k = e[skill]
		self.name = skill
		self.category = k["category"]
		self.flavor = k["flavor"]
		self.requirements = k["requirements"]
		self.effect = k["effect"]
		self.uses = int(k["uses"])
