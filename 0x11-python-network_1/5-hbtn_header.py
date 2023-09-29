#!/usr/bin/python3
"""  script that takes in a URL, sends a request to the URL
and displays the value of the variable X-Request-Id in the response header
"""
from sys import argv
import requests


url = argv[1]
if __name__ == "__main__":
    req = requests.get(url)
    print(req.headers.get("X-Request-Id"))
