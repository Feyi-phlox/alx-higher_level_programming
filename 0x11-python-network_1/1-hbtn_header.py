#!/usr/bin/python3
# script that takes in a URL, sends a request to the URL
# and displays the value of the X-Request-Id variable
import urllib.request
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    with urllib.request.urlopen(url) as response:
        x_request_id = response.getheader("X-Request-Id")
        print(x_request_id)
