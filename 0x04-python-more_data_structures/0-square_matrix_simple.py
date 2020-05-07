#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix:
        listt = []
        for i in matrix:
            listt.append([j ** 2 for j in i])
        return listt
