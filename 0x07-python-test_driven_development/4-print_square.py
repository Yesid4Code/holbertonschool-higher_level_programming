#!/usr/bin/python3
'''
    Well this file is in charge of printing a simple square
'''


def print_square(size):
    '''
        This function is able to print a square.
        Args:
            param1: size of square.
        Returns:
            Nothing.
        Raises:
            TypeError: if size is not int or negative.
    '''
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    for i in range(0, size):
        print("#" * size)
