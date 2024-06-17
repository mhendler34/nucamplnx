#!/usr/bin/python3


state_capitals = {'Washington': 'Olympia', 'Oregon': 'Salem',
                  'California': 'Sacremento'}

#  Default is to loop through KEYS, these 2 are the same
for key in state_capitals:
    print(key)

for state in state_capitals:
    print(state)

#  Loopoing through Values, have to declare with values()
print()
for value in state_capitals.values():
    print(value)

for city in state_capitals.values():
    print(city)
print()

for state in state_capitals:
    print(f"{state_capitals[state]}, is the capital of {state}")

# Looping through Both
for key, value in state_capitals.items():
    print(f"Key: {key}")
    print(f"Value: {value}")

for state, city in state_capitals.items():
    print(f"{city}, is the capital of {state}")
