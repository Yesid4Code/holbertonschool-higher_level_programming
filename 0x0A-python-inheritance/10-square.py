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
        self.area()
