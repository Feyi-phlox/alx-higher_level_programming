#!/usr/bin/python3
# script that fetches https://alx-intranet.hbtn.io/status
import urllib.request

url = "https://alx-intranet.hbtn.io/status"

with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    html = response.read()
    print("Body response:")
    print("\t- type:", type(html))
    print("\t- content:", html)
    print("\t- utf8 content:", html.decode('utf-8'))
