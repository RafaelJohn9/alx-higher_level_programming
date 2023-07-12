#!/usr/bin/python3

"""
a class student
"""


class Student:
    """
    this is a class student
    """

    def __init__(self, first_name, last_name, age):
        """ contains the attributes of student """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ converts the clss to json
        object
        """

        if attrs is None or not isinstance(attrs, list):
            attrs = self.__dict__.keys()
        else:
            attrs = [attr for attr in attrs if isinstance(attr, str)]

        json_dict = {}
        for attr in attrs:
            if attr in self.__dict__ and\
                    isinstance(self.__dict__[attr], (str, int)):
                json_dict[attr] = self.__dict__[attr]
        return json_dict
