#!/usr/bin/python3
""" Script that adds arguments to a Python list and save them to a file. """


from sys import argv
import save_to_json_file from 7-save_to_json_file.py
import load_from_json_file from 8-load_from_json_file.py


filename = "add_item.json"

try:
    listt = load_from_json_file(filename)
except:
    listt = []

for arg in argv[1:]:
    listt.append(arg)

save_to_json_file(listt, filename)
