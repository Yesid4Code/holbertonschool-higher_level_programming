#!/usr/bin/python3
""" . """


def find_peak(list_of_integers):
    """ . """
    listt = list_of_integers
    length = len(listt)
    if length == 0:
        return None
    pivot = length // 2
    # 4, 2, 1, [ 2 ],       -- 3 --    , 1
    if (pivot == 0 or listt[pivot] >= listt[pivot - 1]) and\
       (pivot == length - 1 or listt[pivot] >= listt[pivot + 1]):
        return listt[pivot]  # pivot = peak
    if pivot != length -1 and listt[pivot + 1] > listt[pivot]:
        return find_peak(listt[pivot + 1:])
    return find_peak(listt[:pivot])
