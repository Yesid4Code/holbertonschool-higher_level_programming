#!/usr/bin/python3
'''
    2-matrix_divided.py
    Contains function that divides all elements of a matrix
'''


def matrix_divided(matrix, div):
    '''
        Function that divides all elements in the matrix by div.
        Return a matrix with the new value
    '''
    tyerror = "matrix must be a matrix (list of list) of integers/floats"
    sizeerror = "Each row of the matrix must have the same size"

    if type(div) in [int, float]:
        if div != 0:
            if isinstance(matrix, list) and matrix:
                new_matrix = matrix.copy()
                first_el = len(new_matrix[0])
                for row in new_matrix:
                    if isinstance(row, list) and row:
                        if first_el == len(row):
                            for col in row:
                                if type(col) in [int, float]:
                                    pass  # here you can replace return process
                                else:
                                    raise TypeError(tyerror)
                        else:
                            raise TypeError(sizeerror)
                    else:
                        raise TypeError(tyerror)
                return([[round(i/div, 2) for i in row] for row in new_matrix[:]])
            else:
                raise TypeError(tyerror)
        else:
            raise ZeroDivisionError("division by zero")
    else:
        raise TypeError("div must be a number")
