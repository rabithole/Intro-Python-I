# For the exercise, look up the methods and functions that are available for use
# with Python lists.

x = [1, 2, 3]
y = [8, 9, 10]

# For the following, DO NOT USE AN ASSIGNMENT (=).

# Change x so that it is [1, 2, 3, 4]
# YOUR CODE HERE
print('')
x.append(4)
print(x)

# Using y, change x so that it is [1, 2, 3, 4, 8, 9, 10]
# YOUR CODE HERE
print('')
# x = x + y
# print(x)

# Change x so that it is [1, 2, 3, 4, 9, 10]
# YOUR CODE HERE
print('')
x = x + y
x.remove(8)
print(x)

# Change x so that it is [1, 2, 3, 4, 9, 99, 10]
# YOUR CODE HERE
print('')
x.insert(5, 99)
print(x)

# Print the length of list x
# YOUR CODE HERE
print('')
print(len(x))

# Print all the values in x multiplied by 1000
# YOUR CODE HERE
print('')
a = 0
while x:
	# print(x.pop(-1) * 1000)
	print(x[a] * 1000)
	a += 1
	if a == len(x):
		break
	
# for i in x:
# 	print(i * 1000)
print('')
print(x)