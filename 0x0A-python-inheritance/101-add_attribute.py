#!/usr/bin/python3
"""
    Module used to add attribute to an object if it's possible.
"""


def add_attribute(obj, key, value):
    """ Add object """
    if hasattr(obj, key) or not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, key, value)
