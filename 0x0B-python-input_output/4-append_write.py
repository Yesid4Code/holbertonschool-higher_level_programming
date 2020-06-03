#!/usr/bin/python3
""" Append to a file. """


def append_write(filename="", text=""):
    """
    Description: Function that appends a string at the end of a text file.
    Args:
        filename: file to write.
        text: text to add at the en of filename.
    """
    with open(filename, 'a', encoding='utf=8') as my_file:
        return my_file.write(text)
