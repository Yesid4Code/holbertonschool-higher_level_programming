#!/usr/bin/python3
"""
Class Square which inherits from base.
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """ A representation of a Square. """
    def __init__(self, size, x=0, y=0, id=None):
        """ Initializes the Square. """
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """ Informal string representation of the Square. """
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(self.id,
                                                         self.x,
                                                         self.y,
                                                         self.size)

    @property
    def size(self):
        """ Getter for size. """
        return self.width

    @size.setter
    def size(self, base):
        """ Setter for size. """
        self.width = base
        self.height = base

    def update(self, *args, **kwargs):
        """ Updates multiple attributes. """
        if args:
            atribute = ["id", "size", "x", "y"]
            for idx, value in enumerate(args):
                if idx < 5:
                    setattr(self, atribute[idx], value)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)


# Tests comands
# python3 -m unittest discover tests
# python3 -m unittest tests/test_models/test_base.py
