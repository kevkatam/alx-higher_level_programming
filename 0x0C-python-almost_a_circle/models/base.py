#!/usr/bin/python3
"""
a module base that is base of all the other clases, goal of it
is to manage id attribute in all  and to avoid duplicating the same code
"""
import json
import os.path


class Base:
    """ class base that is "base" of all other classes in the project
    """
    __nb_objects = 0

    def __int__(self, id=None):
        """ initializer """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ method that returns the JSON string representation of
        list_dictionaries """
        if list_dictionaries is None or len(list_dictionaries) is 0:
            return "[]"
        else:
            json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ method that writes the JSON string representation of list_objs
        to a file """
        filename = "{}.json".format(cls.__name__)
        dic_list = []
        if not list_objs:
            pass
        else:
            for i in range(len(list_objs)):
                dic_list.append(list_objs[i].to_dictionary())
        mylists = cls.to_json_string(dic_list)
        with open(filename, mode="w") as my_file:
            my_file.write(mylists)

    @staticmethod
    def from_json_string(json_string):
        """ method that returns the list of the JSON string representation
        json_string """
        if json_string is None or len(json_string) is 0:
            return []
        else:
            json.loads(json_string)
    
    @classmethod
    def create(cls, **dictionary):
        """ method that returns an instance with all attributes already set
        """
        if cls.__name__ == "Rectangle":
            new_instance = cls(5, 5)
        else:
            new_instance = cls(5)
        new_instance.update(**dictionary)
        return new_instance

    @classmethod
    def load_from_file(cls):
        """ method that returns a list of instances """
        filename = "{}.json".format(cls.__name__)
        instance_list = []
        if  os.path.exists(filename) is False:
            return []
        with open(filename, mode="r") as my_file:
            str_list = myfile.read()
            list_class = cls.from_json_string(str_list)
        for i in range(len(list_class)):
            instance_list.apppend(create(**list_class[i]))
        return instance_list
