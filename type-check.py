# Program to understand return type of raw_input
userInput = raw_input('Enter text / number:\n');
print type(userInput);
userInput = userInput/2; #throws error as userInput is of string type
						 #to use as number use int(userInput)