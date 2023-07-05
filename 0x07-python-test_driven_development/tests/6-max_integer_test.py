#!/usr/bin/python3

""" this is are testcases for the function max_int"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class Max_test(unittest.TestCase):
    """ it tests the different occurrences of max_int"""
    def test_empty_list(self):
        """ it tests an empty list"""
        self.assertIsNone(max_integer())
        
    def test_single_element(self):
        """ it tests a single element list"""
        self.assertEqual(max_integer([9]), 9)
    
    def test_positive_numbers(self):
        """ it tests  positive number elements of list"""
        self.assertEqual(max_integer([1, 4, 5, 6]), 6)
        self.assertEqual(max_integer([1,7,2,5]), 7)
    
    def test_negative_numbers(self):
        """ it tests negative number elements of list"""
        self.assertEqual(max_integer([-1, -5, -3, -4]), -1)
        self.assertEqual(max_integer([-9, -3, -8, -1]), -1)
        
    def test_mixed_numbers(self):
        """ it tests negative and positive number elements of list"""
        self.assertEqual(max_integer([1,-3, -5, 0, -9, 6]), 6)
        self.assertEqual(max_integer([1, -3, 4, -2, 0, 2]), 4)
        
    def test_duplicate_numbers(self):
        """ tests a list that contain a duplicates """
        self.assertEqual(max_integer([1, 5, 4, 3, 5]), 5)
        self.assertEqual(max_integer([5, 5, 5, 5, 5]), 5)
