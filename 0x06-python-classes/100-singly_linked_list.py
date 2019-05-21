#!/usr/bin/python3
"""Singly Linked-List

Classes to create a singly-linked list

"""


class Node:
    """a single node in a singly-linked list

    Each node holds a piece of data and a reference to the next node.

    """

    @property
    def data(self):
        """int: the data stored in this node

        The setter validates the type

        Returns:
            the private data attribute

        """

        return self.__data

    @data.setter
    def data(self, val):
        if not isinstance(val, int):
            raise TypeError('data must be an integer')
        self.__data = val

    @property
    def next_node(self):
        """Node: reference to the next node

        The setter validates that the value is either a Node or None

        Returns:
            the private next node attribute

        """

        return self.__next_node

    @next_node.setter
    def next_node(self, val):
        if val is not None and not isinstance(val, Node):
            raise TypeError('next_node must be a Node object')
        self.__next_node = val

    def __init__(self, data, next_node=None):
        """Create a new Node object

        Data must be given to put in this node, but it doesn't have to have a
        next node yet.

        Args:
            data (int): data to store in this node
            next_node (Node): the next node in the list

        Raises:
            TypeError: an argument has the wrong type for its attribute

        """

        self.data = data
        self.next_node = next_node


class SinglyLinkedList:
    """The linked list itself, with reference to the first node

    Does not contain a collection of nodes, they refer to each other.

    """

    def __init__(self):
        """Create an empty linked list

        These lists are always sorted

        """

        self.__head = None

    def __str__(self):
        """Show each piece of data in the list

        Returns:
            str: each integer in the list, separated by a line break

        """

        node = self.__head
        data = []
        while node is not None:
            data.append(node.data)
            node = node.next_node
        return '\n'.join('{:d}'.format(i) for i in data)

    def sorted_insert(self, value):
        """Insert a new value at the sorted position

        These lists are sorted smallest to largest

        Args:
            value (int): value to add to list

        """

        if self.__head is None:
            self.__head = Node(value, None)
            return
        node = self.__head
        previous = None
        while node is not None and node.data <= value:
            previous = node
            node = node.next_node
        node = Node(value, node)
        if previous is not None:
            previous.next_node = node
        else:
            self.__head = node
