#!/usr/bin/python3
"""simple request (1line)"""
import requests

if __name__ == "__main__":
    req = requests.get("https://intranet.hbtn.io/status")
    print("Body response:")
    print(f"\t- type: {type(req.text)}")
    print(f"\t- content: {req.text}")
