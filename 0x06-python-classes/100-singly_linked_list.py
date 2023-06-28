#!/usr/bin/python3

""" this is a making of a linked list in python """


class Node:
    """ it is a node of a linked list"""
    def __init__(self, data, next_node=None):
        """ init gives attributes"""
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """ property of data to change private
        instance to be accessed to some point"""
        return (self.__data)

    @data.setter
    def data(self, value):
        """ property to be accessed  is to change value"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """ next node calls next Node this is a class"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """ property accessed is property to change value"""
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


""" this is a singly linked list class"""


class SinglyLinkedList:
    """ used to properly link  the nodes"""
    def __init__(self):
        """ this contain attribute head which is the head of the linked list"""
        self.__head = None

    def sorted_insert(self, value):
        """ enter the node in a sorted manner
        from the lowest number to the highest"""
        new_node = Node(value)
        if self.__head is None or self.__head.data >= value:
            new_node.next_node = self.__head
            self.__head = new_node
            return

        current_node = self.__head
        while current_node.next_node is not None:
            if current_node.data < value and \
                    (current_node.next_node).data > value:
                new_node.next_node = current_node.next_node
                current_node.next_node = new_node
                return
            elif current_node.data == value:
                new_node.next_node = current_node.next_node
                current_node.next_node = new_node
                return
            current_node = current_node.next_node
        current_node.next_node = new_node

    def __str__(self):
        """
        enables attribute visuallisation inform
        of a string. output is first saved in the
        output string then the output string is returned """
        curr_node = self.__head
        output = ""
        while curr_node.next_node is not None:
            output += f"{curr_node.data}\n"
            curr_node = curr_node.next_node
        output += f"{curr_node.data}"
        return output
