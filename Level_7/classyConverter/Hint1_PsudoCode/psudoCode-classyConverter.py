#!/usr/bin/env python3

# Author: Adam Colvin
# Date: December 30, 2021
# Version: 0.5

'''
This program is an example of how to use classes and
object orened programming!

Prompt:
Build a program that utilizes classes to store multiple converted values for a given number.

The class should have paramaters for each of the stored bases (Base 2, 8, 10, and 16)
This class should have methods for the 4 basic mathematical opperations (+, -, *, and /).
This would mean that <class1> + <clas2> should return a class object that contains the
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

# Add required imported modules

# OPTIONAL: Add logging function

# Define number class
    # add init method to enter user's number or set default values if no numbers given
        # Make input smart enough to handle base 2, 8, 10, 16
        # Add error handling in case the user does not enter an expected number or base
        # Add paramaters to store the provided number's values
        # Store all basic conversions at the same time
            # bin oct dec and hex
    # add an add method
    # add a subtract method
    # add a multiply method
    # add a divide method
        # add error handling for divide by zero
        # Can non-base 10 numbers be represented as a float?
        # Floor Division?
    # add method to print all number values
    # add method to update numbers

# Define Menu function
    # Allow user to select any of the above number methods

# add if name == main and any other driver code
