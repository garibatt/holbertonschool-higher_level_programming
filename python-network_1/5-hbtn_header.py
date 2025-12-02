#!/usr/bin/python3
"""sys + requests"""
import sys
import requests
if __name__ == "__main__":
    url = sys.argv[1]
    getr = requests.get(url)
    print(getr.headers.get('X-Request-Id'))
