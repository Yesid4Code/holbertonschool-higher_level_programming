#!/usr/bin/python3
''' def '''


def add_integer(a, b=98):
    """
    My addition function.
    Args:
        a: first integer.
        b: second integer.
    Return:
        The vlue of "a + b".
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be and integer an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be and integer an integer")
    return (int(a) + int(b))
