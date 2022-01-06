#!/usr/bin/env python3
#Author: Adam Colvin
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
'''

# Required import for command line arguments
# Alphabet for encoding / decoding
alph="abcdefghijklmnopqrstuvwxyz ."

# move command line argument to a variable for readability
# initialize output string
# loop for string processing
    # rot 14 index math
    # 'append' encoded / decoded character to output string
# print final output string
