#!/usr/bin/python3
'''0-square.py: Python script that creates a Square Class'''


class Square:
    '''Creates an empty Square type'''
    def __init__(self, size=None):
        """private attribute that defines the size of square.

        Args:
            self: fixed parameter
            size: entered size of square

        """
        self.__size = size
