#!/usr/bin/python3
""" Read n lines. """


def read_lines(filename="", nb_lines=0):
    """
    Function that reads n lines of a text file.
    Args:
        filename: file
        nb_lines: n line to be read
    Retrun:
        line choosed or the file completed
    """
    line = 0
    with open("my_file_0.txt", encoding="utf-8") as my_file:
        n_line = len(x.readlines())
        if nb_lines <= 0 or > n_line:
            print(my_file.read())
        else:
            lists = my_file.readlines()
            print(lists[nb_lines])
