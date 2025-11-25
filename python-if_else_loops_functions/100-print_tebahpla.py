#!/usr/bin/python3

for index, i in enumerate(range(122, 96, -1)):
    print("{}".format(chr(i if index % 2 == 0 else i - 32)), end="")
