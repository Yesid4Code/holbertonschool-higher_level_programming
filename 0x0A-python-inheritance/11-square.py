#!/usr/bin/python3
""" Square """


Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """ Class Square with inheritance from Rectangle. """
    def __init__(self, size):
        """ Initialize size"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """ Return the area. """
        return self.__size ** 2

    def __str__(self):
        """ return str. """
        return "[Square] {:d}/{:d}".format(self.__width, self.__height)
