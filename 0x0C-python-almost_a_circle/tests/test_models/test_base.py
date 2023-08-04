#!/usr/bin/python3

"""
this is a module that contains unittest of the base class
"""

import csv
import os
import unittest
import json
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class Test_Base(unittest.TestCase):
    """
    this class tests the methods of Base class
    """
    def setUp(self):
        Base._Base__nb_objects = 0
        self.base = Base()

    def tearDown(self):
        """
        clean up
        """
        pass

    def test_for_id(self):
        """
        tests the different occurrences of id
        """
        # when id argument has not been passed by user
        self.assertEqual(self.base.id, 1)
        # when id argument has been passed
        self.base.id = 7
        self.assertEqual(self.base.id, 7)
        # when id argument has been not been passed by user (again)
        self.base = Base()
        self.assertEqual(self.base.id, 2)
        # when id argument has not been passed by user (again)
        self.base = Base()
        self.assertEqual(self.base.id, 3)

    def test_for_to_json_string(self):
        """
        tests the method "to_json_string"
        """
        # test for empty list
        stringDictionary = self.base.to_json_string(None)
        self.assertEqual(stringDictionary, [])
        # test for a list with dictionaries
        stringDictionary = self.base.to_json_string([
            {"Name": "John", "age": 11},
            {"Name": "Benjamin", "age": 12}])
        self.assertIsInstance(stringDictionary, str)

    def test_for_save_to_file(self):
        """
        save_to_file method being tested
        tests if object(s) has(ve)  been saved to a file
        """
        self.new_1 = Rectangle(1, 1)
        self.new_2 = Square(1, 1)
        Base().save_to_file([self.new_1, self.new_2])
        try:
            filename = self.base.__class__.__name__ + ".json"
            with open(filename) as f:
                pass
        except FileNotFoundError:
            self.fail(f"File {filename} not found.")

    def test_for_from_json_string(self):
        """
        tests json string
        """
        listOfDictionary = self.base.to_json_string([
            {"Name": "John", "age": 11},
            {"Name": "Benjamin", "age": 12}])
        stringDictionary = json.dumps(listOfDictionary)
        listedDictionary = self.base.from_json_string(stringDictionary)
        # when string is none
        self.assertEqual(self.base.from_json_string(None), [])
        # when length of dictionary is 0
        self.assertEqual(self.base.from_json_string([]), [])
        # when length of dictionary is more than 0
        self.assertEqual(listedDictionary, listOfDictionary)

    def test_for_create(self):
        """
        test for the method create
        """
        # creating an instance of a rectangle and checking it
        rectangle = Rectangle.create(rectangle=Rectangle(1, 5))
        self.assertIsInstance(rectangle, Rectangle)

        # creating an instance of a Square and checking it
        square = Square.create(square=Square(7))
        self.assertIsInstance(square, Square)
