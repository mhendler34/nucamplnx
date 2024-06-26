#!/usr/bin/python3

class Queue:
    """Creating a Queue class"""

    def __init__(self):
        """Contructor Method: Declare and Initialize attirbutes"""
        self.items = []

    def size(self):
        """METHOD: size"""
        return len(self.items)

    def enqueue(self, item):
        """METHOD enqueue"""
        self.items.append(item)

    def dequeue(self):
        """METHOD dequeue"""
        if self.size() == 0:
            return None
        return self.items.pop(0)

    def show_queue(self):
        """METHOD: show queue"""
        print(self.items)


q = Queue()
q.enqueue('a')
q.enqueue('b')
q.enqueue('c')

print("Pass" if (q.size() == 3) else "Fail")
q.enqueue('d')
print("Pass" if (q.size() == 4) else "Fail")

print("Pass" if (q.dequeue() == 'a') else "Fail")
print("Pass" if (q.dequeue() == 'd') else "Fail")
print("Pass" if (q.size() == 2) else "Fail")
q.show_queue()
