#!/usr/bin/env python

from attStats import *

def character_builder():
	print "Give me some stats, bro\n"
	DEX = int(raw_input("Dexterity: "))
	ART = int(raw_input("Artistry: "))
	MGT = int(raw_input("Might: "))
	DIV = int(raw_input("Divine: "))
	INT = int(raw_input("Intelligence: "))
	CON = int(raw_input("Constitution: "))
	print "\nOK! Let's get those stats!\n"
	print "---------------------------------------------------\n"
	print "MaxHP = %s" % str(get_maxHP(CON))
	print "Evade = %s" % str(get_evade(DEX,ART))
	print "Hit = %s" % str(get_hit(DEX,ART))
	print "Ranged Hit = %s" %str(get_rhit(DEX))
	print "Physical Defense = %s" % str(get_physical_defense(MGT,CON))
	print "Physical Attack = %s" % str(get_physical_attack(MGT))
	print "Magical Defense = %s" % str(get_magic_defense(DIV,ART))
	print "Magical Attack = %s" % str(get_magic_attack(DIV))
	print "Resistance = %s" % str(get_resistance(CON))
	print "Carry Strength = %s" % str(get_carry_strength(MGT))
	print "Casting Speed = %s" % str(get_casting_speed(ART))
	print "Spell Memory = %s" % str(get_spell_memory(INT))
	print "Spell Failure = %s" % str(get_spell_failure(INT,ART))
	print "Craft = %s" % str(get_craft(INT,ART,DEX))
	print "--------------------------------------------------\n\n"
	print "Enjoy your character!"

def main():
	character_builder()

if __name__=="__main__":
	main()
