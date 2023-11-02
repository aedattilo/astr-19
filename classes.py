# define a class with an initialized
# set of parameters

import sys

class Shape:
	# a class for geometric shapes

	def print(self):
		print("Here is out shape!")
		print(f"Number of sides = {self.num_sides}")
		print(f"Length of sides = {self.side_length}")

	def __init__(self, nsides=3, length=1.):
		self.num_sides = nsides
		self.side_length = length

def main():

	nsides = 3
	length = 10,

	if(len(sys.argv) >= 2):
		nsides = int(sys.argv[1])


	if(len(sys.argv)>=3):
		length = floaf(sys.argv[2])

	our_shape = Shape(nsides=nsides, length=length)

	our_shape.print()

if __name__=="__main__":
	main()

