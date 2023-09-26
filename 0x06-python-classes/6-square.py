#!/usr/bin/python3
'''0-square.py: Python script that creates a Square Class'''


class Square:
    '''Creates an empty Square type'''
    def __init__(self, size=0, position=(0, 0)):
        """private attribute that defines the size of square.

        Args:
            self: fixed parameter
            size: entered size of square

        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        '''Defines the size of square

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
        if type(value) is not int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')

    def area(self):
        '''Defines the area of a square.

        Returns: area of square
        '''
        return self.__size * self.__size

    def my_print(self):
        '''Prints square by position'''
        if self.position:
            if self.size > 0:
                print('\n' * self.position[1], end="")
                for a in range(self.__size):
                    print(' ' * self.position[0], end="")
                    print('#' * self.size)
        if self.__size == 0:
            print()
    @property
    def position(self):
        """ define position to be retrived

        Returns: object @position
        """
        return self.__position

    @position.setter
    def position(self, value):
        """ settes the poisition to be retrived
        """

        if type(value) is not tuple:
            self.__position = None
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(value) != 2:
            self.__position = None
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[0]) is not int or type(value[1]) is not int:
            self.__position = None
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            self.__position = None
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value
