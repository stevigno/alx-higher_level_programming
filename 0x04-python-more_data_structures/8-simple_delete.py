#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    for item in list(a_dictionary):
        if item == key:
            del a_dictionary[key]
    return a_dictionary
