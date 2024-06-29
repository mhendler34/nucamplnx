#!/usr/bin/python3

import random

i = 0
while i < 2:
    i += 1
    random_int = random.randint(0, 255)
    bin_val = format(random_int, '08b')
    hex_val = format(random_int, 'x')
    print(bin_val)
    print("Hex equivalent is?")
    answer = input('> ')

    if answer == 'x':
        break
    elif answer == str(hex_val):
        print("CORRECT")
    else:
        print("Not quite")
        print(hex_val)


    print(random_int)
    print(type(random_int))
    print(format(random_int, '08b'))
    print(type(random_int))
    print(format(random_int, 'x'))
    print(type(random_int))
    print()


binary = ""
for i in range(8):
    temp = str(random.randint(0, 1))
    binary += temp
print(binary)



b_digits = list(binary)
decimal_value = 0

for i in range(8):
    decimal_value += int(b_digits[i]) * (2 ** (7 - i))
    print(i)
    print(decimal_value)
# --------------
# Another way to caluclate value of binary digits
    for i in range(len(b_digits)):
        b_digit = b_digits.pop()
        if b_digit == '1':
            decimal_value = decimal_value + pow(2, i)

print()
print("-----")
for i in range(7, -1, -1):
    print(i)
# LONG WAY  to convert decimal to binary
# POP EACH ITEM FROM LIST
digit_7 = b_digits.pop()  # Var to hold item poped @ Index position 7
digit_6 = b_digits.pop()  # Var to hold item poped @ Index position 6
digit_5 = b_digits.pop()  # Var to hold item poped @ Index position 5
digit_4 = b_digits.pop()  # Var to hold item poped @ Index position 4
digit_3 = b_digits.pop()  # Var to hold item poped @ Index position 3
digit_2 = b_digits.pop()  # Var to hold item poped @ Index position 2
digit_1 = b_digits.pop()  # Var to hold item poped @ Index position 1
digit_0 = b_digits.pop()  # Var to hold item poped @ Index position 0

# DO MATH ON EACH ITEM
b7 = int(digit_7) * (2 ** 0)  # 2^0 = 1
b6 = int(digit_6) * (2 ** 1)  # 2^1 = 2
b5 = int(digit_5) * (2 ** 2)  # 2^2 = 4
b4 = int(digit_4) * (2 ** 3)  # 2^3 = 8
b3 = int(digit_3) * (2 ** 4)  # 2^4 = 16
b2 = int(digit_2) * (2 ** 5)  # 2^5 = 32
b1 = int(digit_1) * (2 ** 6)  # 2^6 = 64
b0 = int(digit_0) * (2 ** 7)  # 2^7 = 128

# ADD THEM ALL UP
decimal_value = b7 + b6 + b5 + b4 + b3 + b2 + b1 + b0

