#!/usr/bin/python3


def fizzbuzz(num):
    """Function to build basic division algorithm"""

    for x in range(num):
        if x % 3 == 0:
            print("fizz")
            if x % 5 == 0:
                print("buzz")
                if x % 15 == 0:
                    print("fizzbuzz")


fizzbuzz(50)
