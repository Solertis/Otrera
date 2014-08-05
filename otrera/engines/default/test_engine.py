#!/usr/bin/env python

import mock
from builder import *
from content import Content
from engine import *
engine = Content().engine
import pytest

def test_att_stats():
	char = engine["CHARACTER"]
	char = apply_att_stats(char)
	assert char["stats"]["MaxHP"] == 10
	assert char["stats"]["Evade"] == -4
	assert char["stats"]["Hit"] == -4
	assert char["stats"]["Accuracy"] == -4
	assert char["stats"]["PhyDef"] == "1d4"
	assert char["stats"]["PhyAtk"] == "1d2"
	assert char["stats"]["MagDef"] == -4
	assert char["stats"]["MagAtk"] == "1d2"
	assert char["stats"]["Resistance"] == -2
	assert char["stats"]["CarryStrength"] == -2
	assert char["stats"]["Craft"] == -6
