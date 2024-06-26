#!/usr/bin/python3

class DoubleNode:
    """Creating DoubleNode Class"""
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    """Creating a Doubly Linked List"""
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value):
        new_node = DoubleNode(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            print(f"Head Node Created: {self.head.value}")
            return

        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node
        print(f"Appended new Node with value: {self.tail.value}")


dllist = DoublyLinkedList()
dllist.append('First Node')

