#!/usr/bin/python3
""" Class Mylist  """


class MyList(list):
    """
        Inherits from list.
    """
    def print_sorted(self):
        """ Return a list sorted """
        print(sorted(self))
