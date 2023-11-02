# define a dictionary data structure

# dictionaries have a key:value for the elements
example_dict = {
	"class"			: "ASTR 19",
	"prof"			: "Brant",
	"awesomeness"	: 10
}
print(type(example_dict))

# get a value via key
course = example_dict["class"]
print(course)

# change a value via key
example_dict["awesomeness"] += 1 # increase awesomeness

print(example_dict)

# print dictionary element by element
for key in example_dict.keys():
	print(key, example_dict[key])