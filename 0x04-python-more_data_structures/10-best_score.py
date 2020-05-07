#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        i = 0
        for key, value in a_dictionary.items():
            if i < value:
                i = value
                j = key
        return j
    return None

# return (max(a_dictionary, key=a_dictionary.get) if a_dictionary else None)

#  2 def best_score(a_dictionary):
#  3     if a_dictionary:
#  4         for key, value in a_dictionary.items():
#  5             i = max(a_dictionary.values())
#  6             if value == i:
#  7                 return key
#  8     return None
