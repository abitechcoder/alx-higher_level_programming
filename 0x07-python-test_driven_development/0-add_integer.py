#!/usr/bin/python3
"""
This is "0-add_integer" module

The 0-add_integer module supplies one function, add_integer().
For example,
>>> add_integer(1, 2)
3
"""
def add_integer(a, b=98):
    """
    Retun the addition of a and b.
    a and b must be integers or floats.
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    if type(a) is float or type(b) is float:
        a = int(a)
        b = int(b)
    return a + b
