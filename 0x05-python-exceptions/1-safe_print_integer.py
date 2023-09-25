#!/usr/bin/python3
def safe_print_integer(value):
    try:
        print("{:d}".format(value), end = "")
        print()
    except TypeError:
        print("{}".format(value), end = "")
        return (False)
    return (True)
