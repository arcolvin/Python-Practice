#!/usr/bin/env python3
#Author: Adam
#Date: Dec 15, 2021
#Version: 1.0


'''
This program will take a provided string and reverse it
without using negative numbers in the string's index
(stringvar[::-1]), any pre-existing methods or functions
that reverse strings, or a reversed range ( range(10,0,-1) )

Input:
User is expected to provide a string via a statically
assigned variable in the code.

Output:
We would expect the program to print the string backwards.
i.e. 'Hello World!' becomes '!dlroW olleH'
'''

string = 'Hello World!'
rev = ''

for l in string:
    rev = l + rev

print(rev)
