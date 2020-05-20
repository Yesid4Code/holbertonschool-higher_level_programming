#!/usr/bin/python3
""" A Square class definition """


class Square:
        """ Initialization of the class """
        def __init__(self, size=0, position=(0, 0)):
                """ Initialization of the class """
                self.__size = size
                if position[0] < 0 or position[1] < 0:
                        raise TypeError("position must be\
                        a tuple of 2 positive integers")
                self.__position = position

        def area(self):
                """ Calculate the square's area """
                return self.__size ** 2

        @property
        def size(self):
                """ The size of the square """
                return self.__size

        @size.setter
        def size(self, values):
                """ Set the size of the square and check if it's >= 0  """
                if type(values) is not int:
                        raise TypeError("size must be an integer")
                if values < 0:
                        raise ValueError("size must be >= 0")
                self.__size = values

        @property
        def position(self):
                """ The position of the Square """
                return self.__position

        @position.setter
        def position(self, valuep):
                """ Set the position to print """
                if type(valuep) is not tuple or len(valuep) != 2 or \
                   type(valuep[0]) is not int or valuep[0] < 0 or\
                   type(valuep[1]) is not int or valuep[1] < 0:
                        raise TypeError("position must be\
                        a tuple of 2 positive integers")
                self.__position = valuep

        def my_print(self):
                """ prints in stdout the square with the character # """
                if self.__size > 0:
                        print("\n" * self.__position[1], end="")
                        for i in range(self.__size):
                                print(" " * self.__position[0], end="")
                                print("#" * self.__size)
                else:
                        print()
