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

    def save_to_file_csv(cls, list_objs):
        """ Serializes in CSV a list of Rectangles/Squares in Python. """
        with open(cls.__name__ + ".csv", "w") as fil:
            fil_csv = csv.writer(fil)
            if cls.__name__ is "Rectangle":
                for obj in list_objs:
                    fil_csv.writerow([obj.id,
                                      obj.width, obj.height,
                                      obj.x, obj.y])
            elif cls.__name__ is "Square":
                for obj in list_objs:
                    fil_csv.writerow([obj.id, obj.size, obj.x, obj.y])
            fil_csv.writerows(list_objs)

    def load_from_file_cvs(cls):
        """ Deserializes in Python a lsit of Rectangles/Squares in CSV. """
        with
