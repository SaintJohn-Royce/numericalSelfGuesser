import random
import statistics

lowerRInsert = input('please put in the lower range of the randomizer: ')
upperRInsert = input('please put in the upper range of the randomizer: ')
lowerRInsert = int(lowerRInsert)
upperRInsert = int(upperRInsert)
lowerRangeA = lowerRInsert
upperRangeA = upperRInsert

populationControl = input('please input population size: ')
populationControl = int(populationControl)

data = []

for index in range(populationControl):

	lowerRangeA = lowerRInsert
	upperRangeA = upperRInsert

	numberAuth = random.randint(lowerRangeA, upperRangeA)
	numberBeta = random.randint(lowerRangeA, upperRangeA)

	counter = 1

	if numberAuth > numberBeta:

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
		
	data.append(counter)

print('------------')

print('mean: ', statistics.mean(data))

print('median: ', statistics.median(data))

print('population standard deviation: ', statistics.pstdev(data))

print('population variance: ', statistics.pvariance(data))

print('------------')