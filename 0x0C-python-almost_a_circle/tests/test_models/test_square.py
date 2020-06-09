#!/usr/bin/python3
"""
Conteins tests for Square class.
"""


import unittest
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

    def test_10_Square(self):  # Task 10
        """ Instantiation. """
        self.assertEqual(self.r0.size, 8)
        self.assertRaises(TypeError, Square, [1, 2], 2, 7)
        self.assertRaises(TypeError, Square, 2.3, 2, 7)
        self.assertRaises(ValueError, Square, -8, 2, 7)
        self.assertRaises(TypeError, Square, {1, 2}, 2, 7)

    def test_12_update(self):
        """Tests that the update method uses setter with *args and **kwargs """
        self.r0.update(2)
        self.r3.update(3, 2, 2, 20)
        self.assertEqual(self.r0.__str__(), "[Square] (2) 12/2 - 8")
        self.assertEqual(self.r3.__str__(), "[Square] (3) 2/20 - 2")

    def test_14_to_dictionary(self):
        """ Test regular to_dictionary """
        d1 = self.r0.to_dictionary()
        self.assertEqual({"id": 20, "size": 8, "x": 12, "y": 2}, d1)
        self.assertTrue(type(d1) is dict)

# Tests comands
# python3 -m unittest discover tests
# python3 -m unittest tests/test_models/test_base.py
