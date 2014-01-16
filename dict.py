#Python module that defines string dictionaries
#author:amesen
#Last Modified: December 31st

from random import randint

#---------------For Weapon Generation----------------------------------
SIZE = {0:'Small' , 1:'' , 2:'Large' , 3:'Colossal' , 4:'Small' , 5:'' , 6:'Large' , 7:'', 8:'', 9:'Small', 10:''}

#Bone: 1 auto regen, Steel: , Shifting: , Amber: , Stone: , Frozen: , Flaming: 
MAT = {0:'Bone', 1:'Steel', 2:'Amber', 3:'Stone'}
DESC = {0:'Flaming', 1:'Frozen', 2:'Shifting', 3:'', 4:'', 5:'', 6:''}
DIST = {0:[65,30,30], 1:[70,30], 2:[65,30,30], 3:[80], 4:[70,30], 5:[70], 6:[70,30]}

PRIMDMG = {0:'Sunder', 1:'Crush', 2:'Pierce', 3:'Pierce', 4:'Crush', 5:'Flesh', 6:'Pierce'}
SECDMG = {0:'Pierce', 1:'Sunder', 2:'Flesh', 3:'', 4:'Flesh', 5:'', 6:'Sunder'}
TERDMG = {0:'Crush', 1:'', 2:'Crush', 3:'', 4:'', 5:'', 6:''}

MODS = {0:'Glowing', 1:'Keen', 2:'', 3:'', 4:'', 5:'', 6:''}

BASE = {0:"Blade" , 1:"Hammer" , 2:"Pistol" , 3:"Rifle" , 4:"Gauntlet" , 5:"Lash" , 6:"Lance"}
	#Blade		Sunder/Pierce/Crush
	#Hammer		Crush/Sunder
	#Pistol		Flesh/Crush/Pierce
	#Rifle		Pierce
	#Gauntlet	Crush/Flesh
	#Lash		Flesh
	#Lance		Pierce/Sunder

#---------------For Armor Generation----------------------------------
BASETYPE = {0:'Enveloping', 1:'Simple', 2:'Minimal'}
BASEMOD = {0:9, 1:7, 2:6}
ARMORMOD = {0:'Buzzing', 1:'Dull', 2:'Crimson', 3:'Azure'}

#---------------For NPC generation------------------------------------
PERSONA = {0:'Adventurer', 1:'Scholar', 2:'Diva', 3:'Athlete', 4:'Noble', 5:'Charlatan'}
CHARS = {0:'Intimidating', 1:'Cheerful', 2:'Bold', 3:'Shy', 4:'Quiet', 5:'Naive', 6:'Hyperactive', 7:'Sulky', 8:'Loud', 9:'Leader', 10:'Follower', 11:'Stealthy', 12:'Insecure', 13:'Lonely', 14:'Boring', 15:'Worn-out', 16:'Paranoid', 17:'Nervous', 18:'Goofy',  19:'Crazy', 20:'Rude', 21:'Kind', 22:'Loyal', 23:'Honorable', 24:'Sinister', 25:'Greedy', 26:'Tricky', 27:'Charming', 28:'Cute', 29:'Selfish', 30:'Bipolar'} #Add more as able
charnum = 30

HAIRCOLOR = {0:'Blonde', 1:'Red', 2:'Brown', 3:'Black', 4:'White'}
colors = 4
HAIRLENGTH = {0:'Buzzed', 1:'Short', 2:'Long', 3:'Ponytail', 4:'Cropped'}
lengths = 4


AFFINITY1 = {0:'Prefers violent solutions, particularly against Iconodules.', # +Blood
			1:"Prefers loud and destructive approaches, preferably to the environment.", # +Destruction
			2:'Favors exploration and learning above all else.', # +Hope
			3:"Helps any in need."} # +Humanity

AFFINITY2 = {0:"Always tries to find a way to avoid hostilities.", # -Blood
			1:"Would rather sneak about and not draw attention.", # -Destruction
			2:"Has a pessimistic view of the Chancel", # -Hope
			3:"Believes in survival of the fittest- if you can't keep up, so be it."} # -Humanity

#----------------For Enemy Generation------------------------------------

#EnemyCode /str-Name 
#/Str  /Fin  /Vit  /Agi  /Awr
#Sunder  /Pierce  /Crush  /Flesh

#Rankings
z = 100
a = 90
ab = 75
b = 60
c = 40
d = 20

#Blade:0 1:"Hammer" 2:"Pistol" 3:"Rifle" 4:"Gauntlet" 5:"Lash" 6:"Lance"

winding = [['Villager', 1, 2, 1, 4, 2, c, d, c, c, 'Blade', ''], #Villager
           ['Maiden', 0, 4, 4, 0, 2, a, b, c, a, 3], #Maiden
           ['Monument'], #Monument
           []] #Stilts

