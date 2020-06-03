#!/usr/bin/python3
""" Number of lines. """


def number_of_lines(filename=""):
    """
    Function that return the number of lines of a text file.
    Arg: filename.
    """
    line = 0
    with open("my_file_0.txt", encoding="utf-8") as my_file:
        while my_file.readline() != '':
            line += 1
    return line
