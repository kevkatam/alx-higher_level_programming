#!/usr/bin/python3
"""
module that defines the class node
"""


class Node:
    """ class that defines a node of a singly linked """

    def __init__(self, data, next_node=None):
        """ method that initializes the data """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """ retrievs data """
        return self.__data

    @data.setter
    def data(self, value):
        """method that sets the data """
        if type(value) is not int:
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """method that retrievs next_node """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """method that sets next_node"""
        if value is not None or value is not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList(Node):
    """ class that defines a singly linked list """

    def __str__(self):
        """ method that formats the output to human readable string """
        p = ""
        while self.__head is not None:
            p += str(self.__head.data)
            if self.__head.next_node is not None:
                p += "\n"
            self.__head = self.__head.next_node
        return p

    def __init__(self):
        """ init method that initializes the data """
        self.__head = None

    def sorted_insert(self, value):
        """ method that inserts a new Node into the correct sorted position"""
        cur = self.__head

        while cur is not None:
            if cur.data > value:
                break
            cur_prev = cur
            cur = cur.next_node

        new_node = Node(value, cur)
        if cur == self.__head:
            self.__head = new_node
        else:
            cur_prev.next_node = new_node
