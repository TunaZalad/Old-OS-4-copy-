# Game

import random

wyx = 1

print("""
 ____    ____                     _                      
|_   \  /   _|                   / |_                    
  |   \/   |  .--.  _ .--.  .--.`| |-.---. _ .--. .--.   
  | |\  /| |/ .'`\ [ `.-. |( (`\]| |/ /__\[ `/'`\( (`\]  
 _| |_\/_| || \__. || | | | `'.'.| || \__.,| |    `'.'.  
|_____||_____'.__.'[___||__[\__) \__/'.__.[___]  [\__) ) """)
print("""
			   ___      
			 .' _ '.    
			 | (_) '___ 
			 .`___'/ _/ 
			| (___)  \_
			`._____.\__|""")
print("""
 ______                                                     
|_   _ `.                                                   
  | | `. \__   _  _ .--.  .--./).---.  .--.  _ .--.  .--.   
  | |  | [  | | |[ `.-. |/ /'`\/ /__\/ .'`\ [ `.-. |( (`\]  
 _| |_.' /| \_/ |,| | | |\ \._/| \__.| \__. || | | | `'.'.  
|______.' '.__.'_[___||__.',__` '.__.''.__.'[___||__[\__) ) 
                        ( ( __))                            """)

print("Rules -")
print("- You will progress through the dungeon, where monsters will try to kill you!")
print("- Use one of your abilities to defeat the monster as soon as it appears to prevent it from attacking you.")
print("- Your defence stat will reduce the damage you take, but be wary: if your health reaches 0, you lose!")
print("- The damage you deal to the monsters is reduced by their defence, and gets even less as you progress through the levels.")
print("- Upon defeating enough monsters, you will level up. This gives you a small reward.")
print("- Be cautious when casting abilities. You only have a limited amount of AP (ability power)!")
print("- Attacks are calculated like this: ")
print("HeroHP = HeroHp - (MonsAtt x level ÷ HeroDef)")
print("MonsHP = MonsHp - (HeroAtt / level ÷ MonsDef)")
print("")

def turn(xyz, char_arr):
	global name
	global char_HP
	global char_AP
	global char_def
	global char_att
	global turn_AP
	global mon_name
	global mon_HP
	global mon_AP
	global mon_def
	global mon_att
	global score
	global level
	global wyx
	
	if char_AP - turn_AP >= 0:
		char_AP = char_AP - turn_AP
		if char_att - mon_def > 0:
			mon_HP = int(round(mon_HP - (char_att / level / mon_def)))

	if mon_HP > 0:
		if mon_att - char_def > 0:
			char_HP = int(round(char_HP - (mon_att * level / char_def)))

	if mon_HP <= 0:
		if score >= 0:
			char_AP += char_arr[1] // 2
		
		harp_arr = [5, 10, 10, 40]
		gob_arr = [10, 20, 5, 50]
		ogre_arr = [20, 10, 4, 40]
		spid_arr = [15, 30, 2, 60]
		new_mon_arr = []
		new_mon = random.randint(0, 3)
		if new_mon == 0:
			mon_name = "Harpy"
			for x in harp_arr:
				new_mon_arr.append(x)
		elif new_mon == 1:
			mon_name = "Goblin"
			for x in gob_arr:
				new_mon_arr.append(x)
		elif new_mon == 2:
			mon_name = "Ogre"
			for x in ogre_arr:
				new_mon_arr.append(x)
		elif new_mon == 3:
			mon_name = "Spider"
			for x in spid_arr:
				new_mon_arr.append(x)
		mon_HP = new_mon_arr[0]
		mon_AP = new_mon_arr[1]
		mon_def = new_mon_arr[2]
		mon_att = new_mon_arr[3]
		if score >= 0:
			score += 1
			if score % 3 == 0:
				level += 1
				prize = random.randint(0, 3)
				if prize == 0:
					char_def += 10
				elif prize == 1:
					char_HP += 20
				elif prize == 2:
					char_AP += 50
				elif prize == 3:
					char_def += 5
					char_HP += 10
					char_AP += 20
		else:
			score += 1

	if char_HP <= 0:
		wyx = 0

	print("")
	print("------------------------------------")
	print("")
	print("Level - " + str(level))
	print("Kills - " + str(score))
	print("")
	print(name)
	print("HP  - " + str(char_HP))
	print("AP  - " + str(char_AP))
	print("Def - " + str(char_def))
	print("")
	print(mon_name)
	print("HP  - " + str(mon_HP))
	print("AP  - " + str(mon_AP))
	print("Def - " + str(mon_def))
	print("Att - " + str(mon_att))
	print("")

