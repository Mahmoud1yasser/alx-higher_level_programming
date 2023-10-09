#!/usr/bin/python3
"""
Write a function that returns True
if the object is an instance of a class that inherited
(directly or indirectly) from the specified class ;
otherwise False.
"""


def inherits_from(obj, a_class):
    """check if object is an instance of a class
    args:
        obj: object to check
        a_class: class to check
    returns:
        True or False
    """

    if type(obj) == a_class:
        return False
    return issubclass(type(obj), a_class)
