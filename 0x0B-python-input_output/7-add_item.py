#!/usr/bin/python3
"""This module adds all arguments to a python list"""
import sys
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file


argument = sys.argv[1:]

try:
    items = load_from_json_file('add_item.json')
except FileNotFoundError:
    items = []

for i in argument:
    items.append(i)

save_to_json_file(items, 'add_item.json')
