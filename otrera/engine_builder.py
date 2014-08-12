import json
import os

constructs = ["Progression","Performance","Equipment",
				"Ability","Elective","Inherent"]

def make_engine(name):
	if os.path.exists(name):
		print "An engine with this name already exists."
		exit(1)
	else:
		os.makedirs(name)
		enginefile = open(name+"/engine.json","w+")
	pass

def select_constructs():
	pass
