#!/usr/bin/python3
""" script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
"""
import requests
from sys import argv


if __name__ == "__main__":
    username = argv[1]
    token = argv[2]

    auth = (username, token)

    api_url = "https://api.github.com/user"
    response = requests.get(api_url, auth=auth).json()
    user_id = response.get("id")
    print(user_id)
