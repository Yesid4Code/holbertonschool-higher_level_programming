#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if my_list and idx >= 0 and idx < len(my_list):
        n = my_list[:]
        n[idx] = element
        return (n)
    return (my_list)
