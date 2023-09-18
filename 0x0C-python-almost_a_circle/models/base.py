#!/usr/bin/python3
"""
a module base that is base of all the other clases, goal of it
is to manage id attribute in all  and to avoid duplicating the same code
"""
import json
import csv
import os.path


class Base:
    """ class base that is "base" of all other classes in the project
    """
    __nb_objects = 0

    def __init__(self, id=None):
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
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

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
        if not json_string:
            return []
        return json.loads(json_string)

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
        if os.path.exists(filename) is False:
            return []
        with open(filename, mode="r") as my_file:
            str_list = my_file.read()
            list_class = cls.from_json_string(str_list)
        for i in range(len(list_class)):
            instance_list.append(cls.create(**list_class[i]))
        return instance_list

    @classmethod
    def load_from_file_csv(cls):
        """ serializes and deserializes in CSV """
        filename = "{}.csv".format(cls.__name__)

        if os.path.exists(filename) is False:
            return []
        with open(filename, mode='r') as my_file:
            reader = csv.reader(my_file)
            csvlist = list(reader)

        if cls.__name__ == "Rectangle":
            listkeys = ['id', 'width', 'height', 'x', 'y']
        else:
            listkeys = ['id', 'size', 'x', 'y']
        matrix = []
        for csvelem in csvlist:
            dictcsv = {}
            for i in enumerate(csvelem):
                dictcsv[listkeys[0]] = int(i[1])
            matrix.append(dictcsv)

        listins = []
        for indx in range(len(matrix)):
            listins.append(cls.create(**matrix[indx]))

        return (listins)

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ Method that saves a CSV file """
        filename = "{}.csv".format(cls.__name__)

        if cls.__name__ == "Rectangle":
            list_dic = [0, 0, 0, 0, 0]
            list_keys = ['id', 'width', 'height', 'x', 'y']
        else:
            list_dic = ['0', '0', '0', '0']
            list_keys = ['id', 'size', 'x', 'y']

        matrix = []

        if not list_objs:
            pass
        else:
            for obj in list_objs:
                for kv in range(len(list_keys)):
                    list_dic[kv] = obj.to_dictionary()[list_keys[kv]]
                matrix.append(list_dic[:])

        with open(filename, 'w') as writeFile:
            writer = csv.writer(writeFile)
            writer.writerows(matrix)
