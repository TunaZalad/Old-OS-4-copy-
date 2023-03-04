# Code Creator

# Feel free to add characters to 'alpha' but remember to add a counterpart in 'code'
# As long as you follow those instrcutions then there will be NO BUGS!

while True:
	alpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
	code  = "sqtaoihwgcrfypuvxzklmejdnbSQTAOIHWGCRFYPUVXZKLMEJDNB"

	print ("")
	print ("What do you want to do?")
	print ("- Encode")
	print ("- Decode")
	print ("")

	a = input()
	if a == "Back":
		break
	elif a == "Encode":
		print("")
		print("What message would you like to encode?")
		message = str(input())
		result = ""
		if message == "Back":
			break
		else:
			for character in message:
				if character == " ":
					result += " "
				elif alpha.find(character) == -1:
					result += character
				else:
					num = alpha.find(character)
					character = code[num]
					result += character	
			print("")
			print(result)		
	elif a == "Decode":
		print("")
		print("What message would you like to decode?")
		message = str(input())
		result = ""
		if message == "Back":
			break
		else:
			for character in message:
				if character == " ":
					result += " "
				elif alpha.find(character) == -1:
					result += character
				else:
					num = code.find(character)
					character = alpha[num]
					result += character
			print("")
			print(result)