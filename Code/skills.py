from levels import *
from attStats import *
import json

b = open("data/everything.json","r").read()
e = json.loads(b)
r = open("data/types.json","r").read()
t = json.loads(r)

class Skill(object):

	def __init__(self, make=None):

		self.name = ""

		self.category = "" # There are attribute skills and class skills

		self.flavor = "" # This is just a descriptive tag to further categorize skills

		self.rank = 1 # Yet another way of categorizing skills by relative power / difficulty

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
				"Base" : "3", # Minimum effect
				"Element" : "",
				"Status" : "POISON, 10", #Status ailment, skill check against d20 to inflict
				"AOE" : "Touch, 1", #Shape / size of area affected by skill
				"Range" : 1, #How far from the user can I set the skill
				"Time" : 0 #How long does skill take to occur. Most are 0, magic will be more
				}
		self.uses = 1 # The number of times a skill can be used in battle

		if make is not None:
			self.load(make)

	def load(self, skill):
		k = e[skill]
		self.name = skill
		self.category = k["category"]
		self.flavor = k["flavor"]
		self.rank = int(k["rank"])
		self.requirements = k["requirements"]
		self.effect = k["effect"]
		self.uses = int(k["uses"])
