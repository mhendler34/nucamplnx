#!/usr/bin/python3

states = ['Washington', 'Oregon', 'California']

for state in states:
    print(state)

print()

for state in states:
    state = state.lower()
    print(state)

print("Using in and not in the next examples")
print()
print("Should print True")
print("Washington" in states)  # Print True
print("Should print False")
print("Tennessee" in states)  # Print False
print("Should print False")
print("Washington" not in states)  # Print False

states2 = ['Arizona', 'Ohio', 'Louisana']
print()
print("Concatenating Strings")

best_states = states + states2
print(best_states)
print()
print("Slicing strings")

print(best_states[1:3])  # Prints index 1 and 2
print(best_states[:2])  # Prints index 0 and 1
print(best_states[4:])  # Prints index 4 till the end
