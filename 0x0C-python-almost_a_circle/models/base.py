#!/usr/bin/python3
"""
This module contains the "Base" class.
"""


import json


class Base:
    """ Base class with private attributes. """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Initializes the  """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):  # Task 15
        """ Method that return a JSon string. """
        if list_dictionaries and len(list_dictionaries) > 0:
            return json.dumps(list_dictionaries)
        return "[]"

    @classmethod
    def save_to_file(cls, list_objs):
        """ . """
        with open(cls.__name__ + ".json", "w") as fil:
            if list_objs is None or list_objs == []:
                fil.write([])
            else:
                dic_list = []
                for objs in list_objs:
                    dic_list += [objs.to_dictionary()]
                dic = Base.to_json_string(dic_list)
                return fil.write(dic)

    def from_json_string(json_string):
        """ Method that returns the list of JSon string representation. """
        if json_string is None or json_string == "":
            return []
        else:
            return json.loads(json_string)

    def create(cls, **dictionary):
        """ Returns an instance with all attributes already set. """
        if cls.__name__ is "Rectangle":
            dummy = cls(2, 4, 2, 3, 39)
        elif cls.__name__ is "Square":
            dummy = cls(2, 5, 8, 35)
        dummy.update(**dictionary)
        return dummy
