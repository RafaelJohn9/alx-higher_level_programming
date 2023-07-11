#!/usr/bin/python3

"""
a function that returns the JSON representation of an object (string):
"""

import json


def to_json_string(my_obj):
    """ converts  a python object to a string"""

    jsonString = json.dumps(my_obj)
    return (jsonString)
