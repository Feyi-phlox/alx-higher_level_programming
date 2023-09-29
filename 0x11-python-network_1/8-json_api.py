#!/usr/bin/python3
""" script that takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
from sys import argv
import requests


if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    if len(argv) == 2:
        q = argv[1]
    else:
        q = ""
    data = {'q': q}

    try:
        response = requests.post(url, data)
        content = response.headers.get('content-type')

        if content == 'application/json':
            jsonres = response.json()
            if jsonres:
                print("[{}] {}".format(jsonres['id'], jsonres['name']))
            else:
                print("No result")
    except ValueError:
        print("Not a valid JSON")
