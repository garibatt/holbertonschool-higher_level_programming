#!/usr/bin/python3
import sys
import urllib.request

if __name__ = "__main__":
    url = sys.argv[1]

    with urllib.request.urlopen(url) as f:
        header = f.headers
        print(header.get("X-Request-Id"))
