#!/usr/bin/python3
""" Create onject from JSon file. """


import json


def load_from_json_file(filename):
    """ Function that creates an object with json. """
    with open(filename, encoding="UTF-8") as load_f:
        return json.load(load_f)
