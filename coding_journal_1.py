# Session 1 Prompt: Write a Python program to 
# print out your full name, your preferred pronouns (optional), 
# and two sentences about your favorite movie and your favorite food.

def about_me():
	print("~~~~~~~~~~~~~~ABOUT ME~~~~~~~~~~~~~~~")
	print("Hello my name is Anne (she/her/hers)!")
	print("My favorite movie is\nPride & Prejudice (2005)\ndirected by Joe Wright.")
	print("The hand scene....\n.... do I need to explain?")
	print("I am obsessed with heirloom beans,\nas grown by Rancho Gordo.")
	print("Thanks for getting to know me!")
	print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

# Session 2 Prompt: Write a Python that prints
# the sum of two floating point numbers,
# the difference between two integers,
# and the product of a floating point number
# and an integer. In each case, have the program print
# out the data type of the resulting answer.

def lets_do_math(num_1, num_2):
	sum_ = float(num_1) + float(num_2)
	diff = int(num_1) - int(num_2)
	prod = float(num_1) * int(num_2)
	print(sum_, type(sum_))
	print(diff, type(diff))
	print(prod, type(prod))

# Session 3 Prompt: Write a Python program that defines
# a function f(x) that returns x**3 + 8. In the main
# function of the program, call f(x) with x = 9 and print
# the result.  Use an if statement that executes if the
# result is larger than 27 and prints “YAY!”.

def f(x):
	return x**3 + 8

# Session 4 Prompt: Write a Python program that declares
# a class describing your favorite animal. Have the data
# members of the class represent the following physical parameters
# of the animal: length of the arms (float), length of the legs (float),
# number of eyes (int), does it have a tail? (bool), is it furry? (bool).
# Write an initialization function that sets the values of the data
# members when an instance of the class is created. Write a member
# function of the class to print out and describe the data members
# representing the physical characteristics of the animal.

class animal:

	def get_physical_attrs(self):
		print(f"Its arms have length {self.arm_length}.")
		print(f"Its legs have length {self.leg_length}.")
		print(f"It has {self.num_eyes} eyes.")

		if self.tail:
			print("It has a tail.")
		else:
			print("It does NOT have a tail.")

		if self.furry:
			print("It is furry.")
		else:
			print("It is hairless.")

	def __init__(self, name, arm_length=10.,leg_length=20.,
		num_eyes=50, tail=False, furry=False):
		self.name = str(name)
		self.arm_length = float(arm_length)
		self.leg_length = float(leg_length)
		self.num_eyes = int(num_eyes)
		self.tail = bool(tail)
		self.furry = bool(furry)

		print(f"My favorite animal is {self.name}!")

# Session 5 Prompt: Write a Python program that writes out
# a table of the function sin(x) vs. x, where x is tabulated
# between 0 and 2 with a thousand entries. Follow the basic
# Python program structure, including a main program function.

import numpy as np
def trig():
	x = np.linspace(0, 2*np.pi, num=1000)
	sinx = np.sin(x)
	print("    x   | sin(x)  ")
	for i in range(10):
		print(f"{x[i]:8f}|{sinx[i]:8f}")

def main():
	print("#############PROMPT 1################")
	about_me()

	print("#############PROMPT 2################")
	lets_do_math(2, 5)

	print("#############PROMPT 3################")
	print(f(x=9))

	if f(9) > 27:
		print("YAY!")

	print("#############PROMPT 4################")
	favorite = animal(name="MothMan")
	favorite.get_physical_attrs()

	print("#############PROMPT 5################")
	trig()

# let's run this
if __name__=="__main__":
	main()




