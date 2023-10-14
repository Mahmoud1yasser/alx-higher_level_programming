#!/usr/bin/python3
# base.py
'''class to mange id attribute to avoid dublicating'''


class Base:
    ''' Base class for all other classes in project'''
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            Base.id = id
        else:
            __nb_objects += 1
            id = __nb_objects
