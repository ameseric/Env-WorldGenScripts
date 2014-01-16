#Generation for parts of dungeons
#Author: amesen

from random import randint
import sys
import dict
import math

def generateMap(map, exitNum, foeRate):
	roomList = dict.mapList[map]
	#0 - Coliseum, Underground
	#1 - HfLS Bedrooms
	#2 - HfLS Attics

	layout = []
	layout.append(roomList[0])
	end = roomList[1]
	check2 = 0; check3=0; check4=0; check5=0; total=0
	low = 1

	while (end not in layout or total<20) and len(layout)>0:
		currentRoom = layout.pop()
		print currentRoom[0] + ', ' + str(currentRoom[1])
		if(randint(0,99 < foeRate)):#Chance of enemy encounter
			print 'ENEMIES PRESENT'
			
		for x in range(1,currentRoom[1]):
			nextRoom = randint(low,7)

			if(nextRoom == 1):
				layout.append(roomList[1])
				exitNum -= 1
				if(exitNum == 0):
					low = 2

			if(nextRoom == 2 and check2 < 2):
				layout.append(roomList[2])
				check2+=1

			if(nextRoom == 3 and check3 < 4):
				layout.append(roomList[3])
				check3+=1

			if(nextRoom == 4 and check4 < 6):
				layout.append(roomList[4])
				check4+=1

			if(nextRoom == 5 and check5 < 6):
				layout.append(roomList[5])
				check5+=1

			if(nextRoom == 6 or nextRoom == 7):
				layout.append(roomList[nextRoom])
			
			total+=1