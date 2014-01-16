#Enemy Generation
#author: amesen
#November 26, 2013
#Modified as of December 30, 2013

#1 - Dancing Grounds
#2 - HfLS
#3 - Town Dump
#4 - Dermal Repo
#5 - Winding Village
#6 - Happy Days
#7 - Colosseum

#EnemyCode /str-Name /int-Str /Fin /Vit /Agi /Awr /bool-Sunder /Pierce /Crush /Flesh /int-Sunder /Pierce /Crush /Flesh

import dict
from weaponGeneration import generateWeapon
from random import randint
import math

def generateEnemy(low, high, map, enemyAmount, level):
	for x in range(0,enemyAmount):

		foe = randint(low,high)
		mod = randint(0,10)


		#statements for setting enemy code from map options in the dictionary
		chosenMap = list(dict.enemyMaps[map])
		foeCode = list(chosenMap[foe])

		#Generate stats
		dist = []
		for x in range(0,9):
			dist.append(foeCode[x + 1])
			foeCode[x+1] = 0

		#For each strength level
		for j in range(1,level+1):
			#For each stat
			for i in range(0,9):
				if(randint(0,100) <= dist[i]):
					if(1+i<6):
						foeCode[1 + i] += 1
					else:
						foeCode[1 + i] += 2

		#statements for adjusting enemy code based on temperment. 1/str 2/fin 3/vit 4/agi 5/awr
		if(enemyAmount > 1):
			if(mod == 1): #Manic
				foeCode[0] = 'Manic ' + foeCode[0]
				foeCode[1] += math.floor(randint(1,3)*0.1*level)
				foeCode[4] += math.floor(randint(1,3)*0.1*level)
				foeCode[3] -= math.floor(randint(1,3)*0.1*level)

			if(mod == 2): #Deadly
				foeCode[0] = 'Deadly ' + foeCode[0]
				foeCode[1] += math.floor(randint(1,3)*0.1*level)
				foeCode[2] += math.floor(randint(1,3)*0.1*level)
				foeCode[5] -= math.floor(randint(1,3)*0.1*level)

			if(mod == 3): #Stitched
				foeCode[0] = 'Stitched ' + foeCode[0]
				foeCode[3] += math.floor(randint(1,3)*0.1*level)
				foeCode[2] += math.floor(randint(1,3)*0.1*level)

			if(mod == 4): #Trembling
				foeCode[0] = 'Trembling ' + foeCode[0]
				foeCode[2] += math.floor(randint(1,3)*0.1*level)
				foeCode[4] += math.floor(randint(1,3)*0.1*level)
				foeCode[1] -= math.floor(randint(1,3)*0.1*level)

			if(mod == 5): #Lidless
				foeCode[0] = 'Lidless ' + foeCode[0]
				foeCode[2] += math.floor(randint(1,3)*0.1*level)
				foeCode[5] += math.floor(randint(1,3)*0.1*level)
				foeCode[3] -= math.floor(randint(1,3)*0.1*level)

			if(mod == 6): #Broken
				foeCode[0] = 'Broken ' + foeCode[0]
				foeCode[3] -= math.floor(randint(1,3)*0.1*level)

			if(mod == 7): #TwoFaced
				foeCode[0] = 'TwoFaced ' + foeCode[0]
				foeCode[4] += math.floor(randint(1,3)*0.1*level)
				foeCode[5] += math.floor(randint(1,3)*0.1*level)
				foeCode[2] -= math.floor(randint(1,3)*0.1*level)

		#Check minimum and maximum requirements and adjust accordingly
		for x in range(0,5):
			min = math.floor((dist[x]/100.0) * level)
			max = level+1
			if(foeCode[x+1] < min):
				foeCode[x+1] = math.floor(min)
			if(foeCode[x+1] > max):
				foeCode[x+1] = max
				
			

		print
		print 'Name: ' + foeCode[0]
		print 'Str: ' + str(int(foeCode[1]))
		print 'Fin: ' + str(int(foeCode[2]))
		print 'Vit: ' + str(int(foeCode[3]))
		print 'Agi: ' + str(int(foeCode[4]))
		print 'Awr: ' + str(int(foeCode[5]))
		print 'Sunder: ' + str(int(foeCode[6])) + '  Crush: ' + str(int(foeCode[7])) + '  Pierce: ' + str(int(foeCode[8])) + '  Flesh: ' + str(int(foeCode[9]))
		print
		print foeCode[11]
		print generateWeapon(1,level,foeCode[10], False)

	return foeCode

