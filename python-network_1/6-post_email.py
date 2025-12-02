#!/usr/bin/python3
""" post method in use, requests + sys"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    mail = sys.argv[2]
    data = {"email": mail}
    parse = requests.post(url, data=data)
    print(parse.text)
