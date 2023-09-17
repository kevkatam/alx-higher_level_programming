#!/usr/bin/python3
""" module for testing the Rectangle class """
import unittest
from unittest import TestCase
from io import StringIO
from unittest.mock import patch
from models.rectangle import Rectangle
from models.Base import Base


class TestRectangle(unittest.TestCase):
    """ suite that tests rectangle class """
    def setUp(self):
        """ method invoked for each test """
        Base.__nb_objects = 0

    def test_new_rectangle(self):
        """ tests new rectangle """
        new_ins = Rectangle(2, 2)
        self.assertEqual(new_ins.width, 2)
        self.assertEqual(new_ins.height, 2)
        self.assertEqual(new_ins.x, 0)
        self.assertEqual(new_ins.y, 0)
        self.assertEqual(new_ins.id, 1)

    def test_new_rectangle1(self):
        """ tests new rectangle with all attributes """
        new_ins = Rectangle(2, 3, 4, 5, 6)
        self.assertEqual(new_ins.width, 2)
        self.assertEqual(new_ins.height, 3)
        self.assertEqual(new_ins.x, 4)
        self.assertEqual(new_ins.y, 5)
        self.assertEqual(new_ins.id, 6)

    def test_new_rectangles(self):
        """ tests new rectangles """
        new_ins = Rectangle(2, 2)
        new_ins1 = Rectangle(2, 2)
        self.assertEqual(False, new_ins is new_ins2)
        self.assertEqual(False, new_ins.id == new_ins1.id)

    def test_is_base_instance(self):
        """ tests if rectangle is instance of base """
        new_ins = Rectangle(2, 2)
        self.assertEqual(True, isinstance(new_ins, Base))

    def test_incorrect_amount_of_attrs(self):
        """ test when one attribute is passed """
        with self.assertRaises(TypeError):
            new_ins = Rectangle(2)

    def test_incorrect_amount_of_attrs1(self):
        """ test when no attribute is passed """
        with self.assertRaises(TypeError):
            new_ins = Rectangle()

    def test_access_private_attr(self):
        """ test access to private attribute """
        new_ins = Rectangle(2, 2)
        with self.asserRaises(AttributeError):
            new_ins.__width

    def test_access_private_attr1(self):
        """ test access to private attribute """
        new_ins = Rectangle(2, 2)
        with self.asserRaises(AttributeError):
            new_ins.__height

    def test_access_private_attr2(self):
        """ test access to private attribute """
        new_ins = Rectangle(2, 2)
        with self.asserRaises(AttributeError):
            new_ins.__x

    def test_access_private_attr3(self):
        """ test access to private attribute """
        new_ins = Rectangle(2, 2)
        with self.asserRaises(AttributeError):
            new_ins.__y

    def test_valid_attrs(self):
        """ test passing a string """
        with self.asserRaises(TypeError):
            new_ins = Rectangle("2", 2, 2, 2, 2)

    def test_valid_attrs1(self):
        """ test passing a string """
        with self.asserRaises(TypeError):
            new_ins = Rectangle(2, "2", 2, 2, 2)

    def test_valid_attrs2(self):
        """ test passing a string """
        with self.asserRaises(TypeError):
            new_ins = Rectangle(2, 2, "2", 2, 2)

    def test_valid_attrs3(self):
        """ test passing a string """
        with self.asserRaises(TypeError):
            new_ins = Rectangle(2, 2, 2, "2", 2)

    def test_value_attrs(self):
        """ test passing invalid attributes """
        with self.assertRaises(ValueError):
            new_ins = Rectangle(0, 1)

    def test_value_attrs1(self):
        """ test passing invalid attributes """
        with self.assertRaises(ValueError):
            new_ins = Rectangle(1, 0)

    def test_value_attrs2(self):
        """ test passing invalid attributes """
        with self.assertRaises(ValueError):
            new_ins = Rectangle(1, 1, -1)

    def test_value_attrs3(self):
        """ test passing invalid attributes """
        with self.assertRaises(ValueError):
            new_ins = Rectangle(1, 1, 1, -1)

    def test_area(self):
        """ tests return value of square method """
        new_ins = Rectangle(3, 4)
        self.assertEqual(new_ins.area(), 12)

    def test_area1(self):
        """ tests return value of square method """
        new_ins = Rectangle(3, 4)
        self.assertEqual(new_ins.area(), 12)
        new_ins.width = 2
        self.assertEqual(new_ins.area(), 8)
        new_ins.height = 2
        self.assertEqual(new_ins.area(), 4)
