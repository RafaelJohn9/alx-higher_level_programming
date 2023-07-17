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


class  Test_for_id(unittest.TestCase):
    """
    test for the base class
    """

    def test_when_id_is_int(self):
        """
        it tests when id has been given an int number
        """

        second_base_class = Base(18)
        self.assertEqual(second_base_class.id, 18)

class Test_to_json_String(unittest.TestCase):
    """
    test for method "to_json_String"
    """
    def test_for_method_to_json_string(self):
        """
        it tests for method json string
        """
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_single_dictionary(self):
        """
        test  a single dictionary in list
        """
        dictionary = {"id":1 , "width":10, "height":5}
        result = Base.to_json_string([dictionary])
        self.assertEqual(result, '[{"id": 1, "width": 10, "height": 5}]')

    def test_multiple_dictionaries(self):
        """
        tests multiple dictionaries in a list
        """
        dictionary_list = [{"id":1, "width":10, "height":5}, {"id":2, "width":100, "height":50}]
        result = Base.to_json_string(dictionary_list)
        expected = '[{"id": 1, "width": 10, "height": 5}, {"id": 2, "width": 100, "height": 50}]'
        self.assertEqual(result, expected)

    def test_none_input(self):
        """
        tests when no input is put
        """
        result = Base.to_json_string([])
        self.assertEqual(result, "[]")

class Test_for_save_to_file(unittest.TestCase):
    """
    tests for save_to_file function
    """
    def setUp(self):
        """
        creates a test instance for a rectangle
        """
        self.rectangle = Rectangle(10, 7, 2, 8)

    def tearDown(self):
        """
        clean up the test file
        """
        filename = "Rectangle.json"
        if os.path.exists(filename):
            os.remove(filename)

class Test_for_from_json_string(unittest.TestCase):
    """
    tests for testing from_json_String method
    """
    def test_an_empty_string(self):
        """
        tests an empty string
        """
        case1 = Base.from_json_string("")
        self.assertEqual(case1, [])

    def test_uninitialised_string(self):
        """
        tests an uninitialised str or variables of None
        """
        case1 = Base.from_json_string(None)
        self.assertEqual(case1, [])

    def test_multiple_elements(self):
        """
        tests a actual string of json a multiple number of elements
        """
        got = Base.from_json_string('[{"id":5, "width":5, "height":7}, {"id":2, "width":2, "height":2}]')
        expected = [{"id":5, "width":5, "height":7}, {"id":2, "width":2, "height":2}]
        self.assertEqual(got, expected)


    def test_single_elements(self):
        """
        tests a actual string of json a with a single element 
        """
        got = Base.from_json_string('[{"id":2, "width":2, "height":2}]')
        expected = [{"id":2, "width":2, "height":2}]
        self.assertEqual(got, expected)

    def test_empty_list(self):
        """
        tests a actual string of json a multiple number of elements
        """
        got = Base.from_json_string('[]')
        expected = []
        self.assertEqual(got, expected)

class Test_for_create_method(unittest.TestCase):
    """
    tests for create method
    """
    def test_create_rectangle(self):
        """
        creates new rectangle
        """ 
        rectangle_dict = {'id': 1, 'width': 10, 'height': 5, 'x': 2, 'y': 3}
        rectangle_instance = Rectangle.create(**rectangle_dict)
        self.assertIsInstance(rectangle_instance, Rectangle)
        self.assertEqual(rectangle_instance.id, 1)
        self.assertEqual(rectangle_instance.width, 10)
        self.assertEqual(rectangle_instance.height, 5)
        self.assertEqual(rectangle_instance.x, 2)
        self.assertEqual(rectangle_instance.y, 3)

    def test_create_square(self):
        """
        creates a new square
        """
        square_dict = {'id': 1, 'size': 5, 'x': 2, 'y': 3}
        square_instance = Square.create(**square_dict)
        self.assertIsInstance(square_instance, Square)
        self.assertEqual(square_instance.id, 1)
        self.assertEqual(square_instance.size, 5)
        self.assertEqual(square_instance.x, 2)
        self.assertEqual(square_instance.y, 3)

