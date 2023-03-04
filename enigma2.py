# Code Creator

# This is a master piece
# Please fell free to add (or remove if desired) to 'alpha' as the rest of the code will start to use it and be able to read it automatically
# As long as all you change is the contents of 'alpha'. There will be NO BUGS! 

# Note that if something is removed or not found in 'alpha' than it will be unable to read it but decoding does not need it unless you want it to be in the translation or the character is before another character that is in the translation.
# PS order in 'alpha' matters for transferral between two programs

# If truly desired that you want a special character to appear more often in the randomisation then, for better performance, add the character multiple times at the end of all the unique (works for multiple characters)

import random

while True:
	num = 0
	char = ""
	lett = ""
	wrd = ""
	message = ""
	result = ""
	alpha = """abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*(),./<>?-_=+\|]}[{:;"'¡™£¢∞§¶•ªº–≠œ∑´®†¥¨ˆøπ“‘«åß∂ƒ©˙∆˚¬…æΩ≈ç√∫˜µ≤≥÷`⁄€‹›ﬁﬂ‡°·‚—±Œ„´‰ˇÁ¨Ø∏”»ÍÎ˝ÓÔÒÚÆ¸˛Ç◊ı˜Â¯˘¿"""
	
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
		if message == "Back":
			break
		else:
			for character in message:
				if character == " ":
					for i in range(len(alpha) + 2):
						lett = alpha[random.randint(0,len(alpha) - 1)]
						char += lett
						lett = ""
				else:
					num = alpha.find(character)
					for i in range(num + 1):
						lett = alpha[random.randint(0,len(alpha) - 1)]
						char += lett
						lett = ""
				result += char + " "
				char = ""				
			print("")
			print(result)
	elif a == "Decode":
		print("")
		print("What message would you like to decode?")
		message = str(input())
		if message == "Back":
			break
		else:
			for word in message.split():
				if len(word) >= len(alpha) + 1:
					result += " "
				elif len(word) - 1 <= len(alpha):
					char = alpha[len(word) - 1]
					result += char
				char = ""
			print("")
			print(result)