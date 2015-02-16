#!/bin/python

import random
import time

#genNums
#Randomly generates n numbers from the list of possibleNums.
#The output list will contain at most maxOccurs number of each
#number
#Returns a list of the numbers
#Returns nothing if maxOccurs * len( possibleNums ) < n
#does not seed random number generator

def genNums( n, possibleNums, maxOccurs ):
	if maxOccurs * len( possibleNums ) < n:
		return []

	gens = []
	for i in range( n ):
		valid = False
		while valid != True:
			randNum = random.choice( possibleNums )
			numOccurs = 0
			for n in gens:
				if n == randNum:
					numOccurs = numOccurs + 1

			if numOccurs < maxOccurs:
				valid = True
				gens.append( randNum )

	return gens



random.seed( time.time() )

numLarge = int( raw_input( "How many large numbers would you like?" ) )
numSmall = 6 - numLarge

if numLarge > 4 or numLarge < 0: 
	print "Must have 0-4 large numbers"
	#Exit
else:
	gens = genNums( numSmall, range( 1, 10 ), 2 )
	gens = gens + genNums( numLarge, range( 25, 125, 25 ), 1 )
	
	print gens
	print "Target is: " + str( random.randrange( 200, 1000 ) )
