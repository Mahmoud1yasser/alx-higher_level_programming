#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list is None:
        return
    list.reverse(my_list)
    for i in range(0, len(my_list)):
        print("{:d}".format(my_list[i]))
