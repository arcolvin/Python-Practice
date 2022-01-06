#!/usr/bin/python3
#Author: Adam Colvin
#Date: December 22,2021
#Version: 1.0


'''
The collatz conjecture (AKA Hailstone Numbers)
The basis for this is that a user will provide a number
And that number if even will be divided by two (n / 2), if odd
It will be multiplied by 3 and have 1 added to it (3n + 1)
Then repeat with the given output.
Eventually the number will converge to 1 which is
When the program should stop.

Input:
User provides an integer

Output:
Program will print each number result as it works its way to 1

Ex. What Number to Process?: 6
3
10
5
16
8
4
2
1
Done!
'''

# Ask for user to input a number (Integer)
num = int(input('What Number to Process?: '))

# Setup Loop to process the number
while num != 1:
    # add logic to determine if a number is even or odd
    # perform math based on result of even or odd
    if (num % 2) == 0:
        num = num // 2
        
    else:
        num = (num * 3) + 1
        
    # Print the number at the end of each loop to verify the process is working
    print(num)
    

# Print done statement when program finishes
print('Done!')
