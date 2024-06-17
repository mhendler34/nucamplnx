#!/usr/bin/python3

# numbers_set = {1, 2, 3, 4, 4}  # Duplicate values removed
# numbers_set1 = {1, 2, 3, 4, [5, 6]}  # CANNOT use mutable data types, error
# numbers_set = {1, 2, 3, 4, (5, 6)}  # Tuples are okay
# print(numbers_set)  # TUPLES are IMMUTABLE OKAY to use

words_set = {'Alpha', 'Bravo', 'Charlie'}

abcd = ""
for word in words_set:
    abcd += word
    print(abcd)

if 'Alpha' in words_set:  # BOOLEAN, checking if true
    print('Alpha is in set')  # If True, print this
else:
    print('Alpha not in set')  # If False, print this

words_set.add('Delta')
print(words_set)
words_set.discard('Bravo')
print(words_set)
