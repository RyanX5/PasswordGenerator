from .generators import Generators

def GeneratePassword(minLength, maxLength):

	generatorObject = Generators(minLength, maxLength)
	password = ""

	length = generatorObject.GenerateLength()

	for i in range(length):

		if generatorObject.NumberOrLetter():
			randomLetter = generatorObject.GenerateLetter()
			password += randomLetter

		else:
			randomNumber = generatorObject.GenerateNumber()
			password += str(randomNumber)

	return password

