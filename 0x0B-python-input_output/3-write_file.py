#!/usr/bin/python3
""" Write to a file """


def write_file(filename="", text=""):
    """
    Description: Function that writes a string to a text file.
    Args:
        filename: file to write.
        text: text to add to the filename.
    """
    with open(filename, 'w', encoding='utf=8') as my_file:
        return my_file.write(text)
