#!/usr/bin/python3
""" script that fetches https://alx-intranet.hbtn.io/status
using the package requests
"""
import requests

url = "https://alx-intranet.hbtn.io/status"

if __name__ == "__main__":
    req = requests.get(url)
    print("Body response:")
    print("\t- type:", type(req.text))
    print("\t- content:", req.text)
