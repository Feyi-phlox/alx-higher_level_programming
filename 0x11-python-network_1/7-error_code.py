#!/usr/bin/python3
""" script that takes in a URL, sends a request to the URL
and displays the body of the response.
"""
from sys import argv
import requests


if __name__ == "__main__":
    url = argv[1]
    try:
        req = requests.get(url)
        req.raise_for_status()
        print(req.text)
    except requests.RequestException as e:
        print("Error code:", req.status_code)
