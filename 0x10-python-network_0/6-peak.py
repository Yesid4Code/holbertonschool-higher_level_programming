#!/usr/bin/python3
""" . """


def find_peak(list_of_integers):
    """ . """
    listt = list_of_integers.copy()
    length = len(list_of_integers)
    if length == 0:
        return
    if length == 1:
        return listt[0]
    pivot = length // 2
    if (pivot == 0 or listt[pivot] > listt[pivot - 1]) and\
       (pivot == length - 1 or listt[pivot] >= listt[pivot + 1]):
        return listt[pivot]  # pivot = peak
    if pivot > 0 and listt[pivot - 1] > listt[pivot]:
        return find_peak(listt[:pivot])
    return find_peak(listt[pivot + 1:])
