#!/usr/bin/python3
""" From JSon string to Object. """


import json


def from_json_string(my_obj):
    """
    Funtion that returns an object.
    Arg: my_object: JSon object
    Return: Pthon object as dictionary.
    """
    return json.loads(my_obj)
