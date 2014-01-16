#Main python module for generation
#Call desired generation type through calling sequence
#generate <npc/loot/weapon/enemy> <enemy world> <# of enemies>

#My imports
from weaponGeneration import generateWeapon
from armorGeneration import generateArmor
from enemyGeneration import generateEnemy
from npcGeneration import generateNPC
import dict
from mapGeneration import generateMap

#Python imports
from random import randint
import sys

#argument declaration for clarity
arg = sys.argv


#break it up into if's
if(arg[1] == 'loot'):
	type = randint(0,7)	
	if(type<4):
		generateWeapon()
	elif(type<9):
		generateArmor()
	elif(type<10):
		print("Card")
	else:
		print("Whisper Bottle")

if(arg[1] == 'options'):
	print 'npc / map / weapon / armor / encounter / multifoe / foe'

if(arg[1] == 'help'):
	if(arg[2] == 'encounter'):
		print '<Map> <level>'
	if(arg[2] == 'foe'):
		print '<id> <map> <level>'
	if(arg[2] == 'multifoe'):
		print '<low> <high> <map> <enemy amount> <level>'

if(arg[1] == 'npc'):
	generateNPC(int(arg[2]))

#map exitNum foeRate
if(arg[1] == 'map'):
	if(len(arg) < 3):
		print 'Error: bad call sequence.'
	generateMap(arg[2], int(arg[3]), int(arg[4]))

#py generate.py weapon <amount> <level> <type> <name>
if(arg[1] == 'weapon'):
	if(len(arg) < 3):
		arg.append(1); arg.append(7); arg.append(randint(0,6)); arg.append(True)
	if(len(arg) < 4):
		arg.append(7); arg.append(randint(0,6)); arg.append(True)
	if(len(arg) < 5):
		arg.append(randint(0,6)); arg.append(True)
	generateWeapon(int(arg[2]), int(arg[3]), int(arg[4]), True)

if(arg[1] == 'armor'):
	if(len(arg) < 3):
		arg.append(1); arg.append(7)
	if(len(arg) < 4):
		arg.append(7)
	generateArmor(int(arg[2]), int(arg[3]))


#py generate.py encounter <map> <level>
if(arg[1] == 'encounter'):
	if(len(arg) < 3):
		print 'ERROR: bad call sequence'
		sys.exit()
	generateEnemy(0, 2, arg[2], 3, int(arg[3]))

#py generate.py multifoe <low> <high> <map> <enemy amount> <level>
if(arg[1] == 'multifoe'):
	if(len(arg) < 3):
		print 'ERROR: bad call sequence'
		sys.exit()
	generateEnemy(int(arg[2]), int(arg[3]), arg[4], int(arg[5]), int(arg[6]))

#py generate.py foe <id> <map> <level>
if(arg[1] == 'foe'):
	if(len(arg) < 3):
		print 'ERROR: bad call sequence'
		sys.exit()
	generateEnemy(int(arg[2]), int(arg[2]), arg[3], 1, int(arg[4]))




