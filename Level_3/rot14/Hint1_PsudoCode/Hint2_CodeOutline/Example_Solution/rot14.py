#!/usr/bin/env python3
#Author: Adam
#Date: December 22,2021
#Version: 1.0

'''
Background:
Rot13 cyphers allow for the same algorithm to both encode and decode
a given plaintext or cyphertext. This makes the program very efficient
but it is not a very strong encryption method. The rot 14 will provide
additional encryptable characters and makefor a slightly easier to read
plain text, but still is not very secure. In addition to this, by
including whitespace in the alphabet, it is potentially very easy to 
lose data as it might not be clear that there is leading or trailing
whitespace in a cypher text that would need to be decoded.

Practice problem:
With all this in mind the goal of this program is to build a rot14 script
that includes the normal a-z alphabet as well as a space " " and
period "." character. The alphabet will be provided, but the rest of the
code will need to be written.

The goal for this is to make this a command line utility so users should be
able to provide a cypher text or plain text direct on the command line
rather than through an input function.

Input:
The user should be able to encode / decodea message using a command
line argument to provide the string for encoding / decoding

Output:
the program should print the encoded / decoded string to the terminal

Ex. 
encode example
$ ./rot14.py test
fsef

decode example
$ ./rot14.py fsef
test

EXTRA:
If one wanted to run this script as a 1 liner in bash:

python3 -c 'alph="abcdefghijklmnopqrstuvwxyz ."; msg="ekefs msddadnmbzsoesmfdkmouow.n"; ct = [alph[(alph.index(x) + 14) % 28] for x in msg]; [print(x,end="") for x in ct]; print("")'

This utilizes list comprehensions and a lightly modified print function.
'''

# Required import for command line arguments
import sys

# Alphabet for encoding / decoding
alph="abcdefghijklmnopqrstuvwxyz ."

# move command line argument to a variable for readability
msg = sys.argv[1]

'''
The following strings can be used as a testing value but encode / decode should
be proccessed via command line arguments as defined above
'''
# Test decode string (Should equal below test decode string after processing)
# msg="ekefs msddadnmbzsoesmfdkmouow.n"

# Test encode string (Should equal above test decode string after processing)
# msg = "system error. please try again."

# initialize output string
out = ''

# loop for string processing
for x in msg:
    # rot 14 index math
    i = (alph.index(x) + 14) % 28

    # 'append' encoded / decoded character to output string
    out += alph[i]
    
# print final output string
print(out)
