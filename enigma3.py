# Code Creator THE ULTIMATE

import random

while True:
	alpha =    "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
	beta =     "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
	delta =  """abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*(),./<>?-_=+\|]}[{:;"'¡™£¢∞§¶•ªº–≠œ∑´®†¥¨ˆøπ“‘«åß∂ƒ©˙∆˚¬…æΩ≈ç√∫˜µ≤≥÷`⁄€‹›ﬁﬂ‡°·‚—±Œ„´‰ˇÁ¨Ø∏”»ÍÎ˝ÓÔÒÚÆ¸˛Ç◊ı˜Â¯˘¿"""
	echo = ""
	fox = ""
	golf = ""
	lett = ""
	char = ""
	key1 = ""
	key2 = ""
	arr = []
	num = 0
	num2 = 0
	num3 = 0
	num4 = 0
	xy = 0

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
		
		print("")
		print("What key word would like to use?")
		key1 = str(input())
		
		print("")
		print("What other key word would like to use?")
		key2 = str(input())

		result = ""
		if message == "Back":
			break

		else:
			
			for letter in key1.split():
				beta = beta.strip(letter)

			beta = key1 + beta

			for character in message:
				if character == " ":
					fox += " "
				elif alpha.find(character) == -1:
					fox += character
				else:
					num = alpha.find(character)
					character = beta[num]
					fox += character

			print(fox)

			num = 0

			for letter in key2:
				num = alpha.find(letter)
				arr.append(num)

			num = 0

			for character in fox:
				if character == " ":
					golf += " "
				elif alpha.find(character) == -1:
					golf += character
				else:
					num = alpha.find(character) + 1
					num2 = xy % len(key2)
					num3 = arr[num2]
					num4 = (num3 + num) % len(alpha)
					lett = alpha[num4]
					golf += lett
					xy += 1
			
			print(golf)

			for character in golf:
				if character == " ":
					for i in range(len(delta) + 2):
						lett = delta[random.randint(0,len(delta) - 1)]
						char += lett
						lett = ""
				else:
					num = delta.find(character)
					for i in range(num + 1):
						lett = delta[random.randint(0,len(delta) - 1)]
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
		
		print("")
		print("What key word would like to use?")
		key1 = str(input())
		
		print("")
		print("What other key word would like to use?")
		key2 = str(input())

		result = ""

		if message == "Back":
			break

		else:
			for word in message.split():
				if len(word) >= len(delta) + 1:
					fox += " "
				elif len(word) - 1 <= len(delta):
					char = delta[len(word) - 1]
					fox += char
				char = ""

			print(fox)

			num = 0
			
			for letter in key2:
				num = alpha.find(letter)
				arr.append(num)
				num = 0

			for character in fox:
				if character == " ":
					golf += " "
				elif alpha.find(character) == -1:
					golf += character
				else:
					num = alpha.find(character) - 1
					num2 = xy % len(key2)
					num3 = arr[num2]
					num4 = (num - num3) % len(alpha)
					lett = alpha[num4]
					golf += lett
					xy += 1
				
			num = 0

			print(golf)

			for letter in key1.split():
				beta = beta.strip(letter)

			beta = key1 + beta

			for character in golf:
				if character == " ":
					result += " "
				elif beta.find(character) == -1:
					result += character
				else:
					num = beta.find(character)
					character = alpha[num]
					result += character
				
			print("")
			print(result)