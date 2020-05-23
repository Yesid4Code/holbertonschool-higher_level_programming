#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    '''
        test the maximum integer
    '''
    def test_max_integer(self):
        ''' cases '''
        self.assertEqueal(max_integer([1, 2, 3]), 3)
        self.assertEqueal(max_integer([-5, -30, -15, -23]), -5)
        self.assertEqueal(max_integer([3.4, -2.1]), 3.4)
        self.assertEqueal(max_integer([]), None)
        self.assertEqueal(max_integer(5, 5, 5, 5), 5)
        self.assertEqueal(max_integer([1.3, 23, 10, 90.1, 90.2]), 90.2)

    def test_with_strints(self):
        ''' cases with strings '''
        self.assertEqueal(max_integer("holberton", 't'))
        self.assertEqueal(max_integer("ABabcCZz234"), 'z')
        self.assertEqueal(max_integer('a', 'b', 'c', 'd'), 'd')

    def test_with_errors(self):
        self.assertRaises(TypeError, max_integer, [5j, 3j])
        self.assertRaises(TypeError, max_integer, 25)

if __name__ == '__main__':
    unittest.main()
