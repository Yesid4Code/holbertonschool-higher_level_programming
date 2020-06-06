#!/usr/bin/python3
"""
    Conteins tests for Rectangle class.
"""


import unittest
from models.base import Base
from models.rectangle import Rectangle
# here should be more imports like inspect, pep8, json, base,


class TestRectangle(unittest.TestCase):
    """
    Check:
      Test to check the documentation and style of Base class on TestBaseDocs.
    Class contining functions to run
    multiple tests
    Test the functionality of the Rectangle class.
    """
    def setUp(self):
        """ Method to set the start point """
        self.r1 = Rectangle(10, 11)
        self.r2 = Rectangle(11, 12, 13)
        self.r3 = Rectangle(12, 13, 14, 15)
        self.r6 = Rectangle(13, 14, 15, 16, 5)
        self.r4 = Rectangle(2, 4, 5, 6, 7)
        self.r5 = Rectangle(3, 45, 4, 2, id="10")


    def test_0_id(self):
        """ Tests for id. """
        self.assertEqual(self.r1.id, 1)
        self.assertEqual(self.r2.id, 2)
        self.assertEqual(self.r3.id, 3)
        self.assertEqual(self.r6.id, 5)
        self.assertEqual(self.r4.id, 7)
        self.assertEqual(self.r5.id, 10)

    def test_1_id(self):
        """ Tests for checking numbers of objects. """
        with self.assertRaises(TypeError):
            Rectangle(10)
            Rectangle()
            Rectangle(x=10, y=20)

if __name__ == "__main__":
    unittest.main()
