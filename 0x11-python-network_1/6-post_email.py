#!/usr/bin/python3
"""
    Script that send a POST request to the passed URL
    Return the body of the response.
"""
from requests import post
from sys import argv


body = post(argv[1], data={"email": argv[2]})
print(body.text)
