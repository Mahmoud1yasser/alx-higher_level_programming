#!/usr/bin/python3
def check_list_types(lst):
    """
    function check the type of each item to be int or float.

    Args:
        lst: list under test

    Returns: true if all items are int/float.
    """
    for row in lst:
        for item in row:
            if not isinstance(item, (int, float)):
                return False
    return True


def check_row_sizes(lst):
    """function checks row sizes to be equal

    Args:
        lst: matrix under test

    Returns: true if all rows are equal
    """
    row_size = len(lst[0])
    for row in lst:
        if len(row) != row_size:
            return False
    return True


def matrix_divided(matrix, div):
    """function that divides all elements of a matrix

    Args:
        matrix: lists to be divided
        div: number to divid with

    Returns: new matrix for the calculation.
    """
    result = []
    listError = 'matrix must be a matrix (list of lists) of integers/floats'
    # Check if matrix is a list
    if type(matrix) is not list:
        raise TypeError(listError)

    # Check if rows in matrix is list
    for rows in matrix:
        if type(rows) is not list:
            raise TypeError(listError)
    if type(div) is int or type(div) is float:
        if div == 0:
            raise ZeroDivisionError('division by zero')
        else:
            if check_row_sizes(matrix):
                if check_list_types(matrix):
                    for sub_list in matrix:
                        divided_list = [round((element / div), 2) for element in sub_list]
                        result.append(divided_list)
                    return result
                else:
                    raise TypeError(ListError)
            else:
                raise TypeError('Each row of the matrix must have the same size')
    else:
        raise TypeError('div must be a number')
