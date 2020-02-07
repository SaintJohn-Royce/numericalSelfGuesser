import random

#lowerRangeA = input('please put in the lower range of the randomizer: ')
#upperRangeA = input('please put in the upper range of the randomizer: ')

#lowerRangeA = int(lowerRangeA)
#upperRangeA = int(upperRangeA)

lowerRangeA = 1
upperRangeA = 100
numberAuth = random.randint(lowerRangeA, upperRangeA)
numberBeta = random.randint(lowerRangeA, upperRangeA)

counter = 1

if numberAuth == numberBeta:

	print(counter)

elif numberAuth > numberBeta:

	lowerRangeA = numberBeta
	numberBeta = random.randint(lowerRangeA + 1, upperRangeA)

else: # numberAuth < numberBeta 

	upperRangeA = numberBeta
	numberBeta = random.randint(lowerRangeA, upperRangeA - 1)

while numberAuth != numberBeta:

	counter = counter + 1

	if numberAuth > numberBeta:

		lowerRangeA = numberBeta
		numberBeta = random.randint(lowerRangeA + 1, upperRangeA)

	elif numberAuth < numberBeta:

		upperRangeA = numberBeta
		numberBeta = random.randint(lowerRangeA, upperRangeA - 1)

	else:

		break
	
print(counter)