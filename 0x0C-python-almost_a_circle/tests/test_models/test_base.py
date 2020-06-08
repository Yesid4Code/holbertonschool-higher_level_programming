#!/usr/bin/python3
"""
    Conteins tests for Base class.
"""


import unittest
import json
from models.base import Base
from models.rectangle import Rectangle
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
        b1 = Base()
        b2 = Base()
        b3 = Base()
        b4 = Base(12)
        b5 = Base()
        b6 = Base("text")
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)
        self.assertEqual(b4.id, 12)
        self.assertEqual(b5.id, 4)
        self.assertEqual(b6.id, "text")

    def test_15_to_json_string(self):  # Task 15
        """ Test method to_json_string. """
        d0 = {"id": 9, "width": 5, "height": 6, "x": 7, "y": 8}
        d1 = {"id": 2, "width": 2, "height": 3, "x": 4, "y": 0}
        r8 = Rectangle(9, 8, 8, 4)
        d2 = r8.to_dictionary()
        j_dic = Base.to_json_string([d0, d1])
        p_dic = json.loads(j_dic)
        self.assertEqual(p_dic, [d0, d1])
        j_dic = Base.to_json_string([d0, d2])
        p_dic = json.loads(j_dic)
        self.assertEqual(p_dic, [d0, d2])
        j_dic = Base.to_json_string(None)
        self.assertEqual(j_dic, "[]")


if __name__ == '__main__':
        unittest.main()

# Test
# python3 -m unittest discover tests
# python3 -m unittest tests/test_models/test_base.py
