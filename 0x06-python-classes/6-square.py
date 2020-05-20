#!/usr/bin/python3
""" A Square class definition """


class Square:
        """ Initialization of the class """
        def __init__(self, size=0, position=(0, 0)):
                """ Initialization of the class """
                self.__size = size
                self.__position = position

        def area(self):
                """ Calculate the square's area """
                return self.__size ** 2

        @property
        def size(self):
                """ The size of the square """
                return self.__size

        @size.setter
        def size(self, value):
                """ Set the size of the square and check if it's >= 0  """
                if type(value) is not int:
                        raise TypeError("size must be an integer")
                if value < 0:
                        raise ValueError("size must be >= 0")
                self.__size = value

        @property
        def position(self):
                """ The position of the Square """
                return self.__position

        @position.setter
        def position(self, value):
                """ Set the position to print """
                if type(value) is not tuple or len(value) != 2 or
type(value[0]) is not int or value[0] < 0 or
type(value[1]) is not int or value[1] < 0:
                        raise TypeError("position must be a \
tuple of 2 positive integers")
                else:
                        self.__position = value

        def my_print(self):
                """ prints in stdout the square with the character # """
                if self.__size > 0 and self.__position:
                        print("\n" * self.__position[1], end="")
                        for i in range(self.__size):
                                print(" " * self.__position[0], end="")
                                print("#" * self.__size)
                else:
                        print()
