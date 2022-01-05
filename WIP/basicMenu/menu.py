#!/usr/bin/env python3

again = True

while again == True:
    print('What would you like to do?')
    print('A - Option 1')
    print('B - Option 2')
    print('C - Option 3')
    print('Q - quit')

    selection = input('Make a selection - (A,B,C, or Q): ').lower()
    num = int(input('What number do you want to convert? '))

    if selection == 'a':
        print('Option 1 has run!')
        print(f'The user entered {num}')

    elif selection == 'b':
        print('Option 2 has run!')
        print(f'The user entered {num}')

    elif selection == 'c':
        print('Option 3 has run!')
        print(f'The user entered {num}')

    elif selection == 'q':
        print('ENDING PROGRAM!')
        print(f'The user entered {num}')
        again = False

    else:
        print('Invalid Selection! Please Try Again!')
