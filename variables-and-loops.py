import numpy as np

def main():
	i = 0     # an integer
	n = 10    # another integer
	x = 19.0  # a float

	# empty array to fill later
	y = np.zeros(n, dtype=float)

	# calculate n number of odd numbers
	for i in range(n):
		y[i] = 2.0 * float(i) + 1.0

	# print the array, element by element
	for y_element in y:
		print(y_element)

# run this bad thing
if __name__=="__main__":
	main()