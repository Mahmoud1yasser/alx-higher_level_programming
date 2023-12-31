#!/usr/bin/python3
# 10-student.py
'''Student to JSON '''


class Student:
    '''defines a student by first_name, last_name,age'''
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return self.__dict__

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__
        my_dict = {}
        for items in attrs:
            if hasattr(self, items):
                my_dict[items] = getattr(self, items)
        return my_dict
