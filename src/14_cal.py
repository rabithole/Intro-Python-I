"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py [month] [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.

Note: the user should provide argument input (in the initial call to run the file) and not 
prompted input. Also, the brackets around year are to denote that the argument is
optional, as this is a common convention in documentation.

This would mean that from the command line you would call `python3 14_cal.py 4 2015` to 
print out a calendar for April in 2015, but if you omit either the year or both values, 
it should use today’s date to get the month and year.
"""

import sys
import calendar
from datetime import datetime

# x = dir(calendar)

# for(index, element) in enumerate(x):
# 	print(f'Element {index} is {element}')

# print(calendar.firstweekday())

# year, month = map(input('Enter the year and month: ').split())

# print(f'Year: 19{year}, month: {month}')


# currentMonth = datetime.now().strftime('%B')
# print(currentMonth)
# print(datetime.now().year,datetime.now().month)
# print(calendar.TextCalendar().formatmonth(datetime.now().year, datetime.now().month))

# print(calendar.TextCalendar().formatmonth(1971, 11))

# print(datetime.now().month)
# print(datetime.today())
# print(datetime(today.year, today.month, 1))

# Python program to take multiple inputs from the user
# a, b = input("Enter two of your lucky number: ").split() 
# print("First lucky number is: ", a) 
# print("Second lucky number is: ", b) 
# year = datetime.now().year
# month = datetime.now().month
# print(f'Line 62: {year}, {month}')
# for i in sys.argv:
# 	print(i)

def cal():
	# year = input('Enter the four digit year: ')
	# month = input('Enter the month number: ')
	numArg = sys.argv
	# print(numArg[1], numArg[2])
	# year = numArg[1]
	# month = numArg[2]
	# print(year)
	if len(numArg) == 3:
		year = numArg[1]
		month = numArg[2]
		print('3')
	elif len(numArg) == 2:
		year = sys.argv[1]
		month = ''
		print('2')
	else:
		year = ''
		month = ''
		print('1')

	print(f'{year}, {month}')

	if year == '' and month == '':
		print(calendar.TextCalendar().formatmonth(datetime.now().year, datetime.now().month))
		print(f'{year} first if')
	elif year == '':
		print(calendar.month(datetime.now().year, int(month)))
		print('second if')
	elif month == '':
		print(calendar.month(int(year), datetime.now().month))
		print('third if')
	else: 
		print(f'{calendar.month(int(year), int(month))}')

cal()

# print(calendar.month(1971, 4))
# print(sys.argv[2], sys.argv[1], sys.argv[0])