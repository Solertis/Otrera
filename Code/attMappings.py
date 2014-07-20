# Attribute --> Stat bonus/penalty mapping methods

def mgt_to_atk(mgt):
	if mgt <= 4:
		return "1d2"
	elif mgt <= 8:
		return "1d4"
	elif mgt <= 10:
		return "1d6"
	elif mgt <= 12:
		return "1d8"
	elif mgt <= 14:
		return "1d10"
	elif mgt <= 16:
		return "1d12"
	elif mgt <= 18:
		return "1d6+1d8"
	elif mgt <= 20:
		return "2d8"
	elif mgt <= 22:
		return "3d6"
	elif mgt <= 25:
		return "1d20"
	elif mgt > 25:
		return "2d12"

def mgt_to_carry_strength(mgt):
	if mgt < 10:
		return 0
	else:
		diff = mgt - 7
		bonus = diff/3
		return -bonus

def mgt_con_to_def(MGT, CON):
	total = MGT + CON
	if total < 10:
		return "1d4"
	elif total < 20:
		return "1d6"
	elif total < 30:
		return "1d8"
	elif total < 40:
		return "1d12"
	elif total < 50:
		return "3d6"
	elif total >= 50:
		return "2d12"

def dex_to_move(DEX):
	return DEX/3

def dex_to_evade(DEX):
	diff = DEX - 10
	if diff < -5:
		return -2
	elif diff < 0:
		return -1
	elif diff < 3:
		return 0
	else:
		return diff/3

def dex_to_hit(DEX):
	diff = DEX - 10
	if diff < -5:
		return -2
	elif diff < 0:
		return -1
	elif diff < 3:
		return 0
	else:
		return diff/3

def dex_to_accuracy(dex):
	diff = dex - 10
	if diff < -5:
		return -2
	elif diff < 0:
		return -1
	elif diff < 3:
		return 0
	else:
		return diff/3

def art_to_evade(art):
	return art/7

def art_to_hit(art):
	if art <= 5:
		return -1
	elif art <=10:
		return 0
	else:
		diff = art-6
		return diff/4

def art_to_spell_fail(ART):
	return 25/ART

def art_to_casting_speed(ART):
	return ART/3

def int_to_spell_fail(INT):
	return 25/INT

def int_to_craft(INT):
	return INT/2

def dex_art_to_craft(DEX,ART):
	total = DEX+ART
	return total/5

def div_to_magic_attack(DIV):
	if DIV <= 4:
		return "1d2"
	elif DIV <= 8:
		return "1d4"
	elif DIV <= 10:
		return "1d6"
	elif DIV <= 12:
		return "1d8"
	elif DIV <= 14:
		return "1d10"
	elif DIV <= 16:
		return "1d12"
	elif DIV <= 18:
		return "1d6+1d8"
	elif DIV <= 20:
		return "2d8"
	elif DIV <= 22:
		return "3d6"
	elif DIV <= 25:
		return "1d20"
	elif DIV > 25:
		return "2d12"

def div_art_to_magic_defense(DIV,ART):
	total = DIV+ART
	if total < 10:
		return "1d4"
	elif total < 20:
		return "1d6"
	elif total < 30:
		return "1d8"
	elif total < 40:
		return "1d12"
	elif total < 50:
		return "3d6"
	elif total >= 50:
		return "2d12"

def con_to_maxHP(con):
	diff = con - 10
	if diff < 0:
		return diff
	else:
		return diff*2

def con_to_resistance(CON):
	if CON <= 3:
		return -2
	elif CON <= 7:
		return -1
	elif CON <= 10:
		return 0
	else:
		return (CON-8)/3
