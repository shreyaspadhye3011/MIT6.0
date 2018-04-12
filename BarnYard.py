# Problem Description: A farmer has pigs, chieckens & spiders in his barn. Given 2 inputs - number of heads & number of legs, output the number of pigs, chickens and spiders in the barn

def barnYard1(numHeads, numLegs):
	""" Returns number of [chickens, pigs, spiders] for a given [int numberOfHeads, int numberOfLegs] """
	for numPigs in range(0, numHeads + 1):
		for numChickens in range(0, (numHeads - numPigs) + 1):
			numSpiders = numHeads - numPigs - numChickens;
			numCalLegs = (4 * numPigs) + (4 * numSpiders) + (2 * numChickens);
			if (numCalLegs == numLegs):
				return [numPigs, numChickens, numSpiders]; 
	return [None, None, None];

def farmYard1():
	headsInput = raw_input("Enter number of heads: ");
	legsInput = raw_input("Enter number of legs: ");
	numPigs, numChickens, numSpiders = barnYard1(int(headsInput), int(legsInput));
	print (numPigs, ' pigs, ', numChickens, ' chickens & ', numSpiders, ' spiders.');

farmYard1();