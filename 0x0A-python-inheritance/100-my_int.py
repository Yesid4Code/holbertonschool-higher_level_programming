#!/usr/bin/python3
""" My integer. """


class MyInt(int):
    """ Class that inherits from int class. """
    def __ne__(self, other):
        return super().__eq__(other)

    def __eq__(self, other):
        return super().__ne__(other)
