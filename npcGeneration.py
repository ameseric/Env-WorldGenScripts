#NPC Generation
#author: amesen

#Name
#Personality + Mental Chars (Noble/Charlatan/Adventurer/Diva/Scholar/Athlete)
#Role (Dragoon/Cannondier/Shepherd/Scrapper/Rogue/Arbiter)
#Role/Weapon Ranks (A/B/C/D)
#Physical Chars


#NPC Code
#0 - 

from random import randint
import dict
import names
import math

fnumber = names.fnumber
mnumber = names.mnumber
chars = dict.charnum
colors = dict.colors
lengths = dict.lengths

def generateNPC(level):
	npc = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
	stats = [20, 20, 20, 20, 20]

	#0 - Name
	gender = randint(0,1)
	if(gender == 0):
		npc[0] = names.FNAMES[randint(0,fnumber)]
	else:
		npc[0] = names.MNAMES[randint(0, mnumber)]

	#1 - Personality
	npc[1] = (randint(0,5))

	#2,3,4 - Mental Chars
	npc[2] = (randint(0,chars))
	npc[3] = (randint(0,chars))
	npc[4] = (randint(0,chars))

	#5,6,7,8,9 - Stats
	#Points are assigned 2-6 times
	#Each stat has a 20% of increasing
	#x6 +20% are randomly distributed between the stats
	for x in range(0, 6):
		stats[randint(0,4)] += 20

	age = randint(2,18) + randint(2,12) + randint(1,12)

	#For each strength level
	for j in range(0,level+1):
		#For each stat
		for i in range(0,5):
			if((randint(0,90)+randint(0,10)) <= stats[i]):
				npc[5 + i] += 1
				if(randint(0,100) <= 10):
					npc[5+i] += 1

	#Check minimum requirements
	for x in range(0,5):
		min = math.floor((stats[x]/100.0) * level)
		max = level+1
		if(npc[x+5] < min):
			npc[x+5] = math.floor(min)
			print 'Reached a min'
		if(npc[x+5] > max):
			npc[x+5] = max
	

	print
	print("Name: " + npc[0])
	print("Age: " + str(age))
	print(dict.HAIRLENGTH[randint(0,lengths)] + ", " + dict.HAIRCOLOR[randint(0,colors)] + " Hair")
	print
	print(dict.AFFINITY1[randint(0,3)])
	print(dict.AFFINITY2[randint(0,3)])
	print
	print("Matrix: " + str(level))
	print("	Str: " + str(int(npc[5])))
	print("	Fin: " + str(int(npc[6])))
	print("	Vit: " + str(int(npc[7])))
	print("	Agi: " + str(int(npc[8])))
	print("	Awr: " + str(int(npc[9])))
	print("Persona: " + dict.PERSONA[npc[1]])
	print("Traits: " + dict.CHARS[npc[2]] + ', ' + dict.CHARS[npc[3]])
	print ("Stats: " + str(stats))

	return(npc)
	











