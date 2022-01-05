#!/usr/bin/env python3

# Author: Adam Colvin
# Date: December 30, 2021
# Version: 1.1


'''
This program is an example of how to use classes and
object orened programming!

It will combine programs we have already worked with
with object orented concepts.

User input: Users will enter menu options and numbers as requested
            through input functions

Expected Output: Program will print messages depending on the
            program's state. One common state will be to print out
            the numbers entered or calculated by the program

Fixes in this version:
    * Added additional comments
    * Implemented class all call instead of explicitly setting up print command again
    * Code formatting improvements

Known issues:
    None

Future Planned Improvements:
    * Add in other magic dunder methods?
    * Make program more fluid to use rather than the clunky implementation
      currently in place. 
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
    logging.basicConfig(filename='classyConverter.log',level=logging.INFO)
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
        logger.error('CRITICAL - Problem with logging function')
        logger.error(f'Unknown error type requested. Provided paramaters lvl -> {lvl}, txt -> {txt}')

# Define number class
class number:

    # Param names are b# for Base <number>
    # Note: 'bin' and 'hex' are inbuilt functions and cant be used for variable names
    # can use below constants if needed
    '''
    b2 = None
    b8 = None
    b10 = None
    b16 = None
    '''

    # Add init method to collect user's number
    def __init__(self, num='0', base='10'):
        try:
            # Attempt to re assign all base values for the number
            self.b2 = bin(int(num, int(base)))
            self.b8 = oct(int(num, int(base)))
            self.b10 = str(int(num, int(base)))
            self.b16 = hex(int(num, int(base)))

        except TypeError:
            # If unexpected data is ecountered catch the errorand set all
            # parameters to 0
            print('Type Error')
            print('Unexpected input for provided base')
            print('Setting numbers to 0')
            print(f'Num: {num} Base: {base}')

            msg('e', 'Type Error while assigning numbers to class Numbers()' \
                + f' Num-> {num} Base-> {base}')

            self.b2 = bin(0)
            self.b8 = oct(0)
            self.b10 = str(0)
            self.b16 = hex(0)

        except:
            # if unexpectd error is encountered capture error
            # log entered paramiters and set number to 0
            print('Unknown Error')
            print('Setting numbers to 0')

            msg('e', 'Unknown error while assigning numbers to class Numbers()' \
                + f' Num-> {num} Base-> {base}')

            self.b2 = bin(0)
            self.b8 = oct(0)
            self.b10 = str(0)
            self.b16 = hex(0)

        return None
    
    # Add an add methods
    def __add__(self, other):
        # for + operations
        return number(str(int(self.b10) + int(other.b10)))

    # add a subtract methods
    def __sub__(self, other):
        # for - operator
        return number(str(int(self.b10) - int(other.b10)))

    # add a multiply methods
    def __mul__(self, other):
        # for * operator
        return number(str(int(self.b10) * int(other.b10)))

    # add a divide methods
    def __truediv__(self, other):
        # for / operator
        # NOTE: This will function as floordiv as floats don't
        # make sense for non-base 10 numbers

        # error handling for divide by zero
        if other.b10 == str(0):
            print('Divide by 0 error')
            print('Returning 0 for all values')
            return number('0')

        # If no error return answer
        else:
            return number(str(int(self.b10) // int(other.b10)))

    def all(self):
        # Print all conversion outputs
        print('Binary: ', self.b2)
        print('Octal: ', self.b8)
        print('Decimal: ', self.b10)
        print('Hexadecimal: ', self.b16)
        print()

        return None


# Main Menu Function
def menu():
    # Initialize number classes
    num1 = number()
    num2 = number()
    msg('i', 'Number objects created sucessfully!')

    # Setup Loop ending logic
    again = True

    while again:
        # print menu options
        print('What would you like to do?')
        print('1. Add two Numbers')
        print('2. Subtract a number')
        print('3. Multiply Numbers')
        print('4. Divide Numbers')
        print('5. Reset current stored numbers')
        print('6. Print current numbers')
        print('7. Exit Program')
        print('\n\nPlease enter an option\n')

        # accept user input based on above options
        usrin = input('Selection: ')
        print()
        
        if usrin == '1':
            msg('i', 'Numbers added!')

            # Add number 1 and number 2 together and 
            # return new resultant class object for output
            out = num1 + num2

            print('Numbers added. Results:')

            # Use built in class method to print all results
            out.all()

            # add pause so user can review output
            input('Press Enter to Continue\n')

        elif usrin == '2':
            msg('i', 'Numbers subtracted!')

            # subtract number 2 from number 1 together and 
            # return new resultant class object for output
            out = num1 - num2

            print('Number 2 subtrcted from number 1 . Results:')

            # Use built in class method to print all results
            out.all()

            # add pause so user can review output
            input('Press Enter to Continue\n')

        elif usrin == '3':
            msg('i', 'Numbers multiplied!')

            # Multiply number 1 and number 2 together and 
            # return new resultant class object for output
            out = num1 * num2

            print('Numbers multiplied together. Results:')

            # Use built in class method to print all results
            out.all()

            # add pause so user can review output
            input('Press Enter to Continue\n')

        elif usrin == '4':
            msg('i', 'Numbers divided!')
            out = num1 / num2

            print('Number 1 divided by number 2. Results:')

            # Use built in class method to print all results
            out.all()

            # add pause so user can review output
            input('Press Enter to Continue\n')

        elif usrin == '5':
            msg('i', 'Numbers reset!')

            # Request new numbers and bases frim the user for future processing
            fbase = input('What is the base of the first number? ')
            fnum = input('What is the first number? ')

            sbase = input('What is the base of the second number? ')
            snum = input('What is the second number? ')

            # Build new number objects based on user input
            num1 = number(fnum, fbase)
            num2 = number(snum, sbase)

        elif usrin == '6':
            msg('i', 'Numbers printed!')

            # Print first number set
            print('Number 1:')
            num1.all()

            print()

            # Print second number set
            print('Number 2: ')
            num2.all()

            input('Press Enter to Continue')
            print()

        elif usrin == '7':
            msg('i', 'User requested program end.')
            print('\nexiting now\n')
            again = False

        else:
            # capture any unexpected input and print error message
            
            # Use -> in log message so that a ':' does not interfer with
            # ':' log delimiters already in place
            msg('w', f'Invalid menu option entered by user -> {usrin}')
            print('\n\n***ERROR***\n')
            print('Invalid option!')
            print('Please enter a number option (1-7)')
            print(f'You entered: {usrin}\n')


    return None

# add if name == main and any other driver code
if __name__ == '__main__':

    # Initialize program if run natively
    menu()
