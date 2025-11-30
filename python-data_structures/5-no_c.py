#!/usr/bin/python3


def no_c(my_string):
    new_string = ""
    for cC in my_string:
        if cC != "c" and cC != "C":
            new_string += cC
    return new_string
