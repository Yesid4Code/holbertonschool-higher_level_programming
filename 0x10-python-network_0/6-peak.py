#!/usr/bin/python3
""" . """


def find_peak(list_of_integers):
    """ . """
    listt = list_of_integers.copy()
    for idx in range(1, len(listt)):
        if listt[idx] >= listt[idx - 1] and listt[idx] >= listt[idx + 1]:
            return listt[idx]

    return None
