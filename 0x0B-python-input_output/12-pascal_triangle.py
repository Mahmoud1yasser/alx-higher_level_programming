#!/usr/bin/python3
"""
14-main - Pascals Triangle
"""


def pascal_triangle(n):
    if n <= 0:
        return []

    my_list_tri = []
    for count in range(1, n):
        row = [1]
        if my_list_tri:
            last_row = my_list_tri[-1]
            for j in range(len(last_row) - 1):
                row.append(last_row[j] + last_row[j + 1])
        row.append(1)
        my_list_tri.append(row)
    return my_list_tri
