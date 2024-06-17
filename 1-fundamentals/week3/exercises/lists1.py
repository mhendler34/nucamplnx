#!/usr/bin/python3

states = ['Washington', 'Oregon', 'California']

print(states[0])  # Prints Washington
print(states[1])  # Prints Oregon
print(states[2])  # Prints California

print()
print(states[-1])  # Prints California
print(states[-2])  # Prints Oregon
print(states[-3])  # Prints Washington

states[2] = 'Arizona'  # Replaces California with Arizona
print(states)  # Prints Washington, Oregon, Arizona

print(len(states))  # Prints 3
print()

states.append('New York')
print(states)  # Prints Washington, Oregon, Arizona, New York

states.pop()  # Pops last entry, (New York)
print(states)

states.pop(1)  # Pops Oregon
print(states)

