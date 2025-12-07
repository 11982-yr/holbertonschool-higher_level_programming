#!/usr/bin/python3
"""
This module defines the Node and SinglyLinkedList classes.
"""


class Node:
    """
    Represents a node of a singly linked list.

    Attributes:
        data (int): Data stored in the node.
        next_node (Node): The next node in the list.
    """

    def __init__(self, data, next_node=None):
        """
        Initializes a new node.

        Args:
            data (int): The data for the new node.
            next_node (Node): The next node in the list or None.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Retrieve the data attribute."""
        return self.__data

    @data.setter
    def data(self, value):
        """Set the data attribute ensuring it is an integer."""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Retrieve the next_node attribute."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Set the next_node attribute ensuring it is a Node instance
        or None.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """
    Defines a singly linked list.

    Attributes:
        head (Node): The head node of the list.
    """

    def __init__(self):
        """Initializes an empty singly linked list."""
        self.__head = None

    def __str__(self):
        """
        Return a string representation of the list,
        one value per line.
        """
        values = []
        current = self.__head
        while current:
            values.append(str(current.data))
            current = current.next_node
        return "\n".join(values)

    def sorted_insert(self, value):
        """
        Insert a new Node into the correct sorted position
        (increasing order).

        Args:
            value (int): The data for the new node.
        """
        new = Node(value)

        if self.__head is None or value < self.__head.data:
            new.next_node = self.__head
            self.__head = new
            return

        current = self.__head
        while (current.next_node is not None and
               current.next_node.data < value):
            current = current.next_node

        new.next_node = current.next_node
        current.next_node = new
