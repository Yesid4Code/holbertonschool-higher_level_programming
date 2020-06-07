#!/usr/bin/python3
"""
Conteins tests for Square class.
"""


import unittest
import sys
from io import StringIO
from models.square import Square
# here should be more imports.


class TestSquare(unittest.TestCase):
    """
    Class containing functions to test:
        * Functionality of the Square class.
        * Style of the Square class.
        * Documentation of the Rectangle class.
    """

    def setUp(self):
        """ Method to sed the start point. """
        # Square("size", "x", "y", "id")
        self.r0 = Square(8, 12, 2, 20)
        self.r1 = Square(10, 11)
        self.r2 = Square(12, 13, 14)
        self.r3 = Square(6, 5, 2, 21)
        # Redirect output to verify output of print dependent functions.
        sys.stdout = StringIO()

    def tearDown(self):
        """
        Method to cleans everything up after running setup.
        """
        sys.stdout = sys.__stdout__

    def test_10_square(self):  # Task 10
        """ . """
        pass

    def test_11_Get_Setter(self):
        """ . """
        pass

    def test_12_update(self):
        """Tests that the update method uses setter with *args and **kwargs """
        self.r0.update(2)
        self.r3.update(3, 2, 2, 20)
        self.assertEqual(self.r0.__str__(), "[Square] (2) 12/2 - 8")
        self.assertEqual(self.r3.__str__(), "[Square] (3) 2/20 - 2")

    def test_13_to_dictionary(self):
        """ Test regular to_dictionary """
        d1 = self.r0.to_dictionary()
        self.assertEqual({"id": 20, "width": 8, "height": 8, "x": 12, "y": 2},
                         d1)
        self.assertTrue(type(d1) is dict)


# Tests comands
# python3 -m unittest discover tests
# python3 -m unittest tests/test_models/test_base.py
