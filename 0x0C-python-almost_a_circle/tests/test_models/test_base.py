#!/usr/bin/python3

"""
this is a module that contains unittest of the base class
"""


import unittest
from models.base import Base


class Test(unittest.TestCase):
    """
    test for the base class
    """

    def test_when_Id_Is_None(self):
        """
        it tests base class when id is None
        """

        first_base_class = Base()
        self.assertEqual(first_base_class.id, 1)

    def test_when_id_is_int(self):
        """
        it tests when id has been given an int number
        """

        second_base_class = Base(18)
        self.assertEqual(second_base_class.id, 18)
