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


class  Test_Base(unittest.TestCase):
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
