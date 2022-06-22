#!/usr/bin/python3
"""Class Square with size attribute"""


class Square:
    '''Square class definition'''

    def __init__(self, size=0):
        """Initializes instance variables"""
        if type(size) is int:
            if size < 0:
                raise ValueError("size must be >= 0")
            self.__size = size
        else:
            raise TypeError("size must be an integer")

    def area(self):
        return self.__size**2
