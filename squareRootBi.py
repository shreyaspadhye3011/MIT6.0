# Lec 5: Finding square root of a number uaing divide & conquer

def squareRootBi(x, epsilon):
	""" Accepts number whose square root is required & the epsilon value (to manage degree of precision) """
	assert x >= 0, 'x must be non negative: ' + str(x);
	assert epsilon >= 0, 'epsilon must be non negative: '+ str(epsilon);

	low = 0;
	high = max(x, 1);	# to handle cases when 0 < x < 1 as sqrt(0.25) is 0.5 which is greater than 0.25
	guess = (low + high) / 2.0;
	ctr = 1;

	while (abs(guess**2 - x) > epsilon) and ctr < 100:
		if (guess**2 > x):
			high = guess;
		else:
			low = guess;
		print 'Current counter: ' + str(ctr);
		ctr += 1;
	assert ctr < 100, 'Max counter reached';
	print 'Square root: ' + str(guess) + '. Reached in ' + str(ctr) + ' iterations';
	return guess;

squareRootBi(4, 0.001);