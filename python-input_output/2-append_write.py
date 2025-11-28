#!/usr/bin/python3
"""this is document"""


def append_write(filename="", text=""):`
    """this is document"""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
