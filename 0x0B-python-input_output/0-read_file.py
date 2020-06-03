#!/usr/bin/python3
""" Read a file """


def read_file(filename=""):
    """
    Function that reads a file and prints to stdout
    Arg: filename
    """
    with open("my_file_0.txt", encoding="utf-8") as my_file:
        print(my_file.read(), end="")
