#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrix_2 = list(map(lambda row:list(map(lambda x:(x * x), row)), matrix))
    return (matrix_2)

