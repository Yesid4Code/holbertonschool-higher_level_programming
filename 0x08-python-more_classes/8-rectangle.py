#!/usr/bin/python3
""" Class Rectangle """


class Rectangle:
    """ Class that defines a rectangle """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """
        Method that defines instances of a new rectangle
        Args:
            width: x number of elements.
            height:y number of elements.
        Raises:
            TypeError: data not an int
            ValueError: data below zero
        """
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

        @property
        def width(self):
            """ Getter for width """
            return self.__width

        @width.setter
        def width(self, width):
            """ Setter for width """
            if type(width) is not int:
                raise TypeError("width must be an integer")
            if width < 0:
                raise ValueError("width must be >= 0")
            self.__width = width

        @property
        def height(self):
            """ Getter for height """
            return self.__height

        @height.setter
        def height(self, height):
            """ Setter for height """
            if type(height) is not int:
                raise TypeError("height must be an integer")
            if height < 0:
                raise ValueError("height must be >= 0")
            self.__height = height

        def area(self):
            """this method calcs the rectangle area"""
            return self.__height * self.__width

        def perimeter(self):
            """this method calcs the rectangle perimeter """
            if (self.__width == 0 or self.__height == 0):
                return 0
            return 2 * self.__height + 2 * self.__width

        def __str__(self):
            """returns a string with the actual rectangle """
            rectan = ""
            if (self.__width == 0 or self.__height == 0):
                return rectan
            for i in range(self.__height):
                for j in range(self.__width):
                    rectan += '#'
                if (i != self.__height - 1):
                    rectan += '\n'
            return rectan

        def __repr__(self):
            """ Retrun a rep with the rectangle info """
            return 'Rectangle(' + str(self.__width) + \
                ', ' + str(self.__height) + ')'

        def __del__(self):
            """ Delete object """
            print("Bye rectangle...")
            Rectangle.number_of_instances -= 1

        @staticmethod
        def bigger_or_equal(rect_1, rect_2):
            """method to decide what rect is bigger """
            if not isinstance(rect_1, Rectangle):
                raise TypeError("rect_1 must be an instance of Rectangle")
            if not isinstance(rect_2, Rectangle):
                raise TypeError("rect_2 must be an instance of Rectangle")
            if rect_1.area() >= rect_2.area():
                return rect_1
            return rect_2
