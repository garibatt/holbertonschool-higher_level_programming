#!/usr/bin/python3
"""this is document"""
import json


def load_from_json_file(filename):
    """this is document"""
    with open(filename, "r", encoding="utf-8") as json_file:
        return json.load(json_file)
