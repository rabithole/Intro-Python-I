"""
In this exercise, you'll be playing around with the sys module,
which allows you to access many system specific variables and
methods, and the os module, which gives you access to lower-
level operating system functionality.
"""

import sys
# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

# Print out the command line arguments in sys.argv, one per line:
# YOUR CODE HERE

# x = dir(sys.argv)

# for (index, element) in enumerate(x):
# 	print(f'Element {index} is {element}')

# total arguments 
# n = len(sys.argv) 
# print("Total arguments passed:", n) 
  
# # Arguments passed 
# print("\nName of Python script:", sys.argv[0]) 
  
# print("\nArguments passed:", end = " ") 
# for i in range(1, n): 
#     print(sys.argv[i], end = " ") 
      
# # Addition of numbers 
# Sum = 0
# # Using argparse module 
# for i in range(1, n): 
#     Sum += int(sys.argv[i]) 
      
# print("\n\nResult:", Sum) 

# if __name__ == "__main__":
#     print(f"Arguments count: {len(sys.argv)}")
#     for i, arg in enumerate(sys.argv):
#         print(f"Argument {i:>6}: {arg}")


# Print out the OS platform you're using:
# YOUR CODE HERE
import os
import platform

print(os.name)
print(sys.platform)
print(platform.system())
print(platform.release())

# Print out the version of Python you're using:
# YOUR CODE HERE
print('')
print(sys.version)

# See the docs for the OS module: https://docs.python.org/3.7/library/os.html
# Print the current process ID
# YOUR CODE HERE
print('')
print(os.getpid())

# Print the current working directory (cwd):
# YOUR CODE HERE
print('')
print(os.getcwd())

# Print out your machine's login name
# YOUR CODE HERE
print('')
print(os.getlogin())


