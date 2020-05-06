#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        leng = 1
        for item in row:
            print("{:d}".format(item), end="")
            if len(row) > leng:
                print(end=" ")
            leng += 1
        print()
