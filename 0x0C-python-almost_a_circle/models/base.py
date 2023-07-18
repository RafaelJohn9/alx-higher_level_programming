#!/usr/bin/python3

"""
this is a module for the base class.
"""

import json
import csv


class Base:
    """
    the Base class for the specialised subclasses
    """

    __nb_objects = 0
    
    def __init__(self, id=None):
        """
        the base attributes for the subclasses
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        returns json string rep of dictionaries
        """
        if list_dictionaries is None:
            return []
        else:
            return (json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        """
        saves the list of objs  in a json string 
        """
        fileName = cls.__name__ + ".json"
        if list_objs is not None and len(list_objs) != 0:
            for objs in list_objs:
                json_list = cls.to_json_string([obj.to_dictionary() for obj in list_objs])
        with open(fileName, mode="w", encoding="utf-8") as file:
            file.write(json_list)

    @staticmethod
    def from_json_string(json_string):
        """
        converts list from json string back to list of dictionaries
        """

        if json_string is None or len(json_string) == 0:
            return []
        json_string_in_list = json.loads(json_string)
        return (json_string_in_list)

    @classmethod
    def create(cls, **dictionary):
        """
        creates a new dictionary
        """

        if cls.__name__ == "Rectangle":
            dummy = cls(1,1)
        elif cls.__name__ == "Square":
            dummy = cls(1)

        dummy.update(**dictionary)
        return (dummy)

    @classmethod
    def load_from_file(cls):
        """
        loads json  from file
        """

        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as file:
                listOfInstances = json.loads(file.read())
                instances = [cls.create(**dictionary) for dictionary in listOfInstances]
                return (instances)
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        saves  a file attr in a dictionary
        """

        filename = cls.__name__ + ".csv"
        with open(filename, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            if list_objs is not None and len(list_objs) > 0:
                attributes = cls.get_csv_attributes()
                writer.writerow(attributes)
                for obj in list_objs:
                    values = [getattr(obj, attr) for attr in attributes]
                    writer.writerow(values)

    @classmethod
    def load_from_file_csv(cls):
        """Load a list of objects from a file in CSV format"""
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, mode="r", encoding="utf-8") as file:
                reader = csv.reader(file)
                next(reader)
                objs = []
                for row in reader:
                         obj = cls(int(row[1]), int(row[2]), int(row[3]), int(row[4]), int(row[0]))
                         objs.append(obj)
                return objs
        except FileNotFoundError:
            return []

    @classmethod
    def get_csv_attributes(cls):
        """Get the CSV attribute names for the class"""
        if cls.__name__ == "Rectangle":
            return ["id", "width", "height", "x", "y"]
        elif cls.__name__ == "Square":
            return ["id", "size", "x", "y"]
