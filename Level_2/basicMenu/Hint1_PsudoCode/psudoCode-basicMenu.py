#!/usr/bin/python3
#Author: Adam
#Date: Jan 5, 2022
#Version: 1.0


'''
This program should create a basic menu experience for the user
The menu should loop until the user selects a quit or exit option
Give the user 2-3 menu options to select from.
Since there is no main program each menu option should simply print
a unique string for that menu selection.

The program should also react accordingly if an invalid menu option
is provided. i.e. the options are 1, 2, or 3 and the user enters
'potato' as their menu choice. The program should return some kind
of error message indicating that that was not a valid selection.

Once the user selects the exit menu item it should gracefully
end the loop and stop the program.

Input:
The user should enter menu options such as 1, 2, or 3 via an input
function. Alternatively the program could accept letters relevent
to the menu option such as 'q' for quit or 'p' for print.

Output:
The program will print different strings based on the program menu flow

Ex. 

What would you like to do?
A - Option 1
B - Option 2
C - Option 3
Q - quit
Make a selection - (A,B,C, or Q): a
Option 1 has run!
'''

# Add variable to track our menu exit condition
# Initialize the menu loop to continue the program until user select's quit
    # Print all menu options
    # Request and store user input with input function
    # Check user selection with if else and do somethign based on that selection
    # When user wants to exit change exit condition to false to end loop
    # enter error message if user enters an unexpected value
