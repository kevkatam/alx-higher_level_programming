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

    def test_area2(self):
        """ tests return value of square method """
        new_ins = Rectangle(3, 4)
        self.assertEqual(new_ins.area(), 12)
        new_ins1 = Rectangle(5, 5)
        self.assertEqual(new_ins1.area(), 25)

    def test_display(self):
        """ tests string printed """
        rect1 = Rectangle(2, 2)
        result = "##\n##\n"
        with patch('sys.stdout', new=StringIO()) as strout:
            rect1.display()
            self.assertEqual(strout.getvalue(), result)
        rect1.width = 4
        result = "####\n####\n"
        with patch('sys.stdout', new=StringIO()) as strout:
            rect1.display()
            self.assertEqual(strout.getvalue(), result)

    def test_display1(self):
        """ tests string printed """
        rect1 = Rectangle(2, 4)
        result = "##\n##\n##\n##\n"
        with patch('sys.stdout', new=StringIO()) as strout:
            rect1.display()
            self.assertEqual(strout.getvalue(), result)

    def test_str(self):
        """ tests __str__ return value """
        rect1 = Rectangle(2, 3, 4, 5)
        result = "[Rectangle] (1) 4/5 - 2/3\n"
        with patch('sys.stdout', new=StringIO()) as strout:
            print(rect1)
            self.assertEqual(strout.getvalue(), result)

    def test_str1(self):
        """ tests __str__ return value """
        rect1 = Rectangle(2, 3, 4, 5, 6)
        result = "[Rectangle] (6) 4/5 - 2/3\n"
        with patch('sys.stdout', new=StringIO()) as strout:
            print(rect1)
            self.assertEqual(strout.getvalue(), result)
        rect1.id = 2
        rect1.width = 7
        rect1.height = 8
        result = "[Rectangle] (2) 4/5 - 7/8\n"
        with patch('sys.stdout', new=StringIO()) as strout:
            print(rect1)
            self.assertEqual(strout.getvalue(), result)

    def test_str2(self):
        """ tests __str__ return value """
        rect1 = Rectangle(2, 3)
        result = "[Rectangle] (1) 0/0 - 2/3\n"
        with patch('sys.stdout', new=StringIO()) as strout:
            print(rect1)
            self.assertEqual(strout.getvalue(), result)
        rect2 = Rectangle(6, 7, 8, 9)
        result = "[Rectangle] (2) 8/9 - 6/7\n"
        with patch('sys.stdout', new=StringIO()) as strout:
            print(rect2)
            self.assertEqual(strout.getvalue(), result)

        rect3 = Rectangle(2, 2, 2, 2)
        result = "[Rectangle] (3) 2/2 - 2/2\n"
        with patch('sys.stdout', new=StringIO()) as strout:
            print(rect3)
            self.assertEqual(strout.getvalue(), result)

    def test_str3(self):
        """ tests __str__ return value """
        rect1 = Rectangle(2, 3)
        result = "[Rectangle] (1) 0/0 - 2/3\n"
        self.assertEqual(rect1.__str__(), result)

    def test_display2(self):
        """ tests the string printed """
        rect1 = Rectangle(3, 4, 1, 1)
        result = "\n ###\n ###\n ###\n ###\n"
        with patch('sys.stdout', new=StringIO()) as strout:
            rect1.display()
            self.assertEqual(strout.getvalue(), result)

    def test_display3(self):
        """ tests the string printed """
        rect1 = Rectangle(3, 4)
        result = "###\n###\n###\n###\n"
        with patch('sys.stdout', new=StringIO()) as strout:
            rect1.display()
            self.assertEqual(strout.getvalue(), result)

        rect1.x = 3
        result = "   ###\n   ###\n   ###\n   ###\n"
        with patch('sys.stdout', new=StringIO()) as strout:
            rect1.display()
            self.assertEqual(strout.getvalue(), result)

        rect1.y = 2
        result = "\n\n   ###\n   ###\n   ###\n   ###\n"

    def test_to_dictionary(self):
        """ tests dictionary returned """
        rect1 = Rectangle(1, 2, 3, 4, 5)
        result = "[Rectangle] (5) 3/4 - 1/2\n"
        with patch('sys.stdout', new=StringIO()) as strout:
            print(rect1)
            self.assertEqual(strout.getvalue(), result)
        self.assertEqual(rect1.width, 1)
        self.assertEqual(rect1.height, 2)
        self.assertEqual(rect1.x, 3)
        self.assertEqual(rect1.y, 4)
        self.assertEqual(rect1.id, 5)

        result = "<class 'dict'>\n"
        with patch('sys.stdout', new=StringIO()) as strout:
            print(type(rect1.to_dictionary()))
            self.assertEqual(strout.getvalue(), result)

    def test_to_dictionary1(self):
        """ tests dictionary returned """
        rect1 = Rectangle(1, 1, 1, 1)
        result = "[Rectangle] (1) 1/1 - 1/1\n"
        with patch('sys.stdout', new=StringIO()) as strout:
            print(rect1)
            self.assertEqual(strout.getvalue(), result)

        rect2 = Rectangle(6, 5)
        result = "[Rectangle] (2) 0/0 - 6/5\n"
        with patch('sys.stdout', new=StringIO()) as strout:
            print(rect2)
            self.assertEqual(strout.getvalue(), result)
        rect1_dictionary = rect1.to_dictionary()
        rect2.update(**rect1_dictionary)
        self.assertEqual(rect1.width, rect2.width)
        self.assertEqual(rect1.height, rect2.height)
        self.assertEqual(rect1.x, rect2.x)
        self.assertEqual(rect1.y, rect2.y)
        self.assertEqual(rect1.id, rect2.id)

        result = "<class 'dict'>\n"
        with patch('sys.stdout', new=StringIO()) as strout:
            print(type(rect1_dictionary))
            self.assertEqual(strout.getvalue(), result)

    def test_dict_to_json(self):
        """ tests dictionary to json string """
        rect1 = Rectangle(1, 1)
        dictionary = rect1.to_dictionary()
        jsondictionary = Base.to_json_string([dictionary])
        result = "[{}]\n".format(dictionary.__str__)
        with patch('sys.stdout', new=StringIO()) as strout:
            print(jsondictionary)
            self.assertEqual(strout.getvalue(), result.replace("'", "\""))

    def test_checkvalue(self):
        """ tests args passed """
        with self.assertRaises(ValueError):
            rect1 = Rectangle(-2, 3)

    def test_checkvalue1(self):
        """ tests args passed """
        with self.assertRaises(ValueError):
            rect1 = Rectangle(2, -3)

    def test_create(self):
        """ test create method """
        dictionary = {'id': 98}
        rect1 = Rectangle.create(**dictionary)
        self.assertEqual(rect1.id, 98)

    def test_create1(self):
        """ test create method """
        dictionary = {'id': 98, 'width': 1}
        rect1 = Rectangle.create(**dictionary)
        self.assertEqual(rect1.id, 98)
        self.assertEqual(rect1.width, 1)

    def test_create2(self):
        """ test create method """
        dictionary = {'id': 98, 'width': 1, 'height': 2}
        rect1 = Rectangle.create(**dictionary)
        self.assertEqual(rect1.id, 98)
        self.assertEqual(rect1.width, 1)
        self.assertEqual(rect1.height, 2)

    def test_create3(self):
        """ test create method """
        dictionary = {'id': 98, 'width': 1, 'height': 2, 'x': 3}
        rect1 = Rectangle.create(**dictionary)
        self.assertEqual(rect1.id, 98)
        self.assertEqual(rect1.width, 1)
        self.assertEqual(rect1.height, 2)
        self.assertEqual(rect1.x, 3)

    def test_create4(self):
        """ test create method """
        dictionary = {'id': 98, 'width': 1, 'height': 2, 'x': 3, 'y': 4}
        rect1 = Rectangle.create(**dictionary)
        self.assertEqual(rect1.id, 98)
        self.assertEqual(rect1.width, 1)
        self.assertEqual(rect1.height, 2)
        self.assertEqual(rect1.x, 3)
        self.assertEqual(rect1.y, 4)

    def test_load_fromfile(self):
        """ tests load json file """
        loadfile = Rectangle.load_from_file()
        self.assertEqual(loadfile, [])

    def test_load_fromfile(self):
        """ tests load json file """
    rect1 = Rectangle(2, 2)
    rect2 = Rectangle(5, 6, 2, 2)
    linput = [rect1, rect2]
    Rectangle.save_to_file(linput)
    loutput = Rectangle.load_from_file()

    for i in range(len(linput)):
        self.assertEqual(linput[i].__str__(), loutput[i].__str__())
