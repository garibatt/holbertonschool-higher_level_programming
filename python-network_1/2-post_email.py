#!/usr/bin/python3
"""POST request with urllib"""
import sys
import urllib.parse
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    data = {"email": email}

    endata = urllib.parse.urlencode(data).encode("utf-8")

    req = urllib.request.Request(url, data=endata)

    with urllib.request.urlopen(req) as f:
        body = f.read().decode("utf-8")
        print(body)
