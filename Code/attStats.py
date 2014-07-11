# Data file with info on how attributes influence stats
from attMappings import *

relevant_attributes = {
	"Evade" : ["DEX","ART"], "Physical Defense" : ["MGT","CON"],
	"MaxHP" : ["CON"], "Magical Defense" : ["DIV","INT"],
	"Resistance" : ["CON"], "Hit" : ["DEX","ART"], "RHIT" : ["DEX"],
	"Spell Memory" : ["INT"], "Magic Attack" : ["DIV"], "Craft" : ["DEX","INT","ART"],
	"Physical Attack" : ["MGT"], "Carry Strength" : ["MGT"],
	"Casting Speed" : ["ART"], "Spell Failure" : ["INT","ART"]
	}

def get_evade(DEX, ART):
	dex_modifier = dex_to_evade(DEX)
	art_modifier = art_to_evade(ART)
	total_modifier = dex_modifier + art_modifier
	return total_modifier

def get_physical_attack(MGT):
	dice = mgt_to_atk(MGT)
	return dice

def get_physical_defense(MGT, CON):
	dice = mgt_con_to_def(MGT, CON)
	return dice

def get_maxHP(CON):
	bonus = con_to_maxHP(CON)
	HP = 20 + bonus
	return HP

def get_magic_defense(DIV,ART):
	return div_art_to_magic_defense(DIV,ART)

def get_resistance(CON):
	res = con_to_resistance(CON)
	return res

def get_hit(DEX,ART):
	dex_bonus = dex_to_hit(DEX)
	art_bonus = art_to_hit(ART)
	total = dex_bonus + art_bonus
	return total

def get_rhit(DEX):
	rhit = dex_to_rhit(DEX)
	return rhit

def get_spell_memory(INT):
	spell_memory = int_to_spell_memory(INT)
	return spell_memory

def get_magic_attack(DIV):
	dice = div_to_magic_attack(DIV)
	return dice

def get_melee_attack(MGT):
	return mgt_to_attack(MGT)

def get_carry_strength(MGT):
	return mgt_to_carry_strength(MGT)

def get_casting_speed(ART):
	return art_to_casting_speed(ART)

def get_spell_failure(INT,ART):
	total = art_to_spell_fail(ART) + int_to_spell_fail(INT)
	return total

def get_craft(INT,ART,DEX):
	int_bonus = int_to_craft(INT)
	dex_art_bonus = dex_art_to_craft(DEX,ART)
	total = int_bonus+dex_art_bonus
	return total
