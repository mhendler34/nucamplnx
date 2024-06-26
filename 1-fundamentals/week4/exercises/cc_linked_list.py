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
        new_node = Node(value)  # new object created for Node Class

        if self.head is None:  # Check if list is empty
            self.head = new_node  # If so, make new_node head
            print(f"Head Node Created: {self.head.value}")
            return

        node = self.head  # If list is not empty make a last node
        while node.next is not None:  # While next node does not point to None
            node = node.next  # Move pointer to the right until you hit None
            # Once pointer reaches None, BREAK out of while loop and do below

        node.next = new_node  # if last node is None, insert node here
        print(f"Appended new Node with value: {node.next.value}")

    def prepend(self, value):
        """METHOD to prepend values to linked list"""
        new_node = Node(value)  # new object created from Node Class

        if self.head is None:  # If head is None, list empty
            self.head = new_node  # Assign head node to new_node just created
            print(f"Head Node Created: {self.head.value}")
            return

        else:  # If there is data in head node
            new_node.next = self.head  # assign next node to head node
            self.head = new_node  # assign head node to new node
            print(f"Prepended new Head Node with value: {self.head.value}")
            print(f"Node following Head: {new_node.next.value}")


llist = LinkedList()
# llist.append('First Node')
# llist.append('Second Node')
# llist.append('Third Node')

llist.prepend('First Node')
llist.prepend('Inserted New First Node')







