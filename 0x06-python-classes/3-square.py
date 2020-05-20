#!/usr/bin/python3
""" A Square class definition """


class Square:
        """ Initialization of the class """
        def __init__(self, size=0):
                """ Initialization of the class """
                if type(size) is not int:
                        raise TypeError("size must be an integer")
                if size < 0:
                        raise ValueError("size must be >= 0")
                self.__size = size

        def area(self):
                """ Calculate the square's area """
                return self.__size ** 2
