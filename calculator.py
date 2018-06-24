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




	if token[0] == "q":
		pass	
		#quit
		
	if len(token) <=3:
		if token[0] == "+":
			#call the add function
			pass
		if token[0] == "-":
			#call the subtr function
			pass
		if token[0] == "*":
			#call the multip function
			pass
		if token[0] == "/":
			#call the div function
			pass
		if token[0] == "square":
			#call the square funtion
			pass
		if token[0] == "cube":
			#call the cube function
			pass
		if token[0] == "pow":
			#call the power function
			pass

		if token[0] == "mod":
			#call the modulo function
			pass





#the 0'th word in the token is the operator


# the operator determines which command(function) to use

#most functions have 2 arguments, but some have 3


