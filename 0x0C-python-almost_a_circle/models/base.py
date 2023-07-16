#!/usr/bin/python3

"""
this is a module for the base class.
"""


class Base:
    """
    the Base class for the specialised subclasses
    """

    __nb_objects = 0
    
    def __init__(self, id=None):
        """
        the base attributes for the subclasses
        """

        if id is None:
            Base. __nb_objects += 1
            id = Base.__nb_objects

        self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        returns json string rep of dictionaries
        """
        if list_dictionaries is None:
            return ([])
        else:
            return (json.dumps(list_dictionaries))
