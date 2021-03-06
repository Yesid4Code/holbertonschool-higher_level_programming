#!/usr/bin/python3
"""
    Conteins tests for Rectangle class.
"""


import unittest
import sys
import pep8
from io import StringIO
from models import rectangle
from models.base import Base
from models.rectangle import Rectangle


class TestRectanglePep8(unittest.TestCase):
    """ checking for pep8 validation """
    def test_pep8(self):
        """ test rectangle and test_rectangle
            for pep8 conformance """
        style = pep8.StyleGuide(quiet=True)
        file1 = 'models/rectangle.py'
        file2 = 'tests/test_models/test_rectangle.py'
        result = style.check_files([file1, file2])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warning).")


class TestRecDocs(unittest.TestCase):
    """ checking for documentation """
    def test_module_doc(self):
        """ checking for module documentation """
        self.assertTrue(len(rectangle.__doc__) > 0)

    def test_class_doc(self):
        """ checking for class documentation """
        self.assertTrue(len(Rectangle.__doc__) > 0)

    def test_method_docs(self):
        """ checking for method documentation """
        for func in dir(Rectangle):
            self.assertTrue(len(func.__doc__) > 0)


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
        Base._Base__nb_objects = 0
        self.r0 = Rectangle(8, 12, 2, 1, 12)
        self.r1 = Rectangle(10, 11)
        self.r2 = Rectangle(12, 13, 14, 15)
        self.r3 = Rectangle(2, 4, 0, 3, 13)
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
        self.assertEqual(self.r3.width, 2)
        self.assertEqual(self.r4.x, 0)

    def test_TypeErrors(self):
        """ TypeError cases. """
        self.assertRaises(TypeError, Rectangle, "a", 2, 7, 8)
        self.assertRaises(TypeError, Rectangle, [1, 2], 2, 7, 8)
        self.assertRaises(TypeError, Rectangle, 2.2, 2, 7, 8)
        self.assertRaises(TypeError, Rectangle, {2}, 2, 7, 8)
        self.assertRaises(TypeError, Rectangle, 2, 2, 7, (1, 2))
        self.assertRaises(TypeError, Rectangle, 2, 2, 7, 5j)
        self.assertRaises(TypeError, Rectangle, 2, 2, 7, float("inf"))

    def test__ValueErrors(self):
        """ ValueError cases. """
        self.assertRaises(ValueError, Rectangle, -8, 2, 7, 8)
        self.assertRaises(ValueError, Rectangle, 2, 2, 7, -8)
        self.assertRaises(ValueError, Rectangle, -8, 2, -7, 8)
        self.assertRaises(ValueError, Rectangle, -8, -2, 7, 8)

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

    def test_07_display_1(self):
        """ Test display method with 'x' and 'y' position. """
        r1O = "\n\n\n##\n" \
              "##\n" \
              "##\n" \
              "##\n"
        self.r3.display()
        self.assertEqual(sys.stdout.getvalue(), r1O)

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

    def test_13_to_dictionary(self):
        """ Test regular to_dictionary """
        d1 = self.r0.to_dictionary()
        self.assertEqual({"id": 12, "width": 8, "height": 12, "x": 2, "y": 1},
                         d1)
        self.assertTrue(type(d1) is dict)

if __name__ == "__main__":
    unittest.main()

# Tests comands
# python3 -m unittest discover tests
# python3 -m unittest tests/test_models/test_rectangle.py
