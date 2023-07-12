#!/usr/bin/python3

"""
a function that creates an Object from a “JSON file”:
"""

import json


def load_from_json_file(filename):
    """
    loads a json file
    """

    with open(filename, "r") as f:
        jsonObject = json.load(f)
    return (jsonObject)
