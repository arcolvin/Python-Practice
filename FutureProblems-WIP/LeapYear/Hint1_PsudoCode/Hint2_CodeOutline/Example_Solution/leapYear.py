#!/usr/bin/python3
#Author: <NAME>
#Date: <DATE>
#Version: 1.0


'''
If a year is divisible by 4 its a leap year,
unless its also divisible by 100 then its not, 
unless its also divisible by 400 then it is.

Input:
TODO describe program inputs

Output:
TODO describe program outputs

Ex. 
TODO Provide example input / output
'''

import sys

year = int(sys.argv[1])
yes = '{} is a leap year!'.format(year)
no = '{} is NOT a leap year!'.format(year)

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(yes)

        else:
            print(no)

    else:
        print(yes)

else:
    print(no)
