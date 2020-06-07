#!/usr/bin/python3
"""
    Conteins tests for Rectangle class.
"""


import unittest
import sys
from io import StringIO
from models.base import Base
from models.rectangle import Rectangle
# here should be more imports like inspect, pep8, json, base,


class TestRectangle(unittest.TestCase):
    """
    Class containing functions to test:
        * Functionality of the Rectangle class.
        * Style of the Rectangle class.
        * Documentation of the Rectangle class.
    """
    def setUp(self):
        """ Method to set the start point. """
        # Rectangle("width", "height", "x", "y", "id")
        self.r0 = Rectangle(8, 12, 2, 1, 12)
        self.r1 = Rectangle(10, 11)
        self.r2 = Rectangle(12, 13, 14, 15)
        self.r3 = Rectangle(6, 5, 2, 3, 13)
        self.r4 = Rectangle(2, 4, 0, 0)
        # Redirect output to verify output of print dependent functions
        sys.stdout = StringIO()

    def tearDown(self):
        """
        Method to cleans everything up after running setup.
        """
        sys.stdout = sys.__stdout__

    def test_00_id(self):
        """ Tests for id. """
        self.assertEqual(self.r0.id, 12)
        self.assertEqual(self.r1.id, 1)
        self.assertEqual(self.r2.id, 2)

    def test_04_area(self):
        """ Test the area method. """
        self.assertEqual(self.r0.area(), 96)
    def test_05_display_0(self):
        """
        Test display method without x and y
        """
        r1O = "##\n" \
              "##\n" \
              "##\n" \
              "##\n"
        self.r4.display()
        self.assertEqual(sys.stdout.getvalue(), r1O)

    def test_06_str(self):
        """ Test that __str__ method produces correct output. """
        self.assertEqual(self.r0.__str__(), "[Rectangle] (12) 2/1 - 8/12")
        self.assertEqual(self.r1.__str__(), "[Rectangle] (10) 0/0 - 10/11")
    """
    def test_07_display_1(self):
        ""
        Test display method with 'x' and 'y' position. ""
        r1O = "##\n" \
              "##\n" \
              "##\n" \
              "##\n"
        self.r3.display()
        self.assertEqual(sys.stdout.getvalue(), r1O)
    """

    def test_08_update(self):
        """ Tests that the update method uses setter with *args. """
        self.r2.update(9, 3, 2, 0)
        self.assertEqual(self.r2.__str__(), "[Rectangle] (9) 0/15 - 3/2")

    def test_09_update(self):
        """ Tests that the update method uses setter with **kwargs. """
        self.r0.update(x=1, height=2)
        self.r1.update(width=4, x=3, id=14, y=1)
        self.assertEqual(self.r0.__str__(), "[Rectangle] (12) 1/1 - 8/2")
        self.assertEqual(self.r1.__str__(), "[Rectangle] (14) 3/1 - 4/11")

if __name__ == "__main__":
    unittest.main()

# Tests comands
# python3 -m unittest discover tests
# python3 -m unittest tests/test_models/test_base.py
