#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    my_dictionary = a_dictionary.copy()
    for x, y in my_dictionary.items():
        my_dictionary[x] = my_dictionary[y] * 2
    return my_dictionary
