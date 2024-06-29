#!/usr/bin/python3

unsorted_list = [101, 49, 3, 12, 56]


def bubblesort(the_list):
    """Function to practice the bubblesort algorithm"""
    high_idx = len(the_list) - 1
    for i in range(high_idx):
        #  print(f"printing i: {i}")
        for j in range(high_idx):
            #  print(f"printing j: {j}")
            item = the_list[j]
            next = the_list[j+1]
            if item > next:
                the_list[j] = next
                the_list[j+1] = item
            print(f"LIST:{the_list}, i:{i}, j:{j}")


bubblesort(unsorted_list)
