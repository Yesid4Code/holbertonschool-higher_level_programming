#!/usr/bin/python3
"""
    Script that send a POST request to the passed URL
    Return the body of the response.
"""
from urllib.request import urlopen
from urllib.parse import urlencode
from sys import argv


if __name__ == "__main__":
    value = {"email": argv[2]}
    body = urlencode(value)  # convert dictionaries into query strings.
    body = body.encode("utf-8")  # data should be bytes "ascii"
    with urlopen(argv[1], body) as body:  # response ID
        print(body.read().decode("utf-8"))

# encode: when the result contains "str" data ==> "bytes" data
# decode: when the result contains "bytes" data ==> "str" data
