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

    try:
        response = requests.get(api_url, auth=auth)

        if response.status_code == 200:
            user_data = response.json()
            user_id = user_data.get("id")
            print(user_id)
        else:
            print(response.status_code)
    except requests.exceptions.RequestException as e:
        print("Error:", e)
