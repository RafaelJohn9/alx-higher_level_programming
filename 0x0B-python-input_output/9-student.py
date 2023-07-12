#!/usr/bin/python3

"""
a class Student
"""


class Student:
    """
    this is a class that defines a student
    """

    def __init__(self, first_name, last_name, age):
        """
        contains student's attribute
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ changes a class to a dict of json """

        json_dict = {}
        for key, value in self.__dict__.items():
            if isinstance(value, (str, int)):
                json_dict[key] = value
        return json_dict
