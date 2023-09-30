#!/usr/bin/python3
def say_my_name(first_name, last_name=""):
    """ prints the name in order

    Args:
        first_name: name
        last_name: last
    """
    if first_name is None:
        raise TypeError('first_name must be a string')
    if last_name is None:
        raise TypeError('last_name must be a string')
    if type(first_name) is str:
        if type(last_name) is str:
            print("My name is {} {}".format(first_name, last_name))
        else:
            raise TypeError('last_name must be a string')
    else:
        raise TypeError('first_name must be a string')
