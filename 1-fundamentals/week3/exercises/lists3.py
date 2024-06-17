#!/usr/bin/python3

# Negative index with slicing notation

           -7         -6        -5      -4      -3      -2          -1
fruits = ['apple', 'banana', 'pear', 'peach', 'plum', 'apricot', 'mango']

for fruit in fruits[-1:]:  # Prints last 1 (mango)
    print(fruit)
print()

for fruit in fruits[-2:]:  # Prints last 2 (apricot, mango)
    print(fruit)
print()

for fruit in fruits[-3:]:  # Prints last 3 (plum, apricot, mango)
    print(fruit)
print()

for fruit in fruits[-4]:  # Prints peach, one letter at a time
    print(fruit)

for fruit in fruits[:-1]:  # Prints all but last one (mango)
    print(fruit)
print()

for fruit in fruits[:-2]:  # Prints all but last two (apricot/mango)
    print(fruit)


