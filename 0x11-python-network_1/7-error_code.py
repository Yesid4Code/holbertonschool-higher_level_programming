#!/usr/bin/python3
"""
    Script that send a POST request to the passed URL
    Return the body of the response. Manage errors.
"""
from requests import get
from sys import argv


if __name__ == "__main__":
    r = get(argv[1])
    if r.status_code >= 400:
        print("Error code: {}".format(r.status_code))
    else:
        print(r.text)
