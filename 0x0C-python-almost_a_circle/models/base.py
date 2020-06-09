#!/usr/bin/python3
"""
This module contains the "Base" class.
"""


import json
import csv


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
        """
        Method that return a JSon string representation of
        List_dictionaries.
        """
        if list_dictionaries and len(list_dictionaries) > 0:
            return json.dumps(list_dictionaries)
        return "[]"

    @classmethod
    def save_to_file(cls, list_objs):
        """ Method that save a JSon string representation on a file. """
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

    @classmethod
    def create(cls, **dictionary):
        """ Returns an instance with all attributes already set. """
        if cls.__name__ is "Rectangle":
            dummy = cls(2, 4)
        elif cls.__name__ is "Square":
            dummy = cls(2)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """ Method to return a list of instances. """
        listt = []
        try:
            with open("{}.json".format(cls.__name__)) as fil:
                dic = cls.from_json_string(fil.read())
                for item in dic:
                    listt.append(cls.create(**item))
                return listt
        except:
            return listt

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ Serializes in CSV a list of Rectangles/Squares in Python. """
        with open(cls.__name__ + ".csv", "w", newline="") as fil:
            if list_objs is None or list_objs is []:
                fil.write("[]")
            else:
                if cls.__name__ is "Rectangle":
                    key = ["id", "width", "height", "x", "y"]
                if cls.__name__ is "Square":
                    key = ["id", "size", "x", "y"]
                dic = csv.DictWriter(fil, fieldnames=key)
                list_csv = []
                for inst in list_objs:
                    list_csv += [dic.writerow(inst.to_dictionary())]

    @classmethod
    def load_from_file_csv(cls):
        """ Deserializes in Python a lsit of Rectangles/Squares in CSV. """
        try:
            with open("{}.csv".format(cls.__name__), "r", newline="") as fil:
                if cls.__name__ is "Square":
                    key = ["id", "size", "x", "y"]
                else:
                    key = ["id", "width", "height", "x", "y"]
                doc = csv.DictReader(fil, fieldnames=key)
                doc_csv = [{key: int(value)
                            for key, value in dic.items()}
                           for dic in doc]
                return [cls.create(**dicts) for dicts in doc_csv]
        except IOError:
            return []
