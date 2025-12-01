#!/usr/bin/python3


def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    roman_dict = {"I": 1, 
                  "V": 5, 
                  "X": 10, 
                  "L": 50, 
                  "C": 100, 
                  "D": 500, 
                  "M": 1000}

    num = 0
    length = len(roman_string)

    for i in range(length):
        value = roman_dict.get(roman_string[i], 0)
        if value == 0:
            return 0

        if i != length - 1:
            next_value = roman_dict.get(roman_string[i + 1], 0)
            if value < next_value:
                num -= value
            else:
                num += value
        else:
            num += value

    return num
