#!/usr/bin/python3
# 6-from_json_string.py
"""Writes a JSON-to-object function."""
import json


def from_json_string(stv_str):
    """Return the Python object representation of a JSON string."""
    return json.loads(stv_str)
