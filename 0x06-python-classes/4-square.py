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

    @property
    def size(self):
        '''Defines the size of square and returns its value

        Returns: attribute value

        '''
        return self.__size

    @size.setter
    def size(self, value):
        """sets the size to a certain value.

        Args:
            self: fixed argument
            value: size ti be setted

        """
        self.__size = value
        elf.__size = value
        if type(value) is not int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')

    def area(self):
        '''Defines the area of a square.

        Returns: area of square
        '''
        return self.__size * self.__size