class Test_load_from_file_existing_file(unittest.TestCase):
    """
    testing when loading an existing file
    """

    def setUp(self):
        """
        create a temp file for testing
        """
        self.filename = "Rectangle.json"
        self.data = [
                 {"id": 1, "width": 10, "height": 5},
                 {"id": 2, "width": 7, "height": 3}
                 ]
        with open(self.filename, "w") as file:
            json.dump(self.data, file)

    def tearDown(self):
        """
        remove the temporary file after testing
        """

        if os.path.exists(self.filename):
            os.remove(self.filename)

    def test_load_from_file_existing_file(self):
        """
        tests on the existing file
        """

        result = Rectangle.load_from_file()
        self.assertEqual(len(result), 2)
        self.assertIsInstance(result[0], Rectangle)
        self.assertIsInstance(result[1], Rectangle)
        self.assertEqual(result[0].id, 1)
        self.assertEqual(result[0].width, 10)
        self.assertEqual(result[0].height, 5)
        self.assertEqual(result[1].id, 2)
        self.assertEqual(result[1].width, 7)
        self.assertEqual(result[1].height, 3)

    def test_load_from_file_nonexistent_file(self):
        """
        tests when the file does not exist
        """
        nonexistent_filename = "NonexistentClass.json"
        result = Base.load_from_file()
        self.assertEqual(result, [])

class TestCSVSerialization(unittest.TestCase):
    """
    Unit tests for CSV serialization and deserialization
    """

    def setUp(self):
        """
        Set up test data
        """
        self.rectangle = Rectangle(1, 2, 3, 4)
        self.square = Square(5, 6, 7)

    def test_save_to_file_csv_rectangle(self):
        """
        Test save_to_file_csv for Rectangle objects
        """
        Rectangle.save_to_file_csv([self.rectangle])
        filename = "Rectangle.csv"
        self.assertTrue(os.path.exists(filename))

        with open(filename, mode="r", newline="") as file:
            reader = csv.reader(file)
            rows = list(reader)
            self.assertEqual(len(rows), 2)  # Header + data row

    def test_save_to_file_csv_square(self):
        """
        Test save_to_file_csv for Square objects
        """
        Square.save_to_file_csv([self.square])
        filename = "Square.csv"
        self.assertTrue(os.path.exists(filename))

        with open(filename, mode="r", newline="") as file:
            reader = csv.reader(file)
            rows = list(reader)
            self.assertEqual(len(rows), 2)  # Header + data row

    def test_load_from_file_csv_rectangle(self):
        """
        Test load_from_file_csv for Rectangle objects
        """
        filename = "Rectangle.csv"
        with open(filename, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["id", "width", "height", "x", "y"])
            writer.writerow(["1", "1", "2", "3", "4"])

        rectangles = Rectangle.load_from_file_csv()
        self.assertEqual(len(rectangles), 1)
        self.assertEqual(rectangles[0].id, 1)
        self.assertEqual(rectangles[0].width, 1)
        self.assertEqual(rectangles[0].height, 2)
        self.assertEqual(rectangles[0].x, 3)
        self.assertEqual(rectangles[0].y, 4)

    def test_load_from_file_csv_square(self):
        """
        Test load_from_file_csv for Square objects
        """
        filename = "Square.csv"
        with open(filename, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["id", "size", "x", "y"])
            writer.writerow(["5", "5", "6", "7"])

        squares = Square.load_from_file_csv()
        self.assertEqual(len(squares), 1)
        self.assertEqual(squares[0].id, 5)
        self.assertEqual(squares[0].size, 5)
        self.assertEqual(squares[0].x, 6)
        self.assertEqual(squares[0].y, 7)

    def test_get_csv_attributes_rectangle(self):
        """
        Test get_csv_attributes for Rectangle class
        """
        attributes = Rectangle.get_csv_attributes()
        self.assertEqual(attributes, ["id", "width", "height", "x", "y"])

    def test_get_csv_attributes_square(self):
        """
        Test get_csv_attributes for Square class
        """
        attributes = Square.get_csv_attributes()
        self.assertEqual(attributes, ["id", "size", "x", "y"])

    def tearDown(self):
        """
        Clean up test files
        """
        filenames = ["Rectangle.csv", "Square.csv"]
        for filename in filenames:
            if os.path.exists(filename):
                os.remove(filename)
