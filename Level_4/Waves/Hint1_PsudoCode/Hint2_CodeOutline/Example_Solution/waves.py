#!/usr/bin/python3
#Author: Adam
#Date: 12/13/2021
#Version: 1.0


'''
This program will print a number of waves of a given width then exit.

Input:
User input will be collected via in program prompts
using the input function.

Output:
We would expect a number of waves to be printed to the
terminal

ex.
How many waves do you want to print? 2
How wide should the waves be? 4

#
##
###
####
###
##
#

#
##
###
####
###
##
#
'''

# Initialize legnth and width variables
legnth = ''
width = ''


# set up basic input validation to ensure the user is entering an intiger
# Ask user for number of waves
while not(legnth.isnumeric()):
    legnth = input('How many waves do you want to print? ')
    if not(legnth.isnumeric()):
        print('Please enter a whole number!')

# set up basic input validation to ensure the user is entering an intiger
# Ask user for width of waves
while not(width.isnumeric()):
    width = input('How wide should the waves be? ')
    if not(width.isnumeric()):
        print('Please enter a whole number!')
    
# Convert collected numbers to intiger type if not done already
wlegnth = int(legnth)
wwidth = int(width)

# Set up loop counter and end condition variables
again = True
wavedone = 0

# build wave printing loop
while again:
    # add logic to end loop if we have finished counting
    if wavedone == wlegnth:
        again = False
    
    # otherwise keep going
    else:
        # Add code to print the wave counting up
        for x in range(wwidth):
            print(x * '#')
            
        # Add code to count back down so the wave gets shorter
        for y in range(wwidth):
            print((wwidth - y) * '#')
            
        # Count that one wave has finished printing
        wavedone +=1
        