#!/usr/bin/python3

"""
a class that is changed to json object
"""


def class_to_json(obj):
    """ this is a function that changes a class to json object
    """

    json_dict = {}
    for key, value in obj.__dict__.items():
        if isinstance(value, (list, dict, str, int, bool)):
            json_dict[key] = value
    return json_dict
