#!/usr/bin/python3
# rectangle.py
'''First Rectangle'''


from models.base import Base


class Rectangle(Base):
    '''a class to define a rectangle'''
    def __init__(self, width, height, x=0, y=0, id=None):
        '''initiate new rectangle
        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
            x (int): The x coordinate of the new Rectangle.
            y (int): The y coordinate of the new Rectangle.
            id (int): The identity of the new Rectangle.
        Raises:
            TypeError: If either of width or height is not an int.
            ValueError: If either of width or height <= 0.
            TypeError: If either of x or y is not an int.
            ValueError: If either of x or y < 0.
            '''
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def __str__(self):
        '''Update the class Rectangle by overriding the __str__ method'''
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
                    self.id, self.__x, self.__y, self.__width, self.__height)

    @property
    def width(self):
        """set the property of width"""
        return self.__width

    @width.setter
    def width(self, value):
        '''set the width attribute'''
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """set the property of height"""
        return self.__height

    @height.setter
    def height(self, value):
        '''set the height attribute'''
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """set the property of x"""
        return self.__x

    @x.setter
    def x(self, value):
        '''set the x positional attribute'''
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """set the property of y"""
        return self.__y

    @y.setter
    def y(self, value):
        '''set the y positional attribute'''
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        '''calculates area of rectangle
        Returns: value of area'''
        return self.__width * self.__height

    def display(self):
        '''Display rectangle in shape of # '''
        space = ' '
        character = '#'
        line = character * self.__width
        print('\n' * self.__y, end='')
        print(((space * self.__x) + (line + '\n')) * self.__height, end='')

    def update(self, *args, **kwargs):
        '''assigns an argument to each attribute'''
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
            if len(args) >= 3:
                self.height = args[2]
            if len(args) >= 4:
                self.x = args[3]
            if len(args) >= 5:
                self.y = args[4]
        elif kwargs:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def to_dictionary(self):
        '''Rectangle instance to dictionary representation
        Returns: the dictionary representation of a Rectangle
        '''
        dic = {'id': self.id, 'width': self.width, 'height': self.height,
               'x': self.x, 'y': self.y}
        return dic
