#!/usr/bin/python3

class Node:
    """Creating a class Node"""

    def __init__(self, value):
        """Declare and Initialize class attributes"""
        self.value = value
        self.next = None


head = Node('1st Node')
head.next = Node('2nd Node')
head.next.next = Node('3rd Node')
head.next.next.next = Node('4th Node')


def iter_linked_list(node):
    """METHOD to iterate through nodes"""
    while node is not None:
        print(node.value)
        node = node.next


iter_linked_list(head)
