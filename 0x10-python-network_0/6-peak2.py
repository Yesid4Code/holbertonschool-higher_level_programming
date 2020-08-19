#!/usr/bin/python3
""" . """


def find_peak(list_of_integers):
    """ . """
    listt = list_of_integers.copy()
    for idx in range(len(listt)):
        if (idx - 1) >= 0 and (idx + 1) <= (len(listt) - 1):
            if listt[idx] >= listt[idx - 1] and listt[idx] >= listt[idx + 1]:
                return listt[idx]
        if (idx - 1) < 0:
            if listt[idx] >= listt[idx + 1]:
                return listt[idx]
        if (idx + 1) > (len(listt) - 1):
            if listt[idx] >= listt[idx - 1]:
                return listt[idx]

    return None

7
length = 7
pivot = 3 -- numero 7
--> pivot - 1 = 2 -- numero 6
--> pivot + 1 = 4 -- numero 8

2, 5, 6
length = 3
pivot = 1 -- numeor 5
--> pivot - 1 = 0 -- numeor 2
--> pivot + 1 = 2 -- numero 6

2
length = 1
pivot = 0 -- 2
--> pivot - 1 = NON




2, 5, 6, 7, 8, 2 

