"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


# Replace this with your code

while True:

	input_string = input('Enter your equation > ')
		
	tokens = input_string.split(' ')

	if tokens[0] == '+':
		print(add(int(tokens[1]), int(tokens[2])))

	elif tokens[0] == '-':
		print(subtract(int(tokens[1]), int(tokens[2])))

	elif tokens[0] == '*':
		print(multiply(int(tokens[1]), int(tokens[2])))

	elif tokens[0] == '/':
		print(divide(int(tokens[1]), int(tokens[2])))

	elif tokens[0] == 'square':
		print(square(int(tokens[1])))

	elif tokens[0] == 'cube':
		print(cube(int(tokens[1])))		 			

	elif tokens[0] == 'pow':
		print(power(int(tokens[1]), int(tokens[2])))

	elif tokens[0] == 'mod':
		print(mod(int(tokens[1]), int([tokens[2]])))