dermal = [["Maitre'D",	d, b, d, a, c,	b, z, a, c,		2,'Revolver'], #Matre'D
          ['Customer',	ab,d, b, c, d,	ab,c, z, z,		0, 'Claws'], #Customer
		  ['Binder',	d, d, a, d, a,	c, z, b, z,		5, "Cat o' Nine"], #Binder
          ['Skinner',	a, d, b, c, b,	c, a, a, a,		0, 'Cleaver'], #Skinner
		  ['Chained Customer',b,d,b,c,d,  b, c,b,d,		0, 'Claws'], #Chained Customer (Skinner)
		  ['M. Bound',	d, a, a, d, a,	a, a, a, a,		5, 'Streamers'],#Mistress Bound
		  ['M.Streamer', 0, 0, 0, 0, 0, d, a, a, a,		5,	'Streamer'],#Mistress Support Streamer
		  ['M. Freed', 	0, 0, 0, 0, 0,	d, c, a, a,		6,	'Talons']] #Mistress Unbound/Freed

hfls = [['Guest', ], #Guest
        [''], #Butler (Seeker)
        [], #Doll
        []] #Ogmios (tongue-chain-ear)

coliseum = [['Squeaker', d, b, c, b, c,   d, c, b, a,    6,'Stinger'], #Squeaker (summons spec)
             ['Juggler',  d, a, d, b, a,   b, b, b, d,    2,'Eyeball'], #Juggler
             ['Spectator',b, d, b, c, c,   c, b, c, c,    0,'Knife'], #Spectator
             ['Legs Body',a, d, a, c, c,   a, c, a, a,    1,'Feet'], #Legs Body
			 ['Legs Head',0, 0, 0, 0, 0,   c, c, d, a,    6, 'Tusks'], #Legs Head
			 ['Multitude Foot',a,d,d,c,a,	b,b,a,a,	  6, 'Barbed Foot'],
			 ['Multitude Body',b,d,c,a,a,	b,b,b,a,	  4, 'Teeth'],
			 ['Nero',	  c, c, c, a, a,   a, a, c, c,    0, 'Butcher Knife']] #Ringmaster


dump = [['Congregant', 	d, c, d, b, c,   c, c, c, b, 	5, 'Lash'], #Congregant, auto-share (tongue)
        ['Clergyman', 	a, d, a, d, d,	 c, b, d, b, 	1, 'Chained Corpse'], #Worshiper (Pillar)
        ['Bookie', 		c, c, d, d, b,   c, b, b, c, 	6, 'Bladed Tome'], #Keeper, (huge tome)
        []] #Priest

happy = [[], #???
         [], #???
         [], #???
         []] #???

dancing = [['Dancer',	d, c, c, c, c,   b, b, d, d,	5, 'Hands'], #Dancer (redead)
           ['Soldier',	b, b, b, d, c, 	 c, c, b, a, 	2, 'Rifle'], #Soldier
           ['Sniper',	d, a, d, b, a,   d, d, a, b, 	3, 'Rifle'], #Sniper
           ['Tank Body',b, c, a, a, d,	 a, b, a, a,	1, 'Treads'], #Tank Body
		   ['Tank Treads,',0,0,0,0, 0,	 b, d, b, a,	0, 'None'],
		   ['Chernobog']] #Tank (use crush)

enemyMaps = {'winding':winding, 'dermal':dermal, 'hfls':hfls, 'coliseum':coliseum, 'dump':dump, 'happy':happy, 'dancing':dancing}

#----------------For Map Generation------------------------------------

hflsBedroom = {0:('Lobby', 3), 1:('Bedroom', 2), 2:('Stairwell', 2), 3:('Hallway', 6), 4:('a', 3), 5:('d', 3), 6:('f', 3)}

#Entry/1 Exit/1 Special1/2 Special2/4 Special3/6 Special4/6 Hallway/i

coloUnderground = {0:('Archway', 2),
				   1:('Stairwell', 1),
					2:('Holding Lake', 3),
					3:('Support Column', 4),
					4:('Channelway', 2),
					5:('Drain', 3),
					6:('Columned Hallway', 2),
					7:('Dead End', 1)}

burningCity = {0:('Checkpoint (entered)', 2), 	#Entrance - 1
				   1:('Checkpoint', 1),			#Exit - x
					2:('Plaza', 4), 				#Special1 - 2
					3:('Scorched Lake', 3),		#Special2 - 4
					4:('Dropzone', 2),			#Special3 - 6
					5:('Corpse Pile', 3),		#Special4 - 6
					6:('Cratered Street', 2),	#Hallway - i
					7:('Collapsed Building', 1)}#Cap - i

dermalStacks = {0:('Doorway', 2),
			  1:('Archive Door', 1),
			  2:('Skin Heaps', 3),
			  3:('Sleeping Pit', 4),
			  4:('Crumbling Stacks', 2),
			  5:('Specimen Containment', 3),
			  6:('Corridor', 2),
			  7:('Bookcase', 1)}

dermalSkinning = {0:('Doorway', 2),
			  1:('???', 1),
			  2:('Drying Racks', 3),
			  3:('', 4),
			  4:('', 2),
			  5:('Skinning Chamber', 3),
			  6:('', 2),
			  7:('Window', 1)}

mapList = {'coloUnderground':coloUnderground, 'hflsBedroom':hflsBedroom, 'burningCity':burningCity, 'dermalStack':dermalStacks}




























