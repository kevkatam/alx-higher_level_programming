#!/usr/bin/python3
"""
module square that inherits from rectangle
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ class square that inherits from Rectangle """
    def __init__(self, size, x=0, y=0, id=None):
        """ initializer """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ method that overides the str method to print a formated string """
        str_s = "[Square] "
        str_id = "({}) ".format(self.id)
        str_xy = "{}/{} - ".format(self.x, self.y)
        str_size = "{}".format(self.size)

        return str_s + str_id + str_xy + str_size

    @property
    def size(self):
        """ size getter """
        return self.__size

    @size.setter
    def size(self, value):
        """ size setter """
        self.__width = value
        self.__height = value

    def update(self, *args, **kwargs):
        """ updated method that assigns attributes """
        if args is not None and len(args) is not 0:
            atr_list = ["id", "size", "x", "y"]
            for i in atr_list:
                if atr_list[i] == "size":
                    setattr(self, "width", args[i])
                    setattr(self, "height", args[i])
                else:
                    setattr(self, attr_list[i], args[i])
        else:
            for key, value in kwargs.items():
                if key == "size":
                    setattr(self, "width", value)
                    setattr(self, "height", value)
                else:
                    setattr(self, key, value)
    
    def to_dictionary(self):
        """ method  that returns the dictionary representation of a Square """
        atr_list = ["id", "size", "x", "y"]
        result_dic = {}
        for key in atr_list:
            if key == size:
                result_dic[key] = getattr(self, "height")
            else:
                result_dic[key] = getattr(self, key)
        return result_dic
