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

num = int(input('What Number to Process?: '))

while num != 1:
    if (num % 2) == 0:
        num = num // 2
        
    else:
        num = (num * 3) + 1
        
    print(num)
    

print('Done!')
