#!/usr/bin/python3
""" script that takes 2 arguments in order to solve this challenge
The first argument will be the repository name
The second argument will be the owner name
"""
import requests
from sys import argv


def list_commits(repository, owner):
    """
    List up to 10 most recent commits of a specified repository
    owned by a user using the GitHub API.

    Args:
        repository (str): The name of the GitHub repository.
        owner (str): The owner (user) of the GitHub repository.

    Returns:
        None: This function prints the commits
        in the format '<sha>: <author name>'.
    """

    base_url = "https://api.github.com/repos"

    endpoint = f"{base_url}/{owner}/{repository}/commits"

    params = {
        "per_page": 10,
    }

    try:
        response = requests.get(endpoint, params=params)

        if response.status_code == 200:
            commits = response.json()
            for commit in commits:
                sha = commit["sha"]
                author_name = commit["commit"]["author"]["name"]
                print(f"{sha}: {author_name}")
        else:
            print(response.status_code)

    except requests.exceptions.RequestException as e:
        print("Error:", e)


if __name__ == "__main__":
    repository_name = argv[1]
    owner_name = argv[2]

    list_commits(repository_name, owner_name)
