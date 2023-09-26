#!/usr/bin/python3
'''0-square.py: Python script that creates a Square Class'''


class Square:
    '''Creates an empty Square type'''
    def __init__(self, size=0):
        """private attribute that defines the size of square.

        Args:
            self: fixed parameter
            size: entered size of square

        """
        self.__size = size
        if type(size) is not int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
