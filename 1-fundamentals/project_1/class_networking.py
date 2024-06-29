#!/usr/bin/python3

import random


class Networking:
    """Create a class Networking, under which to place all the trng packages"""

    def __init__(self):
        """Constructor Method: Declare and Initialize attributes"""
        #  self.subject = subject
        #  self.dictionary = dictionary

    def flash_cards(self, subject, dictionary):
        """METHOD: Spin through k,v pairs to quiz user on subject"""
        print("==== LET'S TRAIN ====")
        print(f"This session's training topic: {subject.upper()}")
        print("(x) at any time to Exit")

        wrong_answers = {}
        i = 0
        answer = ""
        while i < len(dictionary):
            if answer == 'x':
                break
            for key in dictionary:
                i += 1
                print(f"\n{key}")
                answer = input('> ').lower()
                value = dictionary[key]
                if answer == 'x':
                    break
                elif answer == value.lower():
                    print("<< CORRECT >>")
                else:
                    print("Not quite")
                    print(value)
                    wrong_answers[key] = value
        print(f"\n{subject.upper()} missed:\n")
        for key, value in wrong_answers.items():
            print(f"{key} : {value}")

    def bin_dec(self):
        """METHOD: Convert binary to decimal"""
        print("Binary to Decimal Conversions")
        print("(x) to exit at any time")

        while True:
            random_int = random.randint(0, 255)
            bin_val = format(random_int, '08b')
            print(bin_val)
            print("Decimal equivalent is?")
            answer = input('> ')

            if answer == 'x':
                break
            elif int(answer) == random_int:
                print("<< CORRECT >>\n")
            else:
                print("Not quite\n")
                print(random_int)

    def bin_hex(self):
        """Method to convert Binary to Hexadecimal"""
        print("Binary to Hexadecimal Conversions")
        print("(x) to exit")

        while True:
            random_int = random.randint(0, 255)
            bin_val = format(random_int, '08b')
            hex_val = format(random_int, '02x')
            print(bin_val)
            print("Hex equivalent is?")
            answer = input('> ')

            if answer == 'x':
                break
            elif answer == str(hex_val):
                print("<< CORRECT >>\n")
            else:
                print("Not quite\n")
                print(hex_val)

    def hex_dec(self):
        """Method to convert Hexadecimal to Decimal"""
        print("Hexadecimal to Decimal Conversions")
        print("(x) to exit")
        while True:
            random_int = random.randint(0, 255)
            hex_val = format(random_int, '02x')
            print(hex_val)
            print("Decimal Equivalent is?")
            answer = input('> ')

            if answer == 'x':
                break
            elif int(answer) == random_int:
                print("<< CORRECT >>\n")
            else:
                print("Not quite\n")
                print(random_int)


