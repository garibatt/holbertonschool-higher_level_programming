#!/usr/bin/python3
"""this is document"""
import json


def save_to_json_file(my_obj, filename):
    """this is something"""
    with open(filename, "w", encoding="utf-8") as json_file:
        return json.dump(my_obj, json_file)
