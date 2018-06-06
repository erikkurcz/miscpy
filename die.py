import random as rand
import re

class Die:
	"""A class for a die to be rolled"""

	allRolls = []

	def __init__(self,givenname):
		self.face = None
		self.name = givenname
		self.rollct = 0
		self.rollhistory = []

	def roll(self):
		self.face = rand.randrange(1,7)
		self.rollhistory.append(self.face)
		Die.allRolls.append("Die "+self.name+" - Roll #"+ \
			str(self.rollct)+": "+str(self.face))

		return

	def printRollHistory(self):
		for c,x in enumerate(self.rollhistory,1):
			print("Roll #"+c+": "+x)
		return

	def getRollCount(self):
		return self.rollct

	def getFace(self):
		return self.face

	@staticmethod
	def printAllRollHistory():
		for x in allRolls:
			print(x)

	@staticmethod
	def faceFrequency(doubles):
		freq = {str(i):0 for i in range(1,7,1)}

		for x in doubles:
			key = str(x[-1])
			freq[key] = freq[key]+1

		return freq

	@staticmethod
	def printDictionary(freq):
		print("\n"+"*"*40+"\nFrequency Map of Rolled Doubles\n"+"*"*40+"\n")
		for x in freq:
			print("Face value of '"+str(x)+"': "+str(freq[x]))

		return


def main():
	resp = input("Enter how many attempts you'd like to try to get doubles: ")
	tryForDoubles = int(re.search("\d+",resp).group(0))

	print("Let's see how many doubles we can get in "+ \
		str(tryForDoubles)+" rolls of both dice...")
	a = Die("A")
	b = Die("B")

	doubles = []

	for x in range(tryForDoubles):
		a.roll()
		b.roll()

		if a.getFace() == b.getFace():
			doubles.append("Doubles rolled at attempt #"+str(x)+ \
				"\t Face value: "+str(a.getFace()))

	print("Total of "+str(len(doubles))+" doubles in "+str(tryForDoubles)+" attempts.")

	if len(doubles) > tryForDoubles//10:
		if re.search(input("There are a significant number of doubles, " + \
			"would you still like to print them all?"),"y"):
			for x in doubles:
				print(x)
	else:
		for x in doubles:
			print(x)

	d = Die.faceFrequency(doubles)
	Die.printDictionary(d)

if __name__ == "__main__":
	main()



