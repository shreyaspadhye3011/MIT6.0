# Program to distinguish even & odd numbers without using '%' operator
userInput = int(raw_input('Enter a number: '));
# print type(userInput);
if((userInput / 2) * 2 == userInput):
	print userInput, ' IS even';		#concatenating int & strings without type cast
else:
	print str(userInput) + ' is odd';