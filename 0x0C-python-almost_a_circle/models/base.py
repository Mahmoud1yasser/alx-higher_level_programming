#!/usr/bin/python3
# base.py
'''class to mange id attribute to avoid dublicating'''


import json


class Base:
    ''' Base class for all other classes in project'''
    __nb_objects = 0

    def __init__(self, id=None):
        ''' initiate class'''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        '''Dictionary to JSON string
        Returns: the JSON string
        representation of list_dictionaries
        '''
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        '''Method that writes JSON string representation to file'''
        if list_objs is None:
            list_objs = []
        list_dictionaries = [obj.to_dictionary() for obj in list_objs]
        json_string = cls.to_json_string(list_dictionaries)
        filename = "{}.json".format(cls.__name__)
        with open(filename, 'w') as json_file:
            json_file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        '''JSON string to dictionary
        Returns: list of the JSON string representation
        '''
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        '''
        Dictionary to Instance
        Returns: an instance with all attributes already set
        '''
        if cls.__name__ == 'Rectangle':
            dummy = cls(1, 1)
        elif cls.__name__ == 'Square':
            dummy = cls(1)
        else:
            return None
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        '''File to instances
        Returns: list of instances
                 If the file doesn’t exist, return an empty list
        '''
        new_list = []
        try:
            filename = "{}.json".format(cls.__name__)
            with open(filename, 'r') as json_string:
                new = cls.from_json_string(json_string.read())
        except IOError:
            return []
        for i in new:
            new_list.append(cls.create(**i))
        return new_list
