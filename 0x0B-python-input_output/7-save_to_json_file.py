#!/usr/bin/python3
""" Save Object to file. """


import json


def save_to_json_file(my_obj, filename):
    """
    Description: Create a file with JSon.
    Args:
        my_object: text to added to filename.
        filename: file to create.
    """
    with open(filename, 'w', encoding="UTF-8") as filej:
        json.dump(my_obj, filej)
