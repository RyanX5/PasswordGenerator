import random

class Generators:

	def __init__(self, minLength, maxLength):
		
		self.minLength = minLength
		self.maxLength = maxLength



	def GenerateLength(self):

		minLength = self.minLength
		maxLength = self.maxLength

		length = random.randrange(minLength, maxLength + 1)

		return length



	def NumberOrLetter(self):

		choice = random.randrange(0, 2)

		if choice == 0:

			return True

		else:

			return False


	def GenerateLetter(self):

		letterArray = self.GenerateLetterArray()

		randomIndex = random.randrange(0, len(letterArray) - 1)

		randomLetter = chr(letterArray[randomIndex])

		return randomLetter


	def GenerateLetterArray(self):

		arr = []

		symbolArray = [91, 92, 93, 94, 95, 96]

		for i in range(65, 123):
			if i not in symbolArray:
				arr.append(i)

		return arr

	def GenerateNumber(self):
		randomNumber = random.randrange(0, 10)
		return randomNumber

