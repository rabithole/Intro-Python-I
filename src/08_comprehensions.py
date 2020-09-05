"""
List comprehensions are one cool and unique feature of Python.
They essentially act as a terse and concise way of initializing
and populating a list given some expression that specifies how
the list should be populated. 

Take a look at https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
for more info regarding list comprehensions.
"""

# Write a list comprehension to produce the array [1, 2, 3, 4, 5]

y = [num for num in range(1, 6)]

# comprehension above is derived from the for loop below. 
# for num in range(1, 6):
# 	y.append(num)

print (y)

# Write a list comprehension to produce the cubes of the numbers 0-9:
# [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]

y = [num ** 3 for num in range(10)]

# num ** 3 in append is added to the front of the list comprehension. 
# for num in range(10):
# 	y.append(num ** 3)

print(y)

# Write a list comprehension to produce the uppercase version of all the
# elements in array a. Hint: "foo".upper() is "FOO".

a = ["foo", "bar", "baz"]
i = 0
# while i < len(a):
# 	print('')
# 	print(a[i].upper())
# 	i += 1
print('')
# for i in a:
# 	print(i.upper())

y = [i.upper() for i in a]

print(y)

# Use a list comprehension to create a list containing only the _even_ elements
# the user entered into list x.

x = input("Enter comma-separated numbers: ").split(',')

# What do you need between the square brackets to make it work?
print('')
y = [i for i in x if int(i) % 2 == 0 ]

# for i in x:
# 	if int(i) % 2 == 0:
# 		print(i)

print(y)
print('')