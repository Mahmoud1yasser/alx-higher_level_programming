#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if len(matrix) == 1 and any(matrix) is False:
        print('')
    else:
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if j == len(matrix[i]) - 1:
                    print("{:d}".format(matrix[i][j]), end = '\n')
                else:
                    print("{:d}".format(matrix[i][j]), end = ' ')
