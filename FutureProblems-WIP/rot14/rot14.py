#!/usr/bin/env python3

# If you want to run this script as a 1 liner in bash:
# python3 -c 'alph="abcdefghijklmnopqrstuvwxyz ."; msg="ekefs msddadnmbzsoesmfdkmouow.n"; ct = [alph[(alph.index(x) + 14) % 28] for x in msg]; [print(x,end="") for x in ct]; print("")'


alph="abcdefghijklmnopqrstuvwxyz ."
msg="ekefs msddadnmbzsoesmfdkmouow.n"
ct = [alph[(alph.index(x) + 14) % 28] for x in msg]
[print(x,end="") for x in ct]
 print("")