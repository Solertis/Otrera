#!/usr/bin/env python

# Program for building games
# Publishes content to content.json

from content import Content
from engine import *
from character import Character
import json
import os

engine = Content().engine
game = Content().data

def get_input(prompt):
	return raw_input(prompt)

def create_game_directory_and_file(game_name):
	if os.path.exists("games/"+game_name):
		print "A game with this name already exists for this engine!!!"
		exit(1)
	else:
		os.makedirs("games/"+game_name)
		gamefile = open("games/"+game_name+"/content.json","w+")

def make_game(game_name):
	"""
	Top level method in game builder
	module for creating new games
	from scratch.
	"""
	create_game_directory_and_file(game_name)

if __name__ == "__main__":
	game_name = get_input("What is the name of your game?: ")
	make_game(game_name)
