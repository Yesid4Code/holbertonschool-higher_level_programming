#!/usr/bin/python3
"""
    Script that takes the Github credentials (username and password)
    Return the id using the Github API
"""
import requests
from sys import argv


if __name__ == "__main__":
    req = requests.get("https://api.github.com/user", auth=(argv[1], argv[2])
    req_dic = req.json()  # decode
    print(name.get("id"))
