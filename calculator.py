"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *


# Your code goes here

# take input and split it into a list (tokenize)
while True:
	user_input = input()

	token = user_input.split(" ")


#the 0'th word in the token is the operator
	operator = token[0]
	if operator == "q":
		break
		pass	

	if len(token) == 2:
		print("Please enter in a valid input")
		continue

	num1 = int(token[1])
	num2 = int(token[2])


	if len(token) <=3:
		if operator == "+":
			print(add(num1, num2))
		if operator == "-":
			print(subtract(num1, num2))
		if operator == "*":
			print(multiply(num1, num2))
		if operator == "/":
			print(divide(num1, num2))
		if operator == "square":
			print(square(num1, num2))
		if operator == "cube":
			print(cube(num1, num2))
		if operator == "pow":
			print(power(num1, num2))
		if operator == "mod":
			print(mod(num1, num2))
		if operator == "cube+":
			print(add_cubes(num1, num2))

	if len(token) == 4:
		num3 = int(token[3])
		if operator == "x+":
			print(add_mult(num1, num2, num3))

	if len(token) > 4:
		print("Please enter in a valid input")
		



# the operator determines which command(function) to use

#most functions have 2 arguments, but some have 3


