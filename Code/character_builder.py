#!/usr/bin/env python

from attStats import *
from levels import *
from character import Character

def level_zero_character_builder():
	zero_character = Character()
	print "Give me some stats, bro\n"
	base_character = get_base_attributes(zero_character)
	print "\nOK! Let's get those stats!\n"
	print "---------------------------------------------------\n"
	base_character.stats = get_stats(base_character.attributes)
	publish_character(base_character.stats)

def custom_level_character_builder():
	charac = Character()
	print "Ok, lets make a custom level character.\n"
	charac.level = int(raw_input("What is the character's level?: "))
	charac.character_class = raw_input("What is the character's class?: ").lower().strip()
	print "OK! Let's get some base stats.\n"
	full_charac =  get_base_attributes(charac)
	level_mods = get_level_mods(full_charac.character_class, full_charac.level)
	for key in full_charac.attributes.keys():
		full_charac.attributes[key] = full_charac.attributes[key] + int(level_mods[key])
	full_charac.stats = get_stats(full_charac.attributes)
	print "---------------------------------------------------\n"
	publish_character(full_charac.stats)

def get_base_attributes(charac):
	DEX = int(raw_input("Dexterity: "))
	ART = int(raw_input("Artistry: "))
	MGT = int(raw_input("Might: "))
	DIV = int(raw_input("Divine: "))
	INT = int(raw_input("Intelligence: "))
	CON = int(raw_input("Constitution: "))
	charac.attributes = {
			"DEX":DEX,"ART":ART,"MGT":MGT,"DIV":DIV,"INT":INT,"CON":CON
			}
	return charac

def publish_character(stats):
	print "MaxHP = %s" % str(stats["maxHP"])
	print "Evade = %s" % str(stats["Evade"])
	print "Hit = %s" % str(stats["Hit"])
	print "Accuracy = %s" %str(stats["Accuracy"])
	print "Physical Defense = %s" % str(stats["Physical Defense"])
	print "Physical Attack = %s" % str(stats["Physical Attack"])
	print "Magical Defense = %s" % str(stats["Magical Defense"])
	print "Magical Attack = %s" % str(stats["Magical Attack"])
	print "Resistance = %s" % str(stats["Resistance"])
	print "Carry Strength = %s" % str(stats["Carry Strength"])
	print "Casting Speed = %s" % str(stats["Casting Speed"])
	print "Spell Memory = %s" % str(stats["Spell Memory"])
	print "Spell Failure = %s" % str(stats["Spell Failure"])
	print "Craft = %s" % str(stats["Craft"])
	print "--------------------------------------------------\n\n"
	print "Enjoy your character!"

def choose_program():
	print "Welcome to the Mythology Character Builder!\n"
	print "---------------------------------------------------"
	print "Press '1' to build a level 0 character"
	print "Press '2' to build a custom level character"
	print "Press any other key to exit"
	user_input = raw_input("Enter a number and press 'enter': ")
	if user_input == "1":
		level_zero_character_builder()
	elif user_input == "2":
		custom_level_character_builder()
	else:
		return

def main():
	choose_program()

if __name__=="__main__":
	main()
