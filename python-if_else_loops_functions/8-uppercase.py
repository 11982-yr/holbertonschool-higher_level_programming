#!/usr/bin/python3

def uppercase(str):
    for c in str:
        asc = ord(c)
        if 97 <= asc <= 122:
            asc -= 32
        print("{}".format(chr(asc)), end="")
    print("")
