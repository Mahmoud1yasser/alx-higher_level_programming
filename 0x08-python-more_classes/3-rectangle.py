#!/usr/bin/python3

'''0-rectangle: Python Funtion that defines an empty class'''


class Rectangle:

    '''create empty rectangle'''

    def __init__(self, width=0, height=0):
        '''create instance of object'''

        self.width = width
        self.height = height

    def __str__(self):
        if self.height == 0 or self.width == 0:
            return ""
        else:
            for i in range(self.height):
                for w in range(self.height - 1):
                    print('#' * self.__width)
                return '#' * self.width

    @property
    def width(self):
        '''Returns: width'''

        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = value

    @property
    def height(self):
        '''Returns: height'''

        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = value

    def area(self):
        '''Returns: Area of rectangle'''

        return self.height * self.width

    def perimeter(self):
        '''calculates the perimeter
        Returns:
            primeter for the rectangle
        '''
        if self.height == 0 or self.width == 0:
            return 0
        else:
            perimeter = 2 * (self.width + self.height)
            return perimeter
