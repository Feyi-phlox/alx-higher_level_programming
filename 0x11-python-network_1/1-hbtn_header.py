#!/usr/bin/python3
# script that takes in a URL, sends a request to the URL
# and displays the value of the X-Request-Id variable
import urllib.request
import sys


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("URL required")
        sys.exit(1)

url = sys.argv[1]

try:
    with urllib.request.urlopen(url) as response:
        x_request_id = response.info().get("X-Request-Id")
        print(x_request_id)
except Exception as e:
    print("Error:", e)
