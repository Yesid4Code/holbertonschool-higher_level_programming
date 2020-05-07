#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
        for idx, item enumerate(a_dictionary):
            if key in a_dictionary:
                a_dictionary[key] = value
            a_dictionary[key] = value # Key always change, jus this line
        return a_dictionary
