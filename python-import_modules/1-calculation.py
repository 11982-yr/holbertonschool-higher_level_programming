#!/usr/bin/python3
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    a = 10
    b = 5

    print("{} + {} = {}".format(add(a, b)))
    print("{} - {} = {}".format(sub(a, b)))
    print("{} * {} = {}".format(mul(a, b)))
    print("{} / {} = {}".format(div(a, b)))
