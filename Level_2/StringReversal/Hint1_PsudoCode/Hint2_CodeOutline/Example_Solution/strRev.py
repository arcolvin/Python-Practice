#!/usr/bin/env python3
#Author: Adam
#Date: Dec 15, 2021
#Version: 1.0


'''
This program will take a provided string and reverse it
without using negative numbers in the string's index
(stringvar[::-1]), any pre-existing methods or functions
that reverse strings, reversed range ( range(10,0,-1), or
any other process of 'counting down' in the string's index).

Input:
User is expected to provide a string via a statically
assigned variable in the code.

Output:
We would expect the program to print the string backwards.

ex:
'Hello World!' should print as '!dlroW olleH'
'''

# The string to be reversed
string = 'Hello World!'

# Initialize the final reversed string
rev = ''

# Build loop for string processing
for l in string:

    # Code to add each letter to the front of the reversed string
    rev = l + rev

# Print final String
print(rev)
