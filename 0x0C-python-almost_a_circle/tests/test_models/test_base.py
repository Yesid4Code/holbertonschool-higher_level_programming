#!/usr/bin/python3
"""
    Conteins tests for Base class.
"""


import unittest
from models.base import Base
# here should be more imports like inspect, pep8, json, base,


class TestBase(unittest.TestCase):
    """
    Check:
      Test to check the documentation and style of Base class on TestBaseDocs.
    Class contining functions to run
    multiple tests
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


    if __name__ == '__main__':
        unittest.main()
