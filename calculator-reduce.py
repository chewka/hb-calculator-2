"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *
from functools import reduce


# Your code goes here

# take input and split it into a list (tokenize)
print("Welcome to the calculator!")


operation_file = open("operations.txt", "r")
result_file = open("results.txt", "w")

while True:

	user_input = operation_file.readline().rstrip()
	#print(user_input)

	"""	lines = [0, 5]
		i = 0
		for line in operation_file:
			print (line)
			print(user_input)
			i+=1
	"""
	if user_input == "STOP HERE":
		break

	token = user_input.split(" ")
	for i in range(1,len(token)):
		token[i] = float(token[i])

#the 0'th word in the token is the operator
	operator = token[0]
	if operator == "q":
		break
		pass	

	error_message = "Please enter in a valid input."

	if operator == "+":
		result = reduce(add, token[1:])
	elif operator == "-":
		result = reduce(subtract, token[1:])
		print(token[1:])
	elif operator == "*":
		result = reduce(multiply, token[1:])
	elif operator == "/":
		result = reduce(divide, token[1:])
	elif operator == "square":
		if len(token) != 2:
			result = error_message
		else:
			result = square(token[1])
	elif operator == "cube":
		if len(token) != 2:
			result = error_message
		else:
			result = cube(token[1])
	elif operator == "pow":
		result = reduce(power, token[1:])
	elif operator == "mod":
		result = reduce(mod, token[1:])
	elif operator == "cube+":
		result = reduce(add_cubes, token[1:])
	else:
		result = error_message

	if len(token) == 4:
		num3 = int(token[3])
		if operator == "x+":
			result = reduce(add_mult, token[1:])
		else:
			result = error_message


	result_file.write(" >>> {} \n".format(result))	


operation_file.close()
result_file.close()
# the operator determines which command(function) to use

#most functions have 2 arguments, but some have 3


