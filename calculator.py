"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *


# Your code goes here

# take input and split it into a list (tokenize)
print("Welcome to the calculator!")


operation_file = open("operations.txt", "r")
result_file = open("results.txt", "w")

while True:

	user_input = operation_file.readline().rstrip()
	print(user_input)

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


#the 0'th word in the token is the operator
	operator = token[0]
	if operator == "q":
		break
		pass	

	error_message = "Please enter in a valid input."


	if len(token) < 3:
		result = error_message
		continue

	if len(token) > 4:
		result = error_message
		continue

	num1 = int(token[1])
	num2 = int(token[2])

	if len(token) == 3:
		if operator == "+":
			result = add(num1, num2)
		elif operator == "-":
			result = subtract(num1, num2)
		elif operator == "*":
			result = multiply(num1, num2)
		elif operator == "/":
			result = divide(num1, num2)
		elif operator == "square":
			result = square(num1, num2)
		elif operator == "cube":
			result = cube(num1, num2)
		elif operator == "pow":
			result = power(num1, num2)
		elif operator == "mod":
			result = mod(num1, num2)
		elif operator == "cube+":
			result = add_cubes(num1, num2)
		else:
			result = error_message

	if len(token) == 4:
		num3 = int(token[3])
		if operator == "x+":
			result = add_mult(num1, num2, num3)
		else:
			result = error_message


	result_file.write(" >>> {} \n".format(result))	


operation_file.close()
result_file.close()
# the operator determines which command(function) to use

#most functions have 2 arguments, but some have 3


