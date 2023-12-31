#!/usr/bin/python3
"""Defines a JSON file writing function."""
import json


def save_to_json_file(my_objs, filename):
    """Write an object to a text file using JSON representation."""
    with open(filename, "w") as fl:
        json.dump(my_objs, fl)
