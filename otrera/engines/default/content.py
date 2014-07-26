# Class for handling everything.json
# The 'game' variable may be passed in by the user at runtime.
# This allows an engine to load a specific game's everything.json

import json

class Content(object):

	def __init__(self, game=None):
		if game==None:
			default_path = "games/default/everything.json"
			f = open(default_path,"r").read()
			data=json.loads(f)
			self.data = data
			self.path = default_path
		else:
			game_path = "games/"+game+"/everything.json"
			f = open(game_path,"r").read()
			data=json.loads(f)
			self.data = data
			self.path = game_path
