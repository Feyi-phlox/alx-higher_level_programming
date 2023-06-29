#!/usr/bin/python3

"""
This module defines a Node class and a SinglyLinkedList class.
"""


class Node:
    """
    This class represents a node of a singly linked list.
    """

    def __init__(self, data, next_node=None):
        """
        Initializes a Node instance with data and next_node.

        Args:
            data (int): The data value of the node.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Retrieves and returns the data value of the node.
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Sets the data value of the node.

        Args:
            value (int): The new data value of the node.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """
        Retrieves and returns the next node in the linked list.
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Sets the next node in the linked list.

        Args:
            value (Node): The new next node in the linked list.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """
    represents a singly linked list.
    """

    def __init__(self):
        """
        Initializes a SinglyLinkedList instance with an empty head node.
        """
        self.head = None

    def sorted_insert(self, value):
        """
        Inserts a new Node into the correct sorted position in the list

        Args:
            value (int): The value of the new Node to be inserted.
        """
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
        elif value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
        else:
            current = self.head
            while (current.next_node is not None and
                    value >= current.next_node.data):
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """
        Returns a string representation of the linked list.
        """
        node = self.head
        result = ""
        while node is not None:
            result += str(node.data) + "\n"
            node = node.next_node
        return result.rstrip()
