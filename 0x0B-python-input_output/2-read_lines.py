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
    with open(filename, encoding="utf-8") as my_file:
        n_line = len(my_file.readlines())
        n_linee = 0
        if nb_lines <= 0 or nb_lines > n_line:
            my_file.seek(0)
            print(my_file.read(), end="")
        else:
            my_file.seek(0)
            x = my_file.readline()
            while x != '' and n_linee != nb_lines:
                print(x, end="")
                x = my_file.readline()
                n_linee += 1
