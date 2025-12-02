#!/usr/bin/python3
"""request error"""
import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]
    req = requests.get(url)
    StatusCode = req.status_code
    if StatusCode >= 400:
        print(f"Error code: {StatusCode}")
    else:
        print("Regular request")
