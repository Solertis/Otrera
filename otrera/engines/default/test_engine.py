#!/usr/bin/env python

import mock
from builder import *
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

def test_att_stats():
	charac = engine["CHARACTER"]
	charac = apply_att_stats(charac)
	check_stats(charac, 10,-4,-4,-4,"1d4","1d2",-4,"1d2",-2,-2,-6)
