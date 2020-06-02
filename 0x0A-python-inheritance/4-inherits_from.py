#!/usr/bin/python3
""" Function to check if an object is an instance  """


def inherits_from(obj, a_class):
    """
    Function to check if an object is an instance of a class inherit.
    Args:
        obj: object to verify.
        a_class: class to verify.
    Return:
        True: if the object is an instance of a class.
        Fasle: otherwise.
    """
    # return isinstance(obj, a_class) an easy option.
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    else:
        return False
