#!/usr/bin/python3
"""This modules adds all arguments to a Python list and save them to a file"""
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

args = sys.argv[1:]

try:
    items = load_from_json_file('add_item.json')
except FileNotFoundError:
    items = []
for items in args:
    items.append(item)

save_to_json_file(items, 'add_item.json')
