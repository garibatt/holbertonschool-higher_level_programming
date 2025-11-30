#!/usr/bin/env python3
"""
task_00_basic_serialization.py
Basic module to serialize a Python dictionary to a JSON file
and deserialize a JSON file back to a Python dictionary.
"""

import json

def serialize_and_save_to_file(data, filename):
    """Serialize a Python dictionary and save it to a JSON file."""
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def load_and_deserialize(filename):
    """Load and deserialize data from a JSON file to a Python dictionary."""
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
