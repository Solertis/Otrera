# Class for handling everything.json

import json

class Content(object):

	def __init__(self, game=None):
		if game==None:
			f = open("games/default/everything.json","r").read()
			data=json.loads(f)
			self.data = data
		else:
			f = open("games/"+game+"/everything.json","r").read()
			data=json.loads(f)
			self.data = data
