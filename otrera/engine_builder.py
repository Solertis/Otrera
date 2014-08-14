import json
import os
from shutil import copyfile

constructs = ["Progression","Performance","Equipment", 
			"Story","Rules", "Ability", "Character",
			"Elective","Inherent", "Setting"]

def make_engine(name):
	if os.path.exists("engines/"+name):
		print "An engine with this name already exists."
		exit(1)
	else:
		os.makedirs("engines/"+name)
		copyfile("template.json", "engines/"+name+"/engine.json") 
