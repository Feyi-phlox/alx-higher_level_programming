#!/usr/bin/python3
# script that takes in a URL, sends a request to the URL
# and displays the value of the X-Request-Id variable
import urllib.request
import sys

url = sys.argv[1]

if __name__ == "__main__":
    if len(sys.argv) == 2:
        with urllib.request.urlopen(url) as response:
            x_request_id = response.info().get("X-Request-Id")
            print(x_request_id)
