#!/usr/bin/python3
"""
    Script that send a POST request to the passed URL
    Return the id and the name from a JSON format.
"""
from requests import post
from sys import argv


if __name__ == "__main__":
    try:
        letter = argv[1]
    except Exception:
        letter = ""

    try:
        url = "http://0.0.0.0:5000/search_user"
        req = post(url, data={"q": letter})
        req_dic = req.json()
        req_id = req_dic.get("id")
        req_name = req_dic.get("name")
        if len(req_dic) == 0 or not req_id or not req_name:
            print("No result")
        else:
            print("[{}] {}".format(req_id, req_name))
    except Exception:
        print("Not a valid JSON")


# json() = decode
