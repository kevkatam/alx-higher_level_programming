#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """body test for max_integer function"""
    def test_max_integer(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)

    def test_repeated_number(self):
        self.assertEqual(max_integer([700, 700, 700]), 700)

    def test_float_number(self):
        self.assertEqual(max_integer([60, 61, 60, 59]), 61)

    def test_max_operated_number(self):
        self.assertEqual(max_integer([4 * 5, 3, 9, 10]), 20)

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-5, -9, -4, -2]), -2)

    def test_max_at_beginning(self):
        self.assertEqual(max_integer([10, 4, 6, 8]), 10)

    def test_zero_numbers(self):
        self.assertEqual(max_integer([0, 0, 0]), 0)

    def test_large_list(self):
        self.assertEqual(max_integer([
            501, 502, 503, 504, 505, 506, 507, 508, 509, 510,
            511, 600, 512, 513, 514, 515, 516, 517, 518, 519,
            520, 521, 522, 523, 524, 525, 526, 527, 528, 529,
            530, 531, 532, 533, 534, 535, 536, 537, 538, 539,
            540, 541, 542, 543, 544]), 600)

    def test_lists_withloop(self):
        mylist = [1, 2, 3, 4, 5, 6]
        self.assertEqual(max_integer([i * 4 for i in mylist]), 24)

    def test_single_number_in_list(self):
        self.assertEqual(max_integer([2]), 2)

    def test_string_no_in_list(self):
        with self.assertRaises(TypeError):
            max_integer([1, '2'])

    def test_tuple_in_list(self):
        with self.assertRaises(TypeError):
            max_integer([(1, 2), 3])

    def test_dictionary(self):
        with self.assertRaises(KeyError):
            max_integer({'key': 1, 'key1': 2})

    def test_number(self):
        with self.assertRaises(TypeError):
            max_integer(3)
