#!/usr/bin/python3
"""basic auth via github api"""
import sys
import requests


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]

    url = "https://api.github.com/user"

    response = requests.get(url, auth=(username, password))

    try:
        r = response.json()
    except ValueError:
        print("None")
    finally:
        id = r.get("id")
        print(id)
