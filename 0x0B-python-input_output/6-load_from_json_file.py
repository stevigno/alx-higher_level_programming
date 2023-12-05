#!/usr/bin/python3
"""Define a JSON file reading function."""
import json


def load_from_json_file(filename):
    """Create a Python object from a JSON file."""
    with open(filename) as fl:
        return json.load(fl)
