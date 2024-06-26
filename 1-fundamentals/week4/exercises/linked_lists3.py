#!/usr/bin/python3

class Node:
    """Creating a class Node"""

    def __init__(self, value):
        """Declare and Initialize class attributes"""
        self.value = value
        self.next = None


class LinkedList:
    """Creating a class LinkedList"""

    def __init__(self):
        """Declare and Initialize instance attributes"""
        self.head = None

    def append(self, value):
        """METHOD to append values to linked list"""
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            print(f"Head Node Created: {self.head.value}")
            return

        node = self.head
        while node.next is not None:
            node = node.next

        node.next = new_node
        print(f"Appended new Node with value: {node.next.value}")


llist = LinkedList()
llist.append('First Node')
llist.append('Second Node')
llist.append('Third Node')



