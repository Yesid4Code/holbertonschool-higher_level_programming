#!/usr/bin/python3
def fuzzbuzz():
    for x in range(1, 101):
        out = ""
        if (x % 3) == 0:
            out += "Fizz"
        if (x % 5) == 0:
            out += "Buzz"
        if out == "":
            out = x
        print(out, end=" ")
