#!/usr/bin/python3
""" Function to check the class of an instance  """


def is_same_class(obj, a_class):
    """
    Args:
        obj: object to verify.
        a_class: class to verify.
    Return:
        True: if the object is an instance of a class.
        Fasle: otherwise.
    """
    if type(obj) is a_class:
        return True
    else:
        return False
