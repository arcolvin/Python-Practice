#!/usr/bin/python3
#Author: Adam
#Date: 12/13/2021
#Version: 1.0


'''
This program will print a number of waves then exit.

It was programmed and tested in Thonny

Input:
User input will be collected via in program prompts
using the input function.

Output:
We would expect a number of waves to be printed to the
terminal
'''

legnth = ''
width = ''

while not(legnth.isnumeric()):
    legnth = input('How many waves do you want to print? ')
    if not(legnth.isnumeric()):
        print('Please enter a whole number!')

while not(width.isnumeric()):
    width = input('How wide should the waves be? ')
    if not(width.isnumeric()):
        print('Please enter a whole number!')
    
wlegnth = int(legnth)
wwidth = int(width)

again = True
wavedone = 0

while again:
    if wavedone == wlegnth:
        again = False
    
    else:
        for x in range(wwidth):
            print(x * '#')
            
        for y in range(wwidth):
            print((wwidth - y) * '#')
            
        wavedone +=1
        