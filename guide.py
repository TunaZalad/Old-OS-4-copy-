 # Guide

while True:
	print ("")
	print ("Options:")
	print ("- Calculator")
	print ("- Funny Song Maker")
	print ("- Enigma")
	print ("- Enigma 2.0")
	print ("- Enigma 3.0")
	print ("- Emoji Coder")
	print ("- Dice Roller")
	print ("- Monsters & Dungeons")
	print ("")

	r = 1

	while r == 1:
		z = input()
		if z == "Calculator":
			import calculator
			r = 0
			pass
		elif z == "Funny Song Maker":
			import funny_song_maker
			r = 0
			pass
		elif z == "Enigma":
			import enigma
			r = 0
			pass
		elif z == "Enigma 2.0":
			import enigma2
			r = 0
			pass
		elif z == "Enigma 3.0":
			import enigma3
			r = 0
			pass
		elif z == "Emoji Coder":
			import emoji_coder
			r = 0
			pass
		elif z == "Dice Roller":
			import dice_roller
			r = 0
			pass
		elif z == "Monsters & Dungeons" or z == "M&D" or z == "MnD":
			import monsters_and_dungeons
			r = 0
			pass
		else:
			print ("")
			print ("Options:")
			print ("- Calculator")
			print ("- Funny Song Maker")
			print ("- Enigma")
			print ("- Enigma 2.0")
			print ("- Enigma 3.0")
			print ("- Emoji Coder")
			print ("- Dice Roller")
			print ("- Monsters & Dungeons")
			print ("")