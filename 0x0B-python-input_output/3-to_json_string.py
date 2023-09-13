#!/usr/bin/python3
"""Writes a string-to-JSON function."""
import json


def to_json_string(obj):
    """Return the JSON representation of a string object."""
    return json.dumps(obj)
