"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


# Replace this with your code

#??? do while NOT function??? 

def tokenization(input_string):
		
	tokens = input_string.split(' ')

		if tokens[0] == 'add':
			return add(int(tokens[1]), int(tokens[2]))

		elif tokens[0] == 'subtract':
			return subtract(int(tokens[1]), int(tokens[2]))

		elif tokens[0] == 'multiply':
			return multiply(int(tokens[1]), int(tokens[2]))

		elif tokens[0] == 'divide':
			return divide(int(tokens[1]), int(tokens[2]))

		elif tokens[0] == 'square':
			return square(int(tokens[1]), int(tokens[2]))

		elif tokens[0] == 'cube':
			return cube(int(tokens[1]), int(tokens[2]))		 			

		elif tokens[0] == 'pow':
			return power(int(tokens[1]), int(tokens[2]))

		elif tokens[0] == 'mod':
			return mod(int(tokens[1]), int([tokens[2]]))		


print(tokenization(input('Enter your equation > ')))

