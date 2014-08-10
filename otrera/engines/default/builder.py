#!/usr/bin/env python
# Program for building characters
# For now it just prints character info to the console
# We need to give this script the ability to save characters as JSON blobs.

from content import Content
from engine import *
from character import Character
import json

engine = Content().engine

def level_zero_character_builder():
	zero_character = engine["Character"]["Player"]
	print "Give me some stats, bro\n"
	base_character = get_base_attributes(zero_character)
	print "\nOK! Let's get those stats!\n"
	print "---------------------------------------------------\n"
	level_zero_character = apply_att_stats(base_character)
	return level_zero_character

def custom_level_naked_character_builder():
	if engine.has_key("Progression"):
		l = engine["Progression"]["Level"]
		mods = []
		charac = level_zero_character_builder()
		charac["level"] = int(raw_input("What is the character's level?: "))
		charac["class"] = raw_input("What is the character's class?: ").lower().strip()
		ans = raw_input("Do you want to randomly apply level bonuses? y/n: ")
		if ans == "y":
			final_charac = apply_level_mods(charac, rand=True)
		else:
			final_charac = apply_level_mods(charac)
		custom_charac = apply_att_stats(final_charac)
		return custom_charac
	else:
		print "Engine has no concept of 'levels"

def fully_equipped_character_builder():
	full_charac = custom_level_naked_character_builder()
	print "Cool! Lets add some equipment"
	inventory_list = raw_input("Give me a list of inventory separated by commas: ")
	inv_list = inventory_list.split(",")
	fin_list = []
	for thing in inv_list:
		thing = thing.lstrip()
		fin_list.append(thing)
	full_charac["inventory"] = get_inventory_from_strings(fin_list)
	final_charac = user_sets_equipment(full_charac, full_charac["inventory"])
	return final_charac

def complete_character_builder():
	charac = fully_equipped_character_builder()
	print "Score! Lets complete the character by choosing skills"
	eligible = get_learnable_skills(charac)
	charac = user_picks_skills(charac, eligible)
	return charac

def user_sets_equipment(charac, inventory):
	print "Here is your inventory: "
	for item in inventory:
		print item["name"]
	print "Name the item you wish to equip"
	w = raw_input("Select your weapon: ").lower()
	a = raw_input("Select your armor: ").lower()
	equip_from_string(charac, w)
	equip_from_string(charac, a)
	return charac

def user_picks_skills(charac, eligible_skills):
	print "Here are your eligible skills:"
	for thing in eligible_skills:
		print thing["name"]
	print "You may select %s skills (character level)\n" % str(charac["level"])
	selected = raw_input("Enter a comma-separated list: ")
	list_names = selected.split(",")
	skill_names = []
	for item in list_names:
		item = item.lstrip()
		skill_names.append(item)
	for item in eligible_skills:
		if item["name"] in skill_names:
			charac["skills"].append(item)
	return charac

def get_base_attributes(charac):

	try:
		charac["name"] = raw_input("Name your character: ")
		charac["sex"] = raw_input("What is your sex?: ")
		DEX = int(raw_input("Dexterity: "))
		ART = int(raw_input("Artistry: "))
		MGT = int(raw_input("Might: "))
		DIV = int(raw_input("Divine: "))
		INT = int(raw_input("Intelligence: "))
		CON = int(raw_input("Constitution: "))
	except ValueError:
		print "Stats must be a number"
		get_base_attributes(charac)

	charac["attributes"] = {
			"DEX":DEX,"ART":ART,"MGT":MGT,"DIV":DIV,"INT":INT,"CON":CON
			}
	return charac

def publish_character(charac):
	stats = charac["stats"]
	print "Character Name: %s" % charac["name"]
	print "MaxHP = %s" % str(stats["MaxHP"])
	print "Evade = %s" % str(stats["Evade"])
	print "Hit = %s" % str(stats["Hit"])
	print "Accuracy = %s" %str(stats["Accuracy"])
	print "Physical Defense = %s" % str(stats["PhyDef"])
	print "Physical Attack = %s" % str(stats["PhyAtk"])
	print "Magical Defense = %s" % str(stats["MagDef"])
	print "Magical Attack = %s" % str(stats["MagAtk"])
	print "Resistance = %s" % str(stats["Resistance"])
	print "Carry Strength = %s" % str(stats["CarryStrength"])
	print "Craft = %s" % str(stats["Craft"])
	print "ATTRIBUTES\n"
	print charac["attributes"]

def publish_charac_combat_stats(charac):
	print "Here is your character's combat profile:"
	print "-------------------------------------------------\n"
	print "PWR = %s %s" % (charac["equipment"]["weapon"]["base_dmg"], charac["stats"]["PhyAtk"])
	print "Armor Durability = %s" % str(charac["equipment"]["armor"]["durability"])
	print "Armor Defense = %s" % charac["equipment"]["armor"]["defense"]
	print "Encumbrance = %s" % str(charac["encumbrance"])
	print "Equipment Bonuses = %s" % (charac["equipment"]["eqp_mods"])
	print "NOTE: Evade score now accounts for Carry Weight penalty (adjusted for strength)"

def publish_charac_skills(charac):
	print "--------------------------------------------------\n"
	print "Here is a list of your character's skills: "
	for item in charac["skills"]:
		print item["name"]
	return

def publish_complete_character(charac):
	publish_character(charac)
	publish_charac_combat_stats(charac)
	publish_charac_skills(charac)

def choose_program():
	print "Welcome to the Mythology Character Builder!\n"
	print "---------------------------------------------------"
	print "Press '1' to build a level 0 character"
	print "Press '2' to build a custom level character"
	print "Press '3' to build a custom level character with equipment"
	print "Press '4' to build a complete character with skills and equipment"
	print "Press any other key to exit"
	user_input = raw_input("Enter a number and press 'enter': ")
	if user_input == "1":
		character = level_zero_character_builder()
		publish_character(character)
	elif user_input == "2":
		character = custom_level_naked_character_builder()
		publish_character(character)
	elif user_input == "3":
		character = fully_equipped_character_builder()
		publish_character(character)
		publish_charac_combat_stats(character)
	elif user_input == "4":
		charac = complete_character_builder()
		publish_complete_character(charac)
	else:
		return

def main():
	choose_program()

if __name__=="__main__":
	main()
