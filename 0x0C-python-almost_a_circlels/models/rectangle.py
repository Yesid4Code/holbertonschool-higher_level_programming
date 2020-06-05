#!/usr/bin/python3
"""
Contains the "Rectangle" class
"""


from models.base import Base


class Rectangle(Base):
    """ A representation of a Rectangle. """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initializes the rectangle. """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """ Getter for width. """
        return self.__width

    @width.setter
    def width(self, width):
        """ Setter of width. """
        self.__width = width

    @property
    def height(self):
        """ Getter of height. """
        return self.__height

    @height.setter
    def height(self, height):
        """ Setter of height. """
        self.__height = height

    @property
    def x(self):
        """ Getter of x. """
        return self.__x

    @x.setter
    def x(self, x):
        """ Setter of x. """
        self.__x = x

    @property
    def y(self):
        """ Getter of y. """
        return self.__y

    @y.setter
    def y(self, y):
        """ Setter of y. """
        self.__y = y
