#!/usr/bin/python3
"""
Integer validator
Rectangle
"""


class BaseGeometry:
    """ Class BaseGeometry used to print raise errors. """
    def area(self):
        """ raise an Exception """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Method used to validate "Value"
        Args:
            name:
            vale:
        Raises:
            TypeError: if value is not an int
            ValueError:if value is less or equal to 0
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

# BaseGeometry = __import__("7-base_geometry").BaseGeometry if the class is in other file

class Rectangle(BaseGeometry):
    """ Class Rectangle with BaseGeometry as baseclass """
    def __init__(self, width, height):
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
