#!/usr/bin/python3
"""Sends a POST request with an email parameter and displays the response."""

import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    # Encode the POST data
    data = urllib.parse.urlencode({"email": email}).encode("utf-8")

    # Send POST request
    with urllib.request.urlopen(url, data) as response:
        body = response.read()

    # Decode and print response body
    print(body.decode("utf-8"))
