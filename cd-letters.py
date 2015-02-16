#!/bin/python

import random
import time

#An exponent used to weight the frequencies. The frequencies of certain letters
#in the result is too high otherwise
exponent = 0.65

#English letter frequencies. Copied from wikipedia
freq = { 
		'a': 8.167 ** exponent,
		'b': 1.492 ** exponent,
		'c': 2.782 ** exponent,
		'd': 4.253 ** exponent,
		'e': 12.702 ** exponent,
		'f': 2.228 ** exponent,
		'g': 2.015 ** exponent,
		'h': 6.094 ** exponent,
		'i': 6.966 ** exponent,
		'j': 0.153 ** exponent,
		'k': 0.772 ** exponent,
		'l': 4.025 ** exponent,
		'm': 2.406 ** exponent,
		'n': 6.749 ** exponent,
		'o': 7.507 ** exponent,
		'p': 1.929 ** exponent,
		'q': 0.095 ** exponent,
		'r': 5.987 ** exponent,
		's': 6.327 ** exponent,
		't': 9.056 ** exponent,
		'u': 2.758 ** exponent,
		'v': 0.978 ** exponent,
		'w': 2.360 ** exponent,
		'x': 0.150 ** exponent,
		'y': 1.974 ** exponent,
		'z': 0.074 ** exponent
}


#Randomly generates n letters from the urn. A dictionary of letter
#frequencies should be passed in so that the letters can be drawn
#in correspondence with their frequency in the english language
# n -- Number of letters to gen
# urn -- List of letters to draw from
# freqs -- List of letter frequencies
# Returns a list of letters 
#Does not seed the random number generator

def genLetters( n, urn, freqs ):
	outList = []

	#Create a dictionary with just the letters 
	relFreqs = dict( ( x,  freqs[x] ) for x in urn ) 
	totalProb = sum( relFreqs.values() )

	for i in range( n ):
		randNum = random.random() * totalProb
		found = False
		for key, value in relFreqs.iteritems():
			if found == False and randNum < value:
				found = True
				outList.append( key )
			else:
				randNum = randNum - value

	return outList


random.seed( time.time() )

numVowels = int( raw_input( "How many vowels would you like?" ) )
numCons = 9 - numVowels

if numVowels > 5 or numVowels < 3: 
	print "Must have 3-5 vowels and 4-6 consonants"
	#Exit
else:
	gens = genLetters( numVowels, [ 'a', 'e', 'i', 'o', 'u' ], freq )
	gens = gens + genLetters( numCons, [ 'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z' ], freq )

	print gens
