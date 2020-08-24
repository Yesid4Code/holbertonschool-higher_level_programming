#!/usr/bin/python3
""" print the id of the request"""
from urllib.request import urlopen
from sys import argv


if __name__ == "__main__":
    with urlopen(argv[1]) as rid:  #response ID
        print(rid.headers.get("X-Request-Id"))
