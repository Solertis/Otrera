#!/usr/bin/env python

import mock
from player import *
from content import Content
from engine import *
engine = Content().engine
import pytest

def check_stats(charac,hp,evd,hit,acc,df,atk,mdf,mtk,res,cst,crf):
	assert charac["stats"]["MaxHP"] == hp
	assert charac["stats"]["Evade"] == evd
	assert charac["stats"]["Hit"] == hit
	assert charac["stats"]["Accuracy"] == acc
	assert charac["stats"]["PhyDef"] == df
	assert charac["stats"]["PhyAtk"] == atk
	assert charac["stats"]["MagDef"] == mdf
	assert charac["stats"]["MagAtk"] == mtk
	assert charac["stats"]["Resistance"] == res 
	assert charac["stats"]["CarryStrength"] == cst
	assert charac["stats"]["Craft"] == crf

def test_default_character():
	charac = engine["Character"]["Player"]
	charac = apply_att_stats(charac)
	check_stats(charac, 10,-4,-4,-4,"1d4","1d2",-4,"1d2",-2,-2,-6)

def test_leveled_character():
	charac = engine["Character"]["Player"]
	charac["attributes"]={"DEX":5,"ART":5,"MGT":5,"INT":5,"DIV":5,"CON":5}
	charac = apply_att_stats(charac)
	base_hp = charac["stats"]["MaxHP"]
	charac["level"] = 10
	charac["class"] = "mage"
	charac = apply_level_mods(charac, rand=True)
	charac = apply_att_stats(charac)
	assert charac["stats"]["MaxHP"] > (base_hp+45)

def test_equipped_character():
	charac = engine["Character"]["Player"]
	charac["class"] = "mage"
	charac["sex"] = "female"
	gear = ["mage staff", "mage robes"]
	charac["inventory"] = get_inventory_from_strings(gear)
	equip_from_string(charac, "mage staff")
	equip_from_string(charac, "mage robes")
	assert charac["equipment"]["weapon"]["name"] == "mage staff"
	assert charac["equipment"]["armor"]["name"] == "mage robes"
	assert charac["equipment"]["eqp_mods"] == [ "DIV2" ]

def test_skilled_character():
	charac = engine["Character"]["Player"]
	charac["class"] = "mage"
	learnable = get_learnable_skills(charac)
	charac["skills"].append(learnable[0])
	skill = charac["skills"][0]
	assert skill["name"] == "fire blast"
	assert skill["AOE"] == 3
	assert skill["power"] == "1d6"
	assert "mage" in skill["requirements"]["class"]
