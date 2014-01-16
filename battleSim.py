#Attempt at a combat simulation
#author: amesen
#call sequence: py battleSim.py <map> <self_level> <enemy_level>

#Thoughts: use dictionaries as enemy/npc info storage units

#how to handle enemy AI (in a semi-intelligent fashion) 
#What about range?
#Tactics, i.e. special techniques. How to do that? Seperate database?
#Maybe have a tactic.py script, call it with the tactic number and execute the code under that statement

#TODO: for now, just generate 1 enemy, 1 playable, and have them ENG

#Combatent: limbs, weapon(s), Gimmicks, 5 stats, 4 armors, name, 
#code = {'name':'Foe1', 'stats':[Str, Fin, Vit, Agi, Awr], 'armor':[S,C,P,F], 'weapon':[weaponCode], etc...}
#Suggestion: Create a seperate script for taking two weapon types, finding the appropriate dice, and calcualting an action encounter result
#So have battleSim.py, tactics.py, and actionResolution.py?

import dict
from weaponGeneration import generateWeapon
from armorGeneration import generateArmor
from enemyGeneration import generateEnemy
from npcGeneration import generateNPC
from random import randint
import sys

arg = sys.argv
# arg1<map> arg2<level> arg3<?>

#generate enemy party
foe = generateEnemy(0, 2, arg[1], 3, int(arg[2]))

#generate npc
self = generateNPC(arg[2])

#check npc stats, decide Role.
#?

#Generate Weapon, Aegis.
self['armor'] = generateArmor(level)
self['weapon'] = generateWeapon(level)

#check agility scores, set up turn order


#begin turn sequence
#pseudocode, there isn't actually hp
while(npc['hp']!=0 and foe['hp']!=0):