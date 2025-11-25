#!/usr/bin/python3

for index, i in enumerate(range(122, 96, -1)):
    if index % 2 == 0:
        print(chr(i), end="")
    else:
        print(chr(i - 32), end="")
