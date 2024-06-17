#!/usr/bin/python3

inches_snow = {'Monday': 2, 'Tuesday': 4, 'Wednesday': 5}


def print_total_snowfall(inches_snow):
    """Function to display inches of snow fallen"""
    total_inches = 0
    for inches in inches_snow.values():
        total_inches += inches
    print(f"Total snowfall inches: {total_inches}")


print_total_snowfall(inches_snow)


print("How many inches of snow fell Thursday?")
response = int(input('> '))
inches_snow['Thursday'] = response

print_total_snowfall(inches_snow)
