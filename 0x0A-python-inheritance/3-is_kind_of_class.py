#!/usr/bin/pyton3
""" Function to check if an object is an instance  """


def is_kind_of_class(obj, a_class):
    """
    Args:
        obj: object to verify.
        a_class: class to verify.
    Return:
        True: if the object is an instance of a class.
        Fasle: otherwise.
    """
    #return isinstance(obj, a_class) an easy option.
    if isinstance(obj, a_class):
        return True
    else:
        return False
