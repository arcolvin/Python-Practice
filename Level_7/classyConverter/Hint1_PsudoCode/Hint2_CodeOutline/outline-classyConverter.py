#!/usr/bin/env python3
# Author: Adam
# Date: December 30, 2021
# Version: 0.5

'''
This program is an example of how to use classes and
object orened programming!

Prompt:
Build a program that utilizes classes to store multiple converted values for a given number.

The class should have paramaters for each of the stored bases (Base 2, 8, 10, and 16)
This class should have methods for the 4 basic mathematical opperations (+, -, *, and /).
This would mean that <class1> + <class2> should return a class object that contains the
results of that operation in all common bases (bases 2, 8, 10, 16)

There should be a method to update the classes' stored number. the user should be able
to specify the base of the entered number.

There should be a method to print all stored values.

Optional stretch Goal:
Implement logging via the logging module


Input:
User will enter numbers and their bases as well as menu items

Output:
Program will return a list of stored numbers or the 
result of basic mathemetical opperations

---

Helpful resources:

Python Classes:
https://www.w3schools.com/python/python_classes.asp

Classes or Functions First?:
https://stackoverflow.com/questions/28365304/python-declaration-order-classes-or-functions-first

Magic / Dunder methods:
https://www.section.io/engineering-education/dunder-methods-python/#73-other-operators

Magic / Dunder Methods 2:
https://www.tutorialsteacher.com/python/magic-methods-in-python

'''

# Required imported modules
import logging
import datetime

# Add simplified logging function
def msg(lvl, txt):
    '''
    We expect the program to pass a string for lvl
    d = debug
    i = info
    w = warn
    e = error
    
    and the text for the logged message as a string
    '''
    logging.basicConfig(filename='bintodecclean.log',level=logging.INFO)
    logger = logging.getLogger(__name__)
    
    # Error messages
    if lvl == 'e':
        logger.error(str(datetime.datetime.now()) + ':' + txt)
        
    # Warning messages
    elif lvl == 'w':
        logger.warning(str(datetime.datetime.now()) + ':' + txt)
    
    # Info messages
    elif lvl == 'i':
        logger.info(str(datetime.datetime.now()) + ':' + txt)
    
    # Debug messages
    elif lvl == 'd':
        logger.debug(str(datetime.datetime.now()) + ':' + txt)
        
    # Error message if incorrect error type is coded
    else:
        # Use -> in log message so that a ':' does not interfer with
        # ':' log delimiters already in place
        logger.error('CRITICAL - Problem with logging function')
        logger.error(f'Unknown error type requested. Provided paramaters lvl -> {lvl}, txt -> {txt}')

# Define number class
class number:

    # Param names are b# for Base <number>
    # Note: 'bin' and 'hex' are inbuilt functions and cant be used for variable names
    # can use below constants if needed
    '''
    b2 = None
    b10 = None
    b16 = None
    '''

    # Add init method to collect user's number
    def __init__(self):
        # TODO make this capable of accepting a user's input
        # TODO make input smart enough to handle base 2, 8, 10, 16
        # TODO Add error handling in case the user does not enter an expected number

        self.b2 = bin(0)
        self.b8 = oct(0)
        self.b10 = str(0)
        self.b16 = hex(0)

        return None
    
    # Add an add method
    def __add__(self, other):
        # TODO for + operations
        return None 

    # add a subtract method
    def __sub__(self, other):
        # TODO for - operator
        return None

    # add a multiply method
    def __mul__(self, other):
        # TODO for * operator
        return None

    # add a divide method
    def __truediv__(self, other):
        # TODO for / operator
        # TODO add error handling for divide by zero
        # NOTE: This will function as floordiv as floats don't
        # make sense for non-base 10 numbers
        return None

    def all(self):
        # TODO Print all conversion outputs

        return None


# Add Menu function (Make Classy?)
# TODO Make it classy maybe?
def menu():
    # add menu options for the following operations
    # TODO Add
    # TODO Subtract
    # TODO Multiply
    # TODO Divide
    # TODO reset numbers
    # TODO print all numbers
    # TODO other maybe?
    return None

# add if name == main and any other driver code
if __name__ == '__main__':

    menu()

    # test code to make sure program can run
    # Comment out or remove from final program
    print("The program finished even if it didn't do what you wanted it to!")