def action(class1):
	global turn_AP
	global char_att
	if class1 == "Wizard":
		print("1: Fireball       Att - 40  AP - 0")
		print("2: Telekinesis    Att - 90  AP - 5")
		print("3: Sunbeam        Att - 500 AP - 30")
		turn = int(input("Action #: "))
		if turn == 1:
			turn_AP = 0
			char_att = 40
		elif turn == 2:
			turn_AP = 5
			char_att = 90
		elif turn == 3:
			turn_AP = 20
			char_att = 500
	elif class1 == "Paladin":
		print("1: Slash          Att - 20  AP - 0")
		print("2: Lunge          Att - 60  AP - 10")
		print("3: Raging Strike  Att - 200 AP - 40")
		turn = int(input("Action #: "))
		if turn == 1:
			turn_AP = 0
			char_att = 20
		elif turn == 2:
			turn_AP = 10
			char_att = 60
		elif turn == 3:
			turn_AP = 40
			char_att = 200
	elif class1 == "Rogue":
		print("1: Cut            Att - 30  AP - 0")
		print("2: Poison         Att - 70  AP - 10")
		print("3: Blade Storm    Att - 120 AP - 20")
		turn = int(input("Action #: "))
		if turn == 1:
			turn_AP = 0
			char_att = 30
		elif turn == 2:
			turn_AP = 10
			char_att = 70
		elif turn == 3:
			turn_AP = 20
			char_att = 120
	elif class1 == "Hunter":
		print("1: Scratch        Att - 20  AP - 0")
		print("2: Shoot          Att - 60  AP - 10")
		print("3: Ricochet       Att - 150 AP - 30")
		turn = int(input("Action #: "))
		if turn == 1:
			turn_AP = 0
			char_att = 20
		elif turn == 2:
			turn_AP = 10
			char_att = 60
		elif turn == 3:
			turn_AP = 30
			char_att = 150

while True:

	class1 = ""
	name = ""
	mon_name = ""
	wiz_arr = [60, 20, 10]
	pal_arr = [150, 30, 30]
	rog_arr = [100, 40, 15]
	hun_arr = [120, 40, 20]
	char_arr = []
	mon_arr = []
	char_HP = 0
	char_AP = 0
	char_def = 0
	char_att = 0
	mon_att = 0
	mon_def = 0
	mon_HP = 0
	mon_AP = 0
	turn_AP = 0
	score = -1
	level = 1

	print("")
	print("Choose a class:")
	print("- Wizard")
	print("- Paladin")
	print("- Rogue")
	print("- Hunter")
	print("")
	
	class1 = str(input())

	if class1 == "Wizard":
		for x in wiz_arr:
			char_arr.append(x)
	elif class1 == "Paladin":
		for x in pal_arr:
			char_arr.append(x)
	elif class1 == "Rogue":
		for x in rog_arr:
			char_arr.append(x)
	elif class1 == "Hunter":
		for x in hun_arr:
			char_arr.append(x)
	elif class1 == "Back":
		break
	else:
		print("")
		print("Try again")
		print("")

		class1 = str(input())

		if class1 == "Wizard":
			for x in wiz_arr:
				char_arr.append(x)
		elif class1 == "Paladin":
			for x in pal_arr:
				char_arr.append(x)
		elif class1 == "Rogue":
			for x in rog_arr:
				char_arr.append(x)
		elif class1 == "Hunter":
			for x in hun_arr:
				char_arr.append(x)
		elif class1 == "Back":
			break
		else:
			print("Can't you type?")
			print("Exiting...")
			break

	char_HP = char_arr[0]
	char_AP = char_arr[1]
	char_def = char_arr[2]

	print("")
	print("What is your hero's name?")
	name = str(input())
	
	xyz = 1
	while xyz == 1:
		turn(xyz, char_arr)
		xyz = wyx
		wyx = 1
		if xyz == 1:
			action(class1)
	
	for x in range(50):
		print("")

	print("""
	__   _______ _   _   _   _   ___  _   _ _____  
	\ \ / /  _  | | | | | | | | / _ \| | | |  ___| 
	 \ V /| | | | | | | | |_| |/ /_\ \ | | | |__   
	  \ / | | | | | | | |  _  ||  _  | | | |  __|  
	  | | \ \_/ / |_| | | | | || | | \ \_/ / |___  
	  \_/  \___/ \___/  \_| |_/\_| |_/\___/\____/  """)
	print("""
		______ _____ ___________ _ 
		|  _  \_   _|  ___|  _  \ |
		| | | | | | | |__ | | | | |
		| | | | | | |  __|| | | | |
		| |/ / _| |_| |___| |/ /|_|
		|___/  \___/\____/|___/ (_)""")
	print("")
	print("")
	print("")
	print("")
	print("")
	print("")
	print("")