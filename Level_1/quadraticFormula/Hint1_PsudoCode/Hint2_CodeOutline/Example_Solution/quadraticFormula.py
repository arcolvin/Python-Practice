#!/usr/bin/python3
#Author: Adam
#Date: March 26, 2022
#Version: 1.0


'''
Create a program capable of discerning the results of the quadratic formula for a user given a, b, and c.

Input:
User will provide an A, B and C value.

Output:
The program will return the possible solutions to the formula

Ex. 
Provide an A: 2
Provide a B: 4
Provide a C: -6

Solutions are: 1,-3
'''
import math

# Collect a, b, and c from the user
a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

# if a is 0 print "No Solution" and end program
if a == 0:
    print("No Solution Possible")
    exit()

# Solve for the discriminant
    # If 4*a*c is greater than b*b print "No Solution" and exit
    # otherwise finish solution
if (4 * a * c) > (b * b):
    print("No Solution Possible")
    exit()

else:
    disc = math.sqrt((b * b) - (4 * a * c))

# Save solution 1 with + solution
x1 = (-b + disc) / (2 * a)

# Save solution 2 with - solution
x2 = (-b - disc) / (2 * a)

# compare solution 1 and 2
# If solution 1 is equal to solution 2 print only one answer
if x1 == x2:
    print("Only 1 solution x =", x1)
# else print both solutions
else:
    print("Your solutions are:")
    print("x1 =", x1)
    print("x2 =", x2)
