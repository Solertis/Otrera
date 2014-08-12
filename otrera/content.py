# Class for handling everything.json
# The 'game' variable may be passed in by the user at runtime.
# This allows an engine to load a specific game's everything.json

import json

default_engine_path = "engines/default/engine.json"
default_content_path = "engines/default/games/default/content.json"

class Content(object):

	def __init__(self, engine=None, game=None):
		if engine==None:
			r = open(default_engine_path,"r").read()
			self.engine=json.loads(r)
			self.engine_path = default_engine_path
		else:
			r = open(engine,"r").read()
			self.engine=json.loads(r)
			self.engine_path = engine
		if game==None:
			f = open(default_content_path,"r").read()
			self.data = json.loads(f)
			self.game_path = default_content_path
		else:
			game_path = self.engine_path+"/games/"+game+"content.json"
			f = open(game_path,"r").read()
			self.data=json.loads(f)
			self.game_path = game_path
