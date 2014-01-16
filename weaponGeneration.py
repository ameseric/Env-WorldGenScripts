#Weapon Generation
#author: amesen
#Weapon Code Layout: Base  primDamage	secDamage	primType	secType	size	name range

from random import randint
import dict
import sys
import math

def generateWeapon(amount, level, type, name):
	selection = False
	if(type == -1):
		selection = True;

	for x in range(0,amount):


		if(selection):
			type = randint(0,6)
			
		#initialize parameter lists
		weaponCode = []
		modifiers = []
		tierThree = False
		primaryCap = math.ceil(level*0.8)


		#-----------------Generate base [0]-----------------------------
		weaponCode.append(type)
		#Look up damage distribution for the weapon type
		dist  = dict.DIST[weaponCode[0]]

		typeRemove = randint(1,2)

		if(len(dist) > 2):
			tierThree = True
			dist.pop(typeRemove)

		#-----------------Generate damage [1] [2]----------------------------
		weaponCode.append(0) #1
		weaponCode.append(0) #2

		#For each strength level
		for j in range(0,level+1):
			#For each stat
			for i in range(0,len(dist)):
				capCheckPrim = weaponCode[1]
				capCheckTot = weaponCode[1] + weaponCode[2]
				
				if(randint(0,100) <= dist[i] and capCheckPrim<level and capCheckTot<level+3):
					weaponCode[1 + i] += 1	
					if(randint(0,99) < 10):
						weaponCode[1 + i] += 1

		if(weaponCode[1] >= primaryCap):
			weaponCode[1] = int(primaryCap)
			if(randint(0,100) <= 6):
				weaponCode[1]+=1

		#-----------------Generate primary and secondary damage type [3] [4]----------------------------
		weaponCode.append(dict.PRIMDMG[weaponCode[0]])
		weaponCode.append('None')

		if(len(dist)>1 and not tierThree):
			weaponCode[4] = dict.SECDMG[weaponCode[0]]
			
		elif(tierThree):
			if(typeRemove == 2):
				weaponCode[4] =  dict.SECDMG[weaponCode[0]]
			else:
				weaponCode[4] = dict.TERDMG[weaponCode[0]]


		#------------------Generate size [5]----------------------------
		#Colossal, -3 Agility, -2 Style, +4 Dmg
		#Large, -2 Agility, -1 Style, +2 Dmg
		#Medium, 
		#Small, +2 Agility, -2 Dmg, 
		weaponCode.append(dict.SIZE[randint(0,10)])
		if(weaponCode[5] == "Small"):
			modifiers.append("Small: +2 Agility")
			weaponCode[1]-=1
		elif(weaponCode[5] == "Large"):
			modifiers.append("Large: -2 Agi/-1 Action/+1 Crush")
			weaponCode[1]+=1
		elif(weaponCode[5] == "Colossal"):
			modifiers.append("Colossal: -3Agi/-2 Action/+2 Crush")
			weaponCode[1]+=2

		#------------------Piece name together [6]---------------------------------
		#if(randint()):
			
		weaponCode.append(weaponCode[5] + " " + dict.MAT[randint(0,3)] + " " + dict.BASE[weaponCode[0]])

		#------------------If ranged, generate [7]---------------------------------
		if(weaponCode[0] == 3):
			weaponCode.append('Ranged, Long')
		elif(weaponCode[0] == 2):
			weaponCode.append('Ranged, Short')
		elif(weaponCode[0] == 6):
			weaponCode.append('Ranged Melee (Reach)')
		else:
			weaponCode.append('Melee')

		

		#----------------Generate Random Modifiers [8]-------------------------------



		#------------------Print finished weapon for enjoyment of the masses!------
		if(name == True):
			print("Name: " + weaponCode[6])
			print('Level: ' + str(level))
		print(weaponCode[3] + " Damage: " + str(weaponCode[1]))
		if(weaponCode[2] > 0):
			print(weaponCode[4] + " Damage: " + str(weaponCode[2]))
		print("Range: " + str(weaponCode[7]))
		print("Modifiers: " + str(modifiers))
		print

	return weaponCode


