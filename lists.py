x = [0.0, 3.0, 5.0, 2.5, 3.7]
print(type(x))

# remove the third element
x.pop(2) # remember that we zero-index!
print("x.pop(2)?", x)

x.remove(2.5)
print("x.remove(2.5)?", x)

x.append(1.2)
print("x.append(1.2)?", x)

y = x.copy() # we have to make a copy!!!!!
print(y)

print("y.count(0.0)?", y.count(0.0))

print("y.index(3.7)?", y.index(3.7))

y.sort()
print("y.sort", y)

y.reverse()
print("y.reverse", y)

y.clear()
print("y.clear", y)