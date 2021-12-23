def passwordLength():
	print('How long do you want you password to be?')
	desiredPasswordLength = input()

	try:
		desiredPasswordLength = int(desiredPasswordLength)
		return desiredPasswordLength
	except:
		print('Desired password length provided must be a number')
