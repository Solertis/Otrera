# Class for handling everything.json

import json

class Content(object):

	def __init__(self):
		f = open("data/everything.json","r").read()
		data=json.loads(f)
		self.data = data
