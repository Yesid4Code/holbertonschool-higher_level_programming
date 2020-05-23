#!/usr/bin/python3
'''
    d
'''


def text_indentation(text):
    '''
        This function automatically ident text
        Args:
            param1: text to ident.
        Return:
            Nothin.
        Raises:
            TypeError: if text is not a string.
    '''
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    special_ch = [':', '.', '?']
    flag = True

    for c in text:
        if c == " " and flag is True:
            continue
        if c in special_ch:
            print(c, end="")
            print("\n")
            flag = True
        else:
            print(c, end="")
            flag = False
