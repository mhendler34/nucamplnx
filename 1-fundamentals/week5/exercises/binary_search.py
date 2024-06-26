#!/usr/bin/python3

def binary_search(test_list, target):
    """Function for binary search algo"""
    lower_bound = 0
    upper_bound = len(test_list) - 1  # because pivot is index of list (for -1)
    # Index in list is 0-9
    while lower_bound <= upper_bound:
        pivot = (lower_bound + upper_bound) // 2
        pivot_value = test_list[pivot]
        print(f"pivot/index on list: {pivot}")
        print(f"pivot value: {pivot_value}")

        if pivot_value == target:
            return pivot
        if pivot_value > target:
            upper_bound = pivot - 1
        else:
            lower_bound = pivot + 1
    return -1


test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(binary_search(test_list, 10))
print(binary_search(test_list, 4))
print(binary_search(test_list, 33))

