#!/usr/bin/python3
def best_score(a_dictionary):
    a = 0
    for x in a_dictionary:
        if a < a_dictionary[x]:
            a = a_dictionary[x]
    return a
