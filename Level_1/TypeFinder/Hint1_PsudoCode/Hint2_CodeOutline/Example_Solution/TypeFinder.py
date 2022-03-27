#!/usr/bin/python3
#Author: Adam
#Date: Mar 26, 2022
#Version: 1.0


'''
Make a program capable of identifying different data types.
Critical tools include type(), print(), and if/else

Input:
Static variables assigned in the code

Output:
Program will print the type of the provided data

Ex. 
Your variable XXX is type String
'''

# Set variable
whatAmI = ('Data', 'str')

# Compare variable to known types
# Print Result
if type(whatAmI) == str:
    print('The variable is a String!')

elif type(whatAmI) == list:
    print('Your variable is a List!')

elif type(whatAmI) == tuple:
    print('Your variable is a Tuple!')

elif type(whatAmI) == dict:
    print('Your variable is a Dictionary!')

else:
    print('I don\'t know what type that is!')
