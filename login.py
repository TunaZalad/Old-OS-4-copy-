# Login

tries_left = int(3)
x = 1
y = 0
z = 1
w = 0

while x == 1 and w == 0:
	if y != 1:
		print ("Name:")
	if input() == "TunaZalad" or y == 1:
		y = 1
		print ("Password:")
		while z == 1:
			if input() == "Python" and tries_left > 0:
				print("")
				print ("Welcome!")
				print ("")
				print ("Enter 'Back' at any time to exit a program.")
				print("")
				w = 1
				z = 0
			elif input != "Python":
				if tries_left > 0:
					tries_left = tries_left - 1
				tries_lefta = str(tries_left)
				print (" ")
				print ("Incorrect Password")
				print (tries_lefta + " tries left.")
				print (" ")
				if tries_left != 0:
					print ("Password:")
			if tries_left <= 0:
				print ("You have been locked out. Go away!")
				print ("")
	else:
		print ("That is not your name!")
		print ("")