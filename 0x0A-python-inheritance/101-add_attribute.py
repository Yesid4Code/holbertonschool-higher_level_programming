#!/usr/bin/python3
"""
    Module used to add attribute to an object if it's possible.
"""


def add_attribute(obj, key, value):
    # if not hasattr(obj, "__slots__") and not hasattr(obj, "__dic__"):
    #    raise TypeError("can't add new attribute")
    # if hasattr(obj, "__slots__") and not hasattr(abj, key):
    #    raise TypeError("can't add new attribute")

    if obj.__class__.__module__ == 'builtins':
        raise TypeError("can't add new attribute")
    elif hasattr(obj, "__slots__") and key not in obj.__slots__:
        raise TypeError("can't add new attribute")
    setattr(obj, key, value)
