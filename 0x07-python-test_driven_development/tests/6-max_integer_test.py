#!/usr/bin/python3

import unittest
def max_integer(list=[]):
    """Function to find and return the max integer in a list of integers
        If the list is empty, the function returns None
    """
    if len(list) == 0:
        return None
    result = list[0]
    i = 1
    while i < len(list):
        if list[i] > result:
            result = list[i]
        i += 1
    return result



class Max_test(unittest.TestCase):
    def test_empty_list(self):
        self.assertIsNone(max_integer())
        
    def test_single_element(self):
        self.assertEqual(max_integer([9]), 9)
    
    def test_positive_numbers(self):
        self.assertEqual(max_integer([1, 4, 5, 6]), 6)
        self.assertEqual(max_integer([1,7,2,5]), 7)
    
    def test_negative_numbers(self):
        self.assertEqual(max_integer([-1, -5, -3, -4]), -1)
        self.assertEqual(max_integer([-9, -3, -8, -1]), -1)
        
    def test_mixed_numbers(self):
        self.assertEqual(max_integer([1,-3, -5, 0, -9, 6]), 6)
        self.assertEqual(max_integer([1, -3, 4, -2, 0, 2]), 4)
        
    def test_duplicate_numbers(self):
        self.assertEqual(max_integer([1, 5, 4, 3, 5]), 5)
        self.assertEqual(max_integer([5, 5, 5, 5, 5]), 5)
