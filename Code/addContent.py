import json

o = open("data/everything.json","r").read()
e = json.loads

# Load up everything.json, append new dicts based on templates
# From help(json) -- use this to print the final document????!!!!
#s = json.dumps({'4': 5, '6': 7}, sort_keys=True, indent=4)
#print '\n'.join([l.rstrip() for l in  s.splitlines()])
