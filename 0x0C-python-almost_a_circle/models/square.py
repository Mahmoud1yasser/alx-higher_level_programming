#!/usr/bin/python3
# square.py
'''class Square that inherits from Rectangle'''


from models.rectangle import Rectangle


class Square(Rectangle):
    '''Square is a special Rectangle,
    so it makes sense that Square inherits from Rectangle'''
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        '''Update the class Rectangle by overriding the __str__ method'''
        return "[Square] ({}) {}/{} - {}".format(
                    self.id, self.x, self.y, self.width)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value

    def update(self, *args, **kwargs):
        '''assigns an argument to each attribute'''
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
                self.height = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        elif kwargs:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def to_dictionary(self):
        '''Square instance to dictionary representation
        Returns: dictionary representation of a Square
        '''
        dictio = {'id': self.id, 'size': self.width, 'x': self.x, 'y': self.y}
        return dictio
