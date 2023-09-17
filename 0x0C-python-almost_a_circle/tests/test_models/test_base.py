#!/usr/bin/python3
""" modelue for test of class Base """
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
from io import StringIO
from unittest import TestCase
from unittest.mock import patch


class TestBaseMethods(unittest.TestCase):
    """ suite totest base class """

    def setUp(self):
        """ method that is invoked for each test """
        Base._Base__nb_objects = 0

    def test_id(self):
        """ test the assigne id """
        new_ins = Base(2)
        self.assertEqual(new_ins.id, 2)

    def test_id_default(self):
        """ test the default id """
        new_ins = Base()
        self.assertEqual(new_ins.id, 1)

    def test_id_nb_objects(self):
        """ tests the __nb_objects attribute """
        new_ins = Base()
        new_ins1 = Base()
        new_ins2 = Base()
        self.assertEqual(new_ins.id, 1)
        self.assertEqual(new_ins.id, 2)
        self.assertEqual(new_ins.id, 3)

    def test_id_dif(self):
        """ tests the __nb_objects attribute and id """
        new_ins = Base()
        new_ins1 = Base(250)
        new_ins2 = Base()
        self.assertEqual(new_ins.id, 1)
        self.assertEqual(new_ins.id, 250)
        self.assertEqual(new_ins.id, 3)

    def test_id_string(self):
        """ tests string id """
        new_ins = Base("2")
        self.assertEqual(new_ins.id, "2")

    def test_id_more_args(self):
        """ test passing more args to base """
        with self.assertRaises(TypeError):
            new_ins = Base(2, 2)

    def test_private_atrs(self):
        """ tests private attributes """
        new_ins = Base()
        with self.assertRaises(AttributeError):
            new_ins.__nb_objects

    def test_save_to_file(self):
        """ tests JSON file """
        Rectangle.save_to_file(None)
        result = "[]\n"
        with open("Rectangle.json", mode="r") as my_file:
            with patch("sys.stdout", new_ins=StringIO()) as strout:
                print(my_file.read())
                self.assertEqual(strout.getvalue(), result)
        try:
            os.remove("Rectangle.json")
        except:
            pass
        Rectangle.save_to_file([])
        with open("Rectangle.json", mode="r") as my_file:
            self.assertEqual(my_file.read(), "[]")

    def test_save_to_file(self):
        """ tests JSON file """
        Square.save_to_file(None)
        result = "[]\n"
        with open("Square.json", mode="r") as my_file:
            with patch("sys.stdout", new_ins=StringIO()) as strout:
                print(my_file.read())
                self.assertEqual(strout.getvalue(), result)
        try:
            os.remove("Square.json")
        except:
            pass
        Square.save_to_file([])
        with open("Square.json", mode="r") as my_file:
            self.assertEqual(my_file.read(), "[]")
