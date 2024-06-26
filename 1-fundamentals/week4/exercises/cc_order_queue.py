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


class IceCreamShop:
    """Creating a class IceCreamShop"""

    def __init__(self, flavors):
        """Constructor Method: Declare and Initialize attributes"""
        self.flavors = flavors
        self.orders = Queue()

    def take_order(self, customer, flavor, scoops):
        """Method to take an order"""
        if flavor in self.flavors:
            if scoops >= 1 and scoops <= 3:
                print("Order created!")
                return True
            else:
                print("Choose between 1-3 scoops")
        else:
            print("Sorry, we don't have that flavor")

        order = {'customer': customer, 'flavor': flavor, 'scoops': scoops}
        self.orders.enqueue(order)

    def show_all_orders(self):
        """Method: print all orders"""
        print("All Pending Ice Cream Orders:")
        self.orders.show_queue()

    def next_order(self):
        """Method: dequeue the head order and print it"""
        print(self.orders.dequeue())


""" Test Code """
shop = IceCreamShop(['rocky road', 'mint chip', 'pistachio'])
shop.take_order('Zachary', 'pistachio', 3)
shop.take_order('Marcy', 'mint chip', 1)
shop.take_order('Leopold', 'vanilla', 2)
shop.take_order('Bruce', 'rocky road', 0)
shop.show_all_orders()
shop.next_order()
shop.show_all_orders()

