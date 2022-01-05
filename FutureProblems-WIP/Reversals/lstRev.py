#!/usr/bin/python3
#Author: Adam Colvin
#Date: December 17, 2021
#Version: 1.0

'''
This program will take a provided list and reverse it
without using negative numbers in the list's index
(lstvar[::-1]), any pre-existing methods or functions
that reverse lists ( reverse(lstvar) ), or a reversed
range ( range(10,0,-1) ).

Input:
User is expected to provide a list via a statically
assigned variable in the code.

Output:
We would expect the program to print the list backwards.
i.e. [1, 2, 3, 4, 5] becomes [5, 4, 3, 2, 1]
'''

lst = [1,2,3,4,5]
rev = []

for i in lst:
    rev.insert(0, i)
    
print(rev)
