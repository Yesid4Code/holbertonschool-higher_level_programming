#!/usr/bin/python3
"""
    Conteins tests for Base class.
"""


import unittest
import json
from models.base import Base
# here should be more imports like inspect, pep8, json, base,


class TestBase(unittest.TestCase):
    """
    Class containing functions to test on the Bass class:
        * Functionality.
        * Style.
        * Documentation.
    """
    def SetUp(self):
        """ Method to set the start point """
        Base.Base__nb_objects = 0

    def test_0_id(self):
        """
        Test to chec for id method.
        """
        b0 = Base()
        b1 = Base(23)
        b2 = Base("text")
        self.assertEqual(b0.id, 1)
        self.assertEqual(b1.id, 23)
        self.assertEqual(b2.id, "text")

if __name__ == '__main__':
        unittest.main()

# Test
# python3 -m unittest discover tests
# python3 -m unittest tests/test_models/test_base.py
