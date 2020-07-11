import sys
import calendar as cal
from datetime import datetime as dt

num_args = len(sys.argv)

if num_args == 1:
	cal.TextCalendar().prmonth(dt.now().year, dt.now().month)
elif num_args == 2:
	cal.TextCalendar().prmonth(dt.now().year, int(sys.argv[1]))
elif num_args == 3:
	cal.TextCalendar().prmonth(int(sys.argv[2]), int(sys.argv[1]))
else:
	print((
        "usage: if no input, returns current month's calendar,\n"
        "if one arg is input, returns month calendar of current year,\n"
        "if two args input, return month calendar of year"
        ))

# print('Number of arguments:', len(sys.argv), 'arguments.')
# print('Argument List:', str(sys.argv))

# argList = sys.argv[1]
# print(argList)
# for i in argList:
# 	print(i)
# year = sys.argv[1]

# print(type(year))
