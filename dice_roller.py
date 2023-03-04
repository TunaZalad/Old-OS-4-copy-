# Dice Roller

import random

while True:
	print ("")
	print ("Please type the number of faces (Enter '0' to reroll)")
	
	face = input()
	
	if face == "Back":
		break
	else:
		try:
			n_face = int(face)
		except ValueError:
			print("Try again.")
			n_face = -1
	
	if n_face == 0:
		roll = int(random.randint(1, (re_face)))
		print (roll)
	
	elif n_face >= 1:
		re_face = n_face
		roll = int(random.randint(1, n_face))
		print (str(random.randint(1, n_face)))