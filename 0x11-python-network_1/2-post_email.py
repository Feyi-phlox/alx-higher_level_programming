#!/usr/bin/python3
""" script that takes in a URL and an email, sends a POST request
to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)
"""
from urllib.request import urlopen
from urllib.parse import urlencode
from sys import argv


if __name__ == "__main__":
    email = {"email": argv[2]}
    email = urlencode(email).encode('utf-8')

    with urlopen(argv[1], data=email) as response:
        html = response.read().decode('utf-8')
        print(html)
