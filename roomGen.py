#Room-by-room dungeon enemy generation.
#author: amesen
#Takes world number, enemy level as argv1 & 2

from random import randint
import sys
from enemyGeneration import generateEnemy

roll = randint(1,10)

if(roll <=6):
	print("Room clear.")
elif(roll <=8):
	print("Enemies!")
	generateEnemy(int(sys.argv[1]), randint(1,4), int(sys.argv[2]))
elif(roll <=9):
	print("Enemies+")
	generateEnemy(int(sys.argv[1]), randint(1,4), int(sys.argv[2])+3)
else:
	print("Self!")
