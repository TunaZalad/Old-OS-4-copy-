# Calculator

ra = 1

print ("1 for +")
print ("2 for -")
print ("3 for x")
print ("4 for ÷")
print ("")

while ra == 1:
	q = input()

	if q == "1":
		print ("Type your two numbers (Press Enter after each)")
		t = int(input())
		s = int(input())
		print (t + s)
		print ("")
		print ("1 for +")
		print ("2 for -")
		print ("3 for x")
		print ("4 for ÷")
		print ("")
	elif q == "2":
		print ("Type your two numbers (Press Enter after each)")
		t = int(input())
		s = int(input())
		print (t - s)
		print ("")
		print ("1 for +")
		print ("2 for -")
		print ("3 for x")
		print ("4 for ÷")
		print ("")
	elif q == "3":
		print ("Type your two numbers (Press Enter after each)")
		t = int(input())
		s = int(input())
		print (t * s)
		print ("")
		print ("1 for +")
		print ("2 for -")
		print ("3 for x")
		print ("4 for ÷")
		print ("")
	elif q == "4":
		print ("Type your two numbers (Press Enter after each)")
		t = int(input())
		s = int(input())
		print (t / s)
		print ("")
		print ("1 for +")
		print ("2 for -")
		print ("3 for x")
		print ("4 for ÷")
		print ("")
	elif q == "Back":
			ra = 0
			pass
	
	else:
		print ("")
		print ("1 for +")
		print ("2 for -")
		print ("3 for x")
		print ("4 for ÷")
		print ("")

