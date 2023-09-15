#!/usr/bin/python3
# Author: Muiz Olaore

def square_matrix_simple(matrix=[]):
    new_matrix = []
    for row in matrix:
        a = []
        for col in row:
            a.append(col ** 2)
        new_matrix.append(a)
    return new_matrix
