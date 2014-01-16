#Armor Generation
#author: amesen
#Armor Code Layout: Base  Modifier	Sunder	Pierce	Crush	Flesh

from random import randint
import dict
import math

def generateArmor(amount, level):
	AMOD = dict.ARMORMOD
	BASE = dict.BASETYPE
	BMOD = dict.BASEMOD


	for x in range(0,amount):
		armorCode = [0, 0, 0, 0, 0, 0, '']


		# Base
		case = armorCode[0] = randint(0,2)

		#Armor type agility mod & cap choice
		agiMod = 'None'
		cap = math.ceil(level*3)
		if(armorCode[0] == 0):
			agiMod = '-' + str(int(math.floor(level*0.5))) + ' Agility'
			cap = math.floor(level*4)
		if(armorCode[0] == 1):
			agiMod = '-' + str(int(math.floor(level*0.25))) + ' Agility'
			cap = math.ceil(level*3.5)


		dist = [30, 30, 30, 30]

		for x in range(0, BMOD[armorCode[0]]):
			dist[randint(0,3)] += 30

		#Mods
		armorCode[1] = randint(0,3)
		mod = str(int(math.floor(level*0.2)))

		if(armorCode[1] == 0):
			armorCode[6] = 'Agility +' + mod
		elif(armorCode[1] == 1):
			armorCode[6] = 'Vitality +' + mod
		elif(armorCode[1] == 2):
			armorCode[6] = 'Strength +' + mod
		elif(armorCode[1] == 3):
			armorCode[6] = 'Finesse +' + mod

		#For each strength level
		for j in range(0,level):
			#For each stat
			for i in range(0,4):
				capCheck = armorCode[2]+armorCode[3]+armorCode[4]+armorCode[5]
				if(randint(0,100) <= dist[i] and capCheck<cap):
					armorCode[2 + i] += 2

		#Check min requirement
		for x in range(0,4):
			min = level*(dist[x]/100.0)
			if( armorCode[x+2] < min):
				armorCode[x+2] = int(math.floor(min))

		print AMOD[armorCode[1]] + ' ' + BASE[armorCode[0]] + ' Aegis'
		print 'Level: ' + str(level)
		print 'Sunder: ' + str(int(armorCode[2]))
		print 'Pierce: ' + str(armorCode[3])
		print 'Crush: ' + str(armorCode[4])
		print 'Flesh: ' + str(armorCode[5])
		print 'Modifier: ' + armorCode[6]
		print 'Armor Mod: '+ agiMod
		print

	return armorCode
