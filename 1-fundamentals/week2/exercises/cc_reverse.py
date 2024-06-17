#!/usr/bin/python3

def reverse_1(name):
    """Function to reverse a string"""
    name = name[::-1]
    return name


name = input("What is your name? ")
print("Your name reversed is:", reverse_1(name))
