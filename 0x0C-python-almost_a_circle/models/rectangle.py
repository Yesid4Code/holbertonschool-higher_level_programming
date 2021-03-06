#!/usr/bin/python3
"""
Class Rectangle which inherits from base.
"""


from models.base import Base


class Rectangle(Base):
    """ A representation of a Rectangle. """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initializes the rectangle. """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ Getter for width. """
        return self.__width

    @width.setter
    def width(self, width):
        """ Setter of width. """
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """ Getter of height. """
        return self.__height

    @height.setter
    def height(self, height):
        """ Setter of height. """
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """ Getter of x. """
        return self.__x

    @x.setter
    def x(self, x):
        """ Setter of x. """
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """ Getter of y. """
        return self.__y

    @y.setter
    def y(self, y):
        """ Setter of y. """
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """ Calculates the area of the rectangle. """
        return self.__width * self.__height

    def display(self):
        """ Print a display of the rectangle. """
        for y in range(self.__y):
            print()
        for i in range(self.__height):
            print(" " * (self.__x) + "#" * self.__width)

    def __str__(self):
        """ Informal string representation of the rectangle. """
        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(self.id,
                                                                 self.__x,
                                                                 self.__y,
                                                                 self.__width,
                                                                 self.__height)

    def update(self, *args, **kwargs):
        """ Updates multiple attributes. """
        if args:
            atribute = ["id", "width", "height", "x", "y"]
            for idx, value in enumerate(args):
                if idx < 5:
                    setattr(self, atribute[idx], value)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):  # Task 13.
        """ Dictionary representation of a Rectangle """
        dic = ["id", "height", "width", "x", "y"]
        return {key: getattr(self, key) for key in dic}
