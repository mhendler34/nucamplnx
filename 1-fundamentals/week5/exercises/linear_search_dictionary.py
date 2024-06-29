#!/usr/bin/python3

def linear_search_dictionary(dictionary, target):
    """Function to search dictionary for a value and return its key"""
    for key in dictionary:
        if dictionary[key] == target:
            print(f"Found at key, {key}")
            return key
    print("Target is not in the dictionary")
    return None


my_dictionary = {'red': 5, 'blue': 3, 'yellow': 12, 'green': 7}
linear_search_dictionary(my_dictionary, 5)
linear_search_dictionary(my_dictionary, 3)
linear_search_dictionary(my_dictionary, 8)
linear_search_dictionary(my_dictionary, 12)
linear_search_dictionary(my_dictionary, 7)

# DIRECTIONS
# Parameter list should dictionary and target value
# Function should search each value in dict to see if matches target value
# If match, PRINT a success message and return the key of matched value
# Found at key red, Found at key blue
# If no match in dictionary, PRINT failure message and return NONE
# Target is not in the dictionary